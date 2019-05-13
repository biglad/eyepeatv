# -*- coding: utf-8 -*-

# Deleting this file cripples the entire addon

#  This Program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2, or (at your option)
#  any later version.
#
#  This Program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this Program; see the file LICENSE.txt.  If not, write to
#  the Free Software Foundation, 675 Mass Ave, Cambridge, MA 02139, USA.
#  http://www.gnu.org/copyleft/gpl.html
#
# http://kodi.wiki/view/How-to:Write_Python_Scripts
################################################

import sys,os,json,base64
import xbmc, xbmcgui, xbmcaddon, xbmcplugin,re
import shutil
import xbmcvfs
import urllib
import time
import datetime

addon         = 'script.ivueguide'
ADDONID       = addon
addon_name    = addon
addonPath     = xbmc.translatePath(os.path.join('special://home/addons', addon))
basePath      = xbmc.translatePath(os.path.join('special://profile', 'addon_data', addon))
tmp_File      = os.path.join(basePath, 'tmp.ini')
icon          = xbmc.translatePath(os.path.join('special://home/addons', addon, 'icon.png'))
dialog        = xbmcgui.Dialog();dp = xbmcgui.DialogProgress()
Addon         = 'plugin.video.eyepeatv' 
inipath       = xbmc.translatePath(os.path.join(basePath, 'resources', 'ini', Addon))
m3upath       = xbmc.translatePath(os.path.join(basePath, 'resources', 'm3u', Addon))
addre_ss      = base64.b64decode('aHR0cDovL21lb3d5YXBtZW93LmNvbQ==')
po_rt         = base64.b64decode('ODA4MA==')

if not os.path.exists(basePath):
    os.makedirs(basePath)
            
if not os.path.exists(os.path.join(basePath, 'resources')):
    os.makedirs(os.path.join(basePath, 'resources'))
def notify(header,msg,icon_path):
    duration=2000
    xbmcgui.Dialog().notification(header, msg, icon=icon_path, time=duration, sound=False)
def validTime(setting, maxAge):
    previousTime = getPreviousTime(setting)
    now          = datetime.datetime.today()
    delta        = now - previousTime
    nSeconds     = (delta.days * 86400) + delta.seconds
    return nSeconds <= maxAge     
def SetSetting(param, value):
    value = str(value)
    if GetSetting(param) == value:
        return
    xbmcaddon.Addon(addon).setSetting(param, value)
def DialogOK(line1, line2='', line3=''):
    d = xbmcgui.Dialog()
    d.ok('Subscriptions', line1, line2 , line3)     
def log(text):
    try:
        output = '%s V%s : %s' % ("Log", 'Error?', str(text))
        if DEBUG:
            xbmc.log(output)
        else:
            xbmc.log(output, xbmc.LOGDEBUG)
    except: pass

def StartCreate():
  
    if os.path.exists(basePath + '/playlist.m3u'):
        os.remove(basePath + '/playlist.m3u')


    if os.path.exists(inipath):
        shutil.rmtree(inipath) 
    if not os.path.exists(inipath):
        os.makedirs(inipath)
              
    if not os.path.exists(m3upath):
        os.makedirs(m3upath)
        
     

    add_pvr()
    add_Addonini()

    return


def add_Addonini():
    TheseAddons   =  [Addon]
    for FoundAddon in TheseAddons:
        if CheckHasThisAddon(FoundAddon):
            notify('generating channels',FoundAddon,os.path.join('special://home/addons', FoundAddon, 'icon.png'))##NOTIFY##
            ParseAddonData(FoundAddon)
def CheckHasThisAddon(FoundAddon):
    if xbmc.getCondVisibility('System.HasAddon(%s)' % FoundAddon) == 1:
        settingsFileCheck = xbmc.translatePath(os.path.join('special://home/userdata/addon_data',FoundAddon,'settings.xml'))
        if os.path.exists(settingsFileCheck):
            return True
    else:
        return False
#
	
def ParseAddonData(FoundAddon):
    AddonININame = FoundAddon  + '.ini'   
    Addoninipath  = os.path.join(inipath, AddonININame)
    response = GrabSettingsFromAddon(FoundAddon)
    result   = response['result'] 
    ChannelsResult = result['files']    
    ExtrasFileToWrite  = file(Addoninipath, 'w')  
    ExtrasFileToWrite.write('[')
    ExtrasFileToWrite.write(FoundAddon)
    ExtrasFileToWrite.write(']')
    ExtrasFileToWrite.write('\n')   
    TheAddonURL = []   
    for channel in ChannelsResult:
        ParsedChannels = channel['label']
        stream  = channel['file']
        ChannelURL  = GetAddonStuff(FoundAddon, ParsedChannels)
        channel = RemoveAddonChanCrap(FoundAddon, ChannelURL)
        FinalChannelString = channel + '\t\t=' + stream#Jules: make correct formating for channel names
        TheAddonURL.append(FinalChannelString)
        TheAddonURL.sort()
    for item in TheAddonURL:
      ExtrasFileToWrite.write("%s\n" % item)
    ExtrasFileToWrite.close()
    Clean_Names_Addon(Addoninipath,tmp_File)
#
def GrabSettingsFromAddon(FoundAddon):
    Addon    =  xbmcaddon.Addon(FoundAddon)
    username =  Addon.getSetting('Username')
    password =  Addon.getSetting('Password')
    BeginningOfPluginString   = 'plugin://' + FoundAddon    
    urlBody     = '/?action=stream_video&extra&page&plot&thumbnail=&title=All&url='
    endOfString    =  GetAddonVariables(FoundAddon)
    startOfString  =  BeginningOfPluginString + urlBody + endOfString
    GrabThisUrl = 'username=' + username + '&password=' + password + '&type=get_live_streams&cat_id=0'
    queryURL = BeginningOfPluginString  + '/?action=security_check&extra&page&plot&thumbnail&title=Live%20TV&url'
    query = startOfString +  urllib.quote_plus(GrabThisUrl)
    checkthisurl = ('{"jsonrpc":"2.0", "method":"Files.GetDirectory", "params":{"directory":"%s"}, "id": 1}' % queryURL)
    checkthisurltoo = ('{"jsonrpc":"2.0", "method":"Files.GetDirectory", "params":{"directory":"%s"}, "id": 1}' % query)   
    try:
        xbmc.executeJSONRPC(checkthisurl)
        response = xbmc.executeJSONRPC(checkthisurltoo)
        content = json.loads(response.decode('utf-8', 'ignore'))
        return content
    except Exception as e:
        #RunSetSetting(e)
        print e
        return {'Error' : 'Plugin Error'}
#    
def GetAddonStuff(FoundAddon, RemoveURLGarbage):
    RemoveURLGarbage = RemoveURLGarbage.replace('COLOR+', '').replace(' [/B]', '').replace('[COLOR steelblue]', '').replace('[/COLOR]', '').replace('[COLOR firebrick]', '').replace('COLOR+steelblue', '')      
    return RemoveURLGarbage
#    
def RemoveAddonChanCrap(FoundAddon, FoundChannels):
    channel = FoundChannels.rsplit('[/B]', 1)[0].split('[B]', 1)[-1]        
    return channel
#       
def GetAddonVariables(FoundAddon):
    Addon    =  xbmcaddon.Addon(FoundAddon) 
    correct_address = addre_ss + ':' + po_rt + '/enigma2.php?'
    return correct_address
	

def add_pvr():
    iniFle = 'pvr.ini';writestyle = 'w'
    iniPvrAddonName = 'script.ivueguide'
    #iniPvrAddonName = 'pvr.iptvsimple'
    #
    PVRACTIVE   = (xbmc.getCondVisibility('Pvr.HasTVChannels')) or (xbmc.getCondVisibility('Pvr.HasRadioChannels')) == True    
    if not PVRACTIVE:
        return       
    pvrinipath  = os.path.join(inipath, iniFle)
    notify('PVR',iniFle,os.path.join(addonPath, 'resources', 'png', 'pvr.png'))##NOTIFY##
    
    try:
        tryTvChannels  = _getPVRChannels('"tv"')
        tryTvChannelsCommand = tryTvChannels['result']          
    except: pass   
    
    try:
        tryRadio  = _getPVRChannels('"radio"')
        tryRadioCommand = tryRadio['result']
    except: pass
    
    try:
        foundTvChannels  = tryTvChannelsCommand['channels']      
        foundRadioChannels  = tryRadioCommand['channels']
    except: pass    
    ThePVRini  = file(pvrinipath, writestyle)    
    ThePVRini.write('['+iniPvrAddonName+']\n')       
    try:
        for TryToFindStreams in foundTvChannels:
            WhatsTheGroupID  = TryToFindStreams['label']  
            stream = ('%s') % TryToFindStreams['channelid']
            ThePVRini.write('%s' % WhatsTheGroupID)
            ThePVRini.write("=")
            ThePVRini.write(('%s') % stream)            
            ThePVRini.write("\n")
    except: pass    
    try:
        for TryToFindStreams in foundRadioChannels:          
            WhatsTheGroupID  = TryToFindStreams['label']  
            stream = ('%s') % TryToFindStreams['channelid']
            ThePVRini.write('%s' % WhatsTheGroupID)
            ThePVRini.write("=")
            ThePVRini.write('%s' % stream)            
            ThePVRini.write("\n")
    except: pass   
    ThePVRini.write("\n")
    ThePVRini.close()

def _getPVRChannels(group):   
    method   = 'PVR.GetChannels'
    params   = 'channelgroupid'
    WhatAreGroupIDs  =  getGroupID(group)
    checkPVR =  sendJSONpvr(method, params, WhatAreGroupIDs)   
    return checkPVR
#
def getGroupID(group):
    method   = 'PVR.GetChannelGroups'
    params   = 'channeltype'   
    checkPVR = sendJSONpvr(method, params, group)
    result   = checkPVR['result']
    groups   = result['channelgroups']
    #
    for group in groups:
        WhatsTheGroupID = group['label']
        if WhatsTheGroupID == 'All channels':
            return group['channelgroupid']
#
def sendJSONpvr(method, params, value):
    JSONPVR  = ('{"jsonrpc":"2.0","method":"%s","params":{"%s":%s}, "id":"1"}' % (method, params, value))    
    checkPVR = xbmc.executeJSONRPC(JSONPVR)
    return json.loads(checkPVR.decode("utf-8"),"ignore")
# PVR End #
def Clean_Names_Addon(Clean_Name,tmpFile):
    if os.path.exists(tmpFile):
        os.remove(tmpFile)
    os.rename(Clean_Name, tmpFile)
    s=open(tmpFile).read()

    s=s.replace('[COLOR white]','')
    s=s.replace('ITV HD','ITV1 HD')
    s=s.replace('A&E HD','A AND E HD')
    s=s.replace('CBS HD','CBS NEW YORK HD')
    s=s.replace('Universal UK HD','Universal Channel UK HD ')
    s=s.replace('AMC SD','AMC UK SD')
    s=s.replace('Cinemax HD','Cinemax East HD')
    s=s.replace('TV3 SD','TV3 Irish SD')
    s=s.replace('HBO 2 HD','HBO 2 EAST HD')
    s=s.replace('LMN','Lifetime Movie Network')
    s=s.replace('Hallmark HD','Hallmark Channel HD')
    s=s.replace('Nat Geo US HD','National Geographic Channel US HD')
    s=s.replace('Sky Cinema Hits ','Sky Cinema Showcase')
    s=s.replace('Sky Cinema Crime & Thriller','Sky Cinema Thriller')
    s=s.replace('Sky Cinema Sci-Fi/Horror HD','SKY CINEMA SCI-FI AND HORROR')
    s=s.replace('Sky Cinema Drama & Romance','Sky Cinema Drama')
    s=s.replace('Sky Cinema Select HD','Sky Movies Select HD')
    s=s.replace('Hallmark Movies & Mysteries HD','HALLMARK Movie CHANNEL HD')
    s=s.replace('Nat Geo HD','National Geographic Channel HD')
    s=s.replace('Nat Geo US HD','National Geographic Channel US HD')
    s=s.replace('Eurosport 1 HD','BRITISH EUROSPORT HD')
    s=s.replace('NBC EXTRA TIME','NotUsedNBCEXTRATIME')
    s=s.replace('SportsNet ONE HD','Sports Net One HD')
    s=s.replace('SportsNet Ontario HD','Sports Net Ontario HD')
    s=s.replace('NHL LIVE ','NHL Center Ice ')
    s=s.replace('NBA PASS','NBA LEAGUE PASS')
    s=s.replace('LIVE NFL','NFL SUNDAY TICKET')
    s=s.replace('MLB EXTRA','MLB EXTRA INNINGS')
    s=s.replace('PAC12','PAC-12')
    s=s.replace('PAC 12','PAC-12')
    s=s.replace('Sky Sports 1 FHD','Sky Sports 1 HD')
    s=s.replace('Sky Sports 2 FHD','Sky Sports 2 HD')
    s=s.replace('Sky Sports 3 FHD','Sky Sports 3 HD')
    s=s.replace('Sky Sports 4 FHD','Sky Sports 4 HD')
    s=s.replace('Sky Sports 5 FHD','Sky Sports 5 HD')
    s=s.replace('BEIN 1','BEIN-SPORTS-1HD')
    s=s.replace('BEIN 2','BEIN-SPORTS-2HD')
    s=s.replace('BEIN 3','BEIN-SPORTS-3HD')
    s=s.replace('BEIN 4','BEIN-SPORTS-4HD')
    s=s.replace('BEIN 5','BEIN-SPORTS-5HD')
    s=s.replace('BEIN 6','BEIN-SPORTS-6HD')
    s=s.replace('BEIN 7','BEIN-SPORTS-7HD')
    s=s.replace('BEIN 8','BEIN-SPORTS-8HD')
    s=s.replace('BEIN 9','BEIN-SPORTS-9HD')
    s=s.replace('BEIN 10','BEIN-SPORTS-10HD')
    s=s.replace('BEIN 11','BEIN-SPORTS-11HD')
    s=s.replace('BEIN 12','BEIN-SPORTS-12HD')
    s=s.replace('Astro Sports','ASTRO SUPERSPORT')
    s=s.replace('DISCOVERY SCIENCE HD','DISCOVERY SCIENCE US HD')
    s=s.replace('Discovery Crime & Investigation FHD','CI UK FHD')
    s=s.replace('Discovery Home SD','DISCOVERY HOME AND HEALTH SD')
    s=s.replace('Discovery ID HD','ID US HD')
    s=s.replace('Discovery Channel US HD','DISCOVERY US HD')
    s=s.replace('STARZ EDGE HD','STARZ EDGEEAST HD')
    s=s.replace('CINEMAX MOREMAX HD','MOREMAX HD')
    s=s.replace('CINEMAX HD','CINEMAX EAST HD')
    s=s.replace('TENNIS CHANNEL','THE TENNIS CHANNEL HD')
    s=s.replace('Drama SD','Drama UK SD')
    s=s.replace('CTV FHD','CTV Canada FHD')
    s=s.replace('HGTV CA HD','HGTV Canada HD')
    s=s.replace('NBC Sports Network HD','NBCSN HD')
    s=s.replace('GOLF HD','The Golf Channel HD')
    s=s.replace('.m3u8','.ts')

    f=open(Clean_Name,'a')
    f.write(s)
    f.close()
    os.remove(tmpFile)
    return

def Clean_Names(Clean_Name,tmpFile):
    if os.path.exists(tmpFile):
        os.remove(tmpFile)
    os.rename(Clean_Name, tmpFile)
    s=open(tmpFile).read()
    s=s.replace('','') 
    f=open(Clean_Name,'a')
    f.write(s)
    f.close()
    os.remove(tmpFile)
    return

if __name__ == '__main__':
    if StartCreate():
        StartCreate()
        print 'Subscriptions1'
    else:
        print 'Subscriptions2'
xbmc.executebuiltin("Dialog.Close(busydialog)")
choice = xbmcgui.Dialog().yesno('[COLOR white]iVue Integrated[/COLOR]','[COLOR white]iVue is now integrated[/COLOR]', ' ', '[COLOR white]Would you like to launch iVue now?[/COLOR]', nolabel='[COLOR white]No, not right now[/COLOR]',yeslabel='[COLOR white]Yes, open iVue[/COLOR]')
if choice == 0:
    quit
elif choice == 1:
    xbmc.executebuiltin('RunAddon(script.ivueguide)')