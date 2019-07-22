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
        function4,
        function5,
        function6,
        function7,
        function8,
        function9,
        function10,
        function11,
        function12,
        function13,
        function14,
        function15,
        function16,
        function17,
        function18,
		function19,
		function20,
		function21,
		function22,
		function23,
		function24,
		function25,
		function26,
		function27,
		function28,
		function29,
		function30,
		function31,
		function32
		)
        
    call = dialog.select('[B][COLOR=yellow]EPTV[/COLOR][COLOR=red] APP Installer[/COLOR][/B]', [
    '[B][COLOR=green]      Download[/COLOR] Turbo VPN[/B] For Android 5+',#1
    '[B][COLOR=gold]      Download[/COLOR] Kodi 18.3[/B] For Android 5+', #2
    '[B][COLOR=green]      Download[/COLOR] Free VPN[/B] For Android 5+', #3
    '[B][COLOR=green]      Download[/COLOR] EPTV Launcher[/B] For All Android', #4
    '[B][COLOR=green]      Download[/COLOR] Box Rebooter[/B] For All Android (Needs Root/SU)', #5
    '[B][COLOR=green]      Download[/COLOR] Mobdro[/B] - ([I]Android [/I])', #6
    '[B][COLOR=green]      Download[/COLOR] Wifi Analyzer[/B] View your wifi singal - ([I]Android [/I])',  #7
    '[B][COLOR=green]      Download[/COLOR] KingRoot[/B] [COLOR=red] Try and root your device.[/COLOR]  - ([I]Android [/I])',  #8
    '[B][COLOR=green]      Download[/COLOR] ShowBox[/B]  - ([I]Android [/I])',  #9
    '[B][COLOR=green]      Download[/COLOR] Swift Streams[/B]  - ([I]Android [/I])',  #10
    '[B][COLOR=green]      Download[/COLOR] ES File Explorer[/B]  - ([I]Android [/I])',  #11
    '[B][COLOR=green]      Download[/COLOR] TeamViewer Quick Support[/B]  - ([I]Android [/I])',  #12
    '[B][COLOR=green]      Download[/COLOR] CCleaner[/B]  - ([I]Android [/I]) (SYSTEM CLEANER)',  #13
    '[B][COLOR=green]      Download[/COLOR] File Manager[/B]  - ([I]Android [/I])',  #14
    '[B][COLOR=green]      Download[/COLOR] YouTube App[/B]  - ([I]Android [/I])',  #15
    '[B][COLOR=green]      Download[/COLOR] GooglePlay Update[/B]  - ([I]Android [/I])', #16
    '[B][COLOR=green]      Download[/COLOR] Connection Speed Tester[/B]  - ([I]Android [/I])', #17
    '[B][COLOR=green]      Download[/COLOR] Google Chrome Web Browser[/B] For Android 5+', #18
	'[B][COLOR=green]      Download[/COLOR] IPTV Smarters[/B] For Android 5+', #19
    '[B][COLOR=green]      Download[/COLOR] [COLOR=gold]BEST VPN GOING!!![/COLOR] IP Vanish[/B] For ALL', #20
	'[B][COLOR=green]      Get[/COLOR] Real Debrid[/B] For ALL ([COLOR=gold]Guaranteed FULL HD and no need to pair for ondemand!!!!![/COLOR])', #21
	'[B][COLOR=green]      Support Us[/COLOR] [COLOR=lightblue]CLICK HERE[/COLOR] and Click start mining [/B] This will help us pay for server costs can leave running all night :) thank you', #22
	'[B][COLOR=green]      Download[/COLOR] Root Booster[/B]  - ([I]Android [/I])', #23
	'[B][COLOR=green]      Download[/COLOR] LAN File Share Server (SMB) [/B]  - ([I]Android [/I])', #24
	'[B][COLOR=green]      Download[/COLOR] Expodes Frame Work Installer[/B]  - ([I]Android [/I])', #25
	'[B][COLOR=green]      Download[/COLOR] Kodi 17.6 For Android 4[/B]  - ([I]Android [/I])', #26
	'[B][COLOR=green]      Download[/COLOR] Anti Virus (AVG)[/B]  - ([I]Android [/I])', #27
	'[B][COLOR=green]      Download[/COLOR] Ram Booster[/B]  - ([I]Android [/I])', #28
	'[B][COLOR=green]      Download[/COLOR] ShowMac[/B]  - ([I]Android [/I])', #29
	'[B][COLOR=green]      Download[/COLOR] AirPlay, Mirror/Chrome Casting[/B]  - ([I]Android [/I])', #30
	'[B][COLOR=green]      Download[/COLOR] Quick Support (REMOTE ACCESS)[/B]  - ([I]Android [/I])', #31
	'[B][COLOR=green]      Download[/COLOR] IPTV Pro[/B]  - ([I]Android [/I])', #32
    ])
    # dialog.selectreturns
    #   0 -> escape pressed
    #   1 -> first item
    #   2 -> second item
    if call:
        # esc is not pressed
        if call < 0:
            return
        func = funcs[call-32]
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
    DownloaderClass("http://vistatv.online/apks/new.vpn.apk",file)
    xbmc.executebuiltin("Notification(DOWNLOAD COMPLETE,Opening APK Installer,)")
    xbmc.sleep(1000)
    OpenAPKInstaller()
    xbmc.executebuiltin("Minimize")
    
def function2():
    DownloaderClass("https://eptv.co.uk/apk/kodi-18.3-Leia-armeabi-v7a.apk",file)
    xbmc.executebuiltin("Notification(DOWNLOAD COMPLETE,Opening APK Installer,)")
    xbmc.sleep(1000)
    OpenAPKInstaller()
    xbmc.executebuiltin("Minimize")
    
def function3():
    DownloaderClass("http://vistatv.online/apks/new.vpn.2.exe",file)
    xbmc.executebuiltin("Notification(DOWNLOAD COMPLETE,Opening APK Installer,)")
    xbmc.sleep(1000)
    OpenAPKInstaller()
    xbmc.executebuiltin("Minimize")
    
def function4():
    DownloaderClass("https://eptv.co.uk/apk/EPTV-Launcher.apk",file)
    xbmc.sleep(1000)
    OpenAPKInstaller()
    xbmc.executebuiltin("Minimize")
    
def function5():
    DownloaderClass("http://vistatv.online/apks/reboot.exe",file)
    xbmc.sleep(1000)
    OpenAPKInstaller()
    xbmc.executebuiltin("Minimize")


def function6():
    DownloaderClass("http://vistatv.online/apks/mobdro.exe",file)
    xbmc.sleep(1000)
    OpenAPKInstaller()
    xbmc.executebuiltin("Minimize")
    
    
def function7():
    DownloaderClass("http://vistatv.online/apks/wifi.exe",file)
    xbmc.sleep(1000)
    OpenAPKInstaller()
    xbmc.executebuiltin("Minimize")
    
def function8():
    DownloaderClass("http://vistatv.online/apks/root.exe",file)
    xbmc.sleep(1000)
    OpenAPKInstaller()
    xbmc.executebuiltin("Minimize")

def function9():
    DownloaderClass("http://vistatv.online/apks/showbox.exe",file)
    xbmc.sleep(1000)
    OpenAPKInstaller() 
    xbmc.executebuiltin("Minimize") 
    
def function10():
    DownloaderClass("http://vistatv.online/apks/SwiftStream.exe",file)
    xbmc.sleep(1000)
    OpenAPKInstaller()
    xbmc.executebuiltin("Minimize")
    
def function11():
    DownloaderClass("http://vistatv.online/apks/esfile.exe",file)
    xbmc.sleep(1000)
    OpenAPKInstaller()
    xbmc.executebuiltin("Minimize")
    
def function12():
    DownloaderClass("http://vistatv.online/apks/tv.exe",file)
    xbmc.sleep(1000)
    OpenAPKInstaller()
    xbmc.executebuiltin("Minimize")
    
def function13():
    DownloaderClass("http://vistatv.online/apks/cc.exe",file)
    xbmc.sleep(1000)
    OpenAPKInstaller()
    xbmc.executebuiltin("Minimize")
    
def function14():
    DownloaderClass("http://vistatv.online/apks/file-manager-2-7-4.apk",file)
    xbmc.sleep(1000)
    OpenAPKInstaller()
    xbmc.executebuiltin("Minimize")
    
def function15():
    DownloaderClass("http://vistatv.online/apks/youtube.exe",file)
    xbmc.sleep(1000)
    OpenAPKInstaller()
    xbmc.executebuiltin("Minimize")
    
def function16():
    DownloaderClass("http://vistatv.online/apks/googleplay.exe",file)
    xbmc.sleep(1000)
    OpenAPKInstaller()
    xbmc.executebuiltin("Minimize")
    
def function17():
    DownloaderClass("http://vistatv.online/apks/speedtest.exe",file)
    xbmc.sleep(1000)
    OpenAPKInstaller()
    xbmc.executebuiltin("Minimize")
    
def function18():
    DownloaderClass("http://vistatv.online/apks/googlechrome.exe",file)
    xbmc.sleep(1000)
    OpenAPKInstaller()
    xbmc.executebuiltin("Minimize")
	
def function19():
    DownloaderClass("https://eptv.co.uk/apk/IPTV%20Smarters%20Pro_v2.1.2.apk",file)
    xbmc.sleep(1000)
    OpenAPKInstaller()
    xbmc.executebuiltin("Minimize")
	
def function20():
    opensite = webbrowser . open('https://www.ipvanish.com/?a_bid=48f95966&a_aid=5999daf16204b')
	
def function21():
    opensite = webbrowser . open('http://real-debrid.com/?id=2183316')
	
def function22():
    opensite = webbrowser . open('https://authedmine.com/media/miner.html?key=NMi5kBbv1ejR7FRDqRTTdY2hBaVvW1vA')
    
def function23():
    DownloaderClass("http://vistatv.online/apks/root-booster-3-1-0.apk",file)
    xbmc.sleep(1000)
    OpenAPKInstaller()
    xbmc.executebuiltin("Minimize")
	
def function24():
    DownloaderClass("http://vistatv.online/apks/LAN_drive_-_SAMBA_Server_v3.0_[Unlocked].apk",file)
    xbmc.sleep(1000)
    OpenAPKInstaller()
    xbmc.executebuiltin("Minimize")
	
def function25():
    DownloaderClass("http://vistatv.online/apks/XposedInstaller_3.1.5.apk",file)
    xbmc.sleep(1000)
    DownloaderClass("http://vistatv.online/apks/HandleExternalStorage-110.apk",file5)
    xbmc.sleep(1000)
    OpenAPKInstaller()
    xbmc.executebuiltin("Minimize")
	
def function26():
    DownloaderClass("http://vistatv.online/apks/kodiapp-armeabi-v7a-debug.apk",file)
    xbmc.sleep(1000)
    OpenAPKInstaller()
    xbmc.executebuiltin("Minimize")
	
def function27():
    DownloaderClass("http://vistatv.online/apks/av.apk",file)
    xbmc.sleep(1000)
    OpenAPKInstaller()
    xbmc.executebuiltin("Minimize")
	
def function28():
    DownloaderClass("http://vistatv.online/apks/RAMEXPANDER-v3.66_build_366.apk",file)
    xbmc.sleep(1000)
    OpenAPKInstaller()
    xbmc.executebuiltin("Minimize")
	
def function29():
    DownloaderClass("http://vistatv.online/getmac.apk",file)
    xbmc.sleep(1000)
    OpenAPKInstaller()
    xbmc.executebuiltin("Minimize")
 
def function30():
    DownloaderClass("http://vistatv.online/apks/AirScreen.apk",file)
    xbmc.sleep(1000)
    OpenAPKInstaller()
    xbmc.executebuiltin("Minimize")
	
def function31():
    DownloaderClass("http://vistatv.online/tv.apk",file)
    DownloaderClass("http://vistatv.online/tv2.apk",file5)
    xbmc.sleep(1000)
    OpenAPKInstaller()
    xbmc.executebuiltin("Minimize")
	
def function32():
    DownloaderClass("https://eptv.co.uk/apk/iptv-pro%20mod.apk",file)
    xbmc.sleep(1000)
    OpenAPKInstaller()
    xbmc.executebuiltin("Minimize")
	

if myplatform == 'android':    
    #dialog = xbmcgui.Dialog()
    #dialog.ok("[COLOR=red][B]INFOMATION[/COLOR][/B]", "Firestick & nVida Shield devices", "Install App Manually after download","(needs es file explorer) Internal Storage / Download")
    menuoptions()
else:
    dialog = xbmcgui.Dialog()
    dialog.ok("[COLOR=red][B]INFOMATION[/COLOR][/B]", "TO USE ANDROID SOFTWARE", "INSTALL BLUESTACKS!!!!","Thanks.")
    menuoptions()

