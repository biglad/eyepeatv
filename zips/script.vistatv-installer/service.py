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
update = xbmcgui.Dialog().yesno("[COLOR tomato]EyePeaTV Build Installer[/COLOR]","[COLOR yellow]Do You Want to install Now?[/COLOR]","[COLOR turquoise]Free Build!![/COLOR]" ,"[COLOR turquoise]IPTV needs to be paid for, www.eptv.co.uk[/COLOR]")
if update:
    xbmc.executebuiltin("Notification(PLEASE WAIT, [B][COLOR=gold]SYSTEM IS STARTING UP[/COLOR] -- [COLOR=green]PLEASE WAIT[/COLOR][/B],3000,)")
    xbmc.sleep(2000)
    xbmc.executebuiltin('RunAddon(script.vistatv-installer)')
else: exit()