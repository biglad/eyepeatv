import xbmc,xbmcplugin,xbmcgui,re,os,xbmcaddon,sys,base64,plugintools,time,urllib2,string,logging,array,shutil
AddonID = 'plugin.video.eyepeatv'
Username = plugintools.get_setting("Username")
Password = plugintools.get_setting("Password")
PVRon = plugintools.get_setting("PVRUpdater")
lehekylg = base64.b64decode("aHR0cDovL3dhdGNoLmdvdGRhcmsuY29t")
#pordinumber = base64.b64decode("Njk2OQ==")
EPGurl = base64.b64decode("JXMveG1sdHYucGhwP3VzZXJuYW1lPSVzJnBhc3N3b3JkPSVz")%(lehekylg,Username,Password)
NewPVR = xbmc.translatePath('special://home/userdata/addon_data/pvr.iptvsimple/EyePeaTV.m3u8')
dialog = xbmcgui.Dialog()
VAddon = xbmcaddon.Addon('plugin.video.eyepeatv')
iVueRepo = xbmc.translatePath('special://home/addons/xbmc.repo.ivueguide')
if os.path.exists(iVueRepo):
	shutil.rmtree(iVueRepo)

def Check():
	if PVRon == 'true':
		time.sleep(20)
		if os.path.exists(NewPVR):
			os.remove(NewPVR)
		time.sleep(1)
		f = open(NewPVR, 'a')
		f.write('#EXTM3U\n')
		UserList = base64.b64decode("JXMvZ2V0LnBocD91c2VybmFtZT0lcyZwYXNzd29yZD0lcyZ0eXBlPW0zdV9wbHVzJm91dHB1dD10cw==")%(lehekylg,Username,Password)
		link = open_url(UserList).replace('\r','').replace(',',' Channel="').replace('\nhttp','", Link=http')
		match = re.compile('#EXTINF:-1 tvg-id="(.+?)" tvg-name="(.+?)" tvg-logo="(.+?)" group-title="(.+?)" Channel="(.+?)", Link=(.+?).ts').findall(link)
		for EPGid, ChannelName, ChanLogo, GroupTitle, StreamTitle, StreamLink in match:
				OutpuT = '#EXTINF:-1 tvg-id="'+EPGid+'" tvg-name="'+ChannelName+'" tvg-logo="'+ChanLogo+'" group-title="'+GroupTitle+'",'+StreamTitle+'\n'+StreamLink+'.ts\n'
				OutpuT = OutpuT.replace(',,','\n')
				f = open(NewPVR, 'a')
				f.write(OutpuT)
		if PVRon == 'false':
			VAddon.setSetting(id='PVRUpdater', value='true')
		
		xbmc.executebuiltin('Notification(PVR Updated,[COLOR white]PVR Playlist Updated[/COLOR],3000,special://home/addons/'+AddonID+'/icon.png)')

def open_url(url):
    try:
        req = urllib2.Request(url,headers={"Accept" : "application/xml","User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36"})
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        return link
    except:quit()
	
Check()