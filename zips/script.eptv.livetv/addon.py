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
        function2
		)
        
    call = dialog.select('[B][COLOR=yellow]Eye Pea Movies Menu[/COLOR][/B]', [
    "[B][COLOR=orange]      Eye Pea TV Normal Service[/COLOR][/B]", #1
    "[B][COLOR=gold]      Eye Pea TV Gold Service[/COLOR][/B]",#2
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
    xbmc.executebuiltin('RunAddon(plugin.video.eyepeatv)')

    exit()	
	
def function2():
    xbmc.executebuiltin('RunAddon(plugin.video.eyepeatv.2)')
	
    exit()
		
	
	
menuoptions()
