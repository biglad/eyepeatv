# -*- coding: utf-8 -*-

'''
    VistaTV Scraper

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
    
    thanks to MuadDib, FilmNet, Sirius & the others iv missed
'''

import re,urllib,urlparse

from resources.lib.modules import cleantitle
from resources.lib.modules import client
from resources.lib.modules import dom_parser2


class source:
    def __init__(self):
        self.priority = 1
        self.language = ['en']
        self.domains = ['watchepisodes.com','watchepisodes.unblocked.pl']
        self.base_link = 'https://watchepisodes.mrunlock.pw/'
        self.search_link = 'search/ajax_search?q=%s'

    def tvshow(self, imdb, tvdb, tvshowtitle, localtvshowtitle, aliases, year):
        try:
            t = cleantitle.geturl(tvshowtitle)
            url = urlparse.urljoin(self.base_link, t)
            url = url.encode('utf-8')
            return url
        except:
            return

    def episode(self, url, imdb, tvdb, title, premiered, season, episode):
        try:
            if url == None: return
            r = client.request(url)
            if 'The page you requested was not found!' in r:
                t = url.split('/')[-1].replace('-','+')
                r = urlparse.urljoin(self.base_link, self.search_link % t)
                r = client.request(r)
                url = re.findall('''seo['"]:['"]([^'"]+)''', r)[0]
                url = urlparse.urljoin(self.base_link, url)
                r = client.request(url)
            u = dom_parser2.parse_dom(r, 'div', {'class': 'el-item'})
            r = [(dom_parser2.parse_dom(i, 'a', req='href'), \
                  dom_parser2.parse_dom(i, 'div', {'class': 'season'}), \
                  dom_parser2.parse_dom(i, 'div', {'class': 'episode'})) \
                  for i in u]
            r = [(i[0][0].attrs['href'], re.search('(\d+)', i[1][0].content), re.search('(\d+)', i[2][0].content)) for i in r if i[0] and i[1] and i[2]]
            r = [(i[0], i[1].groups()[0], i[2].groups()[0]) for i in r if i[0] and i[1] and i[2]]
            r = [(i[0]) for i in r if i[1] == season and i[2] == episode]
            url = r[0]
            return url
        except:
            return

    def sources(self, url, hostDict, hostprDict):
        try:
            sources = []

            if url == None: return sources
            r = client.request(url)
            links = dom_parser2.parse_dom(r, 'a', req=['href','data-episodeid','data-actuallink'])
            links = [i.attrs['data-actuallink'] for i in links]
            for i in links:
                try:
                    url = i
                    url = client.replaceHTMLCodes(url)
                    url = url.encode('utf-8')
                    host = re.findall('([\w]+[.][\w]+)$', urlparse.urlparse(url.strip().lower()).netloc)[0]
                    if not host in hostDict: raise Exception()
                    host = host.encode('utf-8')
                    sources.append({'source': host, 'quality': 'SD', 'language': 'en', 'url': url, 'direct': False, 'debridonly': False})
                except:
                    pass

            return sources
        except:
            return sources

    def resolve(self, url):
        return url
