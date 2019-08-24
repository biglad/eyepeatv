import time
import xbmc
import os
import xbmcgui
import urllib2
from urllib import urlopen
import re
import platform
import xbmccodecs



def getPublicIp():
    data = str(urlopen('http://checkip.dyndns.com/').read())
    # data = '<html><head><title>Current IP Check</title></head><body>Current IP Address: 65.96.168.198</body></html>\r\n'
    return re.compile(r'Address: (\d+\.\d+\.\d+\.\d+)').search(data).group(1)

def menuoptions():
    dialog = xbmcgui.Dialog()
    funcs = (
        function1,
        function2,
        function3,
        function4,
        function5,
        function6,
        function7,
        function8,
        function9,
        function10,
        function11,
        function12,
        function13,
		function14,
		function15,
		function16,
		function17,
		function18
        )
        
    call = dialog.select('[B][COLOR=yellow]EPTV[/COLOR][COLOR=yellow] Tools Menu[/COLOR][/B]', [
    '[B][COLOR=lightblue]Open VPN[/COLOR][/B] - ([I]Andriod [/I])',
    '[B][COLOR=green]Pairing System[/COLOR][/B]',
    '[B][COLOR=gold]Show Me My Wifi Signal[/COLOR][/B] - ([I]Andriod [/I])',
    '[B][COLOR=gold]PLACE HOLDER[/COLOR][/B]',
    '[B][COLOR=gold]EPTV House Keeper[/COLOR][/B] (clean up system and reboot)', 
    '[B][COLOR=gold]Test My Connection Speed[/COLOR][/B]', 
    '[B][COLOR=gold]PLACE HOLDER[/COLOR][/B]', 
    '[B][COLOR=gold]Open Main Box Settings[/COLOR][/B] - ([I]Andriod [/I])', 
    '[B][COLOR=gold]Update Addons & Repos[/COLOR][/B] (make sure your upto date)',
    '[B][COLOR=gold]Easy Advanced Settings[/COLOR][/B]',
    '[B][COLOR=gold]Player Input Settings[/COLOR][/B] MAKE SURE ALL ARE ENABLED!!!!!!!',
	'[B][COLOR=gold]Authorize Real Debrid and other Providers[/COLOR][/B]',
    '[B][COLOR=gold]Scraper Settings[/COLOR][/B]',
    '[B][COLOR=red]Open Log File[/COLOR](Track Problems)[/B]',
	'[B][COLOR=yellow]Turn on Music Visualizations[/COLOR][/B]',
	'[B][COLOR=orange]Turn On/Off Surface Media Codec[/COLOR][/B] (For Best Playback (needed for x265))',
	'[B][COLOR=orange]Turn On/Off Media Codec[/COLOR][/B] (Needed for live streaming)',
	'[B][COLOR=gold]Vista TV Requisition Settings (Auth Trakt, etc)[/COLOR][/B]'
    ])
    # dialog.selectreturns
    #   0 -> escape pressed
    #   1 -> first item
    #   2 -> second item
    if call:
        # esc is not pressed
        if call < 0:
            return
        func = funcs[call-18]
        #dp = xbmcgui.DialogProgress()
        #dp.create("[COLOR tomato]EPTV[/COLOR]",""+str(func)+" -3","PLEASE EXIT KODI OR PULL THE POWER LEAD")
        #xbmc.sleep(1000)
        return func()
    else:
        func = funcs[call]
        #dp = xbmcgui.DialogProgress()
        #dp.create("[COLOR tomato]EPTV[/COLOR]",""+str(func)+" +0","PLEASE EXIT KODI OR PULL THE POWER LEAD")
        #xbmc.sleep(1000)
        return func()
    return 
    
    
    
def function1():
    xbmc.executebuiltin('RunAddon(script.vista.android.openvpn)') 
    
def function2():
    xbmc.executebuiltin('RunAddon(script.cerebro.pairwith)')  

    
def function3():
    #the content of function 1
    #dp = xbmcgui.DialogProgress()
    #dp.create("[COLOR tomato]EPTV[/COLOR]","PLEASE EXIT KODI OR PULL THE POWER LEAD","PLEASE EXIT KODI OR PULL THE POWER LEAD")
    #xbmc.sleep(5000)
    xbmc.executebuiltin('StartAndroidActivity("com.farproc.wifi.analyzer")')    

def function4():
    dp = xbmcgui.DialogProgress()
    dp.create("[COLOR tomato]EPTV[/COLOR]","Collecting Data","Few Second.....")
    dialog = xbmcgui.Dialog()
    dialog.ok("[COLOR=red][B] ## MY BOX INFO ##[/COLOR][/B]", "[COLOR=red]My ID[/COLOR]: [COLOR=green]"+str(data300)+"[/COLOR]", "[COLOR=red]Build Version[/COLOR]: [COLOR=green]"+str(data)+"[/COLOR]","[COLOR=red]IP Address (public)[/COLOR]: [COLOR=green]"+str(getPublicIp())+"[/COLOR]")
    xbmc.executebuiltin('RunAddon(script.EPTV.info)')
    
def function5():
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://script.vista.exit",return)')

def function6():
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://script.speedtestnet",return)')

def function7():
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://script.EPTV-wizard",return)')


def function8():
    xbmc.executebuiltin('StartAndroidActivity("com.mbx.settingsmbox")')
    xbmc.executebuiltin('StartAndroidActivity("com.android.tv.settings")')
    xbmc.executebuiltin('StartAndroidActivity("com.mbox.settings")')
        
def function9():
    xbmc.executebuiltin('ActivateWindow(10040,"addons://outdated/",return)')
    xbmc.sleep(2000)
    dp = xbmcgui.DialogProgress()
    dp.create("[COLOR tomato]Vista TV[/COLOR]","Checking Repos for Updates","Please Wait (approx 45 secs)")
    xbmc.executebuiltin('xbmc.UpdateAddonRepos()')
    xbmc.sleep(35000)
    dp.create("[COLOR tomato]Vista TV[/COLOR]","Checking Add-ons for Updates","Please Wait (approx 45 secs)")
    xbmc.executebuiltin('xbmc.UpdateLocalAddons()')
    percent = 50
    dp.update(percent)
    xbmc.sleep(35000)
    
    dp.close()
    
def function10():
    xbmc.executebuiltin('RunAddon(script.vista.advset)')  
   
    
def function11():
    xbmc.executebuiltin('ActivateWindow(10040,"addons://repository.xbmc.org/kodi.inputstream",return)')
	
def function12():
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.EPTVshowbox/?action=smuSettings",return)') 
	
def function13():
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.EPTVshowbox/?action=oathscrapersettings",return)') 
    
def function14():
    xbmc.executebuiltin('RunAddon(script.logviewer)')   
	
def function15():
    xbmc.executebuiltin('ActivateWindow(10040,"addons://repository.xbmc.org/xbmc.player.musicviz",return)') 
	
def function16():
    xbmccodecs.setSurfaceCodec() 
	
def function17():
    xbmccodecs.setCodec() 
	
def function18():
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.EPTVshowbox/?action=openSettings&query=0.0",return)')  
    
menuoptions()