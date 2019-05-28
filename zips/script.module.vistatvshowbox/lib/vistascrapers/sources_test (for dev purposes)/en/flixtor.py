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


import re,urllib,urlparse,json,base64
from resources.lib.modules import cleantitle
from resources.lib.modules import client
from resources.lib.modules import source_utils
from resources.lib.modules import directstream
from resources.lib.modules import cfscrape


class source:
    def __init__(self):
        self.priority = 0
        self.language = ['en']
        self.domains = ['flixtor.to']
        self.base_link = 'https://flixtor.to/'
        self.search_link = '/ajax/psearch?q=%s'
       

    def movie(self, imdb, title, localtitle, aliases, year):
        try:
            url = {'imdb': imdb, 'title': title, 'year': year}
            url = urllib.urlencode(url)
            return url
        except:
            return None

    def tvshow(self, imdb, tvdb, tvshowtitle, localtvshowtitle, aliases, year):
        try:
            url = {'imdb': imdb, 'tvdb': tvdb, 'tvshowtitle': tvshowtitle, 'year': year}
            url = urllib.urlencode(url)
            return url
        except:
            return

    def episode(self, url, imdb, tvdb, title, premiered, season, episode):
        try:
            if url == None: return
            url = urlparse.parse_qs(url)
            url = dict([(i, url[i][0]) if url[i] else (i, '') for i in url])
            url['title'],  url['season'], url['episode'], url['premiered'] = title, season, episode, premiered
            url = urllib.urlencode(url)
            return url
        except:
            return

    def sources(self, url, hostDict, locDict):

        sources = []

        try:
            if url == None: return sources

            scraper = cfscrape.create_scraper()

            data = urlparse.parse_qs(url)
            data = dict([(i, data[i][0]) if data[i] else (i, '') for i in data])
            title = data['tvshowtitle'] if 'tvshowtitle' in data else data['title']
            query = self.search_link % (urllib.quote_plus(title))
            query = urlparse.urljoin(self.base_link, query)
            result = scraper.get(query, verify=False).content
            r =  re.findall(r'href="([^"]+)".*?data-txt="([^"]+)"', result)
            r = [i for i in r if cleantitle.get(title) == cleantitle.get(i[1]) and data['year'] in i[1]]
            
            sources = []

            for i in r:                
                try:
                    if 'episode' in data:
                        s = '/season/%s/episode/%s'%(data['season'], data['episode'])
                        ref = urlparse.urljoin(self.base_link, i[0]+s)
                        id = re.findall(r'tv\/(\d+)\/',i[0])[0]
                        url = urlparse.urljoin(self.base_link, 'ajax/getvid/e/%s/%s/%s'%(id, data['season'], data['episode']))
                    else:
                        ref = urlparse.urljoin(self.base_link, i[0])                   
                        id = re.findall(r'movie\/(\d+)\/',i[0])[0]
                        url = urlparse.urljoin(self.base_link, 'ajax/getvid/m/%s'%id)
                    
                    tmp = scraper.get(ref, verify=False)
                    scraper.headers['Referer'] = ref
                    scraper.headers['X-Requested-With'] = 'XMLHttpRequest'
                    scraper.headers['Cookie'] = ''
                    try:
                        for key, value in scraper.cookies.iteritems(): 
                            scraper.headers['Cookie'] += '%s=%s;'%(key, value)                     
                    except:
                        pass

                    res = scraper.get(url, verify=False).content

                    res = base64.b64decode(res.decode("rot13"))
                    res = json.loads(res)
                    res2 = scraper.get(res['file'], verify=False).content
                    streams = re.findall(r'#EXT-X-STREAM-INF.*NAME="([^"]+)"\s*(\/.*)',res2)
                    host = 'https://'+urlparse.urlparse(res['file']).netloc
                    for stream in streams:
                        sources.append({'source': 'CDN', 'quality': source_utils.label_to_quality(stream[0]), 'language': 'en', 'url': urlparse.urljoin(host,stream[1]), 'direct': True, 'debridonly': False}) 
              
                except:
                    pass

            return sources
        except Exception as e:
            return sources

    def resolve(self, url):
        return url
