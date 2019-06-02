import os,xbmc
import xbmcplugin
import kodi
from BeautifulSoup import BeautifulSoup
import urllib2
import urllib
import webbrowser
import resolveurl as urlresolver
import xbmcgui
import xbmcplugin
import sys
import os
import shutil
import requests
addon_id   = 'plugin.video.livehub2'
addon_id2   = 'plugin.video.livehub2/'

icon       = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id+ '/icon.png'))
fanart     = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id+ '/fanart.jpg'))
logfile    = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id+ '/log.txt'))
plugin_path=xbmc.translatePath(os.path.join('special://home/addons/' + addon_id+"/"))
HOME     = xbmc.translatePath('special://userdata/addon_data/plugin.video.streamlink-earthcam/')
file     = os.path.join(HOME, 'urls.lst')

hectoricon = icon
iconimage = icon
import random
header1 = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:20.0) Gecko/20100101 Firefox/20.0"}
header2 = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"}
header3 = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36 OPR/38.0.2220.41"}
header4 = {"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1"}

header = header4

from resources.root import android
#android.cat()
def home():
    #addDir('','url',0,icon,fanart,'')
    #ServerChecker()
    #addDir('[COLOR white][B][/COLOR][/B]','url',0,icon,fanart,'')
    addDir('[B][COLOR gold]Welcome To Neeko [/COLOR][COLOR white][/COLOR][/B]','','',icon,fanart,'')
    addDir('','','',icon,fanart,'')
    addDir('[B][COLOR gold]Neeko: [/COLOR][COLOR white]UK TV[/COLOR][/B] (IPTV)','url',6670,icon,fanart,'')
    addDir('[B][COLOR gold]Neeko: [/COLOR][COLOR white]USA TV[/COLOR][/B] (IPTV)','url',6671,icon,fanart,'')
    addDir('[B][COLOR gold]Neeko: [/COLOR][COLOR white]USA Cable TV[/COLOR][/B] (IPTV)','url',6667,icon,fanart,'')
    addDir('[B][COLOR gold]Neeko: [/COLOR][COLOR white]Sports Channels[/COLOR][/B] (IPTV)','url',6672,icon,fanart,'')
    #addDir('[B][COLOR gold]Vista: [/COLOR][COLOR white][B]Requisition Movies On Demand[/COLOR][/B]','url',5007,icon,fanart,'')
    #addDir('[B][COLOR gold]Vista: [/COLOR][COLOR white][B]Requisition TV On Demand[/COLOR][/B]','url',5008,icon,fanart,'')
    addDir('[B][COLOR gold]Neeko: [/COLOR][COLOR white]Movie / TV On Demand[/COLOR][/B] (Torrents)','url',2001,icon,fanart,'')
    addDir('[B][COLOR gold]Neeko: [/COLOR][COLOR white]Sports On Demand[/COLOR][/B] (Torrents)','url',8888,icon,fanart,'')
    addDir('[B][COLOR gold]Neeko: [/COLOR][COLOR white]Movies On Demand[/COLOR][/B] (Direct H265 Only)','url',2015,icon,fanart,'')
    addDir('[B][COLOR gold]Neeko: [/COLOR][COLOR white]Movies On Demand[/COLOR][/B] (Direct)','url',2016,icon,fanart,'')
    addDir('[B][COLOR gold]Neeko: [/COLOR][COLOR white]Movies On Demand 2[/COLOR][/B] (Direct)','url',2018,icon,fanart,'')
    addDir('[B][COLOR gold]Neeko: [/COLOR][COLOR white]Anim On Demand[/COLOR][/B] (Direct)','url',2017,icon,fanart,'')
    #addDir('[B][COLOR gold]Neeko: [/COLOR][COLOR white]Live TV[/COLOR][/B] (IPTV)','url',6666,icon,fanart,'')
    addDir('[B][COLOR gold]Neeko: [/COLOR][COLOR white]24/7 TV Shows[/COLOR][/B] (IPTV)','url',6668,icon,fanart,'')
    addDir('[B][COLOR gold]Neeko: [/COLOR][COLOR white]24/7 Movies[/COLOR][/B] (IPTV)','url',6669,icon,fanart,'')
    addDir('[B][COLOR gold]Neeko: [/COLOR][COLOR white]CCTV & WebCams[/COLOR][/B] (IPTV)','url',5151,icon,fanart,'')
    addDir('[B][COLOR gold]Neeko: [/COLOR][COLOR white]Clear Cache[/COLOR][/B]','url',8889,icon,fanart,'')
    addDir('','','',icon,fanart,'')
    addDir('Powered by VistaTV.me','','',icon,fanart,'')
    #addDir('VoD Add-ons','','',icon,fanart,'')
    #addDir('[COLOR white][B]Elysium Movies[/COLOR][/B]','url',3000,icon,fanart,'')
    #addDir('[COLOR white][B]Elysium TV[/COLOR][/B]','url',4000,icon,fanart,'')
    #addDir('[COLOR white][B]Covenant Movies[/COLOR][/B]','url',5000,icon,fanart,'')
    #addDir('[COLOR white][B]Covenant TV[/COLOR][/B]','url',5001,icon,fanart,'')    
    #addDir('[COLOR white][B]Poseidon Movies[/COLOR][/B]','url',5002,icon,fanart,'')
    #addDir('[COLOR white][B]Poseidon TV[/COLOR][/B]','url',5003,icon,fanart,'')
    #addDir('[COLOR white][B]Exodus Movies[/COLOR][/B]','url',5004,icon,fanart,'')
    #addDir('[COLOR white][B]Exodus TV[/COLOR][/B]','url',5005,icon,fanart,'')
    #addDir('[COLOR white][B]TV Player[/COLOR][/B]','url',5006,icon,fanart,'')

    
def LiveMenu():#
    addDir('[B][COLOR gold]Neeko: [/COLOR][COLOR white]IPTV[/COLOR][/B]','url',2000,icon,fanart,'')
    addDir('[B][COLOR gold]Neeko: [/COLOR][COLOR white]IPTV UK Geo Locked[/COLOR][/B] (BBCi)','url',1000,icon,fanart,'')
    
def play(url,name,pdialogue=None):
        xbmc.log("BASE URL"+str(url),2)
        if xbmc.getCondVisibility('Player.HasMedia'):
            xbmc.Player().stop()
        from resources.modules import resolvers
        import xbmcgui
        
        url = url.strip()

        url = resolvers.resolve(url)
        if url == 'False':xbmcgui.Dialog().notification('A','This Link is Down, Try Another')
        if url.endswith('m3u8'):
            xbmc.log("M3U8"+str(url),2)
            from resources.root import iptv
            iptv.listm3u(url)
        else:
                
            liz = xbmcgui.ListItem(name, iconImage=iconimage, thumbnailImage=iconimage)
            liz.setInfo(type='Video', infoLabels={'Title':name})
            liz.setProperty("IsPlayable","true")
            liz.setPath(url)

            if url.lower().startswith('plugin') and 'youtube' not in  url.lower():
                xbmc.executebuiltin('XBMC.PlayMedia('+url+')') 
                for i in range(8):
                    xbmc.sleep(500) ##sleep for 10 seconds, half each time
                    try:
                        #print 'condi'
                        if xbmc.getCondVisibility("Player.HasMedia") and xbmc.Player().isPlaying():
                            return True
                    except: pass
                print 'returning now'
                return False
            if url.lower().startswith('plugin') and 'sportsdevil' in  url.lower():
                xbmc.log("SD Player!!!"+str(url),2)
                xbmc.executebuiltin('XBMC.PlayMedia('+url+')') 
                for i in range(9):
                    xbmc.sleep(500) ##sleep for 10 seconds, half each time
                    try:
                        #print 'condi'
                        if xbmc.getCondVisibility("Player.HasMedia") and xbmc.Player().isPlaying():
                            return True
                    except: pass
                print 'returning now'
                return False
            elif url.endswith('.ts'):
                playf4m(url,name)
                from resources.modules import  CustomPlayer
                import time

                player = CustomPlayer.MyXBMCPlayer()
                if (xbmc.Player().isPlaying() == 0):
                    quit()
                try:
                   
                        if player.urlplayed:
                            print 'yes played'
                            return
                        if time.time()-beforestart>4: return False
                    #xbmc.sleep(1000)
                except: pass

                print 'returning now'
                return False
            from resources.modules import  CustomPlayer
            import time

            player = CustomPlayer.MyXBMCPlayer()
            player.pdialogue=pdialogue
            start = time.time() 
            #xbmc.Player().play( liveLink,listitem)
            print 'going to play'
            import time
            beforestart=time.time()
            player.play( url, liz)
            xbmc.log("Custom Player!!!"+str(url),2)
            if (xbmc.Player().isPlaying() == 0):
                quit()
            try:
                while player.is_active:
                    xbmc.sleep(600)
                   
                    if player.urlplayed:
                        print 'yes played'
                        return
                    if time.time()-beforestart>4: return False
                    #xbmc.sleep(1000)
            except: pass
            print 'not played',url
            xbmc.Player().stop()
            return
        
        
def playf4m(url, name):
                import urlparse,json
                if not any(i in url for i in ['.f4m', '.ts', '.m3u8']): raise Exception()
                ext = url.split('?')[0].split('&')[0].split('|')[0].rsplit('.')[-1].replace('/', '').lower()
                if not ext: ext = url
                if not ext in ['f4m', 'ts', 'm3u8']: raise Exception()

                params = urlparse.parse_qs(url)

                try: proxy = params['proxy'][0]
                except: proxy = None

                try: proxy_use_chunks = json.loads(params['proxy_for_chunks'][0])
                except: proxy_use_chunks = True

                try: maxbitrate = int(params['maxbitrate'][0])
                except: maxbitrate = 0

                try: simpleDownloader = json.loads(params['simpledownloader'][0])
                except: simpleDownloader = False

                try: auth_string = params['auth'][0]
                except: auth_string = ''


                try:
                   streamtype = params['streamtype'][0]
                except:
                   if ext =='ts': streamtype = 'TSDOWNLOADER'
                   elif ext =='m3u8': streamtype = 'HLS'
                   else: streamtype = 'HDS'

                try: swf = params['swf'][0]
                except: swf = None

                from F4mProxy import f4mProxyHelper
                return f4mProxyHelper().playF4mLink(url, name, proxy, proxy_use_chunks, maxbitrate, simpleDownloader, auth_string, streamtype, False, swf)
        
def log(text):
    file = open(logfile,"w+")
    file.write(str(text))
    
    

        
def regex_from_to(text, from_string, to_string, excluding=True):
    import re,string
    if excluding:
        try: r = re.search("(?i)" + from_string + "([\S\s]+?)" + to_string, text).group(1)
        except: r = ''
    else:
        try: r = re.search("(?i)(" + from_string + "[\S\s]+?" + to_string + ")", text).group(1)
        except: r = ''
    return r


def regex_get_all(text, start_with, end_with):
    import re
    r = re.findall("(?i)(" + start_with + "[\S\s]+?" + end_with + ")", text)
    return r





def addDir(name,url,mode,iconimage,fanart,description):
    import xbmcgui,xbmcplugin,urllib,sys
    u=sys.argv[0]+"?url="+url+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&description="+urllib.quote_plus(description)
    ok=True
    liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
    liz.setInfo( type="Video", infoLabels={"Title": name,"Plot":description})
    liz.setProperty('fanart_image', fanart)
    if mode==87:
        liz.setProperty("IsPlayable","true")
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
    else:
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
    return ok
    xbmcplugin.endOfDirectory


def OPEN_URL(url):
    import requests
    headers = {}
    headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
    link = requests.session().get(url, headers=headers, verify=False).text
    link = link.encode('ascii', 'ignore')
    return link
    
    
    

def ServerChecker():
    import requests,base64
    try:
        requests.get(base64.b64decode('aHR0cDovL2FmZmlsaWF0ZS5lbnRpcmV3ZWIuY29tL3NjcmlwdHMvY3owNm5mP2E9Y2VyZWJyb3R2JmFtcDtiPWM3ZmJiZDkzJmFtcDtkZXN0dXJsPWh0dHAlM0ElMkYlMkZtdHZiLmNvLnVrJTJGcCUyRg=='),headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0'},verify=False,timeout=4).text
    except:
        pass
        
        
def main_menu2(search):
    #kodi.refresh_container()
    kodi.create_item({'mode': ""}, '[COLOR gold]Search Results: [/COLOR]', is_folder=False, is_playable=False)
    #kodi.create_item({'mode': MODES.SEARCH}, '[COLOR green]Search[/COLOR]', is_folder=False, is_playable=False)
    GetTorLinks(search)
    #kodi.set_content('files')
    #kodi.end_of_directory(cache_to_disc=False)
    
def main_menu4():
    basefolder = "http://avadl.uploadt.com/DL7/Film/X265/"
    #kodi.refresh_container()
    kodi.create_item({'mode': ""}, '[COLOR gold]H265 Movies List: [/COLOR]', is_folder=False, is_playable=False)
    #kodi.create_item({'mode': MODES.SEARCH}, '[COLOR green]Search[/COLOR]', is_folder=False, is_playable=False)
    GetFolderList("http://avadl.uploadt.com/DL7/Film/X265/")
    #kodi.set_content('files')
    #kodi.end_of_directory(cache_to_disc=False)
    
def main_menu5():
    basefolder = "http://avadl.uploadt.com/DL7/Film/"
    #kodi.refresh_container()
    kodi.create_item({'mode': ""}, '[COLOR gold]Movies List (some H265): [/COLOR]', is_folder=False, is_playable=False)
    #kodi.create_item({'mode': MODES.SEARCH}, '[COLOR green]Search[/COLOR]', is_folder=False, is_playable=False)
    GetFolderList2("http://avadl.uploadt.com/DL7/Film/")
    #kodi.set_content('files')
    #kodi.end_of_directory(cache_to_disc=False)
    
def main_menu6():
    basefolder = "http://avadl.uploadt.com/DL7/Animation/"
    #kodi.refresh_container()
    kodi.create_item({'mode': ""}, '[COLOR gold]Animation: [/COLOR]', is_folder=False, is_playable=False)
    #kodi.create_item({'mode': MODES.SEARCH}, '[COLOR green]Search[/COLOR]', is_folder=False, is_playable=False)
    GetFolderList3("http://avadl.uploadt.com/DL7/Animation/")
    #kodi.set_content('files')
    #kodi.end_of_directory(cache_to_disc=False)
    
def main_menu7():
    #kodi.refresh_container()
    kodi.create_item({'mode': ""}, '[COLOR gold]Animation: [/COLOR]', is_folder=False, is_playable=False)
    #kodi.create_item({'mode': MODES.SEARCH}, '[COLOR green]Search[/COLOR]', is_folder=False, is_playable=False)
    GetArcron24("https://www.arconaitv.us/index.php#shows")
    #kodi.set_content('files')
    #kodi.end_of_directory(cache_to_disc=False)
        
        
def GetTorLinks(url):
    r = requests.get(url, headers=header)
    plain_text = r.text
    soup = BeautifulSoup(plain_text)
    for link in soup.findAll('a'):
        #xbmc.log( link.get('href') , 2)
        if "magnet" in link.get('href'):
            name = link.get('href').split("&dn=")
            name = name[1].split("&tr=")
            link = link.get('href')
            lable = urllib.unquote(name[0]).decode('utf8')
            make_link(link, link, lable.replace('.', ' ').replace('+', ' ') , link)
            #xbmc.log( link.get('href') , 2)
            
def GetArcron24(url):
    HOME     = xbmc.translatePath('special://userdata/')
    file     = os.path.join(HOME, '24-7.xml')
    with open(file, "w") as myfile:
        myfile.write("")
    addDir('[B][COLOR gold]Vista: [/COLOR][COLOR white]Clear Cache[/COLOR][/B]','url',8889,icon,fanart,'')
    basefolder = "plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url=https://www.arconaitv.us/"
    r = requests.get(url, headers=header)
    plain_text = r.text

    soup = BeautifulSoup(plain_text)

    for a in soup.findAll('div', {"class":"stream-nav cable"}): 
        for link in a.findAll('a'):
            #xbmc.log(str(link),2)
            title = link.get('title')
            if title == None: title = "Random Stream"
            if "stream.php" in link.get('href'):
                #name = link.get('href').split("&dn=")
                link = link.get('href')
                name = ""+title
                #link = "https://www.arconaitv.us/".str(link)
                #name = str(link.get('href'))
                #name = link# "VistaTV"            
                #lable="TEST" #lable = urllib.unquote(name[0]).decode('utf8')
                #make_link3(name, basefolder+link, name, name)
                #xbmc.log(basefolder+link , 2)
                xmldata = "\r<item>\r<title>[COLOR white]"+name+"[/COLOR]</title>\r<link>"+basefolder+link+"</link>\r<thumbnail>http://vistatv.online/buildrepo-1/icon.png</thumbnail>\r<info></info>\r<fanart>http://vistatv.online/buildrepo-1/zips/plugin.video.vista-iptv-scraper/fanart.jpg</fanart>\r</item>\r"
                with open(file, "a") as myfile:
                    myfile.write(xmldata+"\n")
                xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.vista-iptv-scraper/?fanart=http%3a%2f%2fvistatv.online%2fbuildrepo-1%2fzips%2fplugin.video.vista-iptv-scraper%2ffanart.jpg&mode=9999",return)')
               
                
def GetArcron24shows(url):
    counter1 = 0
    HOME     = xbmc.translatePath('special://userdata/')
    file     = os.path.join(HOME, '24-7.xml')
    with open(file, "w") as myfile:
        myfile.write("")
    #xbmc.executebuiltin('PlayerControl(stop)') 
    #xbmc.executebuiltin("Notification([COLOR=gold]Cerebro TV[/COLOR],This Channel May Take A Few Clicks Checking 5 Servers,7000,"+icon+")")
    addDir('[B][COLOR gold]Vista: [/COLOR][COLOR white]Clear Cache[/COLOR][/B]','url',8889,icon,fanart,'')
    basefolder = "plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url=https://www.arconaitv.us/"
    r = requests.get(url, headers=header)
    plain_text = r.text

    soup = BeautifulSoup(plain_text)
    dp = xbmcgui.DialogProgress()
    dp.create("[COLOR=white][B]VistaTV[/COLOR][/B]","[B][COLOR=red]Getting Streams[/COLOR][/B]",str(counter1))
    for a in soup.findAll('div', {"class":"stream-nav shows"}): 
        for link in a.findAll('a'):
            #xbmc.log(str(link),2)
            title = link.get('title')
            if title == None: title = "Random Stream"
            if "stream.php" in link.get('href'):
                #name = link.get('href').split("&dn=")
                link = link.get('href')
                name = "24/7 - "+title
                #link = "https://www.arconaitv.us/".str(link)
                #name = str(link.get('href'))
                #name = link# "VistaTV"            
                #lable="TEST" #lable = urllib.unquote(name[0]).decode('utf8')
                #make_link3(name, basefolder+link, name, name)
                dp.create("[COLOR=white][B]VistaTV[/COLOR][/B]","[B][COLOR=red]Getting Streams[/COLOR][/B]",name+" ("+str(counter1)+")")
                xbmc.sleep(50)
                counter1=counter1+1
                dp.update(counter1)
                xmldata = "\r<item>\r<title>[COLOR white]"+name+"[/COLOR]</title>\r<link>"+basefolder+link+"</link>\r<thumbnail>http://vistatv.online/buildrepo-1/icon.png</thumbnail>\r<info></info>\r<fanart>http://vistatv.online/buildrepo-1/zips/plugin.video.vista-iptv-scraper/fanart.jpg</fanart>\r</item>\r"
                with open(file, "a") as myfile:
                    myfile.write(xmldata+"\n")
    dp.close()
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.vista-iptv-scraper/?fanart=http%3a%2f%2fvistatv.online%2fbuildrepo-1%2fzips%2fplugin.video.vista-iptv-scraper%2ffanart.jpg&mode=9999",return)')
def GetArcron24movies(url):
    HOME     = xbmc.translatePath('special://userdata/')
    file     = os.path.join(HOME, '24-7.xml')
    with open(file, "w") as myfile:
        myfile.write("")
    addDir('[B][COLOR gold]Vista: [/COLOR][COLOR white]Clear Cache[/COLOR][/B]','url',8889,icon,fanart,'')
    basefolder = "plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url=https://www.arconaitv.us/"
    r = requests.get(url, headers=header)
    plain_text = r.text

    soup = BeautifulSoup(plain_text)

    for a in soup.findAll('div', {"class":"stream-nav movies"}): 
        for link in a.findAll('a'):
            #xbmc.log(str(link),2)
            title = link.get('title')
            if title == None: title = "Random Stream"
            if "stream.php" in link.get('href'):
                #name = link.get('href').split("&dn=")
                link = link.get('href')
                name = "24/7 - "+title
                #link = "https://www.arconaitv.us/".str(link)
                #name = str(link.get('href'))
                #name = link# "VistaTV"            
                #lable="TEST" #lable = urllib.unquote(name[0]).decode('utf8')
                #make_link3(name, basefolder+link, name, name)
                #xbmc.log(basefolder+link , 2)
                xmldata = "\r<item>\r<title>[COLOR white]"+name+"[/COLOR]</title>\r<link>"+basefolder+link+"</link>\r<thumbnail>http://vistatv.online/buildrepo-1/icon.png</thumbnail>\r<info></info>\r<fanart>http://vistatv.online/buildrepo-1/zips/plugin.video.vista-iptv-scraper/fanart.jpg</fanart>\r</item>\r"
                with open(file, "a") as myfile:
                    myfile.write(xmldata+"\n")
                xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.vista-iptv-scraper/?fanart=http%3a%2f%2fvistatv.online%2fbuildrepo-1%2fzips%2fplugin.video.vista-iptv-scraper%2ffanart.jpg&mode=9999",return)')
                
                
def GetShadowNet(url):
    addDir('[B][COLOR gold]Vista: [/COLOR][COLOR white]Clear Cache[/COLOR][/B]','url',8889,icon,fanart,'')
    basefolder = "plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url="
    r = requests.get(url, headers=header)
    plain_text = r.text
    counter = 1
    soup = BeautifulSoup(plain_text)
    #xbmc.log(str(soup),2)
    for a in soup.findAll('div', {"class":"Block CategoryContent Moveable Panel"}): 
        for link in a.findAll('a'):
            
            xbmc.log(str(link),2)
            
            if "channels" in link.get('href'):
                if "png" in link.get('href'): continue
                #name = link.get('href').split("&dn=")
                if counter > 1:
                    counter = 1
                    continue
                link = link.get('href')
                name = link.split("channels/")
                name = name[1].split(".")
                name = name[0].replace("-", " ")
                counter = counter+1
                #link = "https://www.arconaitv.us/".str(link)
                #name = str(link.get('href'))
                #name = link# "VistaTV"            
                #lable="TEST" #lable = urllib.unquote(name[0]).decode('utf8')
                make_link3(name, basefolder+link, name, name)
                #xbmc.log(basefolder+link , 2)
                
    r = requests.get("http://www.sdw-net.me/categories/UK-Channels/?sort=featured&page=2", headers=header)
    plain_text = r.text
    counter = 1
    soup = BeautifulSoup(plain_text)
    #xbmc.log(str(soup),2)
    for a in soup.findAll('div', {"class":"Block CategoryContent Moveable Panel"}): 
        for link in a.findAll('a'):
            
            xbmc.log(str(link),2)
            
            if "channels" in link.get('href'):
                if "png" in link.get('href'): continue
                #name = link.get('href').split("&dn=")
                if counter > 1:
                    counter = 1
                    continue
                link = link.get('href')
                name = link.split("channels/")
                name = name[1].split(".")
                name = name[0].replace("-", " ")
                counter = counter+1
                #link = "https://www.arconaitv.us/".str(link)
                #name = str(link.get('href'))
                #name = link# "VistaTV"            
                #lable="TEST" #lable = urllib.unquote(name[0]).decode('utf8')
                make_link3(name, basefolder+link, name, name)
                #xbmc.log(basefolder+link , 2)
                
    r = requests.get("http://www.sdw-net.me/categories/UK-Channels/?sort=featured&page=3", headers=header)
    plain_text = r.text
    counter = 1
    soup = BeautifulSoup(plain_text)
    #xbmc.log(str(soup),2)
    for a in soup.findAll('div', {"class":"Block CategoryContent Moveable Panel"}): 
        for link in a.findAll('a'):
            
            xbmc.log(str(link),2)
            
            if "channels" in link.get('href'):
                if "png" in link.get('href'): continue
                #name = link.get('href').split("&dn=")
                if counter > 1:
                    counter = 1
                    continue
                link = link.get('href')
                name = link.split("channels/")
                name = name[1].split(".")
                name = name[0].replace("-", " ")
                counter = counter+1
                #link = "https://www.arconaitv.us/".str(link)
                #name = str(link.get('href'))
                #name = link# "VistaTV"            
                #lable="TEST" #lable = urllib.unquote(name[0]).decode('utf8')
                make_link3(name, basefolder+link, name, name)
                #xbmc.log(basefolder+link , 2)
                
def GetShadowNet2(url):
    addDir('[B][COLOR gold]Vista: [/COLOR][COLOR white]Clear Cache[/COLOR][/B]','url',8889,icon,fanart,'')
    basefolder = "plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url="
    r = requests.get(url, headers=header)
    plain_text = r.text
    counter = 1
    soup = BeautifulSoup(plain_text)
    #xbmc.log(str(soup),2)
    for a in soup.findAll('div', {"class":"Block CategoryContent Moveable Panel"}): 
        for link in a.findAll('a'):
            
            xbmc.log(str(link),2)
            
            if "channels" in link.get('href'):
                if "png" in link.get('href'): continue
                #name = link.get('href').split("&dn=")
                if counter > 1:
                    counter = 1
                    continue
                link = link.get('href')
                name = link.split("channels/")
                name = name[1].split(".")
                name = name[0].replace("-", " ")
                name = name.replace("%26", "&")
                counter = counter+1
                #link = "https://www.arconaitv.us/".str(link)
                #name = str(link.get('href'))
                #name = link# "VistaTV"            
                #lable="TEST" #lable = urllib.unquote(name[0]).decode('utf8')
                make_link3(name, basefolder+link, name, name)
                #xbmc.log(basefolder+link , 2)
                
    basefolder = "plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url="
    r = requests.get("http://www.sdw-net.me/categories/USA-Channels/?sort=featured&page=2", headers=header)
    plain_text = r.text
    counter = 1
    soup = BeautifulSoup(plain_text)
    #xbmc.log(str(soup),2)
    for a in soup.findAll('div', {"class":"Block CategoryContent Moveable Panel"}): 
        for link in a.findAll('a'):
            
            xbmc.log(str(link),2)
            
            if "channels" in link.get('href'):
                if "png" in link.get('href'): continue
                #name = link.get('href').split("&dn=")
                if counter > 1:
                    counter = 1
                    continue
                link = link.get('href')
                name = link.split("channels/")
                name = name[1].split(".")
                name = name[0].replace("-", " ")
                name = name.replace("%26", "&")
                counter = counter+1
                #link = "https://www.arconaitv.us/".str(link)
                #name = str(link.get('href'))
                #name = link# "VistaTV"            
                #lable="TEST" #lable = urllib.unquote(name[0]).decode('utf8')
                make_link3(name, basefolder+link, name, name)
                #xbmc.log(basefolder+link , 2)
                
    basefolder = "plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url="
    r = requests.get("http://www.sdw-net.me/categories/USA-Channels/?sort=featured&page=3", headers=header)
    plain_text = r.text
    counter = 1
    soup = BeautifulSoup(plain_text)
    #xbmc.log(str(soup),2)
    for a in soup.findAll('div', {"class":"Block CategoryContent Moveable Panel"}): 
        for link in a.findAll('a'):
            
            xbmc.log(str(link),2)
            
            if "channels" in link.get('href'):
                if "png" in link.get('href'): continue
                #name = link.get('href').split("&dn=")
                if counter > 1:
                    counter = 1
                    continue
                link = link.get('href')
                name = link.split("channels/")
                name = name[1].split(".")
                name = name[0].replace("-", " ")
                name = name.replace("%26", "&")
                counter = counter+1
                #link = "https://www.arconaitv.us/".str(link)
                #name = str(link.get('href'))
                #name = link# "VistaTV"            
                #lable="TEST" #lable = urllib.unquote(name[0]).decode('utf8')
                make_link3(name, basefolder+link, name, name)
                #xbmc.log(basefolder+link , 2)
                
                
    basefolder = "plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url="
    r = requests.get("http://www.sdw-net.me/categories/USA-Channels/?sort=featured&page=4", headers=header)
    plain_text = r.text
    counter = 1
    soup = BeautifulSoup(plain_text)
    #xbmc.log(str(soup),2)
    for a in soup.findAll('div', {"class":"Block CategoryContent Moveable Panel"}): 
        for link in a.findAll('a'):
            
            xbmc.log(str(link),2)
            
            if "channels" in link.get('href'):
                if "png" in link.get('href'): continue
                #name = link.get('href').split("&dn=")
                if counter > 1:
                    counter = 1
                    continue
                link = link.get('href')
                name = link.split("channels/")
                name = name[1].split(".")
                name = name[0].replace("-", " ")
                name = name.replace("%26", "&")
                counter = counter+1
                #link = "https://www.arconaitv.us/".str(link)
                #name = str(link.get('href'))
                #name = link# "VistaTV"            
                #lable="TEST" #lable = urllib.unquote(name[0]).decode('utf8')
                make_link3(name, basefolder+link, name, name)
                #xbmc.log(basefolder+link , 2)
                
                
def GetShadowNet3(url):
    addDir('[B][COLOR gold]Vista: [/COLOR][COLOR white]Clear Cache[/COLOR][/B]','url',8889,icon,fanart,'')
    basefolder = "plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url="
    r = requests.get(url, headers=header)
    plain_text = r.text
    counter = 1
    counter1 = 1
    soup = BeautifulSoup(plain_text)
    dp = xbmcgui.DialogProgress()
    dp.create("[COLOR=white][B]VistaTV[/COLOR][/B]","[B][COLOR=red]Getting Streams[/COLOR][/B]",str(counter1))
    #xbmc.log(str(soup),2)
    for a in soup.findAll('div', {"class":"Block CategoryContent Moveable Panel"}): 
        for link in a.findAll('a'):           
            if "channels" in link.get('href'):
                if "png" in link.get('href'): continue
                #name = link.get('href').split("&dn=")
                dp.create("[COLOR=white][B]VistaTV[/COLOR][/B]","[B][COLOR=red]Getting Streams[/COLOR][/B]",str(counter1))
                counter1=counter1+1
                if counter > 1:
                    counter = 1
                    continue
                link = link.get('href')
                name = link.split("channels/")
                name = name[1].split(".")
                name = name[0].replace("-", " ")
                name = name.replace("%26", "&")
                counter = counter+1
                #link = "https://www.arconaitv.us/".str(link)
                #name = str(link.get('href'))
                #name = link# "VistaTV"            
                #lable="TEST" #lable = urllib.unquote(name[0]).decode('utf8')
                make_link3(name, basefolder+link, name, name)
                #xbmc.log(basefolder+link , 2)
                
    r = requests.get("http://www.sdw-net.me/categories/SPORTS-Channels/?sort=featured&page=2", headers=header)
    plain_text = r.text
    counter = 1
    soup = BeautifulSoup(plain_text)
    #xbmc.log(str(soup),2)
    for a in soup.findAll('div', {"class":"Block CategoryContent Moveable Panel"}): 
        for link in a.findAll('a'):
            
            
            if "channels" in link.get('href'):
                if "png" in link.get('href'): continue
                #name = link.get('href').split("&dn=")
                dp.create("[COLOR=white][B]VistaTV[/COLOR][/B]","[B][COLOR=red]Getting Streams[/COLOR][/B]",str(counter1))
                counter1=counter1+1
                if counter > 1:
                    counter = 1
                    continue
                link = link.get('href')
                name = link.split("channels/")
                name = name[1].split(".")
                name = name[0].replace("-", " ")
                counter = counter+1
                #link = "https://www.arconaitv.us/".str(link)
                #name = str(link.get('href'))
                #name = link# "VistaTV"            
                #lable="TEST" #lable = urllib.unquote(name[0]).decode('utf8')
                make_link3(name, basefolder+link, name, name)
                #xbmc.log(basefolder+link , 2)
                
    r = requests.get("http://www.sdw-net.me/categories/SPORTS-Channels/?sort=featured&page=2", headers=header)
    plain_text = r.text
    counter = 1
    soup = BeautifulSoup(plain_text)
    #xbmc.log(str(soup),2)
    for a in soup.findAll('div', {"class":"Block CategoryContent Moveable Panel"}): 
        for link in a.findAll('a'):
            if "channels" in link.get('href'):
                if "png" in link.get('href'): continue
                dp.create("[COLOR=white][B]VistaTV[/COLOR][/B]","[B][COLOR=red]Getting Streams[/COLOR][/B]",str(counter1))
                counter1=counter1+1
                #name = link.get('href').split("&dn=")
                if counter > 1:
                    counter = 1
                    continue
                link = link.get('href')
                name = link.split("channels/")
                name = name[1].split(".")
                name = name[0].replace("-", " ")
                counter = counter+1
                #link = "https://www.arconaitv.us/".str(link)
                #name = str(link.get('href'))
                #name = link# "VistaTV"            
                #lable="TEST" #lable = urllib.unquote(name[0]).decode('utf8')
                make_link3(name, basefolder+link, name, name)
                #xbmc.log(basefolder+link , 2)
                dp.close()
                        
            
def GetFolderList(url):
    basefolder = "http://avadl.uploadt.com/DL7/Film/X265/"
    lable = "name?"
    r = requests.get(url, headers=header)
    plain_text = r.text
    soup = BeautifulSoup(plain_text)
    for link in soup.findAll('a'):
        #xbmc.log( link.get('href') , 2)
        mlink = link.get('href')
        if ".zip" in mlink:
            continue
        if "/" in mlink:
            continue
        lable = urllib.unquote_plus(link.get('href'))
        make_link2(basefolder+mlink, basefolder+mlink, lable.replace('.', ' ').replace('+', ' ').replace('20%', ' ') , link)
            #xbmc.log( link.get('href') , 2)
            
def GetFolderList2(url):
    basefolder = "http://avadl.uploadt.com/DL7/Film/"
    lable = "name?"
    r = requests.get(url, headers=header)
    plain_text = r.text
    soup = BeautifulSoup(plain_text)
    for link in soup.findAll('a'):
        xbmc.log( link.get('href') , 2)
        mlink = link.get('href')
        if ".zip" in mlink:
            continue
        if "/" in mlink:
            continue
        lable = urllib.unquote_plus(link.get('href'))
        make_link2(basefolder+mlink, basefolder+mlink, lable.replace('.', ' ').replace('+', ' ').replace('20%', ' ') , link)
            #xbmc.log( link.get('href') , 2)
            
def GetFolderList3(url):
    basefolder = "http://avadl.uploadt.com/DL7/Animation/"
    lable = "name?"
    r = requests.get(url, headers=header)
    plain_text = r.text
    soup = BeautifulSoup(plain_text)
    for link in soup.findAll('a'):
        xbmc.log( link.get('href') , 2)
        mlink = link.get('href')
        if ".zip" in mlink:
            continue
        if "/" in mlink:
            continue
        lable = urllib.unquote_plus(link.get('href'))
        make_link2(basefolder+mlink, basefolder+mlink, lable.replace('.', ' ').replace('+', ' ').replace('20%', ' ') , link)
            #xbmc.log( link.get('href') , 2)
            
def GetFolderList4(url):
    basefolder = "http://avadl.uploadt.com/DL4/Film/"
    lable = "name?"
    r = requests.get(url, headers=header)
    plain_text = r.text
    soup = BeautifulSoup(plain_text)
    for link in soup.findAll('a'):
        xbmc.log( link.get('href') , 2)
        mlink = link.get('href')
        if ".zip" in mlink:
            continue
        if "/" in mlink:
            continue
        lable = urllib.unquote_plus(link.get('href'))
        make_link2(basefolder+mlink, basefolder+mlink, lable.replace('.', ' ').replace('+', ' ').replace('20%', ' ') , link)
            #xbmc.log( link.get('href') , 2)


def main_menu3():
    #kodi.refresh_container()
    kodi.create_item({'mode': ""}, '[COLOR gold]Pirate Bay top 200 for last 48 hours[/COLOR]', is_folder=False, is_playable=False)
    #kodi.create_item({'mode': MODES.SEARCH}, '[COLOR green]Search[/COLOR]', is_folder=False, is_playable=False)
    GetTorLinks('https://pirateproxy.id/top/200')
    #kodi.set_content('files')
    #kodi.end_of_directory(cache_to_disc=False) 

def main_menu14():
    #kodi.refresh_container()
    kodi.create_item({'mode': ""}, '[COLOR gold]Pirate Bay top 200 for last 48 hours[/COLOR]', is_folder=False, is_playable=False)
    #kodi.create_item({'mode': MODES.SEARCH}, '[COLOR green]Search[/COLOR]', is_folder=False, is_playable=False)
    GetTorLinks('https://pirateproxy.id/search/UFC/0/99/200')
    #kodi.set_content('files')
    #kodi.end_of_directory(cache_to_disc=False) 

def main_menu15():
    #kodi.refresh_container()
    kodi.create_item({'mode': ""}, '[COLOR gold]Pirate Bay top 200 for last 48 hours[/COLOR]', is_folder=False, is_playable=False)
    #kodi.create_item({'mode': MODES.SEARCH}, '[COLOR green]Search[/COLOR]', is_folder=False, is_playable=False)
    GetTorLinks('https://pirateproxy.id/search/wwe/0/99/200')
    #kodi.set_content('files')
    #kodi.end_of_directory(cache_to_disc=False) 

def Acron24():
    #kodi.refresh_container()
    kodi.create_item({'mode': ""}, '[COLOR gold]USA Cable IPTV[/COLOR]', is_folder=False, is_playable=False)
    kodi.create_item({'mode': ""}, '[COLOR orange]Streams may need more than 1 click[/COLOR]', is_folder=False, is_playable=False)
    #kodi.create_item({'mode': MODES.SEARCH}, '[COLOR green]Search[/COLOR]', is_folder=False, is_playable=False)
    GetArcron24('https://www.arconaitv.us/')
    #kodi.set_content('files')
    #kodi.end_of_directory(cache_to_disc=False)    

def Acron24tv():
    #kodi.refresh_container()
    kodi.create_item({'mode': ""}, '[COLOR gold]24/7 TV Show Streams[/COLOR]', is_folder=False, is_playable=False)
    kodi.create_item({'mode': ""}, '[COLOR orange]Streams may need more than 1 click[/COLOR]', is_folder=False, is_playable=False)
    #kodi.create_item({'mode': MODES.SEARCH}, '[COLOR green]Search[/COLOR]', is_folder=False, is_playable=False)
    GetArcron24shows('https://www.arconaitv.us/')
    #kodi.set_content('files')
    #kodi.end_of_directory(cache_to_disc=False)     
    
def Acron24movies():
    #kodi.refresh_container()
    kodi.create_item({'mode': ""}, '[COLOR gold]24/7 Movie Streams[/COLOR]', is_folder=False, is_playable=False)
    kodi.create_item({'mode': ""}, '[COLOR orange]Streams may need more than 1 click[/COLOR]', is_folder=False, is_playable=False)
    #kodi.create_item({'mode': MODES.SEARCH}, '[COLOR green]Search[/COLOR]', is_folder=False, is_playable=False)
    GetArcron24movies('https://www.arconaitv.us/')
    #kodi.set_content('files')
    #kodi.end_of_directory(cache_to_disc=False)     
    
    

def ShahowNet():
    #kodi.refresh_container()
    kodi.create_item({'mode': ""}, '[COLOR gold]UK IPTV[/COLOR]', is_folder=False, is_playable=False)
    kodi.create_item({'mode': ""}, '[COLOR orange]Streams may need more than 1 click[/COLOR]', is_folder=False, is_playable=False)
    #kodi.create_item({'mode': MODES.SEARCH}, '[COLOR green]Search[/COLOR]', is_folder=False, is_playable=False)
    GetShadowNet('http://www.sdw-net.me/categories/UK-Channels/')
    #kodi.set_content('files')
    #kodi.end_of_directory(cache_to_disc=False) 

def ShahowNet2():
    #kodi.refresh_container()
    kodi.create_item({'mode': ""}, '[COLOR gold]USA IPTV[/COLOR]', is_folder=False, is_playable=False)
    kodi.create_item({'mode': ""}, '[COLOR orange]Streams may need more than 1 click[/COLOR]', is_folder=False, is_playable=False)
    #kodi.create_item({'mode': MODES.SEARCH}, '[COLOR green]Search[/COLOR]', is_folder=False, is_playable=False)
    GetShadowNet2('http://www.sdw-net.me/categories/USA-Channels/')
    #kodi.set_content('files')
    #kodi.end_of_directory(cache_to_disc=False) 

def ShahowNet3():
    #kodi.refresh_container()
    kodi.create_item({'mode': ""}, '[COLOR gold]Sport Channels IPTV[/COLOR]', is_folder=False, is_playable=False)
    kodi.create_item({'mode': ""}, '[COLOR orange]Streams may need more than 1 click[/COLOR]', is_folder=False, is_playable=False)
    #kodi.create_item({'mode': MODES.SEARCH}, '[COLOR green]Search[/COLOR]', is_folder=False, is_playable=False)
    GetShadowNet3('http://www.sdw-net.me/categories/SPORTS-Channels/')
    #kodi.set_content('files')
    #kodi.end_of_directory(cache_to_disc=False)         

def StartTorrents(): 
    addDir('[B][COLOR gold]Neeko: [/COLOR][COLOR orange]TO USE THIS SECTION YOU MUST HAVE[/COLOR][/B]','url','',icon,fanart,'') 
    addDir('[B][COLOR gold]Neeko: [/COLOR][COLOR orange]Real-Debrid or Premiumize[/COLOR][/B]','url','',icon,fanart,'') 
    addDir('','url','',icon,fanart,'')
    addDir('[B][COLOR gold]Neeko: [/COLOR][COLOR green]Open ResolveURL Settings[/COLOR][/B] (authorize accounts)','url',5555,icon,fanart,'') 
    addDir('','url','',icon,fanart,'')  
    addDir('[B][COLOR gold]Neeko: [/COLOR][COLOR white]Pirate Bay[/COLOR][/B] (Search Movies & TV)','https://pirateproxy.id/search/',2002,icon,fanart,'')
    addDir('[B][COLOR gold]Neeko: [/COLOR][COLOR white]GlowTorrents[/COLOR][/B] (Search Movies & TV)','http://glodls.to/search_results.php?search=',2009,icon,fanart,'')
    addDir('[B][COLOR gold]Neeko: [/COLOR][COLOR white]EZTV[/COLOR][/B] (Search TV Shows)','https://eztv.io/search/',2002,icon,fanart,'')
    addDir('[B][COLOR gold]Neeko: [/COLOR][COLOR white]Pirate Bay[/COLOR][/B] (Top 200)','https://eztv.io/search/',2003,icon,fanart,'')
    addDir('','url','',icon,fanart,'')
    addDir('[B][COLOR gold]Neeko: [/COLOR][COLOR lightgreen]Click Here to Get Real-Debrid[/COLOR][/B]','url',5556,icon,fanart,'')
    addDir('[B][COLOR gold]Neeko: [/COLOR][COLOR lightgreen]Click Here to Get Premiumize[/COLOR][/B]','url',5557,icon,fanart,'')
    addDir('[B][COLOR gold]Neeko: [/COLOR][COLOR white]Clear Cache[/COLOR][/B]','url',8889,icon,fanart,'')
    
def StartTorrentsSport(): 
    addDir('[B][COLOR gold]Neeko: [/COLOR][COLOR orange]TO USE THIS SECTION YOU MUST HAVE[/COLOR][/B]','url','',icon,fanart,'') 
    addDir('[B][COLOR gold]Neeko: [/COLOR][COLOR orange]Real-Debrid or Premiumize[/COLOR][/B]','url','',icon,fanart,'') 
    addDir('','url','',icon,fanart,'')
    addDir('[B][COLOR gold]Neeko: [/COLOR][COLOR green]Open ResolveURL Settings[/COLOR][/B] (authorize accounts)','url',5555,icon,fanart,'') 
    addDir('','url','',icon,fanart,'')  
    addDir('[B][COLOR gold]Neeko: [/COLOR][COLOR white]Pirate Bay[/COLOR][/B] (UFC Replays)','http://www.magnetdl.com',2004,icon,fanart,'')
    addDir('[B][COLOR gold]Neeko: [/COLOR][COLOR white]Pirate Bay[/COLOR][/B] (WWE Replays)','http://www.magnetdl.com',2005,icon,fanart,'')
    addDir('','url','',icon,fanart,'')
    addDir('[B][COLOR gold]Neeko: [/COLOR][COLOR lightgreen]Click Here to Get Real-Debrid[/COLOR][/B]','url',5556,icon,fanart,'')
    addDir('[B][COLOR gold]Neeko: [/COLOR][COLOR lightgreen]Click Here to Get Premiumize[/COLOR][/B]','url',5557,icon,fanart,'')
    addDir('[B][COLOR gold]Neeko: [/COLOR][COLOR white]Clear Cache[/COLOR][/B]','url',8889,icon,fanart,'')
    
    
def GetEarchCam(url):
    with open(file, "w") as myfile:
        myfile.write("")
    #addDir('Shark Cam','https://www.earthcam.com/usa/maryland/baltimore/aquarium/?cam=blacktipreef',9999,icon,fanart,'')
    basefolder = "plugin://plugin.video.streamlink-tester/?action=play&url="
    #make_link3('Shark Cam',basefolder+'https://www.earthcam.com/world/uk/bognorregis/?cam=bognorregis', 'Shark Cam', 'Shark Cam')
    r = requests.get(url, headers=header)
    plain_text = r.text
    counter = 1
    soup = BeautifulSoup(plain_text)
    #xbmc.log(str(soup),2)
    dp = xbmcgui.DialogProgress()
    dp.create("[COLOR=white][B]VistaTV[/COLOR][/B]","[B][COLOR=red]Getting Streams[/COLOR][/B]",str(counter))
    for a in soup.findAll('div', {"class":"bodyContainer"}): 
        #a = sorted(a, key=str.lower)
        for link in a.findAll('a'):

            #xbmc.log(str(link),2)
            
            #if "https://www.earthcam.com/world/" in link.get('href'):
            #if "?cam=" in link.get('href'): continue
            if "usa" not in link.get('href'): continue
            if "nps" in link.get('href'): continue
            dp.create("[COLOR=white][B]VistaTV[/COLOR][/B]","[B][COLOR=red]Getting Streams[/COLOR][/B]",str(counter))
            counter=counter+1
            #name = link.get('href').split("&dn=")
            #if counter > 1:
            #    counter = 1
            #    continue
            link = link.get('href')
            name = link.split("usa/")
            #name = name[1].split(".")
            name = name[0].replace("/", " ")
            if name.startswith('/'): name = name[1:]
            #name = link
            #name = name.replace("%26", "&")
            #counter = counter+1
            #link = "https://www.arconaitv.us/".str(link)
            #name = str(link.get('href'))
            #name = link# "VistaTV"            
            #lable="TEST" #lable = urllib.unquote(name[0]).decode('utf8')
            #make_link3(name, basefolder+link, name, name)
            #xbmc.log(basefolder+link , 2)
            with open(file, "a") as myfile:
                myfile.write(link+"\n")

			
    for a in soup.findAll('div', {"class":"bodyContainer"}): 
        for link in a.findAll('a'):
            
            #xbmc.log(str(link),2)
            
            #if "https://www.earthcam.com/world/" in link.get('href'):
            #if "?cam=" in link.get('href'): continue
            if "nps" in link.get('href'): continue
            if "world" not in link.get('href'): continue
            dp.create("[COLOR=white][B]VistaTV[/COLOR][/B]","[B][COLOR=red]Getting Streams[/COLOR][/B]",str(counter))
            counter=counter+1
            #name = link.get('href').split("&dn=")
            #if counter > 1:
            #    counter = 1
            #    continue
            link = link.get('href')
            name = link.split("world")
            #name = name[1].split(".")
            name = name[0].replace("/", " ")
            if name.startswith('/'): name = name[1:]
            #name = link
            #name = name.replace("%26", "&")
            #counter = counter+1
            #link = "https://www.arconaitv.us/".str(link)
            #name = str(link.get('href'))
            #name = link# "VistaTV"            
            #lable="TEST" #lable = urllib.unquote(name[0]).decode('utf8')
            #make_link3(name, basefolder+link, name, name)
            #xbmc.log(basefolder+link , 2)
            with open(file, "a") as myfile:
                myfile.write(link+"\n")
    dp.close()
    xbmc.executebuiltin('RunAddon(plugin.video.streamlink-earthcam)')
                
def EarchCam():
    #kodi.refresh_container()
    kodi.create_item({'mode': ""}, '[COLOR gold]CCTV & WebCams[/COLOR]', is_folder=False, is_playable=False)
    #kodi.create_item({'mode': ""}, '[COLOR orange]Streams may need more than 1 click[/COLOR]', is_folder=False, is_playable=False)
    #kodi.create_item({'mode': MODES.SEARCH}, '[COLOR green]Search[/COLOR]', is_folder=False, is_playable=False)
    GetEarchCam('https://www.earthcam.com/')
    #kodi.set_content('files')
    #kodi.end_of_directory(cache_to_disc=False)   

def play_link(link):
    xbmc.log("PLay Link "+str(link),2)   
    #logger.log('Playing Link: |%s|' % (link), log_utils.LOGDEBUG)
    hmf = urlresolver.HostedMediaFile(url=link)
    if not hmf:
        #logger.log('Indirect hoster_url not supported by urlresolver: %s' % (link))
        kodi.notify('Link Not Supported: %s' % (link), duration=7500)
        return False
    #logger.log('Link Supported: |%s|' % (link), log_utils.LOGDEBUG)
    
    try:
        stream_url = hmf.resolve()
        if not stream_url or not isinstance(stream_url, basestring):
            try: msg = stream_url.msg
            except: msg = link
            raise Exception(msg)
    except Exception as e:
        try: msg = str(e)
        except: msg = link
        kodi.notify('Resolve Failed: %s' % (msg), duration=7500)
        return False
    #logger.log('Link Resolved: |%s|%s|' % (link, stream_url), log_utils.LOGDEBUG)
        
    listitem = xbmcgui.ListItem(path=stream_url)
  
    xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, listitem)

def make_link(index, link, label, path):
    menu_items = []
    queries = {'mode': "", 'index': index, 'path': path}
    menu_items.append(('Delete Link', 'RunPlugin(%s)' % (kodi.get_plugin_url(queries))),)
    queries = {'mode': "", 'index': index, 'path': path}
    menu_items.append(('Edit Link', 'RunPlugin(%s)' % (kodi.get_plugin_url(queries))),)
    kodi.create_item({'mode': 7777, 'url': link}, label, is_folder=False, is_playable=True, menu_items=menu_items)  
    
def make_link2(index, link, label, path):
    menu_items = []
    queries = {'mode': "", 'index': index, 'path': path}
    menu_items.append(('Delete Link', 'RunPlugin(%s)' % (kodi.get_plugin_url(queries))),)
    queries = {'mode': "", 'index': index, 'path': path}
    menu_items.append(('Edit Link', 'RunPlugin(%s)' % (kodi.get_plugin_url(queries))),)
    kodi.create_item({'mode': 9999, 'url': link}, label, is_folder=False, is_playable=True, menu_items=menu_items)  
    
def make_link3(index, link, label, path):
    menu_items = []
    #queries = {'mode': "", 'index': index, 'path': path}
    #menu_items.append(('Delete Link', 'RunPlugin(%s)' % (kodi.get_plugin_url(queries))),)
    #queries = {'mode': "", 'index': index, 'path': path}
    #menu_items.append(('Delete Link', 'RunPlugin(%s)' % (kodi.get_plugin_url(queries))),)
    kodi.create_item({'mode': 9998, 'url': link}, label, is_folder=False, is_playable=True, menu_items=menu_items)
    
def SearchTors(site):
        search_entered = '' 
        keyboard = xbmc.Keyboard(search_entered, 'Enter Movie / TV Show Name For Torrent Search')
        keyboard.doModal()
        if keyboard.isConfirmed():
            search_entered = keyboard.getText().replace(' ','%20')   ##search_entered = keyboard.getText().replace(' ','+')
            if search_entered == 0:
                return False        
        #if search_entered == None or search_entered == "":
        #    main_menu()   
        #xbmc.log( search_entered , 2)
        #global mysearch        
        main_menu2(site+"/"+search_entered+"") 
    
        
def SearchTors2(site):
        search_entered = '' 
        keyboard = xbmc.Keyboard(search_entered, 'Enter Movie / TV Show Name For Torrent Search')
        keyboard.doModal()
        if keyboard.isConfirmed():
            search_entered = keyboard.getText().replace(' ','+')   ##search_entered = keyboard.getText().replace(' ','+')
            if search_entered == 0:
                return False        
        #if search_entered == None or search_entered == "":
        #    main_menu()   
        xbmc.log( site+""+search_entered+"&incldead=Search&order=asc" , 2)
        #global mysearch        
        main_menu2(site+""+search_entered+"&incldead=Search&order=asc") 
        
def SearchTors3(site):
        search_entered = '' 
        keyboard = xbmc.Keyboard(search_entered, 'Enter Movie / TV Show Name For Torrent Search')
        keyboard.doModal()
        if keyboard.isConfirmed():
            search_entered = keyboard.getText().replace(' ','-')   ##search_entered = keyboard.getText().replace(' ','+')
            if search_entered == 0:
                return False        
        #if search_entered == None or search_entered == "":
        #    main_menu()   
        #xbmc.log( search_entered , 2)
        #global mysearch        
        main_menu2(site+"/"+search_entered+"") 
    
def get_params():
    param=[]
    paramstring=sys.argv[2]
    if len(paramstring)>=2:
        params=sys.argv[2]
        cleanedparams=params.replace('?','')
        if (params[len(params)-1]=='/'):
            params=params[0:len(params)-2]
        pairsofparams=cleanedparams.split('&')
        param={}
        for i in range(len(pairsofparams)):
            splitparams={}
            splitparams=pairsofparams[i].split('=')
            if (len(splitparams))==2:
                param[splitparams[0]]=splitparams[1]
    return param
params=get_params()
url=None
name=None
mode=None
iconimage=None
description=None
query=None
type=None
# OpenELEQ: query & type-parameter (added 2 lines above)


def platform():
    if xbmc.getCondVisibility('system.platform.android'):
        return 'android'
    elif xbmc.getCondVisibility('system.platform.linux'):
        return 'linux'
    elif xbmc.getCondVisibility('system.platform.windows'):
        return 'windows'
    elif xbmc.getCondVisibility('system.platform.osx'):
        return 'osx'
    elif xbmc.getCondVisibility('system.platform.atv2'):
        return 'atv2'
    elif xbmc.getCondVisibility('system.platform.ios'):
        return 'ios'

myplatform = platform()






def MainH(): 
    addDir("Welcome to Hector!", "", "", hectoricon)
    addDir("", "", "", hectoricon)
    addDir("[COLOR gold]EPG IPTV CHANNELS[/COLOR]", "http://vistatv.online/VistaEPG.m3u", 3, hectoricon)
    data = urllib2.urlopen("http://www.vistatv.online/m3u8/").read()
    data = data.split("\n") # then split it into lines
    count = 1
    for line in data:
        #line = line.split(" ") 
        addDir("[COLOR green]Hectors IPTV Server[/COLOR] :[COLOR gold]"+str(count)+"[/COLOR]", str(line), 2, hectoricon)
        #xbmc.log(str(line),2)
        count = count+1
    xbmcplugin.endOfDirectory(int(sys.argv[1]))











import urllib

try:
    url=urllib.unquote_plus(params["url"])
except:
    pass
try:
    name=urllib.unquote_plus(params["name"])
except:
    pass
try:
    iconimage=urllib.unquote_plus(params["iconimage"])
except:
    pass
try:
    mode=int(params["mode"])
except:
    pass
try:
    description=urllib.unquote_plus(params["description"])
except:
    pass
try:
    query=urllib.unquote_plus(params["query"])
except:
    pass
try:
    type=urllib.unquote_plus(params["type"])
except:
    pass
# OpenELEQ: query & type-parameter (added 8 lines above)

if mode==None or url==None or len(url)<1:
    home()


elif mode==1:
    from resources.root import ukgeo
    ukgeo.get(url)
    
    
elif mode==2:
    from resources.root import webscrapers
    webscrapers.get(url)
    
    
elif mode==3:
    from resources.root import iptv
    iptv.get(url)
    
elif mode==4:
    from resources.root import android
    android.get(url)
    
    
elif mode==50:
    from resources.root import iptv
    iptv.listm3u(url)
    

    
elif mode==10:
    play(url,name)
    


elif mode==1000:
    from resources.root import ukgeo
    ukgeo.cat()
    
elif mode==2000:
    from resources.root import webscrapers
    android.cat()
    
elif mode==2001:
    StartTorrents()
    
elif mode==2002:
    SearchTors(url)
    
elif mode==2003:
    main_menu3()
    
elif mode==2004:
    main_menu14()
    
elif mode==2005:
    main_menu15()
    
elif mode==2009:
    SearchTors2(url)
    
elif mode==2015:
    main_menu4()
    
elif mode==2016:
    main_menu5()
    
elif mode==2017:
    main_menu6()
    
elif mode==2018:
    main_menu7()

elif mode==3000:
    #from resources.root import iptv
    #iptv.cat()
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.elysium/?action=movieNavigator",return)')
    
elif mode==4000:
    #from resources.root import android
    #android.cat()
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.elysium/?action=tvNavigator",return)')
    
elif mode==5000:
    #from resources.root import android
    #android.cat()
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.covenant/?action=movieNavigator",return)')
    
elif mode==5001:
    #from resources.root import android
    #android.cat()
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.covenant/?action=tvNavigator",return)')
    
elif mode==5002:
    #from resources.root import android
    #android.cat()
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.poseidon/?action=movieNavigator",return)')
    
elif mode==5003:
    #from resources.root import android
    #android.cat()
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.poseidon/?action=tvNavigator",return)')

elif mode==5004:
    #from resources.root import android
    #android.cat()
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.exodus/?action=movieNavigator",return)')

elif mode==5005:
    #from resources.root import android
    #android.cat()
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.exodus/?action=tvNavigator",return)')
    
elif mode==5006:
    #from resources.root import android
    #android.cat()
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://script.module.streamhublive/?description&iconimage=http%3a%2f%2fwww.broadbandtvnews.com%2fwp-content%2fuploads%2f2017%2f04%2fTVPlayer.png&mode=1&name=%5bCOLOR%20white%5d%5bB%5dTv%20Player%5b%2fCOLOR%5d%5b%2fB%5d&url=tvplayer",return)')

elif mode==5007:
    #from resources.root import android
    #android.cat()
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.vistatvshowbox/?action=movieNavigator",return)')
    
elif mode==5008:
    #from resources.root import android
    #android.cat()
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.vistatvshowbox/?action=tvNavigator",return)')
    
elif mode == 5555:
    #urlresolver.display_settings()
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.vistatv247/?fanart=http%3a%2f%2fvistatv.me%2fbuildrepo-1%2ffanart.jpg&mode=1&name=%5bI%5d%5bCOLORgold%5dAuthorize%20RealDebrid%5b%2fI%5d%5b%2fCOLOR%5d&url=http%3a%2f%2fftp.vistatv.online%2fbuildrepo-1%2fto-be-cleaned-up-ed%2fsuper%2520old%2520stuff%2f9534958459845345%2fsdfdsfdsfdsfsdfsfdsf%2f1%2f2%2flol%2fwtf%2fReal%2520Debrid.xml",return)')


    
elif mode == 5556:
    if myplatform == 'android': # Android 
        opensite = xbmc.executebuiltin( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( 'http:/\real-debrid.com/?id=2183316' ) )
    else:
        opensite = webbrowser . open('http:/\real-debrid.com/?id=2183316')
    exit()
    
elif mode == 5557:
    if myplatform == 'android': # Android 
        opensite = xbmc.executebuiltin( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( 'https://www.premiumize.me\ref/297038763' ) )
    else:
        opensite = webbrowser . open('https://www.premiumize.me\ref/297038763')
    exit()
    
elif mode == 6666:
    LiveMenu()
    
elif mode == 6667:
    Acron24()
    
elif mode == 6668:
    Acron24tv()
    
elif mode == 6669:
    Acron24movies()
    
elif mode == 6670:
    ShahowNet()
    
elif mode == 6671:
    ShahowNet2()
    
elif mode == 6672:
    ShahowNet3()
    
elif mode == 7777:
    play_link(url)
    
elif mode == 8888:
    StartTorrentsSport()
    
elif mode == 5151:
    EarchCam()
    
elif mode == 8889:
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.vistatvshowbox/?action=clearAllCache")')
    xbmc.executebuiltin("Notification(VistaTV, [B][COLOR=gold]Select YES[/COLOR] -- [COLOR=green]Then click on .. or press back[/COLOR][/B],10000,)")
    
elif mode==9998:
    
    xbmc.executebuiltin('PlayerControl(stop)') 
    xbmc.sleep(1000)
    import xbmcgui,xbmcplugin
    liz = xbmcgui.ListItem(name, iconImage=iconimage, thumbnailImage=iconimage)
    liz.setInfo(type='Video', infoLabels='24.7')
    liz.setProperty("IsPlayable","true")
    liz.setPath(url)
    try: xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, liz)
    except: pass
    #exit()
        


    
elif mode==9999:
    import xbmcgui,xbmcplugin
    from resources.modules import resolvers
    url = resolvers.resolve(url)
    liz = xbmcgui.ListItem(name, iconImage=iconimage, thumbnailImage=iconimage)
    liz.setInfo(type='Video', infoLabels='')
    liz.setProperty("IsPlayable","true")
    liz.setPath(url)
    xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, liz)
    exit()

    

    

import xbmcplugin
xbmcplugin.endOfDirectory(int(sys.argv[1]))