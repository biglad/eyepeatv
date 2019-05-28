# -*- coding: utf-8 -*-

'''
    Tempest Add-on

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


import re,requests
from bs4 import BeautifulSoup
from resources.lib.modules import source_utils


class source:
    def __init__(self):
        self.priority = 1
        self.language = ['en']
        self.domain = ['tvdownload.net']
        self.base_link = 'http://tvdownload.net'
        self.search_link = '/?s=%s'

    def movie(self, imdb, title, localtitle, aliases, year):
        try:
            url = {'imdb': imdb, 'title': title, 'localtitle': localtitle, 'aliases': aliases, 'year': year}
        except:
            return

    def tvshow(self, imdb, tvdb, tvshowtitle, localtvshowtitle, aliases, year):
        try:
            url = {'imdb': imdb, 'tvdb': tvdb, 'tvshowtitle': tvshowtitle, 'year': year}
            return url
        except:
            return

    def episode(self, url, imdb, tvdb, title, premiered, season, episode):
        try:

            url['episode'] = episode
            url['season'] = season
            return url
        except:
            return

    def sources(self, url, hostDict, hostprDict):

        hostDict = hostDict + hostprDict

        sources = []
        season = url['season']
        episode = url['episode']
        if len(season) == 1:
            season = '0' + season
        if len(episode) == 1:
            episode = '0' + episode

        request = ('%s+season+%s+episode+%s' % (url['tvshowtitle'], season, episode)).replace(" ", "+")
        request = self.base_link + self.search_link % request
        request = requests.get(request).content

        soup = BeautifulSoup(request, 'html.parser')
        soup = soup.find('h2', {'class': 'title'})
        request = soup.find('a')['href']
        request = requests.get(request).content
        soup = BeautifulSoup(request, 'html.parser')
        soup = soup.find('div', {'id': 'content'})
        soup = soup.find_all('a', {'class': 'autohyperlink'})
        source_list = []

        for i in soup:
            for h in hostDict:
                if h in i['href']:
                    if not '.rar' in i['href']:
                        source_list.append(i['href'])
        for i in source_list:
            host = i.replace('www.', '')
            host = re.findall(r'://(.*?)\..*?/', host)[0]

            quality = source_utils.check_sd_url(i)

            info = source_utils.getFileType(i)
            sources.append({'source': host, 'quality': quality, 'language': 'en', 'url': i, 'info': info, 'direct': False, 'debridonly': True})

        return sources

    def resolve(self, url):
        return url
