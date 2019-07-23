import time
import xbmc
import os
import xbmcgui
import urllib2
import platform
import utils

import sfile
import download
import urllib
import webbrowser
KODIV          = float(xbmc.getInfoLabel("System.BuildVersion")[:4])
if KODIV > 17:
    import zfile as zipfile #FTG mod for Kodi 18
else:
    import zipfile
    

    
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
        
myplatform = platform()



if myplatform == 'android':
    HOME1     = '/storage/emulated/0/epsxe/bios/'
    HOME11     = '/storage/emulated/0/epsxe/'
    HOME3     = '/sdcard/epsxe/bios/'
    file = '/storage/emulated/0/Download/downloaded.apk'
    file5 = '/storage/emulated/0/Download/downloaded2.apk'
    file2 = os.path.join(HOME1, 'SCPH1001.bin')
    file3 = os.path.join(HOME1, 'SCPH1001.bin')
    
    
elif myplatform == 'windows':
    HOME1     = 'C:\ProgramData\Bluestacks\Engine\UserData\SharedFolder\epsxe\bios/'
    HOME11     = 'C:\ProgramData\Bluestacks\Engine\UserData\SharedFolder\epsxe/'
    HOME3     = 'C:\ProgramData\Bluestacks\Engine\UserData\SharedFolder\bios/'
    file = 'C:\ProgramData\Bluestacks\Engine\UserData\SharedFolder\downloaded.apk'
    file5 = 'C:\ProgramData\Bluestacks\Engine\UserData\SharedFolder\downloaded2.apk'
    file2 = 'C:\ProgramData\Bluestacks\Engine\UserData\SharedFolder\SCPH1001.bin'
    #file3 = os.path.join(HOME1, 'SCPH1001.bin')
    

def OpenAPKInstaller():
    if myplatform == 'android':
        xbmc.executebuiltin('StartAndroidActivity("com.droidlogic.appinstall")')
        xbmc.executebuiltin('StartAndroidActivity("com.gsoft.appinstall")')
        xbmc.executebuiltin('StartAndroidActivity("com.estrongs.android.pop")')
    if myplatform == 'windows':
        os.system(file)
        os.system("start C:\ProgramData\BlueStacks\Client\BlueStacks.exe")
        xbmc.executebuiltin("Minimize")
        
        

HOME2     = xbmc.translatePath('special://home')

if not os.path.exists('/storage/emulated/0/Download/'):
    try: os.makedirs('/storage/emulated/0/Download/')
    except: pass



del1     = xbmc.translatePath('/storage/emulated/0/Download/downloaded.apk')
del2     = xbmc.translatePath('/storage/emulated/0/Download/downloaded.apk')
try: os.remove(del1)
except: pass
try: os.remove(del2)
except: pass

del11     = 'C:\ProgramData\Bluestacks\Engine\UserData\SharedFolder\downloaded.apk'
del22     = 'C:\ProgramData\Bluestacks\Engine\UserData\SharedFolder\downloaded.apk'
try: os.remove(del11)
except: pass
try: os.remove(del22)
except: pass


def dlProgress(count, blockSize, totalSize):
      percent = int(count*blockSize*100/totalSize)
      dp = utils.Progress("[COLOR tomato]VistaTV Checking For Updates[/COLOR]", line1 = "[COLOR yellow]Please Wait Download in Progress[/COLOR].", line2 = "[COLOR gold]VistaTV Update Service[/COLOR]", line3 = "test")
      dp.update(percent)


def DownloaderClass(url,dest):
    dp = xbmcgui.DialogProgress()
    dp.create("[COLOR tomato]VistaTV App Installer[/COLOR]","Downloading App Installer","This make take a few seconds.")
    try:
        urllib.urlretrieve(url,dest,lambda nb, bs, fs, url=url: _pbhook(nb,bs,fs,url,dp))
        
    except Exception, e:
        xbmc.executebuiltin("Notification(DOWNLOAD FAILED,Try Again,)")
        #print(e)
        #exit()
 
def _pbhook(numblocks, blocksize, filesize, url=None,dp=None):
    try:
        percent = min((numblocks*blocksize*100)/filesize, 100)
        #print percent
        dp.update(percent)
    except:
        percent = 100
        dp.update(percent)
    if dp.iscanceled(): 
        print "DOWNLOAD CANCELLED" # need to get this part working
        #dp.close()
 



def menuoptions():
    dialog = xbmcgui.Dialog()
    funcs = (
        function1,
        function2,
		function3,
		function4
		)
        
    call = dialog.select('[B][COLOR=yellow]EPTV[/COLOR][COLOR=red] APP Menu[/COLOR][/B]', [
    "[B][COLOR=green]      Download[/COLOR] BlueStacks[/B]",#1
    "[B][COLOR=green]      Download[/COLOR] ProgDVB (IPTV Player) x32[/B]", #2
	"[B][COLOR=green]      Download[/COLOR] ProgDVB (IPTV Player) x64[/B]", #3
	"[B][COLOR=green]      Download[/COLOR] Intel HD Driver Update[/B]", #3
    ])
    # dialog.selectreturns
    #   0 -> escape pressed
    #   1 -> first item
    #   2 -> second item
    if call:
        # esc is not pressed
        if call < 0:
            return
        func = funcs[call-4]
        #if myplatform == 'windows':
        #    func = funcs[call-23]
        #dp = xbmcgui.DialogProgress()
        #dp.create("[COLOR tomato]VistaTV[/COLOR]",""+str(func)+" -3","PLEASE EXIT KODI OR PULL THE POWER LEAD")
        #xbmc.sleep(1000)
        return func()
    else:
        func = funcs[call]
        #dp = xbmcgui.DialogProgress()
        #dp.create("[COLOR tomato]VistaTV[/COLOR]",""+str(func)+" +0","PLEASE EXIT KODI OR PULL THE POWER LEAD")
        #xbmc.sleep(1000)
        return func()
    return 


def function1():
    opensite = webbrowser . open('https://saanvi.nokfile.com/zl/838934391/eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJjdXN0b21lcl9pZCI6IjgzODkzNDM5MSIsInppcHJlcXVlc3QiOiI1ZDM3MDM3MjZjOTE1In0.dixw6suZ98jClyRla896wSR2baS20akHm_bQ6IMiyhg/BlueStacks+4+%28v4.50.0.1043%29+HD+App+Player+%2B+Premium+%2B+Root+%7BB4tman%7D.zip')
	
def function2():
    opensite = webbrowser . open('https://eptv.co.uk/apps/ProgDVB7.28.4Std.exe')
	
def function3():
    opensite = webbrowser . open('https://eptv.co.uk/apps/ProgDVB7.28.4x64.exe')
	
def function4():
    opensite = webbrowser . open('https://eptv.co.uk/apps/Intel-Driver-and-Support-Assistant-Installer.exe')
	
	
menuoptions()


