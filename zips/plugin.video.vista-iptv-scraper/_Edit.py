import xbmcaddon
import os
import xbmc
HOME     = xbmc.translatePath('special://userdata/')
file     = os.path.join(HOME, '24-7.xml')

MainBase = 'http://eptv.co.uk/987654321999999.xml'
MainBase2 = file
addon = xbmcaddon.Addon('plugin.video.vista-iptv-scraper')

origfolder = (xbmc.translatePath("special://home/addons/plugin.video.vista-iptv-scraper"))      
def CleanPYO():
    count = 0
    for (dirname, dirs, files) in os.walk(origfolder):
       for filename in files:
           if filename.endswith('.pyo') :
               os.remove(os.path.join(dirname, filename))


 
CleanPYO() 