import urllib,urllib2,sys,re,xbmcplugin,xbmcgui,xbmcaddon,datetime,os,json,base64,plugintools
import xml.etree.ElementTree as ElementTree
reload(sys)
sys.setdefaultencoding('utf8')
SKIN_VIEW_FOR_MOVIES="50"
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
fanart = "ZmFuYXJ0LnBuZw=="
message = "VU5BVVRIT1JJWkVEIEVESVQgT0YgQURET04h"



def randlogin():
    data = urllib.urlopen('http://ftp.vistatv.online/codes.php?server=1&ip=aGFoYWZ1Y2t1aXZ1ZWZvcmF0dGFja2luZ21lZm9ybm9yZWFzb24=&access=bG1hb3dqeWlza29kaWNvbW1uaXR5IGlrZXRoaXM=').read()
    data = data.split(",")
    #xbmc.log(str(data),2)
    import random
    servers = data 
    return str(random.choice(servers))
	



def run():
    userdata = randlogin().split(':')
    global user
    user = userdata[0]
    passw = userdata[1]
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
    kasutajanimi=str(user) # user
    salasona=str(passw) #pass
    lehekylg='http://gorilladick4.us' # HOST
    pordinumber='2086' #port
    uuendused=plugintools.get_setting(sync_data("dXVlbmR1c2Vk"))
    vanemalukk=plugintools.get_setting(sync_data("dmFuZW1hbHVraw=="))
    pnimi = get_live("WHRyZWFtLUNvZGVzIA==")
    LOAD_LIVE = os.path.join( plugintools.get_runtime_path() , get_live("cmVzb3VyY2Vz") , vod_channels("YXJ0") )
    plugintools.log(pnimi+get_live("U3RhcnRpbmcgdXA="))
    televisioonilink = get_live("JXM6JXMvZW5pZ21hMi5waHA/dXNlcm5hbWU9JXMmcGFzc3dvcmQ9JXMmdHlwZT1nZXRfbGl2ZV9jYXRlZ29yaWVz")%(lehekylg,pordinumber,kasutajanimi,salasona)
    filmilink = vod_channels("JXM6JXMvZW5pZ21hMi5waHA/dXNlcm5hbWU9JXMmcGFzc3dvcmQ9JXMmdHlwZT1nZXRfdm9kX2NhdGVnb3JpZXM=")%(lehekylg,pordinumber,kasutajanimi,salasona)
    andmelink = vod_channels("JXM6JXMvcGFuZWxfYXBpLnBocD91c2VybmFtZT0lcyZwYXNzd29yZD0lcw==")%(lehekylg,pordinumber,kasutajanimi,salasona)
    uuenduslink = get_live("aHR0cHM6Ly93d3cuZHJvcGJveC5jb20vcy83ZW0yNHdkMXBkZGlkcW8vdmVyc2lvbi50eHQ/ZGw9MQ==")
    if get_live("WHRyZWFtLUNvZGVz") not in open(addonDir+"/"+sync_data("YWRkb24ueG1s")).read():
       check_user()
    params = plugintools.get_params()
    
    if params.get("action") is None:
        peamenyy(params)
    else:
        action = params.get("action")
        exec action+"(params)"

    plugintools.close_item_list()
def peamenyy(params):
    plugintools.log(pnimi+vod_channels("TWFpbiBNZW51")+repr(params))
    load_channels()
    if not lehekylg:
       plugintools.open_settings_dialog()
    if uuendused == "true":
       kontrolli_uuendusi()
    channels = kontroll()
    if channels == 1:
       plugintools.log(pnimi+vod_channels("TG9naW4gU3VjY2Vzcw=="))
       plugintools.add_item( action=vod_channels("ZXhlY3V0ZV9haW5mbw=="),   title=vod_channels("TXkgQWNjb3VudA==") , thumbnail="" , fanart=os.path.join(LOAD_LIVE,vod_channels("YmFja2dyb3VuZC5wbmc=")) , folder=True )
       plugintools.add_item( action=vod_channels("c2VjdXJpdHlfY2hlY2s="),  title=vod_channels("TGl2ZSBUVg==") , thumbnail="" , fanart=os.path.join(LOAD_LIVE,vod_channels("YmFja2dyb3VuZC5wbmc=")) , folder=True )
       plugintools.add_item( action=vod_channels("ZGV0ZWN0X21vZGlmaWNhdGlvbg=="),   title=vod_channels("VmlkZW8gT24gRGVtYW5k") , thumbnail="" , fanart=os.path.join(LOAD_LIVE,vod_channels("YmFja2dyb3VuZC5wbmc=")) , folder=True )
       plugintools.add_item( action=vod_channels("bGljZW5zZV9jaGVjaw=="), title=vod_channels("U2V0dGluZ3M=") , thumbnail="" , fanart=os.path.join(LOAD_LIVE,vod_channels("YmFja2dyb3VuZC5wbmc=") ), folder=False )
       plugintools.set_view( plugintools.LIST )
    else:
       plugintools.log(pnimi+vod_channels("TG9naW4gU3VjY2Vzcw=="))
       plugintools.add_item( action=vod_channels("ZXhlY3V0ZV9haW5mbw=="),   title=vod_channels("TXkgQWNjb3VudA==") , thumbnail="" , fanart=os.path.join(LOAD_LIVE,vod_channels("YmFja2dyb3VuZC5wbmc=")) , folder=True )
       plugintools.add_item( action=vod_channels("c2VjdXJpdHlfY2hlY2s="),  title=vod_channels("TGl2ZSBUVg==") , thumbnail="" , fanart=os.path.join(LOAD_LIVE,vod_channels("YmFja2dyb3VuZC5wbmc=")) , folder=True )
       plugintools.add_item( action=vod_channels("ZGV0ZWN0X21vZGlmaWNhdGlvbg=="),   title=vod_channels("VmlkZW8gT24gRGVtYW5k") , thumbnail="" , fanart=os.path.join(LOAD_LIVE,vod_channels("YmFja2dyb3VuZC5wbmc=")) , folder=True )
       plugintools.add_item( action=vod_channels("bGljZW5zZV9jaGVjaw=="), title=vod_channels("U2V0dGluZ3M=") , thumbnail="" , fanart=os.path.join(LOAD_LIVE,vod_channels("YmFja2dyb3VuZC5wbmc=") ), folder=False )
       plugintools.set_view( plugintools.LIST )

def license_check(params):
    plugintools.log(pnimi+get_live("U2V0dGluZ3MgbWVudQ==")+repr(params))
    plugintools.open_settings_dialog()
def security_check(params):
    plugintools.log(pnimi+sync_data("TGl2ZSBNZW51")+repr(params))
    request = urllib2.Request(televisioonilink, headers={"Accept" : "application/xml"})
    u = urllib2.urlopen(request)
    tree = ElementTree.parse(u)
    rootElem = tree.getroot()
    plugintools.add_item( action="restart_service", title="[B][COLOR gold]EPTV Preview[/COLOR][/B]" , url="http://", thumbnail="VISTA", plot="VISTA", fanart="" , extra="", isPlayable=False, folder=False )
    plugintools.add_item( action="restart_service", title="[B][COLOR orange]To Get Stable[/COLOR][/B]" , url="http://", thumbnail="VISTA", plot="VISTA", fanart="" , extra="", isPlayable=False, folder=False )
    plugintools.add_item( action="restart_service", title="[B][COLOR orange]IPTV With No Buffering[/COLOR][/B]" , url="http://", thumbnail="VISTA", plot="VISTA", fanart="" , extra="", isPlayable=False, folder=False )
    plugintools.add_item( action="restart_service", title="[B][COLOR orange]Or Cut Outs And More Content![/COLOR][/B]" , url="http://", thumbnail="VISTA", plot="VISTA", fanart="" , extra="", isPlayable=False, folder=False )
    plugintools.add_item( action="restart_service", title="[B][COLOR green]goto www.eptv.co.uk[/COLOR][/B]" , url="http://", thumbnail="VISTA", plot="VISTA", fanart="" , extra="", isPlayable=False, folder=False )
    plugintools.add_item( action="", title="[I][COLOR grey]To Connect to a New Server[/COLOR][/I]" , url="http://", thumbnail="VISTA", plot="VISTA", fanart="" , extra="", isPlayable=False, folder=False )
    plugintools.add_item( action="", title="[I][COLOR grey]Press Back and Go Back In!![/COLOR][/I]" , url="http://", thumbnail="VISTA", plot="VISTA", fanart="" , extra="", isPlayable=False, folder=False )
    plugintools.add_item( action="", title="[B][COLOR grey]Connected to Server: [/COLOR][COLOR green]"+str(user)+"[/COLOR][/B]" , url="http://", thumbnail="VISTA", plot="VISTA", fanart="" , extra="", isPlayable=False, folder=False )
    for channel in tree.findall(sync_data("Y2hhbm5lbA==")):
        kanalinimi = channel.find(get_live("dGl0bGU=")).text
        kanalinimi = base64.b64decode(kanalinimi)
        kategoorialink = channel.find(vod_channels("cGxheWxpc3RfdXJs")).text
        plugintools.add_item( action=get_live("c3RyZWFtX3ZpZGVv"), title=kanalinimi , url=kategoorialink , thumbnail=os.path.join(LOAD_LIVE,sync_data("bG9nby5wbmc=")) , fanart="" , folder=True )
    plugintools.set_view( plugintools.LIST )
def detect_modification(params):
    plugintools.log(pnimi+vod_channels("Vk9EIE1lbnUg")+repr(params))        
    request = urllib2.Request(filmilink, headers={"Accept" : "application/xml"})
    u = urllib2.urlopen(request)
    tree = ElementTree.parse(u)
    rootElem = tree.getroot()
    for channel in tree.findall(sync_data("Y2hhbm5lbA==")):
        filminimi = channel.find(get_live("dGl0bGU=")).text
        filminimi = base64.b64decode(filminimi)
        kategoorialink = channel.find(vod_channels("cGxheWxpc3RfdXJs")).text
        plugintools.add_item( action=vod_channels("Z2V0X215YWNjb3VudA=="), title=filminimi , url=kategoorialink , thumbnail = "" , fanart=os.path.join(LOAD_LIVE,sync_data("dGhlYXRlci5qcGc=")) , folder=True )
    plugintools.set_view( plugintools.LIST )
def stream_video(params):
    plugintools.log(pnimi+sync_data("TGl2ZSBDaGFubmVscyBNZW51IA==")+repr(params))
    if get_live("WHRyZWFtLUNvZGVz") not in open(addonDir+"/"+sync_data("YWRkb24ueG1s")).read():
       check_user()
    if vanemalukk == "true":
       pealkiri = params.get(sync_data("dGl0bGU="))
       vanema_lukk(pealkiri)
    url = params.get(get_live("dXJs"))
    request = urllib2.Request(url, headers={"Accept" : "application/xml"})
    u = urllib2.urlopen(request)
    tree = ElementTree.parse(u)
    xbmc.log(str(tree),2)
    rootElem = tree.getroot()
    plugintools.add_item( action="restart_service", title="[B][COLOR grey]Connected to Server: [/COLOR][COLOR green]"+str(user)+"[/COLOR][/B]" , url="http://", thumbnail="VISTA", plot="VISTA", fanart="" , extra="", isPlayable=False, folder=False )
    for channel in tree.findall(sync_data("Y2hhbm5lbA==")):
        kanalinimi = channel.find(get_live("dGl0bGU=")).text
        kanalinimi = base64.b64decode(kanalinimi)
        kanalinimi = kanalinimi.partition("[")
        striimilink = channel.find(get_live("c3RyZWFtX3VybA==")).text
        pilt = channel.find(vod_channels("ZGVzY19pbWFnZQ==")).text
        kava = kanalinimi[1]+kanalinimi[2]
        #kava = kava.partition("]")
        #kava = kava[2]
        #kava = kava.partition("   ")
        #kava = kava[2]
        shou = get_live("W0NPTE9SIHdoaXRlXSVzIFsvQ09MT1Jd")%(kanalinimi[0])+kava
        kirjeldus = channel.find(sync_data("ZGVzY3JpcHRpb24=")).text
        if kirjeldus:
           kirjeldus = base64.b64decode(kirjeldus)
           nyyd = kirjeldus.partition("(")
           nyyd = sync_data("Tk9XOiA=") +nyyd[0]
           jargmine = kirjeldus.partition(")\n")
           jargmine = jargmine[2].partition("(")
           jargmine = sync_data("TkVYVDog") +jargmine[0]
           kokku = nyyd+jargmine
        else:
           kokku = "VistaTV IPTV"
        if pilt:
           plugintools.add_item( action=sync_data("cnVuX2Nyb25qb2I="), title="[COLOR gold]Svr:"+str(user)+"[/COLOR]-"+shou , url=striimilink, thumbnail=pilt, plot=kokku, fanart=os.path.join(LOAD_LIVE,vod_channels("aG9tZXRoZWF0ZXIuanBn")), extra="VistaTV", isPlayable=True, folder=False )
        else:
           plugintools.add_item( action=sync_data("cnVuX2Nyb25qb2I="), title="[COLOR gold]Svr:"+str(user)+"[/COLOR]-"+shou , url=striimilink, thumbnail=os.path.join(LOAD_LIVE,sync_data("ZGVmYXVsdGxvZ28ucG5n")) , plot=kokku, fanart=os.path.join(LOAD_LIVE,sync_data("aG9tZXRoZWF0ZXIuanBn")) , extra="VistaTV", isPlayable=True, folder=False )
    plugintools.set_view( plugintools.EPISODES )
    #xbmc.executebuiltin(vod_channels("Q29udGFpbmVyLlNldFZpZXdNb2RlKDUwMyk="))
    xbmc.executebuiltin(vod_channels("Q29udGFpbmVyLlNldFZpZXdNb2RlKDUwKQ=="))
def get_myaccount(params):
        plugintools.log(pnimi+get_live("Vk9EIGNoYW5uZWxzIG1lbnUg")+repr(params))
        if vanemalukk == "true":
           pealkiri = params.get(sync_data("dGl0bGU="))
           vanema_lukk(pealkiri)
        purl = params.get(get_live("dXJs"))
        request = urllib2.Request(purl, headers={"Accept" : "application/xml"})
        u = urllib2.urlopen(request)
        tree = ElementTree.parse(u)
        rootElem = tree.getroot()
        for channel in tree.findall(sync_data("Y2hhbm5lbA==")):
            pealkiri = channel.find(get_live("dGl0bGU=")).text
            pealkiri = base64.b64decode(pealkiri)
            pealkiri = pealkiri.encode("utf-8")
            striimilink = channel.find(sync_data("c3RyZWFtX3VybA==")).text
            pilt = channel.find(sync_data("ZGVzY19pbWFnZQ==")).text 
            kirjeldus = channel.find(vod_channels("ZGVzY3JpcHRpb24=")).text
            if kirjeldus:
               kirjeldus = base64.b64decode(kirjeldus) 
            if pilt:
               plugintools.add_item( action="restart_service", title=pealkiri , url=striimilink, thumbnail=pilt, plot=kirjeldus, fanart=os.path.join(LOAD_LIVE,"theater.jpg") , extra="", isPlayable=True, folder=False )
            else:
               plugintools.add_item( action="restart_service", title=pealkiri , url=striimilink, thumbnail=os.path.join(LOAD_LIVE,"noposter.jpg"), plot=kirjeldus, fanart="" , extra="", isPlayable=True, folder=False )
        plugintools.set_view( plugintools.MOVIES )
        xbmc.executebuiltin('Container.SetViewMode(515)')
def run_cronjob(params):
    plugintools.log(pnimi+sync_data("UExBWV9MSVZF")+repr(params))
    if vanemalukk == "true":
       pealkiri = params.get(sync_data("dGl0bGU="))
       vanema_lukk(pealkiri)
    lopplink = params.get(vod_channels("dXJs"))
    plugintools.play_resolved_url( lopplink )
def sync_data(channel):
    video = base64.b64decode(channel)
    return video
def restart_service(params):
    plugintools.log(pnimi+get_live("UExBWSBWT0Qg")+repr(params))
    if vanemalukk == "true":
       pealkiri = params.get(sync_data("dGl0bGU="))
       vanema_lukk(pealkiri)
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
       plugintools.log(pnimi+sync_data("amRhdGEgbG9hZGVkIA=="))
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
       aegub = datetime.datetime.fromtimestamp(int(aegub)).strftime('%H:%M %d.%m.%Y')
    else:
       aegub = vod_channels("TmV2ZXI=") 
    rabbits = kasutajaAndmed[vod_channels("aXNfdHJpYWw=")]
    if rabbits == "0":
       rabbits = sync_data("Tm8=")
    else:
       rabbits = sync_data("WWVz")
    leavemealone = kasutajaAndmed[get_live("bWF4X2Nvbm5lY3Rpb25z")]
    polarbears = kasutajaAndmed[sync_data("dXNlcm5hbWU=")]
    plugintools.add_item( action="",   title=sync_data("W0NPTE9SID0gd2hpdGVdVXNlcjogWy9DT0xPUl0=")+polarbears , thumbnail="" , fanart=os.path.join(LOAD_LIVE,sync_data("YmFja2dyb3VuZC5wbmc=")) , folder=False )
    plugintools.add_item( action="",   title=sync_data("W0NPTE9SID0gd2hpdGVdU3RhdHVzOiBbL0NPTE9SXQ==")+seis , thumbnail="" , fanart=os.path.join(LOAD_LIVE,sync_data("YmFja2dyb3VuZC5wbmc=")) , folder=False )
    plugintools.add_item( action="",   title=get_live("W0NPTE9SID0gd2hpdGVdRXhwaXJlczogWy9DT0xPUl0=")+aegub , thumbnail="" , fanart=os.path.join(LOAD_LIVE,sync_data("YmFja2dyb3VuZC5wbmc=")) , folder=False )
    plugintools.add_item( action="",   title=vod_channels("W0NPTE9SID0gd2hpdGVdVHJpYWwgYWNjb3VudDogWy9DT0xPUl0=")+rabbits , thumbnail="" , fanart=os.path.join(LOAD_LIVE,sync_data("YmFja2dyb3VuZC5wbmc=")) , folder=False )
    plugintools.add_item( action="",   title=vod_channels("W0NPTE9SID0gd2hpdGVdTWF4IGNvbm5lY3Rpb25zOiBbL0NPTE9SXQ==")+leavemealone , thumbnail="" , fanart=os.path.join(LOAD_LIVE,sync_data("YmFja2dyb3VuZC5wbmc=")) , folder=False )
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
def kontrolli_uuendusi():
        req = urllib2.Request(uuenduslink)
        req.add_header(vod_channels("VXNlci1BZ2VudA==") , sync_data("S29kaSBwbHVnaW4gYnkgTWlra00="))
        response = urllib2.urlopen(req)
        repoversion=response.read()
        repoversion = repoversion.partition("\n")
        iversion = repoversion[1]
        global dlink
        dlink = repoversion[2]
        response.close()
        if iversion <> version:
           update = " "
        else:
           if plugintools.message_yes_no(pnimi,sync_data("TmV3IHVwZGF0ZSBpcyBhdmFpbGFibGUh"),get_live("RG8geW91IHdhbnQgdG8gdXBkYXRlIHBsdWdpbiBub3c/")):
              plugintools.log( pnimi+vod_channels("VHJ5aW5nIHRvIHVwZGF0ZSBwbHVnaW4uLi4="))
              try:
                  destpathname = xbmc.translatePath(os.path.join(sync_data("c3BlY2lhbDovLw=="),sync_data("aG9tZS9hZGRvbnMv")))
                  local_file_name = os.path.join( plugintools.get_runtime_path() , get_live("dXBkYXRlLnppcA==") )
                  plugintools.log(pnimi+local_file_name)
                  urllib.urlretrieve(dlink, local_file_name )
                  DownloaderClass(dlink,local_file_name)
                  plugintools.log(pnimi+sync_data("RXh0cmFjdGluZyB1cGRhdGUuLi4="))
                  #import ziptools
                  unzipper = ziptools.ziptools()
                  #destpathname = xbmc.translatePath(os.path.join('special://','home'))
                  plugintools.log(pnimi+destpathname)
                  unzipper.extract( local_file_name , destpathname )
                  os.remove(local_file_name)
                  xbmc.executebuiltin((u'XBMC.Notification("Updated", "The add-on has been updated", 2000)'))
                  #import updater
                  xbmc.executebuiltin( "Container.Refresh" )
                  plugintools.log(pnimi+get_live("VXBkYXRlIHN1Y2Nlc3M="))
              except:
                  plugintools.log(pnimi+get_live("VXBkYXRlIGZhaWxlZA=="))
                  xbmc.executebuiltin((u'XBMC.Notification("Not updated", "An error causes the update to fail", 2000)'))
def DownloaderClass(url,dest):
    dp = xbmcgui.DialogProgress()
    dp.create(sync_data("R2V0dGluZyB1cGRhdGU="),get_live("RG93bmxvYWRpbmc="))
    urllib.urlretrieve(url,dest,lambda nb, bs, fs, url=url: _pbhook(nb,bs,fs,url,dp))
def check_user():
    dummyvalue=0
    #sys.exit()
def _pbhook(numblocks, blocksize, filesize, url=None,dp=None):
    try:
        percent = min((numblocks*blocksize*100)/filesize, 100)
        print percent
        dp.update(percent)
    except:
        percent = 100
        dp.update(percent)
    if dp.iscanceled(): 
        print "DOWNLOAD CANCELLED" # need to get this part working
        dp.close()
def load_channels():
    statinfo = os.stat(LOAD_LIVE+"/"+get_live("YmFja2dyb3VuZC5wbmc="))

    statinfo = os.stat(LOAD_LIVE+"/"+get_live("ZGVmYXVsdGxvZ28ucG5n"))

    statinfo = os.stat(LOAD_LIVE+"/"+get_live("aG9tZXRoZWF0ZXIuanBn"))

    statinfo = os.stat(LOAD_LIVE+"/"+get_live("bm9wb3N0ZXIuanBn"))

    statinfo = os.stat(LOAD_LIVE+"/"+get_live("dGhlYXRlci5qcGc="))

    statinfo = os.stat(addonDir+"/"+get_live("YWRkb24ueG1s"))

    statinfo = os.stat(addonDir+"/"+get_live("aW5pdC5weQ=="))

    statinfo = os.stat(addonDir+"/"+get_live("aWNvbi5wbmc="))

    statinfo = os.stat(addonDir+"/"+vod_channels("ZmFuYXJ0LnBuZw=="))

def vod_channels(channel):
    video = base64.b64decode(channel)
    return video
run()