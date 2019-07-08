import xbmc
import xbmcgui
AddonID = 'script.eptv.core'
xbmc.executebuiltin('Notification(STARTING UP,[COLOR white]Please Wait.....[/COLOR],15000,special://home/addons/'+AddonID+'/icon.png)')
xbmc.Player().play('special://home/addons/script.eptv.core/load.mp4')
window = xbmcgui.Window(10000)
label = xbmcgui.ControlLabel(15, 15, 1000, 50, 'EPTV www.eptv.co.uk')
window.addControl(label)
window = xbmcgui.Window(10025)
label = xbmcgui.ControlLabel(15, 15, 1000, 50, 'EPTV www.eptv.co.uk')
window.addControl(label)
xbmc.executebuiltin("ActivateWindow(10000)")

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




    
