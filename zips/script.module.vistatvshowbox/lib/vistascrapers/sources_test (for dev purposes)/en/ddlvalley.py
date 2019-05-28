# -*- coding: UTF-8 -*-
#######################################################################
# ----------------------------------------------------------------------------
# "THE BEER-WARE LICENSE" (Revision 42):
# @tantrumdev wrote this file.  As long as you retain this notice you
# can do whatever you want with this stuff. If we meet some day, and you think
# this stuff is worth it, you can buy me a beer in return. - Muad'Dib
# ----------------------------------------------------------------------------
#######################################################################



import re
import traceback
import urllib
import urlparse

from resources.lib.modules import cfscrape, cleantitle, client, debrid, dom_parser2, log_utils


class source:
    def __init__(self):
        self.priority = 1
        self.language = ['en']
        self.domains = ['ddlvalley.me']
        self.base_link = 'http://www.ddlvalley.me'
        self.search_link = 'search/%s/'
        self.scraper = cfscrape.create_scraper()

    def movie(self, imdb, title, localtitle, aliases, year):
        try:
            clean_title = cleantitle.geturl(title).replace('-', '+').replace(': ', '+')
            url = urlparse.urljoin(self.base_link, self.search_link % clean_title).lower()
            url = {'url': url, 'title': title, 'year': year}
            url = urllib.urlencode(url)
            return url
        except Exception:
            failure = traceback.format_exc()
            log_utils.log('DDLValley - Exception: \n' + str(failure))
            return

    def tvshow(self, imdb, tvdb, tvshowtitle, localtvshowtitle, aliases, year):
        try:
            url = {'imdb': imdb, 'tvdb': tvdb, 'tvshowtitle': tvshowtitle, 'year': year}
            url = urllib.urlencode(url)
            return url
        except Exception:
            failure = traceback.format_exc()
            log_utils.log('DDLValley - Exception: \n' + str(failure))
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
            log_utils.log('DDLValley - Exception: \n' + str(failure))
            return

    def sources(self, url, hostDict, hostprDict):
        try:
            sources = []

            if url is None:
                return sources

            data = urlparse.parse_qs(url)

            data = dict([(i, data[i][0]) if data[i] else (i, '') for i in data])

            title = data['tvshowtitle'] if 'tvshowtitle' in data else data['title']

            hdlr = 'S%02dE%02d' % (int(data['season']), int(data['episode'])) if 'tvshowtitle' in data else data['year']

            query = '%s S%02dE%02d' % (data['tvshowtitle'], int(data['season']), int(data['episode'])) if\
                'tvshowtitle' in data else '%s %s' % (data['title'], data['year'])

            url = self.search_link % urllib.quote_plus(query).lower()
            url = urlparse.urljoin(self.base_link, url)

            headers = {
                'Referer': 'www.ddlvalley.me/?s=',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'en-US,en;q=0.9',
                'User-Agent':
                'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
            r = self.scraper.get(url, headers=headers).content

            items = dom_parser2.parse_dom(r, 'h2')
            items = [dom_parser2.parse_dom(i.content, 'a', req=['href', 'rel', 'data-wpel-link']) for i in items]
            items = [(i[0].content, i[0].attrs['href']) for i in items]

            hostDict = hostprDict + hostDict

            for item in items:
                try:
                    name = item[0]
                    name = client.replaceHTMLCodes(name)
                    query = query.lower().replace(' ', '-')
                    if query not in item[1]:
                        continue
                    url = item[1]
                    headers = {
                        'Referer': 'www.ddlvalley.me/search/',
                        'Accept':
                        'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                        'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'en-US,en;q=0.9',
                        'User-Agent':
                        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
                    r = self.scraper.get(url, headers=headers).content
                    links = dom_parser2.parse_dom(r, 'a', req=['href', 'rel', 'data-wpel-link'])
                    links = [i.attrs['href'] for i in links]
                    for url in links:
                        try:
                            if hdlr in name:
                                fmt = re.sub('(.+)(\.|\(|\[|\s)(\d{4}|S\d*E\d*|S\d*)(\.|\)|\]|\s)', '', name.upper())
                                fmt = re.split('\.|\(|\)|\[|\]|\s|\-', fmt)
                                fmt = [i.lower() for i in fmt]

                                if any(i.endswith(('subs', 'sub', 'dubbed', 'dub')) for i in fmt):
                                    raise Exception()
                                if any(i in ['extras'] for i in fmt):
                                    raise Exception()

                                if '2160p' in fmt:
                                    quality = '4K'
                                elif '1080p' in fmt:
                                    quality = '1080p'
                                elif '720p' in fmt:
                                    quality = '720p'
                                else:
                                    quality = 'SD'
                                if any(i in ['dvdscr', 'r5', 'r6'] for i in fmt):
                                    quality = 'SCR'
                                elif any(i in ['camrip', 'tsrip', 'hdcam', 'hdts', 'dvdcam', 'dvdts', 'cam', 'telesync', 'ts'] for i in fmt):
                                    quality = 'CAM'

                                info = []

                                if '3d' in fmt:
                                    info.append('3D')

                                try:
                                    size = re.findall('((?:\d+\.\d+|\d+\,\d+|\d+) (?:GB|GiB|MB|MiB))', name[2])[-1]
                                    div = 1 if size.endswith(('GB', 'GiB')) else 1024
                                    size = float(re.sub('[^0-9|/.|/,]', '', size))/div
                                    size = '%.2f GB' % size
                                    info.append(size)
                                except Exception:
                                    pass

                                if any(i in ['hevc', 'h265', 'x265'] for i in fmt):
                                    info.append('HEVC')

                                info = ' | '.join(info)

                                if not any(x in url for x in ['.rar', '.zip', '.iso']):
                                    url = client.replaceHTMLCodes(url)
                                    url = url.encode('utf-8')

                                    host = re.findall('([\w]+[.][\w]+)$',
                                                      urlparse.urlparse(url.strip().lower()).netloc)[0]
                                    if host in hostDict:
                                        host = client.replaceHTMLCodes(host)
                                        host = host.encode('utf-8')

                                        sources.append(
                                            {'source': host, 'quality': quality, 'language': 'en', 'url': url,
                                             'info': info, 'direct': False, 'debridonly': True})
                        except Exception:
                            pass
                except Exception:
                    pass
            check = [i for i in sources if not i['quality'] == 'CAM']
            if check:
                sources = check

            return sources
        except Exception:
            return

    def resolve(self, url):
        return url