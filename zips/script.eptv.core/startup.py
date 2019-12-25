import xbmc
import xbmcgui
import os
import urllib2
buildfile = "version.txt"
buildv = xbmc.translatePath(os.path.join('special://home/', buildfile))

window = xbmcgui.Window(10000)
label = xbmcgui.ControlLabel(60, 230, 500, 50, "[COLOR black]Welcome to Eye Pea TV's Kodi Build[/COLOR]")
window.addControl(label)
window = xbmcgui.Window(10000)
label = xbmcgui.ControlLabel(58, 228, 500, 50, "[COLOR lightgrey]Welcome to Eye Pea TV's Kodi Build[/COLOR]")
window.addControl(label)

window = xbmcgui.Window(10000)
label = xbmcgui.ControlLabel(60, 260, 500, 50, "[COLOR black]Merry Christmas & Happy New Year![/COLOR]")
window.addControl(label)
window = xbmcgui.Window(10000)
label = xbmcgui.ControlLabel(58, 258, 500, 50, "[COLOR lightgrey]Merry Christmas & Happy New Year![/COLOR]")
window.addControl(label)


window = xbmcgui.Window(10000)
label = xbmcgui.ControlLabel(60, 460, 500, 50, "[COLOR black]For Latest News & Offers Join[/COLOR]")
window.addControl(label)
window = xbmcgui.Window(10000)
label = xbmcgui.ControlLabel(58, 458, 500, 50, "[COLOR lightgrey]For Latest News & Offers Join[/COLOR]")
window.addControl(label)

window = xbmcgui.Window(10000)
label = xbmcgui.ControlLabel(60, 490, 500, 50, "[COLOR black]t.me/eyepeatv[/COLOR]")
window.addControl(label)
window = xbmcgui.Window(10000)
label = xbmcgui.ControlLabel(58, 488, 500, 50, "[COLOR lightgrey]t.me/eyepeatv[/COLOR]")
window.addControl(label)




import os.path
#if os.path.exists(buildv):
#    with open(buildv, 'r') as myfile:
#        data = myfile.read()
#        buildv = float(data)
#else:
#    try:
#        fo = open("0.0", "w")
#        fo.write(buildv);
#        fo.close()
#        buildv = "0.0"
#    except:
#        buildv = "0.0"
        
        
        





AddonID = 'script.eptv.core'
#xbmc.executebuiltin('Notification(STARTING UP,[COLOR white]Please Wait.....[/COLOR],15000,special://home/addons/'+AddonID+'/icon.png)')
#xbmc.Player().play('special://home/addons/script.eptv.core/load.mp4')



KODIV          = float(xbmc.getInfoLabel("System.BuildVersion")[:4])


if KODIV < 18.5:
    dialog = xbmcgui.Dialog()
    dialog.ok("[COLOR=white][B]EPTV[/COLOR][/B]","Your Kodi is needs updating","Your Version = "+str(KODIV),"Press OK to Continue and udpate ASAP")

xbmc.executebuiltin('xbmc.UpdateAddonRepos')
xbmc.executebuiltin('xbmc.UpdateLocalAddons')
#xbmc.executebuiltin('ActivateWindow(10001,"plugin://script.module.aliunde.maintenance.wizard/?mode=systeminfo",return)')
xbmc.executebuiltin("XBMC.AlarmClock('MTVBCS',XBMC.RunAddon(script.eptv.core),30,silent)")


#xbmc.executebuiltin("Dialog.Close(busydialog)")
#xbmc.executebuiltin('Notification(STARTING UP,[COLOR white]Please Wait.....[/COLOR],15000,special://home/addons/'+AddonID+'/icon.png)')    
#xbmc.executebuiltin("ActivateWindow(10000)")

#webversion = urllib2.urlopen('http://eptv.co.uk/version.txt').read()
#webversion = float(webversion)
#buildv = float(buildv)

#loaded = urllib2.urlopen('http://eptv.co.uk/loaded.php').read()
#loaded = int(loaded)

#buildinfo1 = "[COLOR black]Your Build Version : "+str(buildv)+" - Latest Version : "+str(webversion)+"[/COLOR]"
#buildinfo2 = "[COLOR darkgrey]Your Build Version : "+str(buildv)+" - Latest Version : "+str(webversion)+"[/COLOR]"
#buildinfo3 = "[COLOR black]Total Build Loads : "+str(loaded)+"[/COLOR]"
#buildinfo4 = "[COLOR darkgrey]Total Build Loads : "+str(loaded)+"[/COLOR]"

#window = xbmcgui.Window(10000)
#label = xbmcgui.ControlLabel(55, 60, 1000, 50, buildinfo1)
#window.addControl(label)
#window = xbmcgui.Window(10000)
#label = xbmcgui.ControlLabel(53, 58, 1000, 50, buildinfo2)
#window.addControl(label)


#window = xbmcgui.Window(10000)
#label = xbmcgui.ControlLabel(86, 86, 1000, 50, "[COLOR black]Kodi Version : "+str(KODIV)+"[/COLOR]")
#window.addControl(label)
#window = xbmcgui.Window(10000)
#label = xbmcgui.ControlLabel(84, 84, 1000, 50, "[COLOR darkgrey]Kodi Version : "+str(KODIV)+"[/COLOR]")
#window.addControl(label)

#window = xbmcgui.Window(10000)
#label = xbmcgui.ControlLabel(116, 116, 1000, 50, buildinfo3)
#window.addControl(label)
#window = xbmcgui.Window(10000)
#label = xbmcgui.ControlLabel(114, 114, 1000, 50, buildinfo4)
#window.addControl(label)



    
