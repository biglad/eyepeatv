import utils
import xbmc
import os
import xbmcgui

import sfile
import download
import urllib
import urllib2
import time 
import xbmcvfs
import base64
import shutil

KODIV          = float(xbmc.getInfoLabel("System.BuildVersion")[:4])
if KODIV > 17:
    import zfile as zipfile #FTG mod for Kodi 18
else:
    dialog = xbmcgui.Dialog()
    dialog.ok("[COLOR=red][B] ## KODI VERSION ERROR ##[/COLOR][/B]", "Kodi 18.x Is Supported", "Please Update","Press OK to Continue")
    exit()
    import zipfile

USERINFO = base64.b64decode("c3BlY2lhbDovL3VzZXJkYXRhLw==")
DATAHOME = base64.b64decode("c3BlY2lhbDovL2hvbWUv")
ADDONDATA = base64.b64decode("c3BlY2lhbDovL2hvbWUvYWRkb25z")
MYDATA = base64.b64decode("c3BlY2lhbDovL2hvbWUvYWRkb25zL3NjcmlwdC52aXN0YXR2LWluc3RhbGxlcg==")

USERDATA    = xbmc.translatePath(USERINFO)
HOME        = xbmc.translatePath(DATAHOME)
ADDONS      = xbmc.translatePath(ADDONDATA)
SELFDIR     = xbmc.translatePath(MYDATA)

#dp = xbmcgui.DialogProgress()
#dp.create("[COLOR tomato]VistaTV[/COLOR]","Connection to Server","Please Wait.....")
#xbmc.sleep(1000)

xbmc.Player().play('http://vistatv.online/intro.mp4')
while xbmc.getCondVisibility('Player.HasMedia'):
    xbmc.sleep(1000)
dp = xbmcgui.DialogProgress()
dp.create("[COLOR tomato]VistaTV[/COLOR]","Connection to Server","Please Wait.....")
xbmc.sleep(8000)



#HOME2     = xbmc.translatePath('special://userdata')
#file2 = os.path.join(HOME2, 'vistatv.xml')

HOME     = xbmc.translatePath('special://home')
#file4 = os.path.join(HOME2, 'networksettings.xml')

#file98 = os.path.join(HOME2, 'vistatv.xml') 

#with open(file98, 'r') as myfile:
#        data=float(myfile.read())
		
#with open(file98, 'r') as myfile:
#    data=float(myfile.read())

#megaver = float(data)

LOCATION     = "http://ftp.vistatv.online/baseinstall.zip"  #"http://vistatv.me/buildrepo-1/updatervista.php?v="+str(megaver)

ROOT     = xbmc.translatePath('special://home')
file     = os.path.join(HOME, '_mega_temp.zip')
GETTEXT  = utils.GETTEXT

file3 = os.path.join(HOME, 'mchangelog.xml')

    
 
def killxbmc():
    #dp = xbmcgui.DialogProgress()
    #dp.create("[COLOR tomato]Mega TV[/COLOR]","SPMC/Kodi is now Closing","This make take a while.")
    with open(file4, 'r') as myfile:
        boxid=myfile.read()
    #response = urllib2.urlopen('http://cerebrotv.co.uk/TV-DATA/auth2.php?id='+str(boxid)+'&die=1').read()
    xbmc.executebuiltin("Notification(VistaTV,Closing SPMC/Kodi, Will take a few seconds,7000,)")
    xbmc.sleep(1000)
    xbmc.executebuiltin("Action(Close)")
    os._exit(1)
    exit()

		
def platform():
    if xbmc.getCondVisibility('system.platform.android'):
        return 'android'
    elif xbmc.getCondVisibility('system.platform.linux'):
        return 'linux'
    elif xbmc.getCondVisibility('system.platform.windows'):
        return 'windows'
    elif xbmc.getCondVisibility('system.platform.osx'):
        return 'osx'
    elif xbmc.getCondVisibility('system.platform.atv2'):
        return 'atv2'
    elif xbmc.getCondVisibility('system.platform.ios'):
        return 'ios'

def noconnection():
    dialog = xbmcgui.Dialog()
    dialog.ok("[COLOR=red][B] ## CONNECTION ERROR ##[/COLOR][/B]", "Unable to download needed data....", "Will Try Again.","Press OK to Continue")
    xbmc.sleep(1000)
    #DownloaderClass(LOCATION,file)


def dlProgress(count, blockSize, totalSize):
      percent = int(count*blockSize*100/totalSize)
      dp = utils.Progress("[COLOR tomato]VistaTV Checking For Updates[/COLOR]", line1 = "[COLOR yellow]Please Wait Download in Progress[/COLOR].", line2 = "[COLOR gold]VistaTV Update Service[/COLOR]", line3 = "test")
      dp.update(percent)


def DownloaderClass(url,dest):
    start_time=time.time()
    dp = xbmcgui.DialogProgress()
    dp.create("[COLOR tomato]VistaTV Installer[/COLOR]","Downloading New Data","Please Wait")
    dp.update(0)
    try:
        #urllib.urlretrieve(url,dest,lambda nb, bs, fs, url=url: _pbhook(nb,bs,fs,url,dp))
        urllib.urlretrieve(url, dest, lambda nb, bs, fs: _pbhook(nb, bs, fs, dp, start_time))
        dp.create("[COLOR tomato]VistaTV IPTV,EPG & Menu Updater[/COLOR]","Installing New Data","Please Wait.......")
        if os.path.exists(file):
            #file3 = os.path.join(HOME, 'mchangelog.xml')
            #open(file3, 'w+')
            #userdata = "test|test"
            #with open(file3, 'w') as f:
            #    f.write(userdata)
            zfile = zipfile.ZipFile(file, 'r')	
            nItem = float(len(zfile.infolist()))
            index = 0
            for item in zfile.infolist():
                index += 1
			
                percent  = int(index / nItem *100)
                filename = item.filename
                dp.update(percent)
                try:
                    zfile.extract(item, ROOT)
                except Exception, e:
                    utils.log('Changelog error in extractAll')
                    utils.log(e)
        
        #xbmc.executebuiltin('UpdateAddonRepos()')
        #xbmc.executebuiltin('UpdateLocalAddons()')
        #utils.DeleteFile(file)	
        #dp.create("[COLOR tomato]VistaTV[/COLOR]","Update Complete","Closing Kodi....")	
        #xbmc.executebuiltin("Notification(VistaTV, [COLOR=green]Menu Updated[/COLOR],3000,)")
        #xbmc.sleep(3000)
        #xbmc.executebuiltin("Notification(VistaTV, [COLOR=green]Menu Reloaded[/COLOR],3000,)")
        #xbmc.executebuiltin("Container.Refresh")
        #exit()
        dialog = xbmcgui.Dialog()
        dialog.ok("[COLOR=red][B]VistaTV[/COLOR][/B]", "Installer Downloaded......", "Kodi will now Exit","Open kodi agin to continue install")
        xbmc.sleep(1000)
        os._exit(1)

    except Exception, e:
        noconnection()
        #print(e)
        exit()
 
def _pbhook(numblocks, blocksize, filesize, dp, start_time):
        try: 
            percent = min(numblocks * blocksize * 100 / filesize, 100)
            currently_downloaded = float(numblocks) * blocksize / (1024 * 1024) 
            kbps_speed = numblocks * blocksize / (time.time() - start_time) 
            if kbps_speed > 0: 
                eta = (filesize - numblocks * blocksize) / kbps_speed 
            else: 
                eta = 0 
            kbps_speed = kbps_speed / 1024 
            total = float(filesize) / (1024 * 1024) 
            mbs = '%.02f MB of %.02f MB' % (currently_downloaded, total) 
            e = 'Speed: %.02f Kb/s ' % kbps_speed 
            e += 'ETA: %02d:%02d' % divmod(eta, 60)
            dp.update(percent, mbs, e,' ')
        except: 
            percent = 100 
            dp.update(percent) 
        if dp.iscanceled(): 
            dp.close() 
 

 
if os.path.exists(file):
    utils.DeleteFile(file)

def CleanKodi():
    addondir = ADDONS
    datadir = USERDATA
    dp = xbmcgui.DialogProgress()
    dp.create("Staring Vista TV's Wizard","Removing",'Add-ons', 'Please Wait')
    percent = 05 
    dp.update(percent)
    try: shutil.rmtree(addondir)
    except: pass
    xbmc.sleep(9000)
    percent = 30 
    try: xbmcvfs.rmdir(addondir)
    except: pass
    xbmc.sleep(1000)
    percent = 50 
    dp.update(percent)
    dp.create("Staring Vista TV's Wizard","Removing",'Userdata', 'Please Wait')
    try: shutil.rmtree(datadir)
    except: pass
    xbmc.sleep(9000)
    percent = 68
    try: xbmcvfs.rmdir(datadir)
    except: pass
    xbmc.sleep(1000)
    percent = 83 
    dp.update(percent)
    dp.create("Staring Vista TV's Wizard","Getting Ready",'To Install', 'Please Wait')
    try: xbmcvfs.mkdir(datadir)
    except: pass
    xbmc.sleep(1000)
    try: xbmcvfs.mkdir(datadir)
    except: pass
    xbmc.sleep(1000)

def ping(host):
    """
    Returns True if host responds to a ping request
    """
    import os, platform

    # Ping parameters as function of OS
    ping_str = "-n 1" if  platform.system().lower()=="windows" else "-c 1"

    # Ping
    return os.system("ping " + ping_str + " " + host) == 0

update = xbmcgui.Dialog().yesno("[COLOR tomato]VistaTV Wizard[/COLOR]","[COLOR yellow]Do You Want to install Now?[/COLOR]","[COLOR turquoise]This is a paid for service!!!![/COLOR]" ,"[COLOR turquoise]Have your auth code ready!!!![/COLOR]")
if update:
    xbmcvfs.delete('special://addons/script.program.v-wizard/service.py')
    utils.DeleteFile('special://addons/script.program.v-wizard/service.py')
    DownloaderClass(LOCATION,file)
else: exit()	

dialog = xbmcgui.Dialog()
dialog.ok("[COLOR=red][B]VISTA TV[/COLOR][/B]", "KODI CLEANED AND SET FOR INSTALL OF VISTA!!", "Kodi will now exit, please re-load kodi","Press OK to Continue")
xbmc.sleep(1000)
os._exit(1)