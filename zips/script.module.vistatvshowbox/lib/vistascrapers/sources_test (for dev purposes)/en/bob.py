# -*- coding: UTF-8 -*-
#######################################################################
 # ----------------------------------------------------------------------------
 # "THE BEER-WARE LICENSE" (Revision 42):
 # @tantrumdev wrote this file.  As long as you retain this notice you
 # can do whatever you want with this stuff. If we meet some day, and you think
 # this stuff is worth it, you can buy me a beer in return. - Muad'Dib
 # ----------------------------------------------------------------------------
#######################################################################

# #Cerebro ShowBox Scraper
#Cerebro ShowBox Scraper
# Addon Provider: MuadDib

import re,urllib,urlparse,base64
import requests

from resources.lib.modules import client

class source:
    def __init__(self):
        self.priority = 1
        self.language = ['en']
        self.domains = ['bobmovies.net']
        self.base_link = 'https://bobmovies.net/'
        self.search_link = '%s/search?q=bobmovies.net+%s+%s'
        self.goog = 'https://www.google.co.uk'

    def movie(self, imdb, title, localtitle, aliases, year):
        try:
            url = {'imdb': imdb, 'title': title, 'year': year}
            url = urllib.urlencode(url)
            return url
        except:
            return

    def sources(self, url, hostDict, hostprDict):
        try:
            if url == None: return
            sources = []
            urldata = urlparse.parse_qs(url)
            urldata = dict((i, urldata[i][0]) for i in urldata)
            title = urldata['title']
            year = urldata['year']

            scrape = title.lower().replace(' ','+').replace(':', '')

            start_url = self.search_link %(self.goog,scrape,year)
            headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'}

            html = client.request(start_url,headers=headers)
            results = re.compile('href="(.+?)"',re.DOTALL).findall(html)
            for url in results:
                if self.base_link in url:
                    if scrape.replace('+','-') in url:
                        if 'webcache' in url:
                            continue
                        sources = self.scrape_results(url, title, year)
                        return sources
            return sources
        except:
            return sources

    def scrape_results(self,url,title,year):
        sources = []
        try:
            headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'}
            html = client.request(url,headers=headers)
            
            chktitle = re.compile('property="og:title" content="(.+?)" ',re.DOTALL).findall(html)[0]
            if title.lower() == chktitle.lower():
                vidpage = re.compile('id="tab-movie".+?data-file="(.+?)"',re.DOTALL).findall(html)
            
                for link in vidpage:
                    if 'trailer' not in link.lower():
                        link = self.base_link + link
                        sources.append({'source':'DirectLink','quality':'HD','language': 'en','url':link,'info':[],'direct':True,'debridonly':False})
            return sources   
        except:
            return sources

    def resolve(self, url):
        return url


