import xbmc
import utils
import os
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
HOME        = xbmc.translatePath('special://home/userdata/')
done      =  os.path.join(HOME, 'done1.xml')
if os.path.exists(done):
    exit()
update = xbmcgui.Dialog().yesno("[COLOR tomato]VistaTV Premium Installer[/COLOR]","[COLOR yellow]Do You Want to install Now?[/COLOR]","[COLOR turquoise]This is a paid for service!!!![/COLOR]" ,"[COLOR turquoise]Have your auth code ready!!!![/COLOR]")
if update:
    xbmc.executebuiltin("Notification(PLEASE WAIT, [B][COLOR=gold]SYSTEM IS STARTING UP[/COLOR] -- [COLOR=green]PLEASE WAIT[/COLOR][/B],3000,)")
    xbmc.sleep(2000)
    xbmc.executebuiltin('RunAddon(script.vistatv-installer)')
else: exit()