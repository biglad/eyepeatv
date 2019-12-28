import xbmc
import xbmcgui
import os
import urllib2
import xbmcaddon
import json
import datetime
addon_id = "plugin.video.eyepeatv"
__settings__=xbmcaddon.Addon(id=addon_id); __language__=__settings__.getLocalizedString
def get_setting(name): dev=__settings__.getSetting(name); return dev
dialog = xbmcgui.Dialog()

KODIV          = float(xbmc.getInfoLabel("System.BuildVersion")[:4])

kupdatet = ""
if KODIV < 18.5:
    dialog = xbmcgui.Dialog()
    dialog.ok("[COLOR=white][B]EPTV[/COLOR][/B]","Your Kodi is needs updating","Your Version = "+str(KODIV),"Press OK to Continue and udpate ASAP")
    kupdatet = "[COLOR gold]  UPDATE KODI ASAP!!![/COLOR]"

buildfile = "version.txt"
buildv = xbmc.translatePath(os.path.join('special://home/', buildfile))
	
import os.path
if os.path.exists(buildv):
    with open(buildv, 'r') as myfile:
        data = myfile.read()
        buildv = float(data)
else:
    try:
        fo = open("0.0", "w")
        fo.write(buildv);
        fo.close()
        buildv = "0.0"
    except:
        buildv = "0.0"
		
		
url = "http://eptv.co.uk/loaded.php"
data = ""
user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
headers = {'User-Agent': user_agent}
req = urllib2.Request(url, data, headers)
response = urllib2.urlopen(req)
loaded = response.read()
		
url = "http://eptv.co.uk/version.txt"
data = ""
user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
headers = {'User-Agent': user_agent}
req = urllib2.Request(url, data, headers)
response = urllib2.urlopen(req)
webversion = float(response.read())



etext = ""
if buildv < webversion:
    etext = "[COLOR gold]  UPDATE BUILD ASAP!!![/COLOR]"

username=get_setting("Username")
password=get_setting("Password")
if username =="":
    dialog.ok('[COLOR white]Eye Pea TV[/COLOR]','[COLOR white]No Login Info Found[/COLOR]','[COLOR white][/COLOR]','[COLOR white]Please Follow the next steps to login[/COLOR]')
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.eyepeatv",return)')
    exit()
	
	
skinname = xbmc.getSkinDir()
#xbmc.log(skinname,2)

url = "http://eptv.co.uk/buildnews.txt"
data = ""
user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
headers = {'User-Agent': user_agent}
req = urllib2.Request(url, data, headers)
response = urllib2.urlopen(req)
newnews = response.read()

PlayerAPI = "http://gotdark.com/player_api.php?username=%s&password=%s"%(username,password)
url = PlayerAPI
data = ""
user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
headers = {'User-Agent': user_agent}
req = urllib2.Request(url, data, headers)
response = json.load(urllib2.urlopen(req))
data = response
x=data['user_info']
Expiry = x['exp_date']
Expired = datetime.datetime.fromtimestamp(int(Expiry)).strftime('%H:%M %d/%m/%Y')

expires = "Loged in as: "+username+" Expires: "+Expired

window = xbmcgui.Window(10000)
label = xbmcgui.ControlLabel(60, 220, 2000, 50, "[COLOR black]Welcome to Eye Pea TV's Kodi Build[/COLOR]")
window.addControl(label)
window = xbmcgui.Window(10000)
label = xbmcgui.ControlLabel(58, 218, 2000, 50, "[COLOR lightgrey]Welcome to Eye Pea TV's Kodi Build[/COLOR]")
window.addControl(label)


window = xbmcgui.Window(10000)
label = xbmcgui.ControlLabel(60, 255, 2000, 50, "[COLOR black]"+newnews+"[/COLOR]")
window.addControl(label)
window = xbmcgui.Window(10000)
label = xbmcgui.ControlLabel(58, 253, 2000, 50, "[COLOR lightgrey]"+newnews+"[/COLOR]")
window.addControl(label)

if skinname == "skin.aeon.nox.silvo":
    window = xbmcgui.Window(10000)
    label = xbmcgui.ControlLabel(1300, 940, 2000, 50, "[COLOR black]"+expires+"[/COLOR]")
    window.addControl(label)
    window = xbmcgui.Window(10000)
    label = xbmcgui.ControlLabel(1298, 938, 2000, 50, "[COLOR lightgrey]"+expires+"[/COLOR]")
    window.addControl(label)
	
    window = xbmcgui.Window(10000)
    label = xbmcgui.ControlLabel(86, 950, 1000, 50, "[COLOR black]Kodi Version : "+str(KODIV)+"[/COLOR]"+kupdatet)
    window.addControl(label)
    window = xbmcgui.Window(10000)
    label = xbmcgui.ControlLabel(84, 948, 1000, 50, "[COLOR darkgrey]Kodi Version : "+str(KODIV)+"[/COLOR]")
    window.addControl(label)
	
    buildinfo1 = "[COLOR darkgrey]Your Build Version : "+str(buildv)+" - Latest Version : "+str(webversion)+"[/COLOR]"+etext
    buildinfo2 = "[COLOR black]Your Build Version : "+str(buildv)+" - Latest Version : "+str(webversion)+"[/COLOR]"
    buildinfo3 = "[COLOR black]Total Build Loads : "+str(loaded)+"[/COLOR]"
    buildinfo4 = "[COLOR darkgrey]Total Build Loads : "+str(loaded)+"[/COLOR]"

    window = xbmcgui.Window(10000)
    label = xbmcgui.ControlLabel(86, 980, 1000, 50, buildinfo1)
    window.addControl(label)
    window = xbmcgui.Window(10000)
    label = xbmcgui.ControlLabel(84, 978, 1000, 50, buildinfo2)
	
    window = xbmcgui.Window(10000)
    label = xbmcgui.ControlLabel(86, 1010, 1000, 50, buildinfo3)
    window.addControl(label)
    window = xbmcgui.Window(10000)
    label = xbmcgui.ControlLabel(84, 1008, 1000, 50, buildinfo4)
    window.addControl(label)
	
	
    xbmc.executebuiltin('xbmc.UpdateAddonRepos')
    xbmc.executebuiltin('xbmc.UpdateLocalAddons')
	
    xbmc.executebuiltin("XBMC.AlarmClock('MTVBCS',XBMC.RunAddon(script.eptv.core),240,silent)")
	
    exit()

window = xbmcgui.Window(10000)
label = xbmcgui.ControlLabel(60, 460, 500, 50, "[COLOR black]For Latest News & Offers Join[/COLOR]")
window.addControl(label)
window = xbmcgui.Window(10000)
label = xbmcgui.ControlLabel(58, 458, 500, 50, "[COLOR lightgrey]For Latest News & Offers Join[/COLOR]")
window.addControl(label)

window = xbmcgui.Window(10000)
label = xbmcgui.ControlLabel(60, 490, 500, 50, "[COLOR black]t.me/eyepeatv[/COLOR]")
window.addControl(label)
window = xbmcgui.Window(10000)
label = xbmcgui.ControlLabel(58, 488, 500, 50, "[COLOR lightgrey]t.me/eyepeatv[/COLOR]")
window.addControl(label)




import os.path
if os.path.exists(buildv):
    with open(buildv, 'r') as myfile:
        data = myfile.read()
        buildv = float(data)
else:
    try:
        fo = open("0.0", "w")
        fo.write(buildv);
        fo.close()
        buildv = "0.0"
    except:
        buildv = "0.0"
        
        
        





AddonID = 'script.eptv.core'
#xbmc.executebuiltin('Notification(STARTING UP,[COLOR white]Please Wait.....[/COLOR],15000,special://home/addons/'+AddonID+'/icon.png)')
#xbmc.Player().play('special://home/addons/script.eptv.core/load.mp4')



KODIV          = float(xbmc.getInfoLabel("System.BuildVersion")[:4])

kupdatet = ""
if KODIV < 18.5:
    dialog = xbmcgui.Dialog()
    dialog.ok("[COLOR=white][B]EPTV[/COLOR][/B]","Your Kodi is needs updating","Your Version = "+str(KODIV),"Press OK to Continue and udpate ASAP")
    kupdatet = "[COLOR gold]  UPDATE KODI ASAP!!![/COLOR]"

xbmc.executebuiltin('xbmc.UpdateAddonRepos')
xbmc.executebuiltin('xbmc.UpdateLocalAddons')
#xbmc.executebuiltin('ActivateWindow(10001,"plugin://script.module.aliunde.maintenance.wizard/?mode=systeminfo",return)')
xbmc.executebuiltin("XBMC.AlarmClock('MTVBCS',XBMC.RunAddon(script.eptv.core),30,silent)")


#xbmc.executebuiltin("Dialog.Close(busydialog)")
#xbmc.executebuiltin('Notification(STARTING UP,[COLOR white]Please Wait.....[/COLOR],15000,special://home/addons/'+AddonID+'/icon.png)')    
#xbmc.executebuiltin("ActivateWindow(10000)")

#webversion = urllib2.urlopen('http://eptv.co.uk/version.txt').read()
#webversion = float(webversion)
#buildv = float(buildv)
url = "http://eptv.co.uk/version.txt"
data = ""
user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
headers = {'User-Agent': user_agent}
req = urllib2.Request(url, data, headers)
response = urllib2.urlopen(req)
webversion = float(response.read())
#webversion = float(webversion)
#buildv = webversion


etext = ""
if buildv < webversion:
    etext = "[COLOR gold]  UPDATE BUILD ASAP!!![/COLOR]"

#loaded = urllib2.urlopen('http://eptv.co.uk/loaded.php').read()
url = "http://eptv.co.uk/loaded.php"
data = ""
user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
headers = {'User-Agent': user_agent}
req = urllib2.Request(url, data, headers)
response = urllib2.urlopen(req)
loaded = response.read()
#loaded = int(loaded)

buildinfo1 = "[COLOR black]Your Build Version : "+str(buildv)+" - Latest Version : "+str(webversion)+"[/COLOR]"+etext
buildinfo2 = "[COLOR darkgrey]Your Build Version : "+str(buildv)+" - Latest Version : "+str(webversion)+"[/COLOR]"
buildinfo3 = "[COLOR black]Total Build Loads : "+str(loaded)+"[/COLOR]"
buildinfo4 = "[COLOR darkgrey]Total Build Loads : "+str(loaded)+"[/COLOR]"

window = xbmcgui.Window(10000)
label = xbmcgui.ControlLabel(55, 600, 1000, 50, buildinfo1)
window.addControl(label)
window = xbmcgui.Window(10000)
label = xbmcgui.ControlLabel(53, 598, 1000, 50, buildinfo2)
window.addControl(label)


window = xbmcgui.Window(10000)
label = xbmcgui.ControlLabel(86, 630, 1000, 50, "[COLOR black]Kodi Version : "+str(KODIV)+"[/COLOR]"+kupdatet)
window.addControl(label)
window = xbmcgui.Window(10000)
label = xbmcgui.ControlLabel(84, 628, 1000, 50, "[COLOR darkgrey]Kodi Version : "+str(KODIV)+"[/COLOR]")
window.addControl(label)

window = xbmcgui.Window(10000)
label = xbmcgui.ControlLabel(116, 660, 1000, 50, buildinfo3)
window.addControl(label)
window = xbmcgui.Window(10000)
label = xbmcgui.ControlLabel(114, 658, 1000, 50, buildinfo4)
window.addControl(label)


window = xbmcgui.Window(10000)
label = xbmcgui.ControlLabel(60, 720, 1000, 50, "[COLOR black]Eye Pea TV News[/COLOR]")
window.addControl(label)
window = xbmcgui.Window(10000)
label = xbmcgui.ControlLabel(60, 718, 1000, 50, "[COLOR lightgrey]Eye Pea TV News[/COLOR]")
window.addControl(label)

url = "http://eptv.co.uk/buildnews.txt"
data = ""
user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
headers = {'User-Agent': user_agent}
req = urllib2.Request(url, data, headers)
response = urllib2.urlopen(req)
newnews = response.read()

window = xbmcgui.Window(10000)
label = xbmcgui.ControlLabel(70, 755, 2000, 50, "[COLOR black]"+newnews+"[/COLOR]")
window.addControl(label)
window = xbmcgui.Window(10000)
label = xbmcgui.ControlLabel(70, 753, 2000, 50, "[COLOR darkgrey]"+newnews+"[/COLOR]")
window.addControl(label)



    
