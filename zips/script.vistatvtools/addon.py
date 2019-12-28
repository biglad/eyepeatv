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
		function5
		)
        
    call = dialog.select('[B][COLOR=yellow]Eye Pea TV Tools Menu[/COLOR][/B]', [
	"[B][COLOR=lightblue]      Player Input Settings[/COLOR][/B]", #1
	"[B][COLOR=lightblue]      Kodi Settings[/COLOR][/B]", #2
	"[B][COLOR=lightblue]      File Manager[/COLOR][/B]", #3
	"[B][COLOR=lightblue]      My Addons[/COLOR][/B]", #4
	"[B][COLOR=yellow]      Exit Kodi[/COLOR][/B]", #5
    ])
    # dialog.selectreturns
    #   0 -> escape pressed
    #   1 -> first item
    #   2 -> second item
    if call:
        # esc is not pressed
        if call < 0:
            return
        func = funcs[call-5]
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
    dialog.ok('[COLOR white]Eye Pea TV[/COLOR]','[COLOR white]Install/Enable the following addon(s)[/COLOR]','[COLOR white][/COLOR]','[COLOR white]This will improve stream quality[/COLOR]')
    xbmc.executebuiltin('ActivateWindow(10040,"addons://repository.xbmc.org/kodi.inputstream",return)')
    exit()	
	
def function2():
    xbmc.executebuiltin('ActivateWindow(10004,"Settings.xml",return)') #Main Settings
    exit()	
	
def function3():
    xbmc.executebuiltin('ActivateWindow(10003,"FileManager.xml",return)') #FileManager
    exit()
	
def function4():
    xbmc.executebuiltin('ActivateWindow(10040,"AddonBrowser.xml",return)') #Addons
    exit()
	
def function5():
    xbmc.executebuiltin('ActivateWindow(10111,"DialogButtonMenu.xml",return)') #Exit
    exit()
	
	
menuoptions()
