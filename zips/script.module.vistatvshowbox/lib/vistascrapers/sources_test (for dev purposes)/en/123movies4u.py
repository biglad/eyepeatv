# -*- coding: UTF-8 -*-
# -Cleaned and Checked on 02-24-2019 by JewBMX in Scrubs.
#Created by Tempest

import re
from resources.lib.modules import client,cleantitle,source_utils


class source:
    def __init__(self):
        self.priority = 1
        self.language = ['en']
        self.domains = ['123movies4u.ch','123movies.live']
        self.base_link = 'https://123movies4u.ch'
        self.search_link = '/movie/%s'


    def movie(self, imdb, title, localtitle, aliases, year):
        try:
            title = cleantitle.geturl(title).replace('--', '-')
            url = self.base_link + self.search_link % title
            return url
        except:
            return

# https://123movies4u.ch/show/star-wars-resistance/season/1/episode/15

    def sources(self, url, hostDict, hostprDict):
        try:
            hostDict = hostDict + hostprDict
            sources = []
            r = client.request(url)
            qual = re.compile('<span class="quality">(.+?)<').findall(r)
            if 'DVD' in qual:
                quality = '720p'
            else:
                quality = 'SD'
            u = client.parseDOM(r, "div", attrs={"id": "link_list"})
            for t in u:
                u = client.parseDOM(t, 'a', ret='href')
                for url in u:
                    info = qual
                    valid, host = source_utils.is_host_valid(url, hostDict)
                    if valid:
                        sources.append({'source': host, 'quality': quality, 'language': 'en', 'info': info, 'url': url, 'direct': False, 'debridonly': False})
                return sources
        except:
            return


    def resolve(self, url):
        return url

