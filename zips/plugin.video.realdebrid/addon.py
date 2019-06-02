import json
import math
import urllib2

from resolveurl import display_settings, relevant_resolvers, common
from resolveurl.lib.net import HttpResponse, Net
from resolveurl.plugins.realdebrid import RealDebridResolver
from resolveurl.resolver import ResolverError

from xbmcswift2 import Plugin
from xbmcswift2 import xbmc
from xbmcswift2 import xbmcgui
from xbmcswift2 import xbmcaddon

def http_DELETE(self, url, headers={}):
    '''
    Perform an HTTP DELETE request.
    Args:
        url (str): The URL to GET.
    Kwargs:
        headers (dict): A dictionary describing any headers you would like
        to add to the request. (eg. ``{'X-Test': 'testing'}``)
    Returns:
        An :class:`HttpResponse` object containing headers and other
        meta-information about the page.
    '''
    request = urllib2.Request(url)
    request.get_method = lambda: 'DELETE'
    request.add_header('User-Agent', self._user_agent)
    for key in headers:
        request.add_header(key, headers[key])
    response = urllib2.urlopen(request)
    return HttpResponse(response)
Net.http_DELETE = http_DELETE

logger = common.log_utils.Logger.get_logger('realdebrid')
logger.disable()

plugin = Plugin()


class CustomRealDebridResolver(RealDebridResolver):

    CLIENT_ID = '3XZIVW7Z23DSW'
    name = 'Real-Debrid (Csutom)'
    base_url = 'https://api.real-debrid.com/rest/1.0'

    def authorize_resolver(self):
        url = (
            'https://api.real-debrid.com/oauth/v2/device/code'
            '?client_id=%s&new_credentials=yes'
        ) % (self.client_id, )
        result = self.net.http_GET(url, headers=self.headers).content
        js_result = json.loads(result)
        title = 'URL Resolver Real Debrid Authorization'
        line1 = 'Go to URL: %s' % (js_result['verification_url'])
        line2 = 'When prompted enter: %s' % (js_result['user_code'])
        with common.kodi.CountdownDialog(
                title, line1, line2, countdown=120,
                interval=js_result['interval']) as cd:
            result = cd.start(self.__check_auth, [js_result['device_code']])

        # cancelled
        if result is None: return
        return self._RealDebridResolver__get_token(
            result['client_id'],
            result['client_secret'],
            js_result['device_code'],
        )

    def __check_auth(self, device_code):
        try:
            url = (
                'https://api.real-debrid.com/oauth/v2/device/credentials'
                '?client_id=%s&code=%s'
            ) % (self.client_id, device_code)
            content = self.net.http_GET(url, headers=self.headers).content
            js_result = json.loads(content)
        except Exception as e:
            logger.log_debug('Exception during RD auth: %s' % (e))
        else:
            return js_result

    @property
    def is_client_id_external(self):
        return plugin.get_setting('client_id_external', bool)

    @property
    def client_id(self):
        if self.is_client_id_external:
            logger.log_debug('Using external Client ID %s' % self.get_setting('client_id'))
            return plugin.get_setting('client_id', str)

        logger.log_debug('Using internal Client ID')
        return self.CLIENT_ID

    def _request(
            self, method, uri, form_data=None, retry=False,
            response_encoder=json.loads, fail_silently=None):
        url = "".join([self.base_url, uri])
        token = self.get_setting('token')
        headers = self.headers.copy()
        headers.update({
            'Authorization': 'Bearer %s' % (token, )
        })

        request_data = {
            'url': url,
            'headers': headers,
        }

        if form_data:
            request_data.update({
                'form_data': form_data,
            })

        request_callable = getattr(self.net, 'http_%s' % (method.upper(), ))

        try:
            result = request_callable(**request_data).content
        except urllib2.HTTPError as e:
            if not retry and self.get_setting('refresh'):
                self.refresh_token()
                return self._request(
                    method, uri, form_data=form_data,
                    response_encoder=response_encoder,
                    fail_silently=fail_silently, retry=True,
                )
            return self._handle_request_error(e, fail_silently)
        except Exception as e:
            raise ResolverError('Unexpected Exception during RD Unrestrict: %s' % (e))

        if not response_encoder:
            return result

        return response_encoder(result)

    def _handle_request_error(self, error, fail_silently=None):
        if fail_silently is None:
            fail_silently = []
        if error.code == 401 and error.code not in fail_silently:
            raise ResolverError('Real Debrid Unauthorized')
        elif error.code == 403 and error.code not in fail_silently:
            xbmcgui.Dialog().ok(
                'Real Debrid Access Denied',
                'Client ID is not authorized to access the resource.',
                'Provide your Client ID in Settings to grant access.',
            )
            raise ResolverError('Real Debrid Access Denied')
        elif error.code == 404 and error.code not in fail_silently:
            raise ResolverError('Real Debrid Resource Not Found')
        else:
            raise ResolverError('Real Debrid API Failed: %s' % str(error))

    def get_downloads(self):
        uri = '/downloads'
        return self._request('get', uri)

    def delete_download(self, download_id):
        uri ='/downloads/delete/{0}'.format(download_id)
        return self._request('delete', uri, response_encoder=None, fail_silently=[404, ])

    def get_torrents(self):
        uri = '/torrents'
        return self._request('get', uri)

    def get_torrent(self, torrent_id):
        uri = '/torrents/info/{0}'.format(torrent_id)
        return self._request('get', uri)

    def delete_torrent(self, torrent_id):
        uri ='/torrents/delete/{0}'.format(torrent_id)
        return self._request('delete', uri, response_encoder=None)

    def unrestrict_link(self, link):
        form_data = {
            'link': link,
        }
        uri = '/unrestrict/link'
        return self._request('post', uri, form_data=form_data)

    def get_account(self):
        uri = '/user'
        return self._request('get', uri)


def index():
    downloads = {
        'label': 'My downloads',
        'path': 'plugin://plugin.video.realdebrid/downloads/',
        'is_playable': False,
    }
    torrents = {
        'label': 'My torrents',
        'path': 'plugin://plugin.video.realdebrid/torrents/',
        'is_playable': False,
    }
    account = {
        'label': 'Account',
        'path': 'plugin://plugin.video.realdebrid/account/',
        'is_playable': False,
    }
    ad = {
        'label': 'EyePeaTV www.eyepeatv.co.uk',
        'path': 'plugin://plugin.video.realdebrid/',
        'is_playable': False,
    }
    return [downloads, torrents, account, ad]


def downloads():
    real_debrid_resolver = get_resolver()
    real_debrid_resolver.login()
 
    download_list = real_debrid_resolver.get_downloads()
    for download in download_list:
        if not download['streamable']:
            continue
        # use https connection
        download['download'] = download['download'].replace("http://","https://")
        
        info = {}
        if download['filesize']:
            info['size'] = download['filesize']

        download_context_menu = []

        delete_link = (
            'plugin://plugin.video.realdebrid/downloads/{0}/delete/'
        ).format(download['id'])
        download_context_menu.append(
            ('Delete', make_run(delete_link))
        )

        yield {
            'label': download['filename'],
            'path': download['download'],
            'is_playable': True,
            'info': info,
            'context_menu': download_context_menu,
        }


def download_delete(download_id):
    real_debrid_resolver = get_resolver()
    real_debrid_resolver.login()
 
    confirmed = xbmcgui.Dialog().yesno(
        'Delete download',
        'Are you sure?',
    )
    if not confirmed:
        return

    try:
        real_debrid_resolver.delete_download(download_id)
    except ResolverError:
        # i dont know why it returns 404 after success xD
        pass

    xbmc.executebuiltin('Container.Refresh') 


def torrents():
    real_debrid_resolver = get_resolver()
    real_debrid_resolver.login()
 
    torrent_list = real_debrid_resolver.get_torrents()
    for torrent in torrent_list:

        info = {}
        if 'bytes' in torrent:
            info['size'] = torrent['bytes']

        torrent_link = (
                'plugin://plugin.video.realdebrid/torrents/{0}/'
            ).format(torrent['id'])
        info_link = (
                'plugin://plugin.video.realdebrid/torrents/{0}/info/'
            ).format(torrent['id'])
        torrent_context_menu = [
            ('Information', make_run(info_link))
        ]

        if torrent['status'] == 'downloaded':
            unrestrict_link = (
                'plugin://plugin.video.realdebrid/torrents/{0}/unrestrict/'
            ).format(torrent['id'])
            torrent_context_menu.append(
                ('Copy to My downloads', make_run(unrestrict_link))
            )

        delete_link = (
            'plugin://plugin.video.realdebrid/torrents/{0}/delete/'
        ).format(torrent['id'])
        torrent_context_menu.append(
            ('Delete', make_run(delete_link))
        )

        yield {
            'label': torrent['filename'],
            'path': torrent_link,
            'is_playable': False,
            'info': info,
            'context_menu': torrent_context_menu,
        }


def torrent_info(torrent_id):
    real_debrid_resolver = get_resolver()
    real_debrid_resolver.login()
 
    torrent_info = real_debrid_resolver.get_torrent(torrent_id)

    titles = [
        "ID", "Filename", "Original filename", "Size", "Original size", "Host",
        "Parts", "Progress", "Status",
    ]
    size_str = convert_size(torrent_info['bytes'])
    original_size_str = convert_size(torrent_info['original_bytes'])
    progress_str = "{0}%".format(torrent_info['progress'])
    end_date_str = torrent_info.get('ended', '-')
    items = [
        torrent_info['id'], torrent_info['filename'],
        torrent_info['original_filename'], size_str, original_size_str,
        torrent_info['host'], torrent_info['split'], progress_str,
        torrent_info['status'],
    ]
    if torrent_info['status'] == "downloaded":
        titles += ["Download ended",]
        end_date_str = torrent_info['ended']
        items += [end_date_str,]
    if torrent_info['status'] in ["downloading", "compressing", "uploading"]:
        titles += ["Download speed",]
        speed_system = (
            "B/s", "KB/s", "MB/s", "GB/s", "TB/s", "PB/s", "EB/s",
            "ZB/s", "YB/s",
        )
        speed_str = convert_size(torrent_info['speed'], system=speed_system)
        items += [speed_str,]
    if torrent_info['status'] in ["downloading", "magnet_conversion"]:
        titles += ["Seeders",]
        seeders_str = torrent_info['seeders']
        items += [seeders_str,]
    items_formatted = map(option_formatter, titles, items)
    xbmcgui.Dialog().select("Torrent information", items_formatted)


def torrent(torrent_id):
    real_debrid_resolver = get_resolver()
    real_debrid_resolver.login()
 
    torrent_info = real_debrid_resolver.get_torrent(torrent_id)

    for torrent_file in torrent_info['files']:
        if not torrent_file['selected']:
            label = disabled_formatter(torrent_file['path'])
        else:
            label = torrent_file['path']
        yield {
            'label': label,
            'is_playable': True,
        }


def torrent_delete(torrent_id):
    real_debrid_resolver = get_resolver()
    real_debrid_resolver.login()
 
    confirmed = xbmcgui.Dialog().yesno(
        'Delete torrent',
        'Are you sure?',
    )
    if not confirmed:
        return

    real_debrid_resolver.delete_torrent(torrent_id)

    xbmc.executebuiltin('Container.Refresh') 


def torrent_download(torrent_id):
    real_debrid_resolver = get_resolver()
    real_debrid_resolver.login()
 
    torrent_info = real_debrid_resolver.get_torrent(torrent_id)

    for torrent_file in torrent_info['files']:
        if not torrent_file['selected']:
            label = disabled_formatter(torrent_file['path'])
        else:
            label = torrent_file['path']
        yield {
            'label': label,
            'is_playable': True,
        }



def unrestrict(torrent_id):
    real_debrid_resolver = get_resolver()
    real_debrid_resolver.login()

    torrent_info = real_debrid_resolver.get_torrent(torrent_id)

    # this torrent is not downloaded yet
    if torrent_info['status'] != 'downloaded':
        return []

    if 'links' not in torrent_info or not torrent_info['links']:
        return []

    link = torrent_info['links'][0]

    real_debrid_resolver.unrestrict_link(link)
    icon = xbmcaddon.Addon().getAddonInfo('icon')
    xbmcgui.Dialog().notification(
        'Real Debrid', 'Copied successfully', icon=icon)


def account():
    real_debrid_resolver = get_resolver()
    real_debrid_resolver.login()

    account = real_debrid_resolver.get_account()
    logger.log_debug('Account data: %s' % (account))

    user = account['username']
    id = str(account['id'])
    email = account['email']
    type = account['type'].capitalize()
    points = str(account['points'])

    expiration = account['expiration']
    msec_idx = expiration.find('.')
    if msec_idx >= 0: expiration = expiration[:msec_idx]
    expiration_date = expiration.strip().lower().replace('t', ' ')

    titles = ["ID", "Username", "E-mail", "Type", "Points", "Expiration date"]
    items = [id, user, email, type, points, expiration_date]
    items_formatted = map(option_formatter, titles, items)
    xbmcgui.Dialog().select("Account", items_formatted)


def auth_reset():
    real_debrid_resolver = get_resolver()
    real_debrid_resolver.reset_authorization()
    icon = xbmcaddon.Addon().getAddonInfo('icon')
    xbmcgui.Dialog().notification(
        'Real Debrid', 'Authorization reset', icon=icon)


def disabled_formatter(title):
    return '[COLOR grey]{0}[/COLOR]'.format(title)


def option_formatter(title, value):
    return '[B]{0}[/B]: {1}'.format(title, value)


def get_resolver(*args, **kwargs):
    return CustomRealDebridResolver(*args, **kwargs)


def make_run(url):
    return 'XBMC.RunPlugin({0})'.format(url)


def convert_size(size_bytes, system=None):
    if size_bytes == 0:
        return "0 B"
    if system is None:
        system = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return "{0} {1}".format(s, system[i])


plugin.add_url_rule("/", index, name=index.__name__)
plugin.add_url_rule('/downloads/', downloads, name=downloads.__name__)
plugin.add_url_rule('/downloads/<download_id>/delete/', download_delete, name=download_delete.__name__)
plugin.add_url_rule('/torrents/', torrents, name=torrents.__name__)
plugin.add_url_rule('/torrents/<torrent_id>/', torrent, name=torrent.__name__)
plugin.add_url_rule('/torrents/<torrent_id>/info/', torrent_info, name=torrent_info.__name__)
plugin.add_url_rule('/torrents/<torrent_id>/unrestrict/', unrestrict, name=unrestrict.__name__)
plugin.add_url_rule('/torrents/<torrent_id>/delete/', torrent_delete, name=torrent_delete.__name__)
plugin.add_url_rule('/account/', account, name=account.__name__)
plugin.add_url_rule('/settings/', display_settings, name='settings')
plugin.add_url_rule('/auth/reset/', auth_reset, name='auth_reset')

if __name__ == '__main__':
    plugin.run()
