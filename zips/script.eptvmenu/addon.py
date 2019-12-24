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
		function10
		)
        
    call = dialog.select('[B][COLOR=yellow]Eye Pea TV Main Menu[/COLOR][/B]', [
    "[B][COLOR=orange]      Live TV (Channels)[/COLOR][/B]",#1
    "[B][COLOR=orange]      Live TV (Guide)[/COLOR][/B]", #2
    "[B][COLOR=orange]      Eye Pea TV Addon[/COLOR][/B]", #3
    "[B][COLOR=orange]      On Demand[/COLOR][/B]", #4
	"[B][COLOR=orange]      24/7 Streams[/COLOR][/B]", #5
	"[B][COLOR=orange]      YouTube[/COLOR][/B]", #6
	"[B][COLOR=lightblue]      Weather[/COLOR][/B]", #7
	"[B][COLOR=lightblue]      Player Input Settings[/COLOR][/B]", #8
	"[B][COLOR=lightblue]      Kodi Settings[/COLOR][/B]", #9
	"[B][COLOR=lightblue]      File Manager[/COLOR][/B]", #10
    ])
    # dialog.selectreturns
    #   0 -> escape pressed
    #   1 -> first item
    #   2 -> second item
    if call:
        # esc is not pressed
        if call < 0:
            return
        func = funcs[call-10]
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
    exit()
	
def function2():
    xbmc.executebuiltin('ActivateWindow(10702,"pvr://channels/tv/All channels/",return)')
    exit()	
	
def function3():
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.eyepeatv",return)')
    exit()

def function4():
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.vistatvshowbox",return)')
    exit()	

def function5():
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.vista-iptv-scraper",return)')
    exit()	
	
def function6():
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.youtube",return)')
    exit()	
	
def function7():
    xbmc.executebuiltin('ActivateWindow(12600,"MyWeather.xml",return)') #Weather
    exit()	
	
def function8():
    #DO NOTICE TO INSTALL BOTH
    xbmc.executebuiltin('ActivateWindow(10040,"addons://repository.xbmc.org/kodi.inputstream",return)')
    exit()	
	
def function9():
    xbmc.executebuiltin('ActivateWindow(10004,"Settings.xml",return)') #Main Settings
    exit()	
	
def function10():
    xbmc.executebuiltin('ActivateWindow(10003,"FileManager.xml",return)') #FileManager
    exit()
	
	
menuoptions()


#xbmc.executebuiltin('ActivateWindow(10003,"FileManager.xml",return)') #FileManager
#xbmc.executebuiltin('ActivateWindow(10004,"Settings.xml",return)') #Main Settings
#xbmc.executebuiltin('ActivateWindow(10030,"SettingsCategory.xml",return)') #Player Settings
#xbmc.executebuiltin('ActivateWindow(10111,"ialogButtonMenu.xml",return)') #Exit