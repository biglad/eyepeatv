# -*- coding: UTF-8 -*-
#######################################################################
# ----------------------------------------------------------------------------
# "THE BEER-WARE LICENSE" (Revision 42):
# @tantrumdev wrote this file.  As long as you retain this notice you can do whatever you want with this
# stuff. Just please ask before copying. If we meet some day, and you think
# this stuff is worth it, you can buy me a beer in return. - Muad'Dib
# ----------------------------------------------------------------------------
#######################################################################


import re
import traceback

from resources.lib.modules import cleantitle, client, log_utils


class source:
    def __init__(self):
        self.priority = 1
        self.language = ['en']
        self.domains = ['filmxy.me']
        self.base_link = 'https://www.filmxy.one/'
        self.search_link = '/%s-%s'

    def movie(self, imdb, title, localtitle, aliases, year):
        try:
            title = cleantitle.geturl(title)
            url = self.base_link + self.search_link % (title, year)
            return url
        except Exception:
            failure = traceback.format_exc()
            log_utils.log('FilmXY - Exception: \n' + str(failure))
            return

    def filter_host(self, host):
        if host not in ['openload.co', 'yourupload.com', 'streamango.com', 'rapidvideo.com', 'uptobox.com',
                        'streamcherry.com', 'vidoza.net', 'vcstream.to', 'uptostream.com', 'vidcloud.co']:
            return False
        return True

    def sources(self, url, hostDict, hostprDict):
        try:
            sources = []

            if url is None:
                return sources
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'}
            result = client.request(url, headers=headers)
            streams = re.compile('data-player="&lt;iframe src=&quot;(.+?)&quot;', re.DOTALL).findall(result)

            for link in streams:
                host = link.split('//')[1].replace('www.', '')
                host = host.split('/')[0].lower()
                if not self.filter_host(host):
                    continue
                sources.append({'source': host, 'quality': '720p', 'language': 'en',
                                'url': link, 'direct': False, 'debridonly': False})

            return sources
        except Exception:
            failure = traceback.format_exc()
            log_utils.log('FilmXY - Exception: \n' + str(failure))
            return sources

    def resolve(self, url):
        return url
