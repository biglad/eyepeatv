import urllib,urllib2,sys,re,xbmcplugin,xbmcgui,xbmcaddon,datetime,os,json,base64,plugintools,xbmc
from datetime import datetime as dtdeep
import GoDev
import common,xbmcvfs,zipfile,downloader,extract
import xml.etree.ElementTree as ElementTree
import unicodedata
import time
import string
reload(sys)
dialog       =  xbmcgui.Dialog()
sys.setdefaultencoding('utf8')
SKIN_VIEW_FOR_MOVIES="515"
addonDir = plugintools.get_runtime_path()
global kontroll
background = "YmFja2dyb3VuZC5wbmc=" 
defaultlogo = "ZGVmYXVsdGxvZ28ucG5n" 
hometheater = "aG9tZXRoZWF0ZXIuanBn"
noposter = "bm9wb3N0ZXIuanBn"
theater = "dGhlYXRlci5qcGc="
addonxml = "YWRkb24ueG1s"
addonpy = "ZGVmYXVsdC5weQ=="
icon = "aWNvbi5wbmc="
# plist = base64.b64decode(b'aHR0cDovL3d3dy52LXN0cmVhbXMuY29tL0JhY2t1cC50eHQ=')
ICON = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.eyepeatv', 'icon.png')) 
fanart = "ZmFuYXJ0LmpwZw=="
FANART = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.eyepeatv', 'fanart.jpg')) 
supplier = "RXllUGVhVFY="
HOME =  xbmc.translatePath('special://home/')
GuideLoc = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.eyepeatv', 'g')) 
Guide = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.eyepeatv', 'guide.xml')) 
lehekylg= base64.b64decode("aHR0cDovL3dhdGNoLmdvdGRhcmsuY29t") 
# pordinumber=base64.b64decode("Njk2OQ==")
message = "VU5BVVRIT1JJWkVEIEVESVQgT0YgQURET04h"
kasutajanimi=plugintools.get_setting("Username")
salasona=plugintools.get_setting("Password")
addon_id = "plugin.video.eyepeatv"
BASEURL = base64.b64decode("bmFkYQ==")
LOAD_LIVEchan = os.path.join( plugintools.get_runtime_path() , "resources" , "art/arch" )

def run():
    global pnimi
    global televisioonilink
    global filmilink
    global andmelink
    global uuenduslink
    global lehekylg
    global LOAD_LIVE
    global uuendused
    global vanemalukk
    global version
    version = int(get_live("MQ=="))
    kasutajanimi=plugintools.get_setting("Username")
    salasona=plugintools.get_setting("Password")
    if not kasutajanimi:
        kasutajanimi = "NONE"
        salasona="NONE"
	
    uuendused=plugintools.get_setting(sync_data("dXVlbmR1c2Vk"))
    vanemalukk=plugintools.get_setting(sync_data("dmFuZW1hbHVraw=="))
    pnimi = get_live("T25lIFZpZXcg")
    LOAD_LIVE = os.path.join( plugintools.get_runtime_path() , "resources" , "art" )
    plugintools.log(pnimi+get_live("U3RhcnRpbmcgdXA="))
    televisioonilink = get_live("JXMvZW5pZ21hMi5waHA/dXNlcm5hbWU9JXMmcGFzc3dvcmQ9JXMmdHlwZT1nZXRfbGl2ZV9jYXRlZ29yaWVz")%(lehekylg,kasutajanimi,salasona)
    filmilink = vod_channels("JXMvZW5pZ21hMi5waHA/dXNlcm5hbWU9JXMmcGFzc3dvcmQ9JXMmdHlwZT1nZXRfdm9kX2NhdGVnb3JpZXM=")%(lehekylg,kasutajanimi,salasona)
    andmelink = vod_channels("JXMvcGFuZWxfYXBpLnBocD91c2VybmFtZT0lcyZwYXNzd29yZD0lcw==")%(lehekylg,kasutajanimi,salasona)
    params = plugintools.get_params()

    if params.get("action") is None:
        peamenyy(params)
    else:
        action = params.get("action")
        exec action+"(params)"
    plugintools.close_item_list()

def peamenyy(params):
    plugintools.log(pnimi+vod_channels("TWFpbiBNZW51")+repr(params))
    if not lehekylg:
        plugintools.open_settings_dialog()

    channels = kontroll()
    if channels == 1 and GoDev.mode != 5 and GoDev.mode != 1:
        plugintools.log(pnimi+vod_channels("TG9naW4gU3VjY2Vzcw=="))
        
        plugintools.add_item( action=vod_channels("c2VjdXJpdHlfY2hlY2s="),  title=vod_channels(supplier)+ " Live" , thumbnail=os.path.join(LOAD_LIVE,vod_channels("bGl2ZXR2LnBuZw==")) , fanart=os.path.join(LOAD_LIVE,vod_channels("YmFja2dyb3VuZC5wbmc=")) ,  folder=True )
        plugintools.add_item( action=vod_channels("ZGV0ZWN0X21vZGlmaWNhdGlvbg=="),   title="On Demand" , thumbnail=os.path.join(LOAD_LIVE,vod_channels("dm9kLnBuZw==")), fanart=os.path.join(LOAD_LIVE,vod_channels("YmFja2dyb3VuZC5wbmc=")) ,  folder=True )
        #plugintools.add_item( action=vod_channels("Ym9udXM="),   title="Bonus Content" , thumbnail=os.path.join(LOAD_LIVE,vod_channels("dm9kLnBuZw==")), fanart=os.path.join(LOAD_LIVE,vod_channels("YmFja2dyb3VuZC5wbmc=")) ,  folder=True )
        #plugintools.add_item( action=vod_channels("TGlzdGluZ3M="),   title="Listings" , thumbnail=os.path.join(LOAD_LIVE,vod_channels("dm9kLnBuZw==")), fanart=os.path.join(LOAD_LIVE,vod_channels("YmFja2dyb3VuZC5wbmc=")) ,  folder=True )
        plugintools.add_item( action=vod_channels("bWFpbnRNZW51"),   title="Maintenance Tools" , thumbnail=os.path.join(LOAD_LIVE,vod_channels("dm9kLnBuZw==")), fanart=os.path.join(LOAD_LIVE,vod_channels("YmFja2dyb3VuZC5wbmc=")) ,  folder=True )
        plugintools.add_item( action=vod_channels("VG9vbHM="),   title="Tools & Settings" , thumbnail=os.path.join(LOAD_LIVE,vod_channels("dm9kLnBuZw==")), fanart=os.path.join(LOAD_LIVE,vod_channels("YmFja2dyb3VuZC5wbmc=")) ,  folder=True )
        
    elif channels != 1 and GoDev.mode != 1:
        plugintools.add_item( action=vod_channels("bGljZW5zZV9jaGVjaw=="), title="Step 1. Insert Login Credentials" , thumbnail=os.path.join(LOAD_LIVE,vod_channels("c2V0dGluZ3MuanBn")), fanart=os.path.join(LOAD_LIVE,vod_channels("YmFja2dyb3VuZC5wbmc=")) , folder=False )	
        plugintools.add_item( action=vod_channels("bGljZW5zZV9jaGVjazI="), title="Step 2. Click Once Login Is Input" , thumbnail=os.path.join(LOAD_LIVE,vod_channels("c2V0dGluZ3MuanBn")), fanart=os.path.join(LOAD_LIVE,vod_channels("YmFja2dyb3VuZC5wbmc=")) , folder=False )	

def Tools(params):
	plugintools.add_item( action=vod_channels("ZXhlY3V0ZV9haW5mbw=="),   title="Account Information", thumbnail=os.path.join(LOAD_LIVE,vod_channels("bXlhY2MucG5n")), fanart=os.path.join(LOAD_LIVE,vod_channels("YmFja2dyb3VuZC5wbmc=")) ,  folder=True )
	#plugintools.addItem('Run Speedtest','speed',9,GoDev.Images + 'speed.png',GoDev.Images + 'background.png')
	plugintools.add_item( action=vod_channels("bGljZW5zZV9jaGVjaw=="), title="Addon Settings" , thumbnail=os.path.join(LOAD_LIVE,vod_channels("c2V0dGluZ3MucG5n")), fanart=os.path.join(LOAD_LIVE,vod_channels("YmFja2dyb3VuZC5wbmc=")) ,  folder=False )

def Listings(params):
	plugintools.add_item( action=vod_channels("U1BPUlRfTElTVElOR1M="),   title="UK Sport Listings" , thumbnail=os.path.join(LOAD_LIVE,vod_channels("dm9kLnBuZw==")), fanart=os.path.join(LOAD_LIVE,vod_channels("YmFja2dyb3VuZC5wbmc=")) ,  folder=True )
	plugintools.add_item( action=vod_channels("R29EZXYuU3BvcnRDaG9pY2U="),   title="All Sport Listings" , thumbnail=os.path.join(LOAD_LIVE,vod_channels("dm9kLnBuZw==")), fanart=os.path.join(LOAD_LIVE,vod_channels("YmFja2dyb3VuZC5wbmc=")) ,  folder=True )

def TheDev(params):

    loginurl   = base64.b64decode("JXMvZ2V0LnBocD91c2VybmFtZT0lcyZwYXNzd29yZD0lcyZ0eXBlPW0zdV9wbHVzJm91dHB1dD10cw==")%(lehekylg,kasutajanimi,salasona)
    try:
        req = urllib2.Request(loginurl,headers={"Accept" : "application/xml","User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36"})
        connection = urllib2.urlopen(req)
        print connection.getcode()
        connection.close()
        pass
        
    except urllib2.HTTPError, e:
        print e.getcode()
        dialog.ok("[COLOR white]Expired Account[/COLOR]",'[COLOR white]You cannot use this service with an expired account[/COLOR]',' ','[COLOR white]Please check your account information[/COLOR]')
        sys.exit(1)
        xbmc.executebuiltin("Dialog.Close(busydialog)")

    tvaAPI = base64.b64decode("JXMvcGFuZWxfYXBpLnBocD91c2VybmFtZT0lcyZwYXNzd29yZD0lcw==")%(lehekylg,kasutajanimi,salasona)
    link=open_url(tvaAPI)
    archivecheck = re.compile('"num":.+?,"name":"(.+?)".+?"stream_id":"(.+?)","stream_icon":"(.+?)".+?"tv_archive":(.+?).+?"tv_archive_duration":(.+?)}').findall(link)
    for kanalinimi,streamid,streamicon,tvarchive,archdays in archivecheck:
        if tvarchive == '1':
            streamicon = streamicon.replace('\/','/')
            archdays = archdays.replace('"','')

            plugintools.add_item( action=sync_data("dHZhcmNoaXZl"), title=kanalinimi , thumbnail=streamicon, extra=streamid, page=archdays, fanart=os.path.join(LOAD_LIVE,sync_data("aG9tZXRoZWF0ZXIuanBn")), isPlayable=False, folder=True )
            plugintools.set_view( plugintools.LIST )

def tvarchive(extra):
    plugintools.set_view( plugintools.EPISODES )
    extra = str(extra)
    extra = extra.replace(',','')
    days = re.compile("'page': '(.+?)'").findall(extra)
    days = str(days)
    days = days.replace("['","").replace("']","")
    days = int(days)
    streamid = re.compile("'extra': '(.+?)'").findall(extra)
    streamicon = re.compile("'thumbnail': '(.+?)'").findall(extra)
    streamid = str(streamid)
    streamid = streamid.replace("['","").replace("']","")
    streamicon = str(streamicon)
    streamicon = streamicon.replace("['","").replace("']","")
    now = str(datetime.datetime.now()).replace('-','').replace(':','').replace(' ','')
    date3 = datetime.datetime.now() - datetime.timedelta(days)
    date = str(date3)
    date = str(date).replace('-','').replace(':','').replace(' ','')
    APIv2 = base64.b64decode("JXMvcGxheWVyX2FwaS5waHA/dXNlcm5hbWU9JXMmcGFzc3dvcmQ9JXMmYWN0aW9uPWdldF9zaW1wbGVfZGF0YV90YWJsZSZzdHJlYW1faWQ9JXM=")%(lehekylg,kasutajanimi,salasona,streamid)
    link=open_url(APIv2)
    match = re.compile('"title":"(.+?)".+?"start":"(.+?)","end":"(.+?)","description":"(.+?)"').findall(link)
    for ShowTitle,start,end,DesC in match:
        ShowTitle = base64.b64decode(ShowTitle)
        DesC = base64.b64decode(DesC)
        format = '%Y-%m-%d %H:%M:%S'
        try:
            modend = dtdeep.strptime(end, format)
            modstart = dtdeep.strptime(start, format)
        except:
            modend = datetime.datetime(*(time.strptime(end, format)[0:6]))
            modstart = datetime.datetime(*(time.strptime(start, format)[0:6]))
        StreamDuration = modend - modstart
        modend_ts = time.mktime(modend.timetuple())
        modstart_ts = time.mktime(modstart.timetuple())
        FinalDuration = int(modend_ts-modstart_ts) / 60
        strstart = start
        Realstart = str(strstart).replace('-','').replace(':','').replace(' ','')
        start2 = start[:-3]
        editstart = start2
        start2 = str(start2).replace(' ',' - ')
        start = str(editstart).replace(' ',':')
        Editstart = start[:13] + '-' + start[13:]
        Finalstart = Editstart.replace('-:','-')
        if Realstart > date:
            if Realstart < now:
                catchupURL = base64.b64decode("JXMvc3RyZWFtaW5nL3RpbWVzaGlmdC5waHA/dXNlcm5hbWU9JXMmcGFzc3dvcmQ9JXMmc3RyZWFtPSVzJnN0YXJ0PQ==")%(lehekylg,kasutajanimi,salasona,streamid)
                ResultURL = catchupURL + str(Finalstart) + "&duration=%s"%(FinalDuration)
                kanalinimi = str(start2)+ " - " + ShowTitle
                plugintools.add_item( action=sync_data("cnVuX2Nyb25qb2I="), title=kanalinimi , url=ResultURL, thumbnail=streamicon , plot=DesC, fanart=os.path.join(LOAD_LIVE,sync_data("aG9tZXRoZWF0ZXIuanBn")) , extra="", isPlayable=True, folder=False )


def SPORT_LISTINGS(params):

	url = base64.b64decode(b'aHR0cDovL3d3dy53aGVyZXN0aGVtYXRjaC5jb20vdHYvaG9tZS5hc3A=')
	r = common.OPEN_URL_NORMAL(url).replace('\r','').replace('\n','').replace('\t','')
	match = re.compile('href="http://www.wheresthematch.com/fixtures/(.+?).asp.+?class="">(.+?)</em> <em class="">v</em> <em class="">(.+?)</em>.+?time-channel ">(.+?)</span>').findall(r)
	for game,team1,team2,gametime in match:
		a,b = gametime.split(" on ")
		plugintools.add_item (action="",  title='[COLOR white]'+team1+' vs '+team2+' - '+a+' [/COLOR]' , thumbnail=os.path.join(LOAD_LIVE,vod_channels("bGl2ZXR2LnBuZw==")) , fanart=os.path.join(LOAD_LIVE,vod_channels("YmFja2dyb3VuZC5wbmc=")) ,  folder=False )
		plugintools.add_item (action="",  title='[COLOR yellowgreen][B]Watch on '+b+'[/B][/COLOR]' , thumbnail=os.path.join(LOAD_LIVE,vod_channels("bGl2ZXR2LnBuZw==")) , fanart=os.path.join(LOAD_LIVE,vod_channels("YmFja2dyb3VuZC5wbmc=")) ,  folder=False )
		plugintools.add_item (action="",  title='------------------------------------------' , thumbnail=os.path.join(LOAD_LIVE,vod_channels("bGl2ZXR2LnBuZw==")) , fanart=os.path.join(LOAD_LIVE,vod_channels("YmFja2dyb3VuZC5wbmc=")) ,  folder=False )

def get_size(start_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size

def convertSize(size):
   import math
   if (size == 0):
       return '[COLOR lime]0 MB[/COLOR]'
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size,1024)))
   p = math.pow(1024,i)
   s = round(size/p,2)
   if size_name == "B" or "KB":
        return '[COLOR lime]%s %s' % (s,size_name[i]) + '[/COLOR]'
   if size_name == "GB" or "TB" or "PB" or "EB" or "ZB" or "YB":
        return '[COLOR red]%s %s' % (s,size_name[i]) + '[/COLOR]'
   if s >= 100:
        return '[COLOR red]%s %s' % (s,size_name[i]) + '[/COLOR]'
   if s < 50:
        return '[COLOR lime]%s %s' % (s,size_name[i]) + '[/COLOR]'
   if s >= 50:
        if i < 100:
            return '[COLOR orange]%s %s' % (s,size_name[i]) + '[/COLOR]'

def maintMenu(params):

	CACHE      =  xbmc.translatePath(os.path.join('special://home/cache',''))
	PACKAGES   =  xbmc.translatePath(os.path.join('special://home/addons','packages'))
	THUMBS     =  xbmc.translatePath(os.path.join('special://home/userdata','Thumbnails'))

	if not os.path.exists(CACHE):
		CACHE     =  xbmc.translatePath(os.path.join('special://home/temp',''))
	if not os.path.exists(PACKAGES):
		os.makedirs(PACKAGES)

	CACHE_SIZE_BYTE    = get_size(CACHE)
	PACKAGES_SIZE_BYTE = get_size(PACKAGES)
	THUMB_SIZE_BYTE    = get_size(THUMBS)
	
	CACHE_SIZE    = convertSize(CACHE_SIZE_BYTE)
	PACKAGES_SIZE = convertSize(PACKAGES_SIZE_BYTE)
	THUMB_SIZE    = convertSize(THUMB_SIZE_BYTE)

	startup_clean = plugintools.get_setting("acstartup")
	weekly_clean = plugintools.get_setting("clearday")

	if startup_clean == "false":
		startup_onoff = "[COLOR red]OFF[/COLOR]"
	else:
		startup_onoff = "[COLOR lime]ON[/COLOR]"
	if weekly_clean == "0":
		weekly_onoff = "[COLOR red]OFF[/COLOR]"
	else:
		weekly_onoff = "[COLOR lime]ON[/COLOR]"

	common.addItem('[COLOR white]Auto Clean Device[/COLOR]','url',19,ICON,FANART,'')
	common.addItem("[COLOR white]Clear Cache[/COLOR] - Current Size: " + str(CACHE_SIZE),BASEURL,20,ICON,FANART,'')
	common.addItem("[COLOR white]Delete Thumbnails [/COLOR] - Current Size: " + str(THUMB_SIZE),BASEURL,22,ICON,FANART,'')
	common.addItem("[COLOR white]Purge Packages [/COLOR] - Current Size: " + str(PACKAGES_SIZE),BASEURL,23,ICON,FANART,'')
	common.addItem('[COLOR white]View Current or Old Log File[/COLOR]','url',18,ICON,FANART,'')
	common.addItem('[COLOR white]View the last error in log file[/COLOR]',BASEURL,24,ICON,FANART,'')
	common.addItem('[COLOR white]View all errors in the log file[/COLOR]',BASEURL,25,ICON,FANART,'')


def license_check(params):
    plugintools.log(pnimi+get_live("U2V0dGluZ3MgbWVudQ==")+repr(params))
    plugintools.open_settings_dialog()
def license_check2(params):
	loginurl   = base64.b64decode("JXMvZ2V0LnBocD91c2VybmFtZT0lcyZwYXNzd29yZD0lcyZ0eXBlPW0zdV9wbHVzJm91dHB1dD10cw==")%(lehekylg,kasutajanimi,salasona)
	try:
		connection = urllib2.urlopen(loginurl)
		print connection.getcode()
		connection.close()
		#playlist found, user active & login correct, proceed to addon
		xbmc.executebuiltin('Container.Refresh')
		
	except urllib2.HTTPError, e:
		print e.getcode()
		#playlist not found, either expired or wrong login

		#check for expired account
		content    = GoDev.OPEN_URL(andmelink)
		match    = re.compile('"auth":(.+?)').findall(content) 

		for result in match:
			if "0" in result:
				dialog.ok('[COLOR white]Invalid Login[/COLOR]','[COLOR white]Incorrect login details found![/COLOR]','[COLOR white]Please check your spelling and case sensitivity[/COLOR]','[COLOR white]Check your password with the team otherwise[/COLOR]')
				plugintools.open_settings_dialog()
			else:
				dialog.ok("[COLOR white]Expired Login[/COLOR]",'[COLOR white]Your login has expired[/COLOR]','[COLOR white]Please review your account information[/COLOR]','[COLOR white]or contact the team[/COLOR]')
				xbmc.executebuiltin('Container.Refresh')

def security_check(params):
    plugintools.add_item( action=vod_channels("VFZzZWFyY2g="),   title="Search Live TV" , thumbnail=os.path.join(LOAD_LIVE,vod_channels("dm9kLnBuZw==")), fanart=os.path.join(LOAD_LIVE,vod_channels("YmFja2dyb3VuZC5wbmc=")) ,  folder=True )
    plugintools.log(pnimi+sync_data("TGl2ZSBNZW51")+repr(params))
    request = urllib2.Request(televisioonilink, headers={"Accept" : "application/xml","User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36"})
    u = urllib2.urlopen(request)
    tree = ElementTree.parse(u)
    rootElem = tree.getroot()
    for channel in tree.findall(sync_data("Y2hhbm5lbA==")):
        kanalinimi = channel.find(get_live("dGl0bGU=")).text
        kanalinimi = base64.b64decode(kanalinimi)
        if 'Sports Corner' in kanalinimi:
			kanalinimi = 'Sports Centre'
        kategoorialink = channel.find(vod_channels("cGxheWxpc3RfdXJs")).text
        CatID = channel.find(get_live("Y2F0ZWdvcnlfaWQ=")).text        
        plugintools.add_item( action=get_live("c3RyZWFtX3ZpZGVv"), title=kanalinimi , url=CatID , thumbnail=os.path.join(LOAD_LIVE,sync_data("bGl2ZXR2LnBuZw==")) , fanart=os.path.join(LOAD_LIVE,sync_data("dGhlYXRlci5qcGc=")) ,info_labels=kanalinimi, folder=True )
	                            
    plugintools.set_view( plugintools.LIST )

def detect_modification(params):
    plugintools.add_item( action=vod_channels("Vk9Ec2VhcmNo"),   title="Search On Demand" , thumbnail=os.path.join(LOAD_LIVE,vod_channels("dm9kLnBuZw==")), fanart=os.path.join(LOAD_LIVE,vod_channels("YmFja2dyb3VuZC5wbmc=")) ,  folder=True )
    plugintools.log(pnimi+vod_channels("Vk9EIE1lbnUg")+repr(params))
    request = urllib2.Request(filmilink, headers={"Accept" : "application/xml","User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36"})
    u = urllib2.urlopen(request)
    tree = ElementTree.parse(u)
    rootElem = tree.getroot()
    for channel in tree.findall(sync_data("Y2hhbm5lbA==")):
        filminimi = channel.find(get_live("dGl0bGU=")).text
        filminimi = base64.b64decode(filminimi)
        kategoorialink = channel.find(vod_channels("cGxheWxpc3RfdXJs")).text
        plugintools.add_item( action=vod_channels("Z2V0X215YWNjb3VudA=="), title=filminimi , url=kategoorialink , thumbnail=os.path.join(LOAD_LIVE,sync_data("dm9kLnBuZw==")) , fanart=os.path.join(LOAD_LIVE,sync_data("dGhlYXRlci5qcGc=")) , folder=True )
	
    plugintools.set_view( plugintools.LIST )

def stream_video(params):
    kasutajanimi=plugintools.get_setting("Username")
    salasona=plugintools.get_setting("Password")
    CatID = params.get(get_live("dXJs")) #description
    url = get_live("JXMvZW5pZ21hMi5waHA/dXNlcm5hbWU9JXMmcGFzc3dvcmQ9JXMmdHlwZT1nZXRfbGl2ZV9zdHJlYW1zJmNhdF9pZD0lcw==")%(lehekylg,kasutajanimi,salasona,CatID)
    request = urllib2.Request(url, headers={"Accept" : "application/xml","User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36"})
    u = urllib2.urlopen(request)
    tree = ElementTree.parse(u)
    rootElem = tree.getroot()
    for channel in tree.findall(sync_data("Y2hhbm5lbA==")): #channel
        kanalinimi = channel.find(get_live("dGl0bGU=")).text #title
        kanalinimi = base64.b64decode(kanalinimi)
        kanalinimi = kanalinimi.partition("[")
        striimilink = channel.find(get_live("c3RyZWFtX3VybA==")).text #stream_url
        pony = striimilink
        if ("%s/enigma2.php")%(lehekylg)  in striimilink: 
            pony = striimilink.split(kasutajanimi,1)[1]
            pony = pony.split(salasona,1)[1]
            pony = pony.split("/",1)[1]            
        pilt = channel.find(vod_channels("ZGVzY19pbWFnZQ==")).text #desc_image
        kava = kanalinimi[1]+kanalinimi[2]
        kava = kava.partition("]")
        kava = kava[2]
        kava = kava.partition("   ")
        kava = kava[2]
        shou = get_live("W0NPTE9SIHdoaXRlXSVzIFsvQ09MT1JdW0NPTE9SIGdvbGRdJXMgWy9DT0xPUl0=")%(kanalinimi[0],kava)
        kirjeldus = channel.find(sync_data("ZGVzY3JpcHRpb24=")).text #description
        if kirjeldus:
           kirjeldus = base64.b64decode(kirjeldus)
           nyyd = kirjeldus.partition("(")
           nyyd = sync_data("Tm93OiA=") +nyyd[0]
           jargmine = kirjeldus.partition(")\n")
           jargmine = jargmine[2].partition("(")
           jargmine = sync_data("TmV4dDog") +jargmine[0] #shou
           kokku = nyyd+jargmine
        else:
           kokku = ""
        if pilt:
           plugintools.add_item( action=sync_data("cnVuX2Nyb25qb2I="), title=shou , url=pony, thumbnail=pilt, plot=kokku, fanart=os.path.join(LOAD_LIVE,sync_data("dGhlYXRlci5qcGc=")), extra="", isPlayable=True, folder=False )
        else:
           plugintools.add_item( action=sync_data("cnVuX2Nyb25qb2I="), title=shou , url=pony, thumbnail=os.path.join(LOAD_LIVE,vod_channels("YWxsY2hhbm5lbHMucG5n")) , plot=kokku, fanart=os.path.join(LOAD_LIVE,sync_data("dGhlYXRlci5qcGc=")) , extra="", isPlayable=True, folder=False )

    plugintools.set_view( plugintools.EPISODES )
	
    kodi_name = common.KODI_VERSION()

    if kodi_name == "Jarvis":
        xbmc.executebuiltin("Container.SetViewMode(504)")
    elif kodi_name == "Krypton":
        xbmc.executebuiltin("Container.SetViewMode(55)")
    else: xbmc.executebuiltin("Container.SetViewMode(50)")

def read_file(filename):
    readfile = open(filename, 'r')
    content  = readfile.read()
    readfile.close()
    return content

def Open_URL(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 10.0; WOW64; Windows NT 5.1; en-GB; rv:1.9.0.3')
    response    = urllib2.urlopen(req)
    link        = response.read()
    response.close()
    return link.replace('\n', '').replace('\t', '').replace('\r', '')

def bonus(params):
	content = Open_URL(plist)
	matches = re.compile('name="(.+?)"stream="(.+?)"').findall(content)
	for item in matches:
		name	= item[0]
		stream	= item[1]
		plugintools.addDir(title= name, icon = ICON, url = stream, fanart = FANART)

def open_url(url):
    try:
        req = urllib2.Request(url,headers={"Accept" : "application/xml","User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36"})
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        return link
    except:quit()

def VODsearch(params):
	SEARCH_LIST = base64.b64decode(b'JXMvZW5pZ21hMi5waHA/dXNlcm5hbWU9JXMmcGFzc3dvcmQ9JXMmdHlwZT1nZXRfdm9kX3N0cmVhbXMmY2F0X2lkPTA=')%(lehekylg,kasutajanimi,salasona)
	keyb = xbmc.Keyboard('', '[COLOR white]Search[/COLOR]')
	keyb.doModal()
	if (keyb.isConfirmed()):
		searchterm=keyb.getText()
		searchterm=string.capwords(searchterm)
	else:quit()
	xbmc.log('User searched for: '+ searchterm)
	link=open_url(SEARCH_LIST) 
	match = re.compile('<title>(.+?)</title><desc_image><!\[CDATA\[(.+?)\]\]></desc_image><description>(.+?)</description>.+?<stream_url><!\[CDATA\[(.+?)\]\]></stream_url>').findall(link)
	for pealkiri,pilt,kirjeldus,striimilink in match:
		pealkiri = base64.b64decode(pealkiri)
		pealkiri = pealkiri.encode("utf-8")
		if kirjeldus:
			kirjeldus = base64.b64decode(kirjeldus)
		if searchterm in pealkiri:
			xbmc.log('***************** FOUND IT *****************')
			if pilt:
				plugintools.add_item( action="restart_service", title=pealkiri , url=striimilink, thumbnail=pilt, plot=kirjeldus, fanart=os.path.join(LOAD_LIVE,sync_data("dGhlYXRlci5qcGc=")) , extra="", isPlayable=True, folder=False )
			else:
				plugintools.add_item( action="restart_service", title=pealkiri , url=striimilink, thumbnail=os.path.join("dm9kLnBuZw=="), plot=kirjeldus, fanart=os.path.join(LOAD_LIVE,sync_data("dGhlYXRlci5qcGc=")) , extra="", isPlayable=True, folder=False )

def TVsearch(params):
	SEARCH_LIST = base64.b64decode(b'JXMvZW5pZ21hMi5waHA/dXNlcm5hbWU9JXMmcGFzc3dvcmQ9JXMmdHlwZT1nZXRfbGl2ZV9zdHJlYW1zJmNhdF9pZD0w')%(lehekylg,kasutajanimi,salasona)
	keyb = xbmc.Keyboard('', '[COLOR white]Search[/COLOR]')
	keyb.doModal()
	if (keyb.isConfirmed()):
		searchterm=keyb.getText()
		searchterm=searchterm.upper()
	else:quit()
	xbmc.log('User searched for: '+ searchterm)
	request = urllib2.Request(SEARCH_LIST, headers={"Accept" : "application/xml","User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36"})
	u = urllib2.urlopen(request)
	tree = ElementTree.parse(u)
	rootElem = tree.getroot()
	for channel in tree.findall(sync_data("Y2hhbm5lbA==")): #channel
		kanalinimi = channel.find(get_live("dGl0bGU=")).text #title
		kanalinimi = base64.b64decode(kanalinimi)
		kanalinimi = kanalinimi.partition("[")
		striimilink = channel.find(get_live("c3RyZWFtX3VybA==")).text #stream_url
		pony = striimilink
		if ("%s:%s/enigma2.php")%(lehekylg) in striimilink:
			pony = striimilink.split(kasutajanimi,1)[1]
			pony = pony.split(salasona,1)[1]
			pony = pony.split("/",1)[1]			
		pilt = channel.find(vod_channels("ZGVzY19pbWFnZQ==")).text #desc_image
		kava = kanalinimi[1]+kanalinimi[2]
		kava = kava.partition("]")
		kava = kava[2]
		kava = kava.partition("   ")
		kava = kava[2]
		shou = get_live("W0NPTE9SIHdoaXRlXSVzWy9DT0xPUl0tIFtDT0xPUiBnb2xkXSVzWy9DT0xPUl0=")%(kanalinimi[0],kava)
		shou = shou.upper()
		kirjeldus = channel.find(sync_data("ZGVzY3JpcHRpb24=")).text #description
		if kirjeldus:
			kirjeldus = base64.b64decode(kirjeldus)
			nyyd = kirjeldus.partition("(")
			nyyd = sync_data("Tm93OiA=") +nyyd[0]
			jargmine = kirjeldus.partition(")\n")
			jargmine = jargmine[2].partition("(")
			jargmine = sync_data("TmV4dDog") +jargmine[0] #shou
			kokku = nyyd+jargmine
		else:
			kokku = ""
		if searchterm in shou:
			if pilt:
				plugintools.add_item( action=sync_data("cnVuX2Nyb25qb2I="), title=shou , url=pony, thumbnail=pilt, plot=kokku, fanart=os.path.join(LOAD_LIVE,sync_data("dGhlYXRlci5qcGc=")), extra="", isPlayable=True, folder=False )
			else:
				plugintools.add_item( action=sync_data("cnVuX2Nyb25qb2I="), title=shou , url=pony, thumbnail=os.path.join(LOAD_LIVE,vod_channels("YWxsY2hhbm5lbHMucG5n")) , plot=kokku, fanart=os.path.join(LOAD_LIVE,sync_data("dGhlYXRlci5qcGc=")) , extra="", isPlayable=True, folder=False )

def get_myaccount(params):
        if vanemalukk == "true":
           pealkiri = params.get("title")
           vanema_lukk(pealkiri)
        purl = params.get("url")
        request = urllib2.Request(purl, headers={"Accept" : "application/xml","User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36"})
        u = urllib2.urlopen(request)
        tree = ElementTree.parse(u)
        rootElem = tree.getroot()
        for channel in tree.findall("channel"):
            try:
                pealkiri = channel.find("title").text
                pealkiri = base64.b64decode(pealkiri)
                pealkiri = pealkiri.encode("utf-8")
                striimilink = channel.find("stream_url").text
                pilt = channel.find("desc_image").text
                kirjeldus = channel.find("description").text
                if kirjeldus:
                   kirjeldus = base64.b64decode(kirjeldus)
                if pilt:
                   plugintools.add_item( action="restart_service", title=pealkiri , url=striimilink, thumbnail=pilt, plot=kirjeldus, fanart=os.path.join(LOAD_LIVE,sync_data("dGhlYXRlci5qcGc=")) , extra="", isPlayable=True, folder=False )
                else:
                   plugintools.add_item( action="restart_service", title=pealkiri , url=striimilink, thumbnail=os.path.join("dm9kLnBuZw=="), plot=kirjeldus, fanart=os.path.join(LOAD_LIVE,sync_data("dGhlYXRlci5qcGc=")) , extra="", isPlayable=True, folder=False )
            except:
                kanalinimi = channel.find("title").text
                kanalinimi = base64.b64decode(kanalinimi)
                kategoorialink = channel.find("playlist_url").text
                plugintools._log(kategoorialink)
                CatID = channel.find("category_id").text
                plugintools.add_item( action=get_live("Z2V0X215YWNjb3VudA=="), title=kanalinimi , url=kategoorialink , thumbnail=os.path.join(LOAD_LIVE,sync_data("dm9kLnBuZw==")) , fanart=os.path.join(LOAD_LIVE,sync_data("dGhlYXRlci5qcGc=")) ,info_labels=kanalinimi, folder=True )
        plugintools.set_view( plugintools.EPISODES )

        kodi_name = common.KODI_VERSION()
        
        if kodi_name == "Jarvis":
            xbmc.executebuiltin("Container.SetViewMode(504)")
        elif kodi_name == "Krypton":
            xbmc.executebuiltin("Container.SetViewMode(55)")
        else: xbmc.executebuiltin("Container.SetViewMode(50)")


def run_cronjob(params):
    kasutajanimi=plugintools.get_setting("Username")
    salasona=plugintools.get_setting("Password")
    lopplink = params.get("url")
    if "http://"  not in lopplink: 
        lopplink = get_live("http://%s:%s/enigma.php/live/%s/%s/%s")%(lehekylg,kasutajanimi,salasona,lopplink)
        lopplink = lopplink[:-2]
        lopplink = lopplink + "ts"
    listitem = xbmcgui.ListItem(path=lopplink)
    xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, listitem)

def sync_data(channel):
    video = base64.b64decode(channel)
    return video

def restart_service(params):
    lopplink = params.get(vod_channels("dXJs"))
    plugintools.play_resolved_url( lopplink )

def grab_epg():
    req = urllib2.Request(andmelink)
    req.add_header(sync_data("VXNlci1BZ2VudA==") , vod_channels("S29kaSBwbHVnaW4gYnkgTWlra00="))
    response = urllib2.urlopen(req)
    link=response.read()
    jdata = json.loads(link.decode('utf8'))
    response.close()
    if jdata:
       plugintools.log(pnimi+sync_data("amRhdGEgbG9hZGVk"))
       return jdata
def kontroll():
    randomstring = grab_epg()
    kasutajainfo = randomstring[sync_data("dXNlcl9pbmZv")]
    kontroll = kasutajainfo[get_live("YXV0aA==")]
    return kontroll
def get_live(channel):
    video = base64.b64decode(channel)
    return video
def execute_ainfo(params):
    plugintools.log(pnimi+get_live("TXkgYWNjb3VudCBNZW51IA==")+repr(params))
    andmed = grab_epg()
    kasutajaAndmed = andmed[sync_data("dXNlcl9pbmZv")]
    seis = kasutajaAndmed[get_live("c3RhdHVz")]
    aegub = kasutajaAndmed[sync_data("ZXhwX2RhdGU=")]
    if aegub:
       aegub = datetime.datetime.fromtimestamp(int(aegub)).strftime('%d/%m/%Y %H:%M')
    else:
       aegub = vod_channels("TmV2ZXI=")
    leavemealone = kasutajaAndmed[get_live("bWF4X2Nvbm5lY3Rpb25z")]
    activecons = kasutajaAndmed[get_live("YWN0aXZlX2NvbnM=")]
    polarbears = kasutajaAndmed[sync_data("dXNlcm5hbWU=")]
    plugintools.add_item( action="",   title=sync_data("W0NPTE9SID0gd2hpdGVdVXNlcjogWy9DT0xPUl0=")+polarbears , thumbnail=os.path.join(LOAD_LIVE,vod_channels("bXlhY2MucG5n")) , fanart=os.path.join(LOAD_LIVE,sync_data("dGhlYXRlci5qcGc=")) , folder=False )
    plugintools.add_item( action="",   title=sync_data("W0NPTE9SID0gd2hpdGVdU3RhdHVzOiBbL0NPTE9SXQ==")+seis , thumbnail=os.path.join(LOAD_LIVE,vod_channels("bXlhY2MucG5n")) , fanart=os.path.join(LOAD_LIVE,sync_data("dGhlYXRlci5qcGc=")) , folder=False )
    plugintools.add_item( action="",   title=get_live("W0NPTE9SID0gd2hpdGVdRXhwaXJlczogWy9DT0xPUl0=")+aegub , thumbnail=os.path.join(LOAD_LIVE,vod_channels("bXlhY2MucG5n")) , fanart=os.path.join(LOAD_LIVE,sync_data("dGhlYXRlci5qcGc=")) , folder=False )
    plugintools.add_item( action="",   title=vod_channels("W0NPTE9SID0gd2hpdGVdTWF4IGNvbm5lY3Rpb25zOiBbL0NPTE9SXQ==")+leavemealone , thumbnail=os.path.join(LOAD_LIVE,vod_channels("bXlhY2MucG5n")) , fanart=os.path.join(LOAD_LIVE,sync_data("dGhlYXRlci5qcGc=")) , folder=False )
    plugintools.add_item( action="",   title=vod_channels("W0NPTE9SID0gd2hpdGVdQWN0aXZlIGNvbm5lY3Rpb25zOiBbL0NPTE9SXQ==")+activecons , thumbnail=os.path.join(LOAD_LIVE,vod_channels("bXlhY2MucG5n")) , fanart=os.path.join(LOAD_LIVE,sync_data("dGhlYXRlci5qcGc=")) , folder=False )
	
    plugintools.set_view( plugintools.LIST )
def vanema_lukk(name):
        plugintools.log(pnimi+sync_data("UGFyZW50YWwgbG9jayA="))
        a = 'XXX', 'Adult', 'Adults','ADULT','ADULTS','adult','adults','Porn','PORN','porn','Porn','xxx'
        if any(s in name for s in a):
           xbmc.executebuiltin((u'XBMC.Notification("Parental Lock", "Channels may contain adult content", 2000)'))
           text = plugintools.keyboard_input(default_text="", title=get_live("UGFyZW50YWwgbG9jaw=="))
           if text==plugintools.get_setting(sync_data("dmFuZW1ha29vZA==")):
              return
           else:
              exit()
        else:
           name = ""
def check_user():
    plugintools.message(get_live("RVJST1I="),vod_channels("VU5BVVRIT1JJWkVEIEVESVQgT0YgQURET04h"))
    sys.exit()

def vod_channels(channel):
    video = base64.b64decode(channel)
    return video

run()