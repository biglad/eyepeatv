import time
import xbmc
import os
import xbmcgui
import urllib2
import xbmcaddon
import subprocess
import platform
import re
import random
import string
from urllib2 import urlopen



__addon__ = xbmcaddon.Addon()
__addonname__ = __addon__.getAddonInfo('name')
__icon__ = __addon__.getAddonInfo('icon')
xbmc.executebuiltin("Notification(EyePeaTV, Checking For Updates,5000,"+__icon__ +")")

def UpdateCheck():
    xbmc.executebuiltin('xbmc.UpdateAddonRepos')
    xbmc.executebuiltin('xbmc.UpdateLocalAddons')
    xbmc.executebuiltin("XBMC.AlarmClock('MTVBCS',XBMC.RunAddon(script.eptv.core),240,silent)")
    return
            

    

UpdateCheck()



    
