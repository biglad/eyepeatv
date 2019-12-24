import time
import xbmc
import os
import xbmcgui
import urllib2
import platform
import utils

import sfile
import download
import urllib
import webbrowser
dialog = xbmcgui.Dialog()



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
		function13
		)
        
    call = dialog.select('[B][COLOR=yellow]Eye Pea TV Main Menu[/COLOR][/B]', [
    "[B][COLOR=orange]      Live TV (Channels)[/COLOR][/B]",#1
    "[B][COLOR=orange]      Live TV (Guide)[/COLOR][/B]", #2
    "[B][COLOR=orange]      Eye Pea TV Addon[/COLOR][/B]", #3
	"[B][COLOR=orange]      Search Live TV[/COLOR][/B]", #4
    "[B][COLOR=orange]      On Demand[/COLOR][/B]", #5
	"[B][COLOR=orange]      24/7 Streams[/COLOR][/B]", #6
	"[B][COLOR=orange]      YouTube[/COLOR][/B]", #7
	"[B][COLOR=lightblue]      Weather[/COLOR][/B]", #8
	"[B][COLOR=lightblue]      Player Input Settings[/COLOR][/B]", #9
	"[B][COLOR=lightblue]      Kodi Settings[/COLOR][/B]", #10
	"[B][COLOR=lightblue]      File Manager[/COLOR][/B]", #11
	"[B][COLOR=lightblue]      My Addons[/COLOR][/B]", #12
	"[B][COLOR=yellow]      Exit Kodi[/COLOR][/B]", #13
    ])
    # dialog.selectreturns
    #   0 -> escape pressed
    #   1 -> first item
    #   2 -> second item
    if call:
        # esc is not pressed
        if call < 0:
            return
        func = funcs[call-13]
        #if myplatform == 'windows':
        #    func = funcs[call-23]
        #dp = xbmcgui.DialogProgress()
        #dp.create("[COLOR tomato]VistaTV[/COLOR]",""+str(func)+" -3","PLEASE EXIT KODI OR PULL THE POWER LEAD")
        #xbmc.sleep(1000)
        return func()
    else:
        func = funcs[call]
        #dp = xbmcgui.DialogProgress()
        #dp.create("[COLOR tomato]VistaTV[/COLOR]",""+str(func)+" +0","PLEASE EXIT KODI OR PULL THE POWER LEAD")
        #xbmc.sleep(1000)
        return func()
    return 


def function1():
    xbmc.executebuiltin('ActivateWindow(10700,"pvr://channels/tv/All channels/",return)')
    xbmc.executebuiltin('SendClick(28)')
    exit()
	
def function2():
    xbmc.executebuiltin('ActivateWindow(10702,"pvr://channels/tv/All channels/",return)')
    xbmc.executebuiltin('SendClick(28)')
    exit()	
	
def function3():
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.eyepeatv",return)')
    exit()
	
def function4():
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.eyepeatv/?action=TVsearch&extra&page&plot&thumbnail=C%3a%5cUsers%5ckhanb%5cAppData%5cRoaming%5cKodi%5caddons%5cplugin.video.eyepeatv%5cresources%5cart%5cSearch-icon.png&title=%5bCOLOR%20gold%5d%5bB%5dLive%20EyePeaTV%20Search%5b%2fB%5d%5b%2fCOLOR%5d%20(Enter%20tv%20show%20or%20movie%20name)&url",return)')
    exit()

def function5():
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.vistatvshowbox",return)')
    exit()	

def function6():
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.vista-iptv-scraper",return)')
    exit()	
	
def function7():
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.youtube",return)')
    exit()	
	
def function8():
    xbmc.executebuiltin('ActivateWindow(12600,"MyWeather.xml",return)') #Weather
    exit()	
	
def function9():
    dialog.ok('[COLOR white]Eye Pea TV[/COLOR]','[COLOR white]Install/Enable the following addon(s)[/COLOR]','[COLOR white][/COLOR]','[COLOR white]This will improve stream quality[/COLOR]')
    xbmc.executebuiltin('ActivateWindow(10040,"addons://repository.xbmc.org/kodi.inputstream",return)')
    exit()	
	
def function10():
    xbmc.executebuiltin('ActivateWindow(10004,"Settings.xml",return)') #Main Settings
    exit()	
	
def function11():
    xbmc.executebuiltin('ActivateWindow(10003,"FileManager.xml",return)') #FileManager
    exit()
	
def function12():
    xbmc.executebuiltin('ActivateWindow(10040,"AddonBrowser.xml",return)') #Addons
    exit()
	
def function13():
    xbmc.executebuiltin('ActivateWindow(10111,"DialogButtonMenu.xml",return)') #Exit
    exit()
	
	
menuoptions()
