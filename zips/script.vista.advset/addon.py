import time
import xbmc
import os
import xbmcgui
import urllib2
import utils
import sfile
import shutil

HOME     = xbmc.translatePath('special://home/addons/script.vista.advset')
HOME2     = xbmc.translatePath('special://userdata/')

lowend    = os.path.join(HOME, 'lowned.xml')
highend    = os.path.join(HOME, 'highend.xml')
pc    = os.path.join(HOME, 'pc.xml')

lowend1    = os.path.join(HOME, 'lowned1.xml')
highend1    = os.path.join(HOME, 'highend1.xml')
pc1    = os.path.join(HOME, 'pc1.xml')

savefile = os.path.join(HOME2, 'advancedsettings.xml')

def saved():
    xbmc.sleep(1000)
    dialog = xbmcgui.Dialog()
    dialog.ok("[COLOR=white][B]VistaTV[/COLOR][/B]","New Settings Saved","Kodi will now close","Press OK to Continue")  
    os._exit(1)
    xbmc.executebuiltin('Quit')

def menuoptions():
    dialog = xbmcgui.Dialog()
    funcs = (
        function1,
        function2,
        function3,
		function4,
		function5,
		function6,
		function7
        )
        
    call = dialog.select('[B][COLOR=yellow]Advanced Settings[/COLOR][/B]', [ 
	'[B][COLOR=green]Super Easy Advanced Settings All Devices[/COLOR][/B]' ,
    '[B][COLOR=gold]Set For Lowend Device (1gb ram) (Fast Connection)[/COLOR][/B]' ,
    '[B][COLOR=gold]Set For Mid Range Device (2gb ram) (Fast Connection)[/COLOR][/B]' ,   
    '[B][COLOR=gold]Set For High Range Device (3gb ram+) (Fast Connection)[/COLOR][/B]',
	'[B][COLOR=gold]Set For Lowend Device (1gb ram) (Slow Connection)[/COLOR][/B]' ,
    '[B][COLOR=gold]Set For Mid Range Device (2gb ram) (Slow Connection)[/COLOR][/B]' ,   
    '[B][COLOR=gold]Set For High Range Device (3gb ram+) (Slow Connection)[/COLOR][/B]',
    ])
    # dialog.selectreturns
    #   0 -> escape pressed
    #   1 -> first item
    #   2 -> second item
    if call:
        # esc is not pressed
        if call < 0:
            return
        func = funcs[call-7]
        return func()
    else:
        func = funcs[call]
        return func()
    return 



def function1():
    try: os.remove(xbmc.translatePath("special://userdata/addon_data/AdvancedSettings.xml"))
    except: pass
    xbmc.executebuiltin('ActivateWindow(10001,"plugin://script.module.aliunde.maintenance.wizard/?mode=maint&name=tweaks",return)')

    
def function2():
    shutil.copy2(lowend, savefile)
    saved()
    
def function3():
    shutil.copy2(highend, savefile)
    saved()
    
def function4():
    shutil.copy2(pc, savefile)
    saved()
	
def function5():
    shutil.copy2(lowend1, savefile)
    saved()
    
def function6():
    shutil.copy2(highend1, savefile)
    saved()
    
def function7():
    shutil.copy2(pc1, savefile)
    saved()
          
menuoptions()