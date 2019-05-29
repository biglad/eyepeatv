import time
import xbmc
import os
import xbmcgui
import urllib2
import utils
import sfile

def menuoptions():
    dialog = xbmcgui.Dialog()
    funcs = (
        function1,
        function2
        )
        
    call = dialog.select('[B][COLOR=yellow]Exit[/COLOR][/B]', [ 
    '[B][COLOR=gold]Close Kodi[/COLOR][/B]' ,	
    '[B][COLOR=gold]Close & Run House Keeper.[/COLOR][/B]',
    ])
    # dialog.selectreturns
    #   0 -> escape pressed
    #   1 -> first item
    #   2 -> second item
    if call:
        # esc is not pressed
        if call < 0:
            return
        func = funcs[call-2]
        return func()
    else:
        func = funcs[call]
        return func()
    return 



    
def function1():
    xbmc.sleep(1000)
    xbmc.executebuiltin("Action(Close)")
    os._exit(1)
    exit()
	
def function2():
    xbmc.executebuiltin('RunAddon(script.program.vistatvhousekeeper)')
		  
menuoptions()