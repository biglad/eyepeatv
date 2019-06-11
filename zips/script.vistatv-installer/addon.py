import xbmc
import utils
import os
import platform
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
import base64
import xbmcaddon
import time
from uuid import getnode as get_mac
from resources.lib.kodion.impl import Context
from resources.lib.kodion.constants import setting
import subprocess
import platform
import random
import string
from urllib2 import urlopen
KODIV          = float(xbmc.getInfoLabel("System.BuildVersion")[:4])
if KODIV > 17:
    import zfile as zipfile #FTG mod for Kodi 18
else:
    import zipfile
dialog = xbmcgui.Dialog()  
mac = "00:00:00:00:00:00"
finalmac = "00:00:00:00:00:00"
xbmc.executeJSONRPC('{ "jsonrpc": "2.0", "id": 0, "method":"Settings.setSettingValue", "params": {"setting":"screensaver.mode", "value":""} } ' )
maclist = []

#xbmc.executebuiltin( "XBMC.SetVolume(50)" )
#xbmc.Player().play('http://www.vistatv.online/music.mp3')


def getMacs():  # WINDOWS ONLY????
    macs = []
    file = os.popen("getmac").read()
    file = file.split("\n")

    for line in file:
        found = re.search(r'([0-9A-F]{2}[:-]){5}([0-9A-F]{2})', line, re.I)
        if found:
            mac = found.group().replace('-', ':')
            if mac == "00:00:00:00:00:00":
                continue
            macs.append(mac)
            

    return macs

######## LIST ALL LINUX INTERFACE IDS  NEED SU / ROOT ACCESS SO DONT USE FOR ANDROID!!!

my_ip = urlopen('http://ip.42.pl/raw').read()
#xbmc.executebuiltin("Notification(VistaTV, Got IP,2000,)")

def getAllInterfaces():
    return os.listdir('/sys/class/net/')

def ListLIDs():
    if xbmc.getCondVisibility('system.platform.linux'):
        try:
            for item in os.listdir('/sys/class/net/'):
                
                o = open('/sys/class/net/'+item+'/address', 'r')

                mac_address = o.read().strip() #on "ff:ff:ff:ff:ff:ff" form
                dialog.ok("[COLOR=white][B]VistaTV Info[/COLOR][/B]","IP Address: "+str(my_ip)+" MAC: "+str(testermac)+"","LOAD : "+item,"Press OK to Continue")
        except: pass
#ListLIDs()

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


    



def checkmac(mac):
    if mac == "00:00:00:00:00:00":
        return False
    if re.match("[0-9a-f]{2}([-:]?)[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$", mac.lower()):
        return True
    else:
        return False

def getserial():
    # Extract serial from cpuinfo file
    cpuserial = "0000000000000000"
    try:
        f = open('/proc/cpuinfo','r')
        for line in f:
            if line[0:6]=='Serial': cpuserial = line[10:26]
        f.close()
    except:
        cpuserial = "ERROR000000000"
    return cpuserial

#if xbmc.getCondVisibility('system.platform.windows'):
#    for item in getMacs():
#        maclist.append(item)
 

  


#macstocheck = ''.join(maclist)  # MAKE ARRAY STING TO DUMP!!
#if len(maclist) > 0:
#    for item in maclist:
#        dialog.ok("",str(item),"","",)
        ## DO CHECK FOR EACH ONE!!!

#xbmc.Player().play('special://home/addons/script.vistatv-installer/intro.mp4')
#xbmc.sleep(20000)

context = Context()

version = context.get_system_version().get_version()
application = context.get_system_version().get_app_name()
settings = context.get_settings()

appversion = 0
if version >= (17, 6):
    appversion = "KODI"
elif version >= (17, 9):
    appversion = "KODI18"
else:
    appversion = "KODI-OUTDATED"
    
    
if appversion == "KODI18":
    Install="GO"
elif appversion == "KODI":
    Install="GO"
else:
    dialog = xbmcgui.Dialog()
    dialog.ok("[COLOR=red][B]EyePeaTV[/COLOR][/B]", "Kodi 18.x Supported ONLY", "Press OK to exit",'Please Use Correct Kodi Version..')
    os._exit(1)
    exit()


HASH1 = base64.b64decode("aHR0cDovL3Zpc3RhdHYub25saW5lL25ld2F1dGgvaW5zdGFsbA==")  
HASH2 = base64.b64decode("aHR0cDovL3Zpc3RhdHYub25saW5lL25ld2F1dGg=")
USERINFO = base64.b64decode("c3BlY2lhbDovL3VzZXJkYXRhLw==")
DATAHOME = base64.b64decode("c3BlY2lhbDovL2hvbWUv")
ADDONDATA = base64.b64decode("c3BlY2lhbDovL2hvbWUvYWRkb25z")
MYDATA = base64.b64decode("c3BlY2lhbDovL2hvbWUvYWRkb25zL3NjcmlwdC52aXN0YXR2LWluc3RhbGxlcg==")


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

    
  
IDPATH    = xbmc.translatePath('special://home/')



PART1  = base64.b64decode("aHR0cHM6Ly9naXRodWIuY29tL2JpZ2xhZC9UcmluaXR5Q29yZS9yYXcvMy4zLjUvMTIzLzM0NS82NzgvOTEwL3AxLmJpbg==")
PART2  = base64.b64decode("aHR0cHM6Ly9naXRodWIuY29tL2JpZ2xhZC9UcmluaXR5Q29yZS9yYXcvMy4zLjUvMTIzLzM0NS82NzgvOTEwL3AyLmJpbg==")
PART3  = base64.b64decode("aHR0cHM6Ly9naXRodWIuY29tL2JpZ2xhZC9UcmluaXR5Q29yZS9yYXcvMy4zLjUvMTIzLzM0NS82NzgvOTEwL3AzLmJpbg==")
PART4  = base64.b64decode("aHR0cDovL2Z0cC52aXN0YXR2Lm9ubGluZS9OZXdVcGRhdGUxOC56aXA=")
if version >= (17, 9):
    PART4  = base64.b64decode("aHR0cDovL2Z0cC52aXN0YXR2Lm9ubGluZS9OZXdVcGRhdGUxOC56aXA=")
else:
    PART4  = base64.b64decode("aHR0cDovL2Z0cC52aXN0YXR2Lm9ubGluZS9OZXdVcGRhdGUuemlw")


    

USERDATA    = xbmc.translatePath(USERINFO)
HOME        = xbmc.translatePath(DATAHOME)
ADDONS      = xbmc.translatePath(ADDONDATA)
SELFDIR     = xbmc.translatePath(MYDATA)


file1     =  os.path.join(HOME, 'install.zip')
file2     =  os.path.join(HOME, 'install2.zip')
file3     =  os.path.join(HOME, 'install3.zip')
file4     =  os.path.join(HOME, 'install4.zip')
iddata    =  os.path.join(HOME, 'userdata/networksettings.xml')
done      =  os.path.join(HOME, 'done.xml')
idbackup = os.path.join(IDPATH, 'datafile.bin')
macdata = os.path.join(IDPATH, 'mac.bin')

try:
    with open(iddata, 'r') as myfile:
        data300=str(myfile.read())
        maclist.append(str(data300))
except: pass
    

if not os.path.exists(iddata):
    fo = open(iddata, "w")
    fo.write('0');
    fo.close()
  
if not os.path.exists(idbackup):
    fo = open(idbackup, "w")
    fo.write('0');
    fo.close()
 
if not os.path.exists(macdata):
    fo = open(macdata, "w")
    fo.write('0');
    fo.close()

DoStart = 0
userid = 0
ipaddy = "0.0.0.0"
dialog = xbmcgui.Dialog()
dp = xbmcgui.DialogProgress()
data300 = ""


def ping(host):
    """
    Returns True if host responds to a ping request
    """
    import os, platform

    # Ping parameters as function of OS
    ping_str = "-n 1" if  platform.system().lower()=="windows" else "-c 1"

    # Ping
    return os.system("ping " + ping_str + " " + host) == 0
    
PART1 = "http://ftp.mgawow.co.uk/www/201902121704.zip"
PART4  = "http://ftp.mgawow.co.uk/www/kodi18.zip"  
UPDATE = PART4
    
if not ping("google.com"):
    dialog = xbmcgui.Dialog()
    dialog.ok("[COLOR=red][B]EyePeaTV[/COLOR][/B]", "No Internet Connection Found!", "Press OK to exit",'Please Check Your Connection.')
    os._exit(1)
    exit()

   
logdata2 = xbmc.getInfoLabel("network.macaddress")

networkcounter=0
while logdata2 == "Busy" or logdata2 == "None" or logdata2 == "00:00:00:00:00:00":
    
    dp = xbmcgui.DialogProgress()
    dp.create("[COLOR=white][B]EyePeaTV[/COLOR][/B]","[B][COLOR=red]Waiting for Network Info[/COLOR][/B]","Please Wait.")
    xbmc.sleep(1000)
    logdata2 = xbmc.getInfoLabel("network.macaddress")
    if networkcounter > 99:
        networkcounter = 0
    networkcounter = networkcounter+1
    dp.update(networkcounter)
    #dp.close()
maclist.append(logdata2) 
xbmc.log(logdata2,2)   
dp.close()
dp.create("[COLOR=white][B]EyePeaTV[/COLOR][/B]","[B][COLOR=red]Getting Auth Data.....[/COLOR][/B]","Please Wait.")  
    
    
macid = logdata2
maclist.append(str(macid))
#dp.close() 

def SetCode2(mac,code):
    try:
        fo = open(iddata, "w")
        fo.write(code);
        fo.close();
        fo = open(idbackup, "w")
        fo.write(code);
        fo = open(macdata, "w")
        fo.write(mac);
        fo.close();
    except: pass 

def stupiddevice():
    ## UNABLE TO GET MAC ID OR CPU ID!!!!
    ## MAKE RANDOM ID AND WARN USER THEY CANT RE-INSTALL WITHOUT SPEAKING TO ADMIN
    #dialog.ok("[COLOR=white][B]VistaTV Info[/COLOR][/B]","UNABLE TO GET A STATIC DEVICE ID","Press OK to Continue")
    #dialog.ok("[COLOR=white][B]VistaTV Info[/COLOR][/B]","PLEASE MATE A NOTE OF THE FOLLOW ID","Press OK to Continue")
    #dialog.ok("[COLOR=white][B]VistaTV Info[/COLOR][/B]","YOU MUST MAKE A NOTE OF THE FOLLOWING ID","Press OK to Continue")
    ranid = id_generator(24)
    #dialog.ok("[COLOR=white][B]MAKE A NOTE OF THIS ID[/COLOR][/B][COLOR=gold]",str(ranid),"[/COLOR]Press OK to Continue")
    dialog.ok("[COLOR=white][B]MAKE A NOTE OF THIS ID[/COLOR][/B][COLOR=gold]",str(ranid),"[/COLOR]Press OK to Continue")
    SetCode2(str(ranid),str(ranid))
    maclist.append(str(ranid)) 
    
#if "0000000000000000" in maclist:     
#    stupiddevice()
#if "ERROR000000000" in maclist:     
#    stupiddevice()
try: maclist.remove('0000000000000000')
except: pass
try: maclist.remove('ERROR000000000')
except: pass
    
if len(maclist) < 1:
    stupiddevice()
    
#######################################################TEST
#######################################################TEST
#######################################################TEST
#######################################################TEST
#stupiddevice()
#######################################################TEST
#######################################################TEST
#######################################################TEST
#######################################################TEST

def GetUserCode(mac):
    code2 = urllib2.urlopen(HASH1+'mac.php?getidfromac=1&mac='+mac).read()

    if code2 == "":
        code2 = "BAD"
    if code2 == "0":
        code2 = "BAD"

        
    if code2 == "BAD":
        dummyval = 1
    else:
        if not code2 == "":
            return code2
    
    return False
    

def SetCode(mac,code):
    if code !="" or MAC != "": 
    #if code == None:
    #    return False
        try:
            fo = open(iddata, "w")
            fo.write(code);
            fo.close();
            fo = open(idbackup, "w")
            fo.write(code);
            fo = open(macdata, "w")
            fo.write(mac);
            fo.close();
        except: pass
        #xbmc.log(HASH2+'/done.php?mac='+mac+'&id='+code,2)
        try: urllib2.urlopen(HASH2+'/done.php?mac='+mac+'&id='+code)
        except: pass


   

def killxbmc():
    xbmc.executebuiltin("Notification(PLEASE WAIT, [B][COLOR=gold]KODI WILL NOW CLOSE[/COLOR] -- [COLOR=green]PLEASE WAIT[/COLOR][/B],,7000)")
    dp = xbmcgui.DialogProgress()
    dp.create("[COLOR tomato]EyePeaTV[/COLOR]","CLOSING","PLEASE WAIT")
    xbmc.sleep(3000)
    os._exit(1)

def killxbmc2():
    xbmc.executebuiltin("Notification(OH DEAR CODE/MAC NOT VALID[/COLOR] -- [COLOR=green]PLEASE PAY[/COLOR][/B],,15000)")
    dp = xbmcgui.DialogProgress()
    dp.create("[COLOR tomato]EyePeaTV[/COLOR]","FAKE/BLOCKED CODE","Please Contant Us")
    xbmc.sleep(18000)
    os._exit(1)
    
def killxbmc3():
    xbmc.executebuiltin("Notification(OH DEAR CODE NOT VALID[/COLOR] -- [COLOR=green]PLEASE PAY[/COLOR][/B],,15000)")
    dp = xbmcgui.DialogProgress()
    dp.create("[COLOR tomato]EyePeaTV[/COLOR]","CODE NOT VALID","WILL TRY AGAIN")
    xbmc.sleep(18000)
    xbmc.executebuiltin('RunAddon(script.vistatv-installer)')
    exit()
    
    
def CleanKodi():
    addondir = ADDONS
    datadir = USERDATA
    dp = xbmcgui.DialogProgress()
    dp.create("Staring EyePeaTV's Wizard","Removing",'Add-ons', 'Please Wait')
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
    dp.create("Staring EyePeaTV's Wizard","Removing",'Userdata', 'Please Wait')
    try: shutil.rmtree(datadir)
    except: pass
    xbmc.sleep(9000)
    percent = 68
    try: xbmcvfs.rmdir(datadir)
    except: pass
    xbmc.sleep(1000)
    percent = 83 
    dp.update(percent)
    dp.create("Staring EyePeaTV's Wizard","Getting Ready",'To Install', 'Please Wait')
    try: xbmcvfs.mkdir(datadir)
    except: pass
    xbmc.sleep(1000)
    try: xbmcvfs.mkdir(datadir)
    except: pass
    xbmc.sleep(1000)
  

def Search(name):
        search_entered = ''
        keyboard = xbmc.Keyboard(search_entered, 'Please Enter '+str(name))
        keyboard.doModal()
        if keyboard.isConfirmed():
            search_entered = keyboard.getText().replace(' ','%20')
            if search_entered == 0:
                return False          
        return search_entered
        if search_entered == None:
            return False 
            

def ServerError():
    dp = xbmcgui.DialogProgress()
    dp.create("[COLOR tomato]EyePeaTV[/COLOR]","[COLOR red][B]ERROR[/B][/COLOR]","EyePeaTV Servers Offline")
    xbmc.sleep(1500)
    dp.close()
    update = xbmcgui.Dialog().yesno("[COLOR gold]EyePeaTV Build Installer[/COLOR]","[COLOR yellow]Sorry Our Server Seems to be[/COLOR] [COLOR red][B]OFFLINE[/B][/COLOR]","Sorry For This Will Will Have It Fixed Soon!!","[COLOR tomato]Try Again NOW??[/COLOR]")
    if update:
        xbmc.executebuiltin('RunAddon(script.vistatv-installer)')
        exit()
    else:
        exit()  
		
def setplayermodes():
    dp.close()
    xbmc.executebuiltin('ActivateWindow(10040,"addons://repository.xbmc.org/kodi.inputstream",return)')
    dialog = xbmcgui.Dialog()
    dialog.ok("[COLOR=red][B]INFORMATION[/COLOR][/B]", "ENABLE!!!", "[COLOR=yellow]ALL OPTIONS","These need to be on for best playback[/COLOR]")
    
    while xbmc.getCondVisibility("Window.IsActive(10040)"):
        xbmc.sleep(1000)  		
    install()
def install():

    
    ###downloader . download(PART1,file1,"Downloading Build Data")
    ###extractor . extract(file1,HOME,"Installing Build Data")
    #downloader . download(PART2,file2,"Downloading Build Data Part 2")
    #extractor . extract(file2,HOME,"Unpacking Part 2")
    #downloader . download(PART3,file3,"Downloading Build Data Part 3")
    #extractor . extract(file3,HOME,"Unpacking Part 3")
    downloader . download(UPDATE,file4,"Downloading Latest Build Info")
    extractor . extract(file4,HOME,"Installing EyePeaTV Data")
    #xbmc.Player().stop()
    #xbmc.executebuiltin( "XBMC.SetVolume(100)" )
    dialog = xbmcgui.Dialog()
    dialog.ok("[COLOR=red][B]EyePeaTV[/COLOR][/B]", "Installer Now Configured", "Kodi will now Exit","Open kodi agin to continue install")
    killxbmc()
    exit()
 
setplayermodes()
 
def KillMe():
    try: shutil.rmtree(SELFDIR)
    except: pass
    xbmc.executebuiltin('Quit')
    os.system("su -c 'reboot'")
    try:
        os.system('@ECHO off')
        os.system('tskill XBMC.exe')
    except: pass
    try:
        os.system('@ECHO off')
        os.system('tskill Kodi.exe')
    except: pass
    try:
        os.system('@ECHO off')
        os.system('TASKKILL /im Kodi.exe /f')
    except: pass
    try:
        os.system('@ECHO off')
        os.system('TASKKILL /im XBMC.exe /f')
    except: pass
    os._exit(1)
    exit()
      
def checkmac():
    counter = 0
    try:
        dp = xbmcgui.DialogProgress()
        dp.create("[COLOR tomato]EyePeaTV[/COLOR]","Connecting To VistaTV Servers","Searching For Your Device......")
        if len(maclist) > 0:
            for item in maclist:
                counter = counter+1
                dp.update(counter+10)
                if item == '0': continue
                if item == '': continue
                item2 = item
                response = urllib2.urlopen(HASH1+'mac.php?mac='+macid).read()
                xbmc.log(HASH1+'mac.php?mac='+macid,2)
                xbmc.log(macid,2)
                dp.update(len(maclist))
                if response == "OKMAC":
                    #maclist = []
                    #maclist.append(item2)
                    dp.close()
                    break
                    return True
    except: 
        ServerError()
        exit()
    dp.close()
    if response == "OKMAC":
        return True
    else:
        return False
        
def checkmac2():
    try: 
        dp = xbmcgui.DialogProgress()
        dp.create("[COLOR tomato]EyePeaTV[/COLOR]","Connecting To VistaTV Servers","Talkng to Auth Server.......")
        for item in maclist:
            response = urllib2.urlopen(HASH1+'mac.php?mac='+macid).read()
    except: 
        ServerError()
        exit()
        dp.close()
    if response == "BLOCKED":
        return True
    else:
        return False
    
def BadCode():
    update = xbmcgui.Dialog().yesno("[COLOR gold]VistaTV Build Installer[/COLOR]","[COLOR yellow]The Code You Have Entered Was Not Valid!![/COLOR]","[COLOR tomato]Try Again??[/COLOR]","VistaTV Security System!!")
    if update:
        xbmc.executebuiltin('RunAddon(script.vistatv-installer)')
    else:
        exit()  
        
def getcode(id):
    try:
        dp = xbmcgui.DialogProgress()
        dp.create("[COLOR tomato]EyePeaTV[/COLOR]","Connecting To VistaTV Servers","Talkng to Auth Server.......")
        response = urllib2.urlopen(HASH1+'id.php?id='+str(id)).read()
    except: 
        ServerError()
        exit()
    dp.close()
    if response == "OKID":
        return True
    else:
        return False
        
if checkmac():
    dpcounter = 0
    update = xbmcgui.Dialog().yesno("[COLOR gold]VistaTV Build Installer[/COLOR]","[COLOR yellow]We Have Detected Your Device[/COLOR]: [COLOR red]" + str(macid),"[COLOR tomato]This Will NOT Wipe Your Data[/COLOR]","Continue?")
    if update: 
        try:
            dp = xbmcgui.DialogProgress()
            dp.create("[COLOR tomato]EyePeaTV[/COLOR]","Connecting To VistaTV Servers","Talkng to Auth Server....... This May Take Some Time.....")
            if len(maclist) > 0:
                for item in maclist:
                    if item == "": continue
                    dpcounter = dpcounter+1
                    code = urllib2.urlopen(HASH1+'mac.php?getidfromac=1&mac='+macid).read()
                    dp.update(dpcounter*len(maclist))
                    xbmc.log(HASH1+'mac.php?getidfromac=1&mac='+macid,2)
                    if not code == "0":
                        code2 = code
                    
        except: 
            ServerError()
            exit()
        #xbmc.log(str(macid),2)
        #xbmc.log(str(code2),2)
        dp.create("[COLOR tomato]EyePeaTV[/COLOR]","Connecting To VistaTV Servers","Updating Auth Server........")
        if len(maclist) > 0:
            dpcounter = 0
            for item in maclist:
                dpcounter = dpcounter+1
                dp.update(dpcounter*len(maclist))
                xbmc.log(str(macid)+'|'+str(code),2)
                try: SetCode(str(macid),str(code))
                except: pass
            setplayermodes()
            exit()
    else:
        exit()
        
#if checkmac2():
#    dialog = xbmcgui.Dialog()
#    dialog.ok("[COLOR=red][B]VistaTV[/COLOR][/B]", "YOUR DEVICE IS BANNED FROM OUR SYSTEM", "Press OK to exit",macid)
#    #CleanKodi()
#    KillMe()
#    exit()
 

code = Search('[B][COLOR=white]Please enter your Authentication code[/COLOR][/B]')
if code == "":
    BadCode()
    exit()
if getcode(code):
    update = xbmcgui.Dialog().yesno("[COLOR gold]VistaTV Build Installer[/COLOR]","[COLOR yellow]We Have Detected A Fresh Install[/COLOR]: [COLOR red]" + str(code),"[COLOR tomato]This will NOT Wipe Your Data!!!!!![/COLOR]","Continue?")
    if update: 
        for item in maclist:
            try: SetCode(str(macid),str(code))
            except: pass
        #xbmc.log(str(macid),2)
        #xbmc.log(str(code),2)
        #CleanKodi()
        setplayermodes()
        exit()   
    else: 
        exit()

else:
    BadCode()
    exit()
killxbmc2()
exit()  


