# -*- coding: UTF-8 -*-
#######################################################################
# ----------------------------------------------------------------------------
# "THE BEER-WARE LICENSE" (Revision 42):
# @tantrumdev wrote this file.  As long as you retain this notice you
# can do whatever you want with this stuff. If we meet some day, and you think
# this stuff is worth it, you can buy me a beer in return. - Muad'Dib
# ----------------------------------------------------------------------------
#######################################################################


import json
import re
import traceback
import urllib
import urlparse

from resources.lib.modules import cfscrape, cleantitle, client, log_utils


class source:
    def __init__(self):
        self.priority = 1
        self.language = ['en']
        self.domains = ['putlockertv.to', 'putlockertv.se']
        self.base_link = 'https://www6.putlockertv.to'
        self.search_path = '/ajax/film/search?ts=%s&_=%i&keyword=%s&sort=year%%3Adesc'
        self.episode_search_path = ('/filter?keyword=%s&sort=post_date:Adesc'
                                    '&type[]=series')
        self.film_path = '/watch/%s'
        self.server_path = '/ajax/film/servers/%s'
        self.info_path = '/ajax/episode/info?ts=%s&_=%i&id=%s&server=%s&update=0'

        self.User_Agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
        self.DEFAULT_ACCEPT = 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
        self.ALL_JS_PATTERN = '<script src=\"(/assets/min/public/all.js?.*?)\"'
        self.DEBRID_HOSTS = {
            'openload': 'openload.co',
            'rapidvideo': 'rapidvideo.com',
            'streamango': 'streamango.com'
        }

    def movie(self, imdb, title, localtitle, aliases, year):
        try:
            aliases.append({'country': 'us', 'title': title})
            url = {'imdb': imdb, 'title': title, 'year': year, 'aliases': aliases}
            url = urllib.urlencode(url)
            return url
        except Exception:
            failure = traceback.format_exc()
            log_utils.log('PLocker - Exception: \n' + str(failure))
            return

    def tvshow(self, imdb, tvdb, tvshowtitle, localtvshowtitle, aliases, year):
        try:
            aliases.append({'country': 'us', 'title': tvshowtitle})
            url = {'imdb': imdb, 'tvdb': tvdb, 'tvshowtitle': tvshowtitle, 'year': year, 'aliases': aliases}
            url = urllib.urlencode(url)
            return url
        except Exception:
            failure = traceback.format_exc()
            log_utils.log('PLocker - Exception: \n' + str(failure))
            return

    def episode(self, url, imdb, tvdb, title, premiered, season, episode):
        try:
            if url is None:
                return
            url = urlparse.parse_qs(url)
            url = dict([(i, url[i][0]) if url[i] else (i, '') for i in url])
            url['title'], url['premiered'], url['season'], url['episode'] = title, premiered, season, episode
            url = urllib.urlencode(url)
            return url
        except Exception:
            failure = traceback.format_exc()
            log_utils.log('PLocker - Exception: \n' + str(failure))
            return

    def sources(self, url, hostDict, hostprDict):
        try:
            sources = []

            data = urlparse.parse_qs(url)
            data = dict([(i, data[i][0]) if data[i] else (i, '') for i in data])

            if 'tvshowtitle' in data:
                title = data['tvshowtitle']
                isMovie = False
            else:
                title = data['title']
                isMovie = True

            session = self._createSession(self.User_Agent)
            extraLocalTitle = ''

            if not isMovie and data['season'] != '1':
                localTitle = cleantitle.geturl(title) + '-' + data['season']
            else:
                localTitle = cleantitle.geturl(title)
                if not isMovie:
                    extraLocalTitle = cleantitle.geturl(title) + '-' + data['season']

            localTitle = localTitle.replace('dcs-', '')

            stringConstant, search_response, timeStamp = self._getSearch(localTitle, session)

            r = re.compile('class="name" href="(.+?)">(.+?)</a>.+?text-danger">(.+?)</span',
                           re.DOTALL).findall(search_response)

            for url, item_name, year in r:
                remoteTitle = cleantitle.geturl(str(item_name))
                # print remoteTitle, localTitle, year
                if localTitle == remoteTitle or extraLocalTitle == remoteTitle:
                    film_id = url.split('.')[-1:]
                    info_url = urlparse.urljoin(self.base_link, self.server_path % film_id[0])

                    servers = client.request(info_url)
                    r = json.loads(servers)['html']

                    if not isMovie:
                        EE = '%02d' % int(data['episode'])

                    tempTokenData = {'ts': timeStamp, 'id': None, 'server': None, 'update': '0'}
                    baseInfoURL = urlparse.urljoin(self.base_link, self.info_path)

                    servers = re.compile(
                        'data-type="iframe" data-id="(.+?)">.+?</i>(.+?)</label>.+?<ul(.+?)</ul>').findall(r.replace('\n', ' ').replace('\r', ''))

                    for serverId, hostName, episodesList in servers:
                        tempTokenData['server'] = serverId
                        hostName = self.DEBRID_HOSTS.get(hostName.lower().strip(), hostName.strip())

                        episodes = re.compile('data-id="(.+?)".+?>(.+?)</a>').findall(episodesList)

                        for hostID, label in episodes:
                            if (not isMovie and EE == label) or isMovie:
                                quality = '720p'
                                tempTokenData['id'] = hostID
                                tempToken = self._makeToken(tempTokenData, stringConstant)
                                url = baseInfoURL % (timeStamp, tempToken, hostID, tempTokenData['server'])

                                sources.append({'source': hostName, 'quality': quality, 'language': 'en',
                                                'url': url, 'direct': False, 'debridonly': False})

            return sources
        except Exception:
            failure = traceback.format_exc()
            log_utils.log('PLocker - Exception: \n' + str(failure))
            return sources

    def resolve(self, url):
        try:
            return self._getHost(url)
        except Exception:
            failure = traceback.format_exc()
            log_utils.log('PLocker - Exception: \n' + str(failure))
            return

    def _sessionGET(self, url, session):
        try:
            return session.get(url, timeout=10)  # Goes through a Cloudflare challenge, if necessary.
        except Exception:
            return type('FailedResponse', (object,), {'ok': False})

    def _requestJSON(self, url):
        try:
            return json.loads(url)
        except Exception:
            return None

    def _getHost(self, url):
        r = client.request(url)
        jsonData = json.loads(r)

        if jsonData:
            return jsonData['target']
        else:
            print('PLOCKER > _getHost JSON request failed')
            return ''

    def _getSearch(self, lowerTitle, session):
        '''
        All the code in here assumes a certain website structure.
        If they change it in the future, it'll crash.
        '''
        # Get the homepage HTML.
        homepageHTML = client.request(self.base_link)
        timeStamp = self._getTimeStamp(homepageHTML)

        # Get the minified main javascript file.
        jsPath = re.search(self.ALL_JS_PATTERN, homepageHTML, re.DOTALL).group(1)
        session.headers['Accept'] = '*/*'  # Use the same 'Accept' for JS files as web browsers do.
        url = urlparse.urljoin(self.base_link, jsPath)
        allJS = client.request(url)

        session.headers['Accept'] = self.DEFAULT_ACCEPT

        # Some unknown cookie flag that they use, set after 'all.js' is loaded.
        # Doesn't seem to make a difference, but it might help with staying unnoticed.
        session.cookies.set('', '__test')

        # Get the underscore token used to verify all requests. It's calculated from all parameters on JSON requests.
        # The value for 'keyword' is the search query, it should have normal spaces (like a movie title).
        data = {'ts': timeStamp, 'keyword': lowerTitle, 'sort': 'year:desc'}
        stringConstant = self._makeStringConstant(allJS)
        token = self._makeToken(data, stringConstant)

        info_url = urlparse.urljoin(self.base_link, (self.search_path % (timeStamp, token, lowerTitle)))
        # print info_url
        servers = client.request(info_url)
        jsonData = json.loads(servers)

        if jsonData:
            return stringConstant, jsonData['html'], timeStamp
        else:
            return ''

    def _createSession(self, userAgent=None, cookies=None, referer=None):
        # Try to spoof a header from a web browser.
        session = cfscrape.create_scraper()
        session.headers.update(
            {
                'Accept': self.DEFAULT_ACCEPT,
                'User-Agent': userAgent,
                'Accept-Language': 'en-US,en;q=0.5',
                'Referer': referer if referer else self.base_link + '/',
                'Upgrade-Insecure-Requests': '1',
                'DNT': '1'
            }
        )
        if cookies:
            session.cookies.update(cookies)
            session.cookies[''] = '__test'  # See _getSearch() for more info on this.

        return session

    def _cloudflareCookiesToDict(self, session):
        return {
            '__cfduid': session.cookies['__cfduid'],
            'cf_clearance': session.cookies['cf_clearance']
        }

    # Token algorithm, present in "all.js".
    # ----------------------------------------------------------
    # You can get to it more quickly by searching for "Number(" in that JS file, one of
    # the occurrences will be in that section.
    # The references in the functions below were beautified with https://beautifier.io.
    #
    # To actually find it in the future in case they change it, you need to use the
    # Javascript debugger of your browser (like Firefox etc.), setting a breakpoint
    # at a specific query handler of an ajax request. It's called every time you type
    # something in the search field.
    # From then on you go step by step with the debugger, using Step-Overs mostly, and
    # then start to Step-In when you reach a part with "encode URI", as it's getting close.
    # Keep stepping until your reach some functions that that use the Math and Number classes.

    def _getTimeStamp(self, html):
        return re.search(r'<html data-ts="(.*?)"', html, re.DOTALL).group(1)

    def _r(self, c):
        '''
        Reference:
        function r() {
            return Jf + Jd + Iy + Jd + y + Jd + Su
        }
        '''
        return c['Tv'] + c['k_'] + c['Pm'] + c['k_'] + c['pf'] + c['k_'] + c['Zu']

    def _e(self, t):
        '''
        Reference:
        function e(t) {
            var i, n = 0;
            for (i = 0; i < t[R]; i++) n += t[Sb + Jd + yc + Jd + dl](i) + i;
            return n
        }
        '''
        return sum(ord(t[i]) + i for i in xrange(len(t)))

    def _makeStringConstant(self, allJS):
        '''
        Assumes the key names of the constants will stay the same.
        If they change 'all.js' in the future you'll need to update these names
        to the ones used in the r() function.
        '''
        return self._r(
            {
                key: re.search(r'\b%s=\"(.*?)\"' % key, allJS, re.DOTALL).group(1)
                for key in ('Tv', 'k_', 'Pm', 'pf', 'Zu')
            }
        )

    def _makeToken(self, params, stringConstant):
        '''
        Reference:
        i[u](function(t) {
            var n = function(t) {
                var n, o, s = e(r()),
                    u = {},
                    f = {};
                f[c] = Jd + a, o = i[Eh](!0, {}, t, f);
                for (n in o) Object[In][rf + Jd + sg + Jd + _p][Hp](o, n) && (s += e(function(t, i) {
                    var n, r = 0;
                    for (n = 0; n < Math[Xe](t[R], i[R]); n++) r += n < i[R] ? i[Sb + Jd + yc + Jd + dl](n) : 0, r += n < t[R] ? t[Sb + Jd + yc + Jd + dl](n) : 0;
                    return Number(r)[ku + Jd + ix](16)
                }(r() + n, o[n])));
                return u[c] = a, u[h] = s, u
        :returns: An integer token.
        '''

        def __convolute(t, i):
            iLen = len(i)
            tLen = len(t)
            r = 0
            for n in xrange(max(tLen, iLen)):
                r += ord(i[n]) if n < iLen else 0
                r += ord(t[n]) if n < tLen else 0
            return self._e(hex(r)[2:])  # Skip two characters to ignore the '0x' from the Python hex string.

        s = self._e(stringConstant)
        for key in params.iterkeys():
            s += __convolute(stringConstant + key, params[key])
        return s
