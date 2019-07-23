import xbmc
import xbmcgui
import os
import urllib2
buildfile = "version.txt"
buildv = xbmc.translatePath(os.path.join('special://home/', buildfile))

window = xbmcgui.Window(10000)
label = xbmcgui.ControlLabel(30, 30, 1000, 50, '[COLOR black]EPTV www.eptv.co.uk[/COLOR]')
window.addControl(label)
window = xbmcgui.Window(10000)
label = xbmcgui.ControlLabel(28, 28, 1000, 50, '[COLOR gold]EPTV[/COLOR] www.eptv.co.uk')
window.addControl(label)




import os.path
if os.path.exists(buildv):
    with open(buildv, 'r') as myfile:
        data = myfile.read()
        buildv = float(data)
else:
    try:
        fo = open("0.0", "w")
        fo.write(buildv);
        fo.close()
        buildv = "0.0"
    except:
        buildv = "0.0"
        
        
        





AddonID = 'script.eptv.core'
xbmc.executebuiltin('Notification(STARTING UP,[COLOR white]Please Wait.....[/COLOR],15000,special://home/addons/'+AddonID+'/icon.png)')
xbmc.Player().play('special://home/addons/script.eptv.core/load.mp4')



window = xbmcgui.Window(10025)
label = xbmcgui.ControlLabel(30, 30, 1000, 50, '[COLOR black]EPTV www.eptv.co.uk[/COLOR]')
window.addControl(label)
window = xbmcgui.Window(10025)
label = xbmcgui.ControlLabel(28, 28, 1000, 50, '[COLOR gold]EPTV[/COLOR] www.eptv.co.uk')
window.addControl(label)


KODIV          = float(xbmc.getInfoLabel("System.BuildVersion")[:4])


if KODIV < 18.3:
    dialog = xbmcgui.Dialog()
    dialog.ok("[COLOR=white][B]EPTV[/COLOR][/B]","Your Kodi is needs updating","Your Version = "+str(KODIV),"Press OK to Continue and udpate ASAP")

xbmc.executebuiltin('xbmc.UpdateAddonRepos')
xbmc.executebuiltin('xbmc.UpdateLocalAddons')
#xbmc.executebuiltin('ActivateWindow(10001,"plugin://script.module.aliunde.maintenance.wizard/?mode=systeminfo",return)')
xbmc.executebuiltin("XBMC.AlarmClock('MTVBCS',XBMC.RunAddon(script.eptv.core),5,silent)")


#xbmc.executebuiltin("Dialog.Close(busydialog)")
xbmc.executebuiltin('Notification(STARTING UP,[COLOR white]Please Wait.....[/COLOR],15000,special://home/addons/'+AddonID+'/icon.png)')    
xbmc.executebuiltin("ActivateWindow(10000)")

webversion = urllib2.urlopen('http://eptv.co.uk/version.txt').read()
webversion = float(webversion)
buildv = float(buildv)

buildinfo1 = "[COLOR black]Your Build Version : "+str(buildv)+" - Latest Version : "+str(webversion)+"[/COLOR]"
buildinfo2 = "[COLOR darkgrey]Your Build Version : "+str(buildv)+" - Latest Version : "+str(webversion)+"[/COLOR]"

window = xbmcgui.Window(10000)
label = xbmcgui.ControlLabel(55, 60, 1000, 50, buildinfo1)
window.addControl(label)
window = xbmcgui.Window(10000)
label = xbmcgui.ControlLabel(53, 58, 1000, 50, buildinfo2)
window.addControl(label)


window = xbmcgui.Window(10000)
label = xbmcgui.ControlLabel(86, 86, 1000, 50, "[COLOR black]Kodi Version : "+str(KODIV)+"[/COLOR]")
window.addControl(label)
window = xbmcgui.Window(10000)
label = xbmcgui.ControlLabel(84, 84, 1000, 50, "[COLOR darkgrey]Kodi Version : "+str(KODIV)+"[/COLOR]")
window.addControl(label)



    
