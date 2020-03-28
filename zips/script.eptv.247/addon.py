import xbmc
import utils
import os
import platform
import xbmcgui
import sfile
import urllib
import urllib2
import time
import re
import downloader
import extractor
import xbmcvfs
import shutil
import base64
import xbmcaddon
import time
from uuid import getnode as get_mac
from resources.lib.kodion.impl import Context
from resources.lib.kodion.constants import setting
import subprocess
import random
import string
global UPDATE
from urllib2 import urlopen



def menuoptions():
    global UPDATE
    dialog = xbmcgui.Dialog()
    funcs = (
        function1,
        function2,
        function3
		)
        
    call = dialog.select('[B][COLOR=yellow]EPTV 24/7 Me nu[/COLOR][/B]', [
    "[B][COLOR=orange]      24/7 TV Shows", #1
    "[B][COLOR=orange]      24/7 Movies",#2
    "[B][COLOR=orange]      24/7 Kids",#3
    ])
    # dialog.selectreturns
    #   0 -> escape pressed
    #   1 -> first item
    #   2 -> second item
    if call:
        # esc is not pressed
        if call < 0:
            return
        func = funcs[call-3]
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
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.eyepeatv.2/?action=stream_video&extra&page&plot&thumbnail=C%3a%5cUsers%5ckhanb%5cAppData%5cRoaming%5cKodi%5caddons%5cplugin.video.eyepeatv.2%5cresources%5cart%5c247.png&title=24%2f7%20Tv%20Shows&url=261",return)')	
	
def function2():
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.eyepeatv.2/?action=stream_video&extra&page&plot&thumbnail=C%3a%5cUsers%5ckhanb%5cAppData%5cRoaming%5cKodi%5caddons%5cplugin.video.eyepeatv.2%5cresources%5cart%5c247.png&title=24%2f7%20Movies&url=262",return)')
    
def function3():
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.eyepeatv.2/?action=stream_video&extra&page&plot&thumbnail=C%3a%5cUsers%5ckhanb%5cAppData%5cRoaming%5cKodi%5caddons%5cplugin.video.eyepeatv.2%5cresources%5cart%5c247.png&title=24%2f7%20Kids&url=263",return)')

		
menuoptions()

 
 
