'''
    Tempest Add-on
    **Created by Tempest**

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

'''

import re, urllib, urlparse,xbmcgui

from vistascrapers.modules import client
from vistascrapers.modules import directstream
from vistascrapers.modules import source_utils


class source:
    def __init__(self):
        self.priority = 1
        self.language = ['en']
        self.domains = ['en.downflix.win']
        self.base_link = 'http://downflix.net'
        self.search_link = '/search/%s'

    def movie(self, imdb, title, localtitle, aliases, year):
        try:
            url = {'imdb': imdb, 'title': title, 'year': year}
            url = urllib.urlencode(url)
            return url
        except:
            return

    def sources(self, url, hostDict, hostprDict):
        sources = []
        try:
            if url == None: return
            urldata = urlparse.parse_qs(url)
            urldata = dict((i, urldata[i][0]) for i in urldata)
            title = urldata['title'].lower()
            year = urldata['year']
            search_id = title.lower()
            url = urlparse.urljoin(self.base_link, self.search_link % (search_id.replace(' ', '+') + '+' + year))
            url = client.request(url)
            links = re.compile('<h1 class="h5 kisitla"><a href="(.+?//en.+?)" class=".+?">(.+?)<', re.DOTALL).findall(url)
            for link, name in links:
                if title.lower() in name.lower():
                    if year in name:
                        r = client.request(link)
                        r = re.compile('<button class="text-capitalize dropdown-item" value="(.+?)"', re.DOTALL).findall(r)
                        for i in r:
                            url = i.split("e=")[1]
                            valid, host = source_utils.is_host_valid(url, hostDict)
                            if valid:
                                sources.append( {'source': host, 'quality': '1080p', 'language': 'en', 'url': url, 'direct': False, 'debridonly': False})

            return sources
        except:
            return

    def resolve(self, url):
        return directstream.googlepass(url)
