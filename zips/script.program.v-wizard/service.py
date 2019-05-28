import xbmc
import os
import xbmcgui
HOME        = xbmc.translatePath('special://home/userdata')
done      =  os.path.join(HOME, 'done.xml')
if os.path.exists(done):
    exit()
else:
    xbmc.executebuiltin('RunAddon(script.program.v-wizard)')