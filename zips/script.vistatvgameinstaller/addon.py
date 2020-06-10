import time
import xbmc
import os
import xbmcgui
import urllib2
import platform
import utils
import zipfile
import sfile
import download
import urllib

ipaddy="0.0.0.0"
HOME     = xbmc.translatePath('special://userdata/')
iddata   = os.path.join(HOME, 'networksettings.xml')
#with open(iddata, 'r') as myfile:
#    data300=str(myfile.read())
#response = urllib2.urlopen('http://cerebrotv.co.uk/TV-DATA/auth2.php?id='+str(data300)+'&ok=OK&ip='+ipaddy).read()
#if not response == "OK":
#    xbmc.executebuiltin("Notification([COLOR=gold]EyePeaTV[/COLOR],NO CODE FOUND, ..,4000,)")
#    exit()
    

    
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



myplatform = platform()
if myplatform == 'android': 
    HOME1     = '/storage/emulated/0/ROMs/MAME4droid/roms/'
    HOME2     = '/storage/emulated/0/Download/'
    HOME3     = '/storage/emulated/0/#MEGADRIVE/'
    HOME4     = '/storage/emulated/0/'
    HOME11     = '/storage/emulated/0/#PSX/'
    HOME5     = '/storage/emulated/0/#N64/'
    file2 = os.path.join(HOME2, 'SCPH1001.bin')
    file3 = os.path.join(HOME2, 'Kickstart1.2.rom')
    file4 = os.path.join(HOME2, 'Kickstart1.3.rom')
    file5 = os.path.join(HOME2, 'Kickstart2.0.rom')
    file6 = os.path.join(HOME2, 'Kickstart3.0.rom')
    file7 = os.path.join(HOME2, 'Kickstart3.1.rom')
    file8 = os.path.join(HOME2, 'Kickstart4.0.rom')
    
elif myplatform == 'windows': 
    HOME1     = 'C:\ProgramData\Bluestacks\Engine\UserData\SharedFolder\#MAME4droid\roms\\'
    HOME2     = 'C:\ProgramData\\Bluestacks\Engine\UserData\SharedFolder\Download\\'
    HOME3     = 'C:\ProgramData\Bluestacks\Engine\UserData\SharedFolder\#MEGADRIVE\\'
    HOME4     = 'C:\ProgramData\Bluestacks\Engine\UserData\SharedFolder\\'
    HOME11     = 'C:\ProgramData\Bluestacks\Engine\UserData\SharedFolder\#PSX\\'
    HOME5     = 'C:\ProgramData\Bluestacks\Engine\UserData\SharedFolder\#N64\\'
    file2 = os.path.join(HOME2, 'SCPH1001.bin')
    os.system("special://home/addons/script.vistatvgameinstaller/bluetacks.bat")

def OpenAPKInstaller():
    if myplatform == 'android':
        xbmc.executebuiltin('StartAndroidActivity("com.droidlogic.appinstall")')
        xbmc.executebuiltin('StartAndroidActivity("com.gsoft.appinstall")')
        xbmc.executebuiltin('StartAndroidActivity("com.estrongs.android.pop")')
    if myplatform == 'windows':
        os.system(file)
        os.system("C:\ProgramData\BlueStacks\Client\BlueStacks.exe ")
        xbmc.executebuiltin("Minimize")
        
        

#HOME2     = xbmc.translatePath('special://home')

if not os.path.exists('/storage/emulated/0/Download/'):
    try: os.makedirs('/storage/emulated/0/Download/')
    except: pass
    
if not os.path.exists(HOME1):
    try: os.mkdir(HOME1)
    except: pass
    
if not os.path.exists(HOME11):
    try: os.mkdir(HOME11)
    except: pass
    
if not os.path.exists(HOME3):
    try: os.mkdir(HOME3)
    except: pass
    
if not os.path.exists(HOME4):
    try: os.mkdir(HOME4)
    except: pass

file = os.path.join(HOME2, 'CLICK-ME-TO-INSTALL-WHAT-YOU-JUST-DOWNLOADED.apk')

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

mamefile = os.path.join(HOME1, 'mame.zip')
gamefile = os.path.join(HOME4, 'psx.zip')
megafile = os.path.join(HOME3, 'mega.zip')
snesfile = os.path.join(HOME4, 'snes.zip')
n64file = os.path.join(HOME5, 'n64')
amigafile = os.path.join(HOME2, 'amiga.zip')


def dlProgress(count, blockSize, totalSize):
      percent = int(count*blockSize*100/totalSize)
      dp = utils.Progress("[COLOR tomato]EyePeaTV Checking For Updates[/COLOR]", line1 = "[COLOR yellow]Please Wait Download in Progress[/COLOR].", line2 = "[COLOR gold]EyePeaTV Update Service[/COLOR]", line3 = "test")
      dp.update(percent)


def DownloaderClass(url,dest):
    dp = xbmcgui.DialogProgress()
    dp.create("[COLOR tomato]EyePeaTV Game Downloader[/COLOR]","Downloading","This may take a few seconds.")
    try:
        urllib.urlretrieve(url,dest,lambda nb, bs, fs, url=url: _pbhook(nb,bs,fs,url,dp))
        
    except Exception, e:
        xbmc.executebuiltin("Notification(DOWNLOAD FAILED,Try Again,)")
        #print(e)
        exit()
 
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
 
def DownloaderClass2(url,dest):
    dp = xbmcgui.DialogProgress()
    dp.create("[COLOR tomato]EyePeaTV Game Downloader[/COLOR]","Downloading Game","This may take a while.")
    try:
        urllib.urlretrieve(url,dest,lambda nb, bs, fs, url=url: _pbhook(nb,bs,fs,url,dp))
        dp.create("[COLOR tomato]EyePeaTV Game Installer[/COLOR]","Adding Game files to system","Please Wait.")

        zfile = zipfile.ZipFile(gamefile, 'r')  
        nItem = float(len(zfile.infolist()))
        index = 0
        for item in zfile.infolist():
            index += 1
        
            percent  = int(index / nItem *100)
            filename = item.filename
            dp.update(percent)
            try:
                zfile.extract(item, HOME11)
            except Exception, e:
                utils.log('Changelog error in extractAll')
                utils.log(e)
        

        utils.DeleteFile(gamefile)  


    except Exception, e:
        #noconnection()
        #print(e)
        exit()
        
        
def DownloaderClass3(url,dest):
    dp = xbmcgui.DialogProgress()
    dp.create("[COLOR tomato]EyePeaTV Game Downloader[/COLOR]","Downloading Game","This may take a while.")
    try:
        urllib.urlretrieve(url,dest,lambda nb, bs, fs, url=url: _pbhook(nb,bs,fs,url,dp))
        dp.create("[COLOR tomato]EyePeaTV Game Installer[/COLOR]","Adding Game files to system","Please Wait.")

        zfile = zipfile.ZipFile(mamefile, 'r')  
        nItem = float(len(zfile.infolist()))
        index = 0
        for item in zfile.infolist():
            index += 1
        
            percent  = int(index / nItem *100)
            filename = item.filename
            dp.update(percent)
            try:
                zfile.extract(item, HOME4)
            except Exception, e:
                utils.log('Changelog error in extractAll')
                utils.log(e)
        

        utils.DeleteFile(mamefile)  


    except Exception, e:
        #noconnection()
        print(e)
        exit()
        
def DownloaderClass4(url,dest):
    dp = xbmcgui.DialogProgress()
    dp.create("[COLOR tomato]EyePeaTV Game Downloader[/COLOR]","Downloading MegaDrive Roms","This may take a few seconds.")
    try:
        urllib.urlretrieve(url,dest,lambda nb, bs, fs, url=url: _pbhook(nb,bs,fs,url,dp))
        dp.create("[COLOR tomato]EyePeaTV Game Installer[/COLOR]","Adding Game files to system","Please Wait.")

        zfile = zipfile.ZipFile(megafile, 'r')  
        nItem = float(len(zfile.infolist()))
        index = 0
        for item in zfile.infolist():
            index += 1
        
            percent  = int(index / nItem *100)
            filename = item.filename
            dp.update(percent)
            try:
                zfile.extract(item, HOME3)
            except Exception, e:
                utils.log('Changelog error in extractAll')
                utils.log(e)
        

        utils.DeleteFile(megafile)  


    except Exception, e:
        #noconnection()
        #print(e)
        exit()
        
def DownloaderClass5(url,dest):
    dp = xbmcgui.DialogProgress()
    dp.create("[COLOR tomato]EyePeaTV Game Downloader[/COLOR]","Downloading SENS Roms","This may take a few seconds.")
    try:
        urllib.urlretrieve(url,dest,lambda nb, bs, fs, url=url: _pbhook(nb,bs,fs,url,dp))
        dp.create("[COLOR tomato]EyePeaTV Game Installer[/COLOR]","Adding Game files to system","Please Wait.")

        zfile = zipfile.ZipFile(snesfile, 'r')  
        nItem = float(len(zfile.infolist()))
        index = 0
        for item in zfile.infolist():
            index += 1
        
            percent  = int(index / nItem *100)
            filename = item.filename
            dp.update(percent)
            try:
                zfile.extract(item, HOME4)
            except Exception, e:
                utils.log('Changelog error in extractAll')
                utils.log(e)
        

        utils.DeleteFile(snesfile)  


    except Exception, e:
        #noconnection()
        #print(e)
        exit()
        
def DownloaderClass6(url,dest):
    dp = xbmcgui.DialogProgress()
    dp.create("[COLOR tomato]EyePeaTV Game Downloader[/COLOR]","Downloading N64 Game","This may take a few seconds.")
    try:
        urllib.urlretrieve(url,dest,lambda nb, bs, fs, url=url: _pbhook(nb,bs,fs,url,dp))
        dp.create("[COLOR tomato]EyePeaTV Game Installer[/COLOR]","Adding Game files to system","Please Wait.")
        


    except Exception, e:
        #noconnection()
        #print(e)
        exit()
        
def DownloaderClass7(url,dest):
    dp = xbmcgui.DialogProgress()
    dp.create("[COLOR tomato]EyePeaTV Game Downloader[/COLOR]","Downloading SENS Roms","This may take a few seconds.")
    try:
        urllib.urlretrieve(url,dest,lambda nb, bs, fs, url=url: _pbhook(nb,bs,fs,url,dp))
        dp.create("[COLOR tomato]EyePeaTV Game Installer[/COLOR]","Adding Game files to system","Please Wait.")

        zfile = zipfile.ZipFile(snesfile, 'r')  
        nItem = float(len(zfile.infolist()))
        index = 0
        for item in zfile.infolist():
            index += 1
        
            percent  = int(index / nItem *100)
            filename = item.filename
            dp.update(percent)
            try:
                zfile.extract(item, HOME2)
            except Exception, e:
                utils.log('Changelog error in extractAll')
                utils.log(e)
        

        utils.DeleteFile(snesfile)  


    except Exception, e:
        #noconnection()
        #print(e)
        exit()
 
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
 
def menuoptions2():
    dialog = xbmcgui.Dialog()
    funcs = (
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
        function32,
        function33,
        function34,
        function35,
        function36,
        function37,
        function38,
        function39,
        function40,
        function41,
        function42
        )
        
    call = dialog.select('[B][COLOR=yellow]EyePeaTV[/COLOR][COLOR=red] Retro Games[/COLOR][/B]', 
    ['[B][COLOR=gold]Download R-Type Delta (PSX)[/COLOR][/B]'
    ,'[B][COLOR=gold]Download Bubble Bobble 2 (PSX)[/COLOR][/B]'
    , '[B][COLOR=gold]Download Crashbandicoot 3 Warped (PSX)[/COLOR][/B]'
    , '[B][COLOR=gold]Download MegaDrive (Genesis) Roms[/COLOR][/B] (Multi Games)'
    , '[B][COLOR=gold]Download M.A.M.E Roms Part 1[/COLOR][/B] (Multi Games)'
    , '[B][COLOR=gold]Download M.A.M.E Roms Part 2[/COLOR][/B] (Multi Games)'
    , '[B][COLOR=gold]Download Dragon Ball GT Final Bout (PSX)[/COLOR][/B]'
    , '[B][COLOR=gold]Download Street Fighter Zero 3 (PSX)[/COLOR][/B]'
    , '[B][COLOR=gold]Download R-Type 1 & 2 (PSX)[/COLOR][/B]'
    , '[B][COLOR=gold]Download SNES Games (Multi Games)[/COLOR][/B]'
    , '[B][COLOR=gold]Azure Dreams (PSX)[/COLOR][/B]'
    , '[B][COLOR=gold]Harvest Moon Back to Nature (PSX)[/COLOR][/B]'
    , '[B][COLOR=gold]Golden Eye (N64)[/COLOR][/B]'
    , '[B][COLOR=gold]Mario Kart (N64)[/COLOR][/B]'
    , '[B][COLOR=gold]Super Mario (N64)[/COLOR][/B]'
    , '[B][COLOR=gold]Donkey Kong (N64)[/COLOR][/B]'
    , '[B][COLOR=gold]Mortal Kombat 4 (N64)[/COLOR][/B]'
    , '[B][COLOR=gold]Super Smash Bros. (N64)[/COLOR][/B]'
    , '[B][COLOR=gold]Bust A Move "99 (N64)[/COLOR][/B]'
    , '[B][COLOR=gold]Banjo-Kazooie (N64)[/COLOR][/B]'  
    , '[B][COLOR=gold]Command & Conquer (N64)[/COLOR][/B]'
    , '[B][COLOR=gold]Gauntlet Legends (N64)[/COLOR][/B]'
    , '[B][COLOR=gold]Star Wars Episode I - Racer (N64)[/COLOR][/B]'
    , '[B][COLOR=gold]Jet Force Gemini (N64)[/COLOR][/B]'
    , '[B][COLOR=gold]Quake 64 (N64)[/COLOR][/B]'
    , '[B][COLOR=gold]Doom 64 (N64)[/COLOR][/B]'
    , '[B][COLOR=gold]Worms Armageddon (N64)[/COLOR][/B]'
    , '[B][COLOR=gold]A Bugs Life (N64)[/COLOR][/B]'
    , '[B][COLOR=gold]Road Rash 64 (N64)[/COLOR][/B]'
    , '[B][COLOR=gold]Resident Evil 2 (N64)[/COLOR][/B]'
    , '[B][COLOR=gold]Mortal Kombat Trilogy (N64)[/COLOR][/B]'
    , '[B][COLOR=gold]Diddy Kong Racing (N64)[/COLOR][/B]'
    , '[B][COLOR=gold]Amiga Game Pack (Amiga)[/COLOR][/B]'
    ])
    # dialog.selectreturns
    #   0 -> escape pressed
    #   1 -> first item
    #   2 -> second item
    if call:
        # esc is not pressed
        if call < 0:
            return
        func = funcs[call-34]
        #dp = xbmcgui.DialogProgress()
        #dp.create("[COLOR tomato]EyePeaTV[/COLOR]",""+str(func)+" -3","PLEASE EXIT KODI OR PULL THE POWER LEAD")
        #xbmc.sleep(1000)
        return func()
    else:
        func = funcs[call]
        #dp = xbmcgui.DialogProgress()
        #dp.create("[COLOR tomato]EyePeaTV[/COLOR]",""+str(func)+" +0","PLEASE EXIT KODI OR PULL THE POWER LEAD")
        #xbmc.sleep(1000)
        return func()
    return 

def function11():
    DownloaderClass2("http://EyePeaTV.online/bins/rtype.zip",gamefile)
    openapp = xbmcgui.Dialog().yesno("[COLOR tomato]EyePeaTV[/COLOR]","[COLOR yellow][/COLOR]","Launch ePSXe?" ,"","No","Yes")
    if openapp:
        xbmc.executebuiltin('StartAndroidActivity("com.epsxe.ePSXe")') 
        if myplatform == 'windows':
            os.system("special://home/addons/script.vistatvgameinstaller/bluetacks.bat")
 
def function12():
    DownloaderClass2("http://EyePeaTV.online/bins/bb.zip",gamefile)
    openapp = xbmcgui.Dialog().yesno("[COLOR tomato]EyePeaTV[/COLOR]","[COLOR yellow][/COLOR]","Launch ePSXe?" ,"","No","Yes")
    if openapp:
        xbmc.executebuiltin('StartAndroidActivity("com.epsxe.ePSXe")') 
        if myplatform == 'windows':
            os.system("special://home/addons/script.vistatvgameinstaller/bluetacks.bat")
            xbmc.executebuiltin("Minimize")

def function13():
    DownloaderClass2("http://EyePeaTV.online/bins/cb.zip",gamefile)
    openapp = xbmcgui.Dialog().yesno("[COLOR tomato]EyePeaTV[/COLOR]","[COLOR yellow][/COLOR]","Launch ePSXe?" ,"","No","Yes")
    if openapp:
        xbmc.executebuiltin('StartAndroidActivity("com.epsxe.ePSXe")') 
        if myplatform == 'windows':
            os.system("special://home/addons/script.vistatvgameinstaller/bluetacks.bat")
            xbmc.executebuiltin("Minimize")
         
def function14():
    if not os.path.exists(HOME3):
        try: os.mkdir(HOME3)
        except: pass
    DownloaderClass4("http://EyePeaTV.online/bins/MEGADRIVE.zip",megafile)
    openapp = xbmcgui.Dialog().yesno("[COLOR tomato]EyePeaTV[/COLOR]","[COLOR yellow][/COLOR]","Launch Gensoid?" ,"","No","Yes")
    if openapp:
        xbmc.executebuiltin('StartAndroidActivity("com.androidemu.gens")')
        if myplatform == 'windows':
            os.system("special://home/addons/script.vistatvgameinstaller/bluetacks.bat")
            xbmc.executebuiltin("Minimize")

def function15():
    if not os.path.exists(HOME1):
        try: os.mkdir(HOME1)
        except: pass
    DownloaderClass3("http://EyePeaTV.online/bins/mame.zip",mamefile)
    openapp = xbmcgui.Dialog().yesno("[COLOR tomato]EyePeaTV[/COLOR]","[COLOR yellow][/COLOR]","Launch M.A.M.E?" ,"","No","Yes")
    if openapp:
        xbmc.executebuiltin('StartAndroidActivity("com.seleuco.mame4droid")')
        if myplatform == 'windows':
            os.system("special://home/addons/script.vistatvgameinstaller/bluetacks.bat")
            xbmc.executebuiltin("Minimize")
        
def function16():
    if not os.path.exists(HOME1):
        try: os.mkdir(HOME1)
        except: pass
    DownloaderClass3("http://EyePeaTV.online/bins/mame2.zip",mamefile)
    openapp = xbmcgui.Dialog().yesno("[COLOR tomato]EyePeaTV[/COLOR]","[COLOR yellow][/COLOR]","Launch M.A.M.E?" ,"","No","Yes")
    if openapp:
        xbmc.executebuiltin('StartAndroidActivity("com.seleuco.mame4droid")')
        if myplatform == 'windows':
            os.system("special://home/addons/script.vistatvgameinstaller/bluetacks.bat")
            xbmc.executebuiltin("Minimize")
        
def function17():
    DownloaderClass2("http://EyePeaTV.online/bins/db.zip",gamefile)
    openapp = xbmcgui.Dialog().yesno("[COLOR tomato]EyePeaTV[/COLOR]","[COLOR yellow][/COLOR]","Launch ePSXe?" ,"","No","Yes")
    if openapp:
        xbmc.executebuiltin('StartAndroidActivity("com.epsxe.ePSXe")') 
        if myplatform == 'windows':
            os.system("special://home/addons/script.vistatvgameinstaller/bluetacks.bat")
            xbmc.executebuiltin("Minimize")
        
def function18():
    xbmc.executebuiltin("Notification(EyePeaTV,THIS GAME WILL TAKE ALONG TIME TO INSTALL, ..,27000,)")
    DownloaderClass2("http://EyePeaTV.online/bins/StreetFighterZero3.zip",gamefile)
    openapp = xbmcgui.Dialog().yesno("[COLOR tomato]EyePeaTV[/COLOR]","[COLOR yellow][/COLOR]","Launch ePSXe?" ,"","No","Yes")
    if openapp:
        xbmc.executebuiltin('StartAndroidActivity("com.epsxe.ePSXe")') 
        if myplatform == 'windows':
            os.system("special://home/addons/script.vistatvgameinstaller/bluetacks.bat")
            xbmc.executebuiltin("Minimize")
        
def function19():
    DownloaderClass2("http://EyePeaTV.online/bins/rtypes.zip",gamefile)
    openapp = xbmcgui.Dialog().yesno("[COLOR tomato]EyePeaTV[/COLOR]","[COLOR yellow][/COLOR]","Launch ePSXe?" ,"","No","Yes")
    if openapp:
        xbmc.executebuiltin('StartAndroidActivity("com.epsxe.ePSXe")') 
        if myplatform == 'windows':
            os.system("special://home/addons/script.vistatvgameinstaller/bluetacks.bat")
            xbmc.executebuiltin("Minimize")
        
def function20():
    DownloaderClass5("http://EyePeaTV.online/bins/snes.zip",snesfile)
    openapp = xbmcgui.Dialog().yesno("[COLOR tomato]EyePeaTV[/COLOR]","[COLOR yellow][/COLOR]","Launch SENS Emulator?" ,"","No","Yes")
    if openapp:
        xbmc.executebuiltin('StartAndroidActivity("com.explusalpha.Snes9xPlus")') 
        if myplatform == 'windows':
            os.system("special://home/addons/script.vistatvgameinstaller/bluetacks.bat")
            xbmc.executebuiltin("Minimize")
        
def function21():
    DownloaderClass2("http://EyePeaTV.online/bins/azuredreams.zip",gamefile)
    openapp = xbmcgui.Dialog().yesno("[COLOR tomato]EyePeaTV[/COLOR]","[COLOR yellow][/COLOR]","Launch ePSXe?" ,"","No","Yes")
    if openapp:
        xbmc.executebuiltin('StartAndroidActivity("com.epsxe.ePSXe")') 
        if myplatform == 'windows':
            os.system("special://home/addons/script.vistatvgameinstaller/bluetacks.bat")
            xbmc.executebuiltin("Minimize")
        
def function22():
    DownloaderClass2("http://EyePeaTV.online/bins/HarvestMoonBacktoNature.zip",gamefile)
    openapp = xbmcgui.Dialog().yesno("[COLOR tomato]EyePeaTV[/COLOR]","[COLOR yellow][/COLOR]","Launch ePSXe?" ,"","No","Yes")
    if openapp:
        xbmc.executebuiltin('StartAndroidActivity("com.epsxe.ePSXe")') 
        if myplatform == 'windows':
            os.system("special://home/addons/script.vistatvgameinstaller/bluetacks.bat")
            xbmc.executebuiltin("Minimize")
        
        
def function23():
    DownloaderClass6("http://EyePeaTV.online/bins/007%20-%20GoldenEye%20(USA).zip",n64file+'-Goldeneye.zip')
    openapp = xbmcgui.Dialog().yesno("[COLOR tomato]EyePeaTV[/COLOR]","[COLOR yellow][/COLOR]","Launch N64 Emulator?" ,"","No","Yes")
    if openapp:
        xbmc.executebuiltin('StartAndroidActivity("com.aspieapps.free.emulator")') 
        if myplatform == 'windows':
            os.system("special://home/addons/script.vistatvgameinstaller/bluetacks.bat")
            xbmc.executebuiltin("Minimize")
        
def function24():
    DownloaderClass6("http://EyePeaTV.online/bins/Mario%20Kart%2064%20(Europe).zip",n64file+'-MarioKart.zip')
    openapp = xbmcgui.Dialog().yesno("[COLOR tomato]EyePeaTV[/COLOR]","[COLOR yellow][/COLOR]","Launch N64 Emulator?" ,"","No","Yes")
    if openapp:
        xbmc.executebuiltin('StartAndroidActivity("com.aspieapps.free.emulator")') 
        if myplatform == 'windows':
            os.system("special://home/addons/script.vistatvgameinstaller/bluetacks.bat")
        
def function25():
    DownloaderClass6("http://EyePeaTV.online/bins/Super%20Mario%2064.zip",n64file+'-SuperMario.zip')
    openapp = xbmcgui.Dialog().yesno("[COLOR tomato]EyePeaTV[/COLOR]","[COLOR yellow][/COLOR]","Launch N64 Emulator?" ,"","No","Yes")
    if openapp:
        xbmc.executebuiltin('StartAndroidActivity("com.aspieapps.free.emulator")')
        if myplatform == 'windows':
            os.system("special://home/addons/script.vistatvgameinstaller/bluetacks.bat") 
            xbmc.executebuiltin("Minimize")         
        
def function26():
    DownloaderClass6("http://EyePeaTV.online/bins/Donkey%20Kong%2064.zip",n64file+'-DonkeyKong.zip')
    openapp = xbmcgui.Dialog().yesno("[COLOR tomato]EyePeaTV[/COLOR]","[COLOR yellow][/COLOR]","Launch N64 Emulator?" ,"","No","Yes")
    if openapp:
        xbmc.executebuiltin('StartAndroidActivity("com.aspieapps.free.emulator")') 
        if myplatform == 'windows':
            os.system("special://home/addons/script.vistatvgameinstaller/bluetacks.bat")
            xbmc.executebuiltin("Minimize")
        
def function27():
    DownloaderClass6("http://EyePeaTV.online/bins/Mortal%20Kombat%204%20(USA).zip",n64file+'-MortlaKombat4.zip')
    openapp = xbmcgui.Dialog().yesno("[COLOR tomato]EyePeaTV[/COLOR]","[COLOR yellow][/COLOR]","Launch N64 Emulator?" ,"","No","Yes")
    if openapp:
        xbmc.executebuiltin('StartAndroidActivity("com.aspieapps.free.emulator")') 
        if myplatform == 'windows':
            os.system("special://home/addons/script.vistatvgameinstaller/bluetacks.bat")
            xbmc.executebuiltin("Minimize")
        
def function28():
    DownloaderClass6("http://EyePeaTV.online/bins/Super%20Smash%20Bros.%20(USA).zip",n64file+'-SuperSmashBros.zip')
    openapp = xbmcgui.Dialog().yesno("[COLOR tomato]EyePeaTV[/COLOR]","[COLOR yellow][/COLOR]","Launch N64 Emulator?" ,"","No","Yes")
    if openapp:
        xbmc.executebuiltin('StartAndroidActivity("com.aspieapps.free.emulator")') 
        if myplatform == 'windows':
            os.system("special://home/addons/script.vistatvgameinstaller/bluetacks.bat")
            xbmc.executebuiltin("Minimize")

def function29():
    DownloaderClass6("http://EyePeaTV.online/bins/Bust-A-Move%20'99%20(USA).zip",n64file+'-BustAMove.zip')
    openapp = xbmcgui.Dialog().yesno("[COLOR tomato]EyePeaTV[/COLOR]","[COLOR yellow][/COLOR]","Launch N64 Emulator?" ,"","No","Yes")
    if openapp:
        xbmc.executebuiltin('StartAndroidActivity("com.aspieapps.free.emulator")') 
        if myplatform == 'windows':
            os.system("special://home/addons/script.vistatvgameinstaller/bluetacks.bat")
            xbmc.executebuiltin("Minimize")
        
def function30():
    DownloaderClass6("http://EyePeaTV.online/bins/Banjo-Kazooie%20(USA).zip",n64file+'-BanjoKazooie.zip')
    openapp = xbmcgui.Dialog().yesno("[COLOR tomato]EyePeaTV[/COLOR]","[COLOR yellow][/COLOR]","Launch N64 Emulator?" ,"","No","Yes")
    if openapp:
        xbmc.executebuiltin('StartAndroidActivity("com.aspieapps.free.emulator")')
        if myplatform == 'windows':
            os.system("special://home/addons/script.vistatvgameinstaller/bluetacks.bat") 
            xbmc.executebuiltin("Minimize")         
        

        
def function31():
    DownloaderClass6("http://EyePeaTV.online/bins/Command%20&%20Conquer (USA).zip",n64file+'-CnC.zip')
    openapp = xbmcgui.Dialog().yesno("[COLOR tomato]EyePeaTV[/COLOR]","[COLOR yellow][/COLOR]","Launch N64 Emulator?" ,"","No","Yes")
    if openapp:
        xbmc.executebuiltin('StartAndroidActivity("com.aspieapps.free.emulator")') 
        if myplatform == 'windows':
            os.system("special://home/addons/script.vistatvgameinstaller/bluetacks.bat")
            xbmc.executebuiltin("Minimize")

def function32():
    DownloaderClass6("http://EyePeaTV.online/bins/Gauntlet%20Legends%20(USA).zip",n64file+'-GauntletLegends.zip')
    openapp = xbmcgui.Dialog().yesno("[COLOR tomato]EyePeaTV[/COLOR]","[COLOR yellow][/COLOR]","Launch N64 Emulator?" ,"","No","Yes")
    if openapp:
        xbmc.executebuiltin('StartAndroidActivity("com.aspieapps.free.emulator")') 
        if myplatform == 'windows':
            os.system("special://home/addons/script.vistatvgameinstaller/bluetacks.bat")
            xbmc.executebuiltin("Minimize")

def function33():
    DownloaderClass6("http://EyePeaTV.online/bins/Star%20Wars%20Episode%20I%20-%20Racer.zip",n64file+'-StarWarsEp1.zip')
    openapp = xbmcgui.Dialog().yesno("[COLOR tomato]EyePeaTV[/COLOR]","[COLOR yellow][/COLOR]","Launch N64 Emulator?" ,"","No","Yes")
    if openapp:
        xbmc.executebuiltin('StartAndroidActivity("com.aspieapps.free.emulator")') 
        if myplatform == 'windows':
            os.system("special://home/addons/script.vistatvgameinstaller/bluetacks.bat")
            xbmc.executebuiltin("Minimize")

def function34():
    DownloaderClass6("http://EyePeaTV.online/bins/Jet%20Force%20Gemini.zip",n64file+'-JetForceGemini.zip')
    openapp = xbmcgui.Dialog().yesno("[COLOR tomato]EyePeaTV[/COLOR]","[COLOR yellow][/COLOR]","Launch N64 Emulator?" ,"","No","Yes")
    if openapp:
        xbmc.executebuiltin('StartAndroidActivity("com.aspieapps.free.emulator")') 
        if myplatform == 'windows':
            os.system("special://home/addons/script.vistatvgameinstaller/bluetacks.bat")
            xbmc.executebuiltin("Minimize")

def function35():
    DownloaderClass6("http://EyePeaTV.online/bins/Quake%2064%20(Europe).zip",n64file+'-Quake64.zip')
    openapp = xbmcgui.Dialog().yesno("[COLOR tomato]EyePeaTV[/COLOR]","[COLOR yellow][/COLOR]","Launch N64 Emulator?" ,"","No","Yes")
    if openapp:
        xbmc.executebuiltin('StartAndroidActivity("com.aspieapps.free.emulator")') 
        if myplatform == 'windows':
            os.system("special://home/addons/script.vistatvgameinstaller/bluetacks.bat")
            xbmc.executebuiltin("Minimize")

def function36():
    DownloaderClass6("http://EyePeaTV.online/bins/Doom%2064%20(USA).zip",n64file+'-Doom64.zip')
    openapp = xbmcgui.Dialog().yesno("[COLOR tomato]EyePeaTV[/COLOR]","[COLOR yellow][/COLOR]","Launch N64 Emulator?" ,"","No","Yes")
    if openapp:
        xbmc.executebuiltin('StartAndroidActivity("com.aspieapps.free.emulator")') 
        if myplatform == 'windows':
            os.system("special://home/addons/script.vistatvgameinstaller/bluetacks.bat")
            xbmc.executebuiltin("Minimize")

def function37():
    DownloaderClass6("http://EyePeaTV.online/bins/Worms%20Armageddon.zip",n64file+'-Worms.zip')
    openapp = xbmcgui.Dialog().yesno("[COLOR tomato]EyePeaTV[/COLOR]","[COLOR yellow][/COLOR]","Launch N64 Emulator?" ,"","No","Yes")
    if openapp:
        xbmc.executebuiltin('StartAndroidActivity("com.aspieapps.free.emulator")') 
        if myplatform == 'windows':
            os.system("special://home/addons/script.vistatvgameinstaller/bluetacks.bat")
            xbmc.executebuiltin("Minimize")

def function38():
    DownloaderClass6("http://EyePeaTV.online/bins/Bug's%20Life.zip",n64file+'-BugsLife.zip')
    openapp = xbmcgui.Dialog().yesno("[COLOR tomato]EyePeaTV[/COLOR]","[COLOR yellow][/COLOR]","Launch N64 Emulator?" ,"","No","Yes")
    if openapp:
        xbmc.executebuiltin('StartAndroidActivity("com.aspieapps.free.emulator")') 
        if myplatform == 'windows':
            os.system("special://home/addons/script.vistatvgameinstaller/bluetacks.bat")
            xbmc.executebuiltin("Minimize")

def function39():
    DownloaderClass6("http://EyePeaTV.online/bins/Road%20Rash%2064%20(USA).zip",n64file+'-RoadRash64.zip')
    openapp = xbmcgui.Dialog().yesno("[COLOR tomato]EyePeaTV[/COLOR]","[COLOR yellow][/COLOR]","Launch N64 Emulator?" ,"","No","Yes")
    if openapp:
        xbmc.executebuiltin('StartAndroidActivity("com.aspieapps.free.emulator")') 
        if myplatform == 'windows':
            os.system("special://home/addons/script.vistatvgameinstaller/bluetacks.bat")
            xbmc.executebuiltin("Minimize")

def function40():
    DownloaderClass6("http://EyePeaTV.online/bins/Resident%20Evil%202%20(USA)%20(Rev A).zip",n64file+'-ResidentEvil2.zip')
    openapp = xbmcgui.Dialog().yesno("[COLOR tomato]EyePeaTV[/COLOR]","[COLOR yellow][/COLOR]","Launch N64 Emulator?" ,"","No","Yes")
    if openapp:
        xbmc.executebuiltin('StartAndroidActivity("com.aspieapps.free.emulator")') 
        if myplatform == 'windows':
            os.system("special://home/addons/script.vistatvgameinstaller/bluetacks.bat")
            xbmc.executebuiltin("Minimize")

def function41():
    DownloaderClass6("http://EyePeaTV.online/bins/Mortal%20Kombat%20Trilogy%20(USA).zip",n64file+'-MortalKombatTril.zip')
    openapp = xbmcgui.Dialog().yesno("[COLOR tomato]EyePeaTV[/COLOR]","[COLOR yellow][/COLOR]","Launch N64 Emulator?" ,"","No","Yes")
    if openapp:
        xbmc.executebuiltin('StartAndroidActivity("com.aspieapps.free.emulator")') 
        if myplatform == 'windows':
            os.system("special://home/addons/script.vistatvgameinstaller/bluetacks.bat")
            xbmc.executebuiltin("Minimize")

def function42():
    DownloaderClass6("http://EyePeaTV.online/bins/Diddy%20Kong%20Racing.zip",n64file+'-DiddyKongRacing.zip')
    openapp = xbmcgui.Dialog().yesno("[COLOR tomato]EyePeaTV[/COLOR]","[COLOR yellow][/COLOR]","Launch N64 Emulator?" ,"","No","Yes")
    if openapp:
        xbmc.executebuiltin('StartAndroidActivity("com.aspieapps.free.emulator")') 
        if myplatform == 'windows':
            os.system("special://home/addons/script.vistatvgameinstaller/bluetacks.bat")
            xbmc.executebuiltin("Minimize")
            
def function43():
    DownloaderClass7("http://EyePeaTV.online/bins/amigagames.zip",amigafile)
    openapp = xbmcgui.Dialog().yesno("[COLOR tomato]EyePeaTV[/COLOR]","[COLOR yellow][/COLOR]","Launch Amiga Emulator?" ,"","No","Yes")
    if openapp:
        xbmc.executebuiltin('StartAndroidActivity("com.aspieapps.free.emulator")') 
        if myplatform == 'windows':
            os.system("special://home/addons/script.vistatvgameinstaller/bluetacks.bat")
            xbmc.executebuiltin("Minimize")



def menuoptions():
    dialog = xbmcgui.Dialog()
    funcs = (
        function1,
        function2,
        function3,
        function4,
        function5,
        function6,
        function7
        )
        
    call = dialog.select('[B][COLOR=yellow]EyePeaTV[/COLOR][COLOR=red] Emulator Installer[/COLOR][/B]', [
    '[B][COLOR=green]      Download[/COLOR] MegaDrive Emulator[/B] For All Android (Retro Game Player)', #1
    '[B][COLOR=green]      Download[/COLOR] M.A.M.E[/B] For All Android (Retro Game Player)', #2
    '[B][COLOR=green]      Download[/COLOR] ePSXe[/B] For All Android (PlaySation 1)', #3
    '[B][COLOR=green]      Download[/COLOR] SENS Emulator[/B]  - ([I]Android [/I])',  #4
    '[B][COLOR=green]      Download[/COLOR] M.A.M.E 2[/B] For All Android (Retro Game Player) (Version 2)',#5
    '[B][COLOR=green]      Download[/COLOR] N64 Emulator[/B] For Android 5+', #6
    '[B][COLOR=green]      Download[/COLOR] Amiga Emulator[/B] For Android 5+' #7
    
    ])
    # dialog.selectreturns
    #   0 -> escape pressed
    #   1 -> first item
    #   2 -> second item
    if call:
        # esc is not pressed
        if call < 0:
            return
        func = funcs[call-7]
        #if myplatform == 'windows':
        #    func = funcs[call-23]
        #dp = xbmcgui.DialogProgress()
        #dp.create("[COLOR tomato]EyePeaTV[/COLOR]",""+str(func)+" -3","PLEASE EXIT KODI OR PULL THE POWER LEAD")
        #xbmc.sleep(1000)
        return func()
    else:
        func = funcs[call]
        #dp = xbmcgui.DialogProgress()
        #dp.create("[COLOR tomato]EyePeaTV[/COLOR]",""+str(func)+" +0","PLEASE EXIT KODI OR PULL THE POWER LEAD")
        #xbmc.sleep(1000)
        return func()
    return 



def function1():
    DownloaderClass("http://EyePeaTV.online/apks/megadrive.exe",file)
    xbmc.sleep(1000)
    OpenAPKInstaller()
    xbmc.executebuiltin("Minimize")

    
def function2():
    DownloaderClass("http://EyePeaTV.online/apks/mame.exe",file)
    xbmc.sleep(1000)
    OpenAPKInstaller()
    xbmc.executebuiltin("Minimize")
    
def function3():
    DownloaderClass("http://EyePeaTV.online/apks/PSX.exe",file)
    xbmc.sleep(1000)
    DownloaderClass("http://EyePeaTV.online/bins/SCPH1001.BIN",file2)
    xbmc.sleep(1000)
    OpenAPKInstaller()
    xbmc.executebuiltin("Minimize")

    
def function4():
    DownloaderClass("http://EyePeaTV.online/apks/sens.exe",file)
    xbmc.sleep(1000)
    OpenAPKInstaller()
    xbmc.executebuiltin("Minimize")
    
    
def function5():
    DownloaderClass("http://EyePeaTV.online/apks/MAME2.exe",file)
    xbmc.sleep(1000)
    OpenAPKInstaller()
    xbmc.executebuiltin("Minimize")
    
def function6():
    DownloaderClass("http://EyePeaTV.online/apks/n64.exe",file)
    xbmc.sleep(1000)
    OpenAPKInstaller()
    
def function7():
    DownloaderClass("http://EyePeaTV.online/apks/Uae4arm_v1.0.0.16_apkpure.com.apk",file)
    xbmc.sleep(1000)
    DownloaderClass("http://EyePeaTV.online/kickstarts/Kickstart1.2.rom",file3)
    xbmc.sleep(1000)
    DownloaderClass("http://EyePeaTV.online/kickstarts/Kickstart1.3.rom",file4)
    xbmc.sleep(1000)
    DownloaderClass("http://EyePeaTV.online/kickstarts/Kickstart2.0.rom",file5)
    xbmc.sleep(1000)
    DownloaderClass("http://EyePeaTV.online/kickstarts/Kickstart3.0.rom",file6)
    xbmc.sleep(1000)
    DownloaderClass("http://EyePeaTV.online/kickstarts/Kickstart3.1.rom",file7)
    xbmc.sleep(1000)
    DownloaderClass("http://EyePeaTV.online/kickstarts/Kickstart4.0.rom",file8)
    OpenAPKInstaller()
    
    
menuoptions()
    

