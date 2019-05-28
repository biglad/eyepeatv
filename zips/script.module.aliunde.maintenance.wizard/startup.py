################################################################################
#      Copyright (C) 2015 Surfacingx                                           #
#                                                                              #
#  This Program is free software; you can redistribute it and/or modify        #
#  it under the terms of the GNU General Public License as published by        #
#  the Free Software Foundation; either version 2, or (at your option)         #
#  any later version.                                                          #
#                                                                              #
#  This Program is distributed in the hope that it will be useful,             #
#  but WITHOUT ANY WARRANTY; without even the implied warranty of              #
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the                #
#  GNU General Public License for more details.                                #
#                                                                              #
#  You should have received a copy of the GNU General Public License           #
#  along with XBMC; see the file COPYING.  If not, write to                    #
#  the Free Software Foundation, 675 Mass Ave, Cambridge, MA 02139, USA.       #
#  http://www.gnu.org/copyleft/gpl.html                                        #
################################################################################

import xbmc, xbmcaddon, xbmcgui, xbmcplugin, os, sys, xbmcvfs, glob
import shutil
import urllib2,urllib
import re
import uservar
from datetime import date, datetime, timedelta
from resources.libs import extract, downloader, notify, loginit, debridit, traktit, skinSwitch, uploadLog, wizard as wiz

ADDON_ID       = uservar.ADDON_ID
ADDONTITLE     = uservar.ADDONTITLE
ADDON          = wiz.addonId(ADDON_ID)
VERSION        = wiz.addonInfo(ADDON_ID,'version')
ADDONPATH      = wiz.addonInfo(ADDON_ID,'path')
ADDONID        = wiz.addonInfo(ADDON_ID,'id')
DIALOG         = xbmcgui.Dialog()
DP             = xbmcgui.DialogProgress()
HOME           = xbmc.translatePath('special://home/')
PROFILE        = xbmc.translatePath('special://profile/')
KODIHOME       = xbmc.translatePath('special://xbmc/')
ADDONS         = os.path.join(HOME,     'addons')
KODIADDONS     = os.path.join(KODIHOME, 'addons')
USERDATA       = os.path.join(HOME,     'userdata')
PLUGIN         = os.path.join(ADDONS,   ADDON_ID)
PACKAGES       = os.path.join(ADDONS,   'packages')
ADDONDATA      = os.path.join(USERDATA, 'addon_data', ADDON_ID)
FANART         = os.path.join(ADDONPATH,'fanart.jpg')
ICON           = os.path.join(ADDONPATH,'icon.png')
ART            = os.path.join(ADDONPATH,'resources', 'art')
SKIN           = xbmc.getSkinDir()
BUILDNAME      = wiz.getS('buildname')
DEFAULTSKIN    = wiz.getS('defaultskin')
DEFAULTNAME    = wiz.getS('defaultskinname')
DEFAULTIGNORE  = wiz.getS('defaultskinignore')
BUILDVERSION   = wiz.getS('buildversion')
BUILDLATEST    = wiz.getS('latestversion')
BUILDCHECK     = wiz.getS('lastbuildcheck')
DISABLEUPDATE  = wiz.getS('disableupdate')
AUTOCLEANUP    = wiz.getS('autoclean')
AUTOCACHE      = wiz.getS('clearcache')
AUTOPACKAGES   = wiz.getS('clearpackages')
AUTOTHUMBS     = wiz.getS('clearthumbs')
AUTOFEQ        = wiz.getS('autocleanfeq')
AUTONEXTRUN    = wiz.getS('nextautocleanup')
TRAKTSAVE      = wiz.getS('traktlastsave')
REALSAVE       = wiz.getS('debridlastsave')
LOGINSAVE      = wiz.getS('loginlastsave')
KEEPTRAKT      = wiz.getS('keeptrakt')
KEEPREAL       = wiz.getS('keepdebrid')
KEEPLOGIN      = wiz.getS('keeplogin')
INSTALLED      = wiz.getS('installed')
EXTRACT        = wiz.getS('extract')
EXTERROR       = wiz.getS('errors')
NOTIFY         = wiz.getS('notify')
NOTEDISMISS    = wiz.getS('notedismiss')
NOTEID         = wiz.getS('noteid')
BACKUPLOCATION = ADDON.getSetting('path') if not ADDON.getSetting('path') == '' else HOME
MYBUILDS       = os.path.join(BACKUPLOCATION, 'My_Builds', '')
NOTEID         = 0 if NOTEID == "" else int(NOTEID)
AUTOFEQ        = int(AUTOFEQ) if AUTOFEQ.isdigit() else 0
TODAY          = date.today()
TOMORROW       = TODAY + timedelta(days=1)
TWODAYS        = TODAY + timedelta(days=2)
THREEDAYS      = TODAY + timedelta(days=3)
ONEWEEK        = TODAY + timedelta(days=7)
KODIV          = float(xbmc.getInfoLabel("System.BuildVersion")[:4])
EXCLUDES       = uservar.EXCLUDES
BUILDFILE      = uservar.BUILDFILE
UPDATECHECK    = uservar.UPDATECHECK if str(uservar.UPDATECHECK).isdigit() else 1
NEXTCHECK      = TODAY + timedelta(days=UPDATECHECK)
NOTIFICATION   = uservar.NOTIFICATION
ENABLE         = uservar.ENABLE
HEADERMESSAGE  = uservar.HEADERMESSAGE
AUTOUPDATE     = uservar.AUTOUPDATE
WIZARDFILE     = uservar.WIZARDFILE
AUTOINSTALL    = uservar.AUTOINSTALL
REPOID         = uservar.REPOID
REPOADDONXML   = uservar.REPOADDONXML
REPOZIPURL     = uservar.REPOZIPURL
COLOR1         = uservar.COLOR1
COLOR2         = uservar.COLOR2
WORKING        = True if wiz.workingURL(BUILDFILE) == True else False
FAILED         = False

###########################
#### Check Updates   ######
###########################
def checkUpdate():
	BUILDNAME      = wiz.getS('buildname')
	BUILDVERSION   = wiz.getS('buildversion')
	link           = wiz.openURL(BUILDFILE).replace('\n','').replace('\r','').replace('\t','')
	match          = re.compile('name="%s".+?ersion="(.+?)".+?con="(.+?)".+?anart="(.+?)"' % BUILDNAME).findall(link)
	if len(match) > 0:
		version = match[0][0]
		icon    = match[0][1]
		fanart  = match[0][2]
		wiz.setS('latestversion', version)
		if version > BUILDVERSION:
			if DISABLEUPDATE == 'false':
				wiz.log("[Check Updates] [Installed Version: %s] [Current Version: %s] Opening Update Window" % (BUILDVERSION, version), xbmc.LOGNOTICE)
				notify.updateWindow(BUILDNAME, BUILDVERSION, version, icon, fanart)
			else: wiz.log("[Check Updates] [Installed Version: %s] [Current Version: %s] Update Window Disabled" % (BUILDVERSION, version), xbmc.LOGNOTICE)
		else: wiz.log("[Check Updates] [Installed Version: %s] [Current Version: %s]" % (BUILDVERSION, version), xbmc.LOGNOTICE)
	else: wiz.log("[Check Updates] ERROR: Unable to find build version in build text file", xbmc.LOGERROR)

while xbmc.Player().isPlayingVideo():
	xbmc.sleep(1000)

if KODIV >= 17:
	NOW = datetime.now()
	temp = wiz.getS('kodi17iscrap')
	if not temp == '':
		if temp > str(NOW - timedelta(minutes=2)):
			wiz.log("Killing Start Up Script")
			sys.exit()
	wiz.log("%s" % (NOW))
	wiz.setS('kodi17iscrap', str(NOW))
	xbmc.sleep(1000)
	if not wiz.getS('kodi17iscrap') == str(NOW):
		wiz.log("Killing Start Up Script")
		sys.exit()
	else:
		wiz.log("Continuing Start Up Script")

wiz.log("[Path Check] Started", xbmc.LOGNOTICE)
path = os.path.split(ADDONPATH)
if not ADDONID == path[1]: DIALOG.ok(ADDONTITLE, '[COLOR %s]Please make sure that the plugin folder is the same as the ADDON_ID.[/COLOR]' % COLOR2, '[COLOR %s]Plugin ID:[/COLOR] [COLOR %s]%s[/COLOR]' % (COLOR2, COLOR1, ADDONID), '[COLOR %s]Plugin Folder:[/COLOR] [COLOR %s]%s[/COLOR]' % (COLOR2, COLOR1, path)); wiz.log("[Path Check] ADDON_ID and plugin folder doesnt match. %s / %s " % (ADDONID, path))
else: wiz.log("[Path Check] Good!", xbmc.LOGNOTICE)

if KODIADDONS in ADDONPATH:
	wiz.log("Copying path to addons dir", xbmc.LOGNOTICE)
	if not os.path.exists(ADDONS): os.makedirs(ADDONS)
	newpath = xbmc.translatePath(os.path.join('special://home/addons/', ADDONID))
	if os.path.exists(newpath):
		wiz.log("Folder already exists, cleaning House", xbmc.LOGNOTICE)
		wiz.cleanHouse(newpath)
		wiz.removeFolder(newpath)
	try:
		wiz.copytree(ADDONPATH, newpath)
	except Exception, e:
		pass
	wiz.forceUpdate(True)

try:
	mybuilds = xbmc.translatePath(MYBUILDS)
	if not os.path.exists(mybuilds): xbmcvfs.mkdirs(mybuilds)
except:
	pass

wiz.log("[Auto Install Repo] Started", xbmc.LOGNOTICE)
if AUTOINSTALL == 'Yes' and not os.path.exists(os.path.join(ADDONS, REPOID)):
	workingxml = wiz.workingURL(REPOADDONXML)
	if workingxml == True:
		ver = wiz.parseDOM(wiz.openURL(REPOADDONXML), 'addon', ret='version', attrs = {'id': REPOID})
		if len(ver) > 0:
			installzip = '%s-%s.zip' % (REPOID, ver[0])
			workingrepo = wiz.workingURL(REPOZIPURL+installzip)
			if workingrepo == True:
				DP.create(ADDONTITLE,'Downloading Repo...','', 'Please Wait')
				if not os.path.exists(PACKAGES): os.makedirs(PACKAGES)
				lib=os.path.join(PACKAGES, installzip)
				try: os.remove(lib)
				except: pass
				downloader.download(REPOZIPURL+installzip,lib, DP)
				extract.all(lib, ADDONS, DP)
				try:
					f = open(os.path.join(ADDONS, REPOID, 'addon.xml'), mode='r'); g = f.read(); f.close()
					name = wiz.parseDOM(g, 'addon', ret='name', attrs = {'id': REPOID})
					wiz.LogNotify("[COLOR %s]%s[/COLOR]" % (COLOR1, name[0]), "[COLOR %s]Add-on updated[/COLOR]" % COLOR2, icon=os.path.join(ADDONS, REPOID, 'icon.png'))
				except:
					pass
				if KODIV >= 17: wiz.addonDatabase(REPOID, 1)
				DP.close()
				xbmc.sleep(500)
				wiz.forceUpdate(True)
				wiz.log("[Auto Install Repo] Successfully Installed", xbmc.LOGNOTICE)
			else: 
				wiz.LogNotify("[COLOR %s]Repo Install Error[/COLOR]" % COLOR1, "[COLOR %s]Invalid url for zip![/COLOR]" % COLOR2)
				wiz.log("[Auto Install Repo] Was unable to create a working url for repository. %s" % workingrepo, xbmc.LOGERROR)
		else:
			wiz.log("Invalid URL for Repo Zip", xbmc.LOGERROR)
	else: 
		wiz.LogNotify("[COLOR %s]Repo Install Error[/COLOR]" % COLOR1, "[COLOR %s]Invalid addon.xml file![/COLOR]" % COLOR2)
		wiz.log("[Auto Install Repo] Unable to read the addon.xml file.", xbmc.LOGERROR)
elif not AUTOINSTALL == 'Yes': wiz.log("[Auto Install Repo] Not Enabled", xbmc.LOGNOTICE)
elif os.path.exists(os.path.join(ADDONS, REPOID)): wiz.log("[Auto Install Repo] Repository already installed")

wiz.log("[Auto Update Wizard] Started", xbmc.LOGNOTICE)
if AUTOUPDATE == 'Yes':
	wiz.wizardUpdate('startup')
else: wiz.log("[Auto Update Wizard] Not Enabled", xbmc.LOGNOTICE)

wiz.log("[Notifications] Started", xbmc.LOGNOTICE)
if ENABLE == 'Yes':
	if not NOTIFY == 'true':
		url = wiz.workingURL(NOTIFICATION)
		if url == True:
			id, msg = wiz.splitNotify(NOTIFICATION)
			if not id == False:
				try:
					id = int(id); NOTEID = int(NOTEID)
					if id == NOTEID:
						if NOTEDISMISS == 'false':
							notify.notification(msg)
						else: wiz.log("[Notifications] id[%s] Dismissed" % int(id), xbmc.LOGNOTICE)
					elif id > NOTEID:
						wiz.log("[Notifications] id: %s" % str(id), xbmc.LOGNOTICE)
						wiz.setS('noteid', str(id))
						wiz.setS('notedismiss', 'false')
						notify.notification(msg=msg)
						wiz.log("[Notifications] Complete", xbmc.LOGNOTICE)
				except Exception, e:
					wiz.log("Error on Notifications Window: %s" % str(e), xbmc.LOGERROR)
			else: wiz.log("[Notifications] Text File not formated Correctly")
		else: wiz.log("[Notifications] URL(%s): %s" % (NOTIFICATION, url), xbmc.LOGNOTICE)
	else: wiz.log("[Notifications] Turned Off", xbmc.LOGNOTICE)
else: wiz.log("[Notifications] Not Enabled", xbmc.LOGNOTICE)

wiz.log("[Trakt Data] Started", xbmc.LOGNOTICE)
if KEEPTRAKT == 'true':
	if TRAKTSAVE <= str(TODAY):
		wiz.log("[Trakt Data] Saving all Data", xbmc.LOGNOTICE)
		traktit.autoUpdate('all')
		wiz.setS('traktlastsave', str(THREEDAYS))
	else: 
		wiz.log("[Trakt Data] Next Auto Save isnt until: %s / TODAY is: %s" % (TRAKTSAVE, str(TODAY)), xbmc.LOGNOTICE)
else: wiz.log("[Trakt Data] Not Enabled", xbmc.LOGNOTICE)

wiz.log("[Real Debrid Data] Started", xbmc.LOGNOTICE)
if KEEPREAL == 'true':
	if REALSAVE <= str(TODAY):
		wiz.log("[Real Debrid Data] Saving all Data", xbmc.LOGNOTICE)
		debridit.autoUpdate('all')
		wiz.setS('debridlastsave', str(THREEDAYS))
	else: 
		wiz.log("[Real Debrid Data] Next Auto Save isnt until: %s / TODAY is: %s" % (REALSAVE, str(TODAY)), xbmc.LOGNOTICE)
else: wiz.log("[Real Debrid Data] Not Enabled", xbmc.LOGNOTICE)

wiz.log("[Login Data] Started", xbmc.LOGNOTICE)
if KEEPLOGIN == 'true':
	if LOGINSAVE <= str(TODAY):
		wiz.log("[Login Data] Saving all Data", xbmc.LOGNOTICE)
		loginit.autoUpdate('all')
		wiz.setS('loginlastsave', str(THREEDAYS))
	else: 
		wiz.log("[Login Data] Next Auto Save isnt until: %s / TODAY is: %s" % (LOGINSAVE, str(TODAY)), xbmc.LOGNOTICE)
else: wiz.log("[Login Data] Not Enabled", xbmc.LOGNOTICE)

wiz.log("[Auto Clean Up] Started", xbmc.LOGNOTICE)
if AUTOCLEANUP == 'true':
	service = False
	days = [TODAY, TOMORROW, THREEDAYS, ONEWEEK]
	feq = int(float(AUTOFEQ))
	if AUTONEXTRUN <= str(TODAY) or feq == 0:
		service = True
		next_run = days[feq]
		wiz.setS('nextautocleanup', str(next_run))
	else: wiz.log("[Auto Clean Up] Next Clean Up %s" % AUTONEXTRUN, xbmc.LOGNOTICE)
	if service == True:
		AUTOCACHE      = wiz.getS('clearcache')
		AUTOPACKAGES   = wiz.getS('clearpackages')
		AUTOTHUMBS     = wiz.getS('clearthumbs')
		if AUTOCACHE == 'true': wiz.log('[Auto Clean Up] Cache: On', xbmc.LOGNOTICE); wiz.clearCache(True)
		else: wiz.log('[Auto Clean Up] Cache: Off', xbmc.LOGNOTICE)
		if AUTOTHUMBS == 'true': wiz.log('[Auto Clean Up] Old Thumbs: On', xbmc.LOGNOTICE); wiz.oldThumbs()
		else: wiz.log('[Auto Clean Up] Old Thumbs: Off', xbmc.LOGNOTICE)
		if AUTOPACKAGES == 'true': wiz.log('[Auto Clean Up] Packages: On', xbmc.LOGNOTICE); wiz.clearPackagesStartup()
		else: wiz.log('[Auto Clean Up] Packages: Off', xbmc.LOGNOTICE)
else: wiz.log('[Auto Clean Up] Turned off', xbmc.LOGNOTICE)

wiz.setS('kodi17iscrap', '')