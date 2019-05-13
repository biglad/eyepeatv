import threading,xbmc,xbmcplugin,xbmcgui,re,os,xbmcaddon,sys
import shutil,plugintools,installer
import zipfile
import urlparse
import urllib,urllib2,json
import common,xbmcvfs,downloader,extract
import datetime
import base64, time
import unicodedata
from datetime import datetime
from datetime import timedelta
import maintenance
AddonID = 'plugin.video.eyepeatv'
AddonTitle = 'EyePeaTV'
Images=xbmc.translatePath(os.path.join('special://home','addons',AddonID,'resources/art/'));
fanart = Images+'fanart.jpg'
icon = Images+'icon.png'
VAddon = xbmcaddon.Addon('plugin.video.eyepeatv')
ADDON=xbmcaddon.Addon(id='plugin.video.eyepeatv')
dialog       =  xbmcgui.Dialog()
dialogprocess =  xbmcgui.DialogProgress()
USERDATA     =  xbmc.translatePath(os.path.join('special://home/userdata',''))
HOME         =  xbmc.translatePath('special://home/')
Username=plugintools.get_setting("Username")
Password=plugintools.get_setting("Password")
PVRon = plugintools.get_setting("PVRUpdater")
lehekylg= base64.b64decode("aHR0cDovL3dhdGNoLmdvdGRhcmsuY29t")
# pordinumber=base64.b64decode("Njk2OQ==")
BASEURL = base64.b64decode("bmFkYQ==")
AddonRes = xbmc.translatePath(os.path.join('special://home','addons',AddonID,'resources'))
loginurl   = base64.b64decode("JXMvZ2V0LnBocD91c2VybmFtZT0lcyZwYXNzd29yZD0lcyZ0eXBlPW0zdV9wbHVzJm91dHB1dD10cw==")%(lehekylg,Username,Password)

try:
    from sqlite3 import dbapi2 as database
except:
    from pysqlite2 import dbapi2 as database
def Add_Directory_Item(handle, url, listitem, isFolder):
    xbmcplugin.addDirectoryItem(handle, url, listitem, isFolder)

##################################################################################


def SportChoice(params):
	choice = dialog.select("[COLOR white]Sport Schedules[/COLOR]", ['[COLOR white]F1[/COLOR]','[COLOR white]Darts[/COLOR]','[COLOR white]NBA[/COLOR]','[COLOR white]NHL[/COLOR]','[COLOR white]MLB[/COLOR]','[COLOR white]UFC[/COLOR]','[COLOR white]Rugby Union[/COLOR]','[COLOR white]Rugby League[/COLOR]','[COLOR white]Tennis[/COLOR]','[COLOR white]Wrestling[/COLOR]','[COLOR white]Horse Racing[/COLOR]','[COLOR white]Boxing[/COLOR]','[COLOR white]Motorsport[/COLOR]','[COLOR white]Golf[/COLOR]','[COLOR white]AFL[/COLOR]','[COLOR white]Moto GP[/COLOR]','[COLOR white]Cycling[/COLOR]','[COLOR white]Hockey[/COLOR]'])
	if choice == 0:
		F1_LISTINGS()
	if choice == 1:
		DARTS_LISTINGS()
	if choice == 2:
		NBA_LISTINGS()
	if choice == 3:
		NHL_LISTINGS()
	if choice == 4:
		MLB_LISTINGS()
	if choice == 5:
		UFC_LISTINGS()
	if choice == 6:
		RugbyUnion_LISTINGS()
	if choice == 7:
		RugbyLeague_LISTINGS()
	if choice == 8:
		Tennis_LISTINGS()
	if choice == 9:
		Wrestling_LISTINGS()
	if choice == 10:
		HorseRacing_LISTINGS()
	if choice == 11:
		Boxing_LISTINGS()
	if choice == 12:
		Motorsport_LISTINGS()
	if choice == 13:
		Golf_LISTINGS()
	if choice == 14:
		AFL_LISTINGS()
	if choice == 15:
		MotoGP_LISTINGS()
	if choice == 16:
		Cycling_LISTINGS()
	if choice == 17:
		Hockey_LISTINGS()

def RugbyUnion_LISTINGS():

	THE_DATE = time.strftime("%Y%m%d") # todays date

	now = datetime.now()
	diff = timedelta(days=7)
	future = now + diff
	Oneweek = future.strftime("%Y%m%d") # date in a week

	url = base64.b64decode(b'aHR0cDovL3d3dy53aGVyZXN0aGVtYXRjaC5jb20vdHYvaG9tZS5hc3A/c2hvd2RhdGVzdGFydD0lcyZzaG93ZGF0ZWVuZD0lcyZzcG9ydGlkPTM=')%(THE_DATE,Oneweek)
	r = common.OPEN_URL_NORMAL(url).replace('\r','').replace('\n','').replace('\t','')
	match = re.compile('<span class="fixture">                        <a class="" href=".+?">                            <em class="">(.+?)</em> <em class="">v</em> <em class="">(.+?)</em> <em class="livestream">Live Stream</em></a></span>                    <span class="ground "><span                         class="time-channel ">(.+?)</span></span>.+?<span class="">(.+?)</span> .+?<span class="stage ').findall(r)
	for team1,team2,when,type in match:
		if 'Live Stream' in when:
			a,b = when.split("on")
			common.addItem('[COLOR white]'+team1+' vs '+team2+'[/COLOR] [COLOR skyblue]in the '+type+'[/COLOR]','','',icon,fanart,'')
			common.addItem('[COLOR yellow]'+a+'[/COLOR][COLOR white] - Not televised in the UK[/COLOR]','','',icon,fanart,'')
			common.addItem('------------------------------------------','','',icon,fanart,'')
		else:
			common.addItem('[COLOR white]'+team1+' vs '+team2+'[/COLOR] [COLOR skyblue]in the '+type+'[/COLOR]','','',icon,fanart,'')
			common.addItem('[COLOR yellow]'+when+'[/COLOR]','','',icon,fanart,'')
			common.addItem('------------------------------------------','','',icon,fanart,'')

def Tennis_LISTINGS():

	THE_DATE = time.strftime("%Y%m%d") # todays date

	now = datetime.now()
	diff = timedelta(days=7)
	future = now + diff
	Oneweek = future.strftime("%Y%m%d") # date in a week

	url = base64.b64decode(b'aHR0cDovL3d3dy53aGVyZXN0aGVtYXRjaC5jb20vdHYvaG9tZS5hc3A/c2hvd2RhdGVzdGFydD0lcyZzaG93ZGF0ZWVuZD0lcyZzcG9ydGlkPTE3')%(THE_DATE,Oneweek)
	r = common.OPEN_URL_NORMAL(url).replace('\r','').replace('\n','').replace('\t','')
	match = re.compile('<span class="fixture"><a class=" eventlink" href=".+?"><strong class="">(.+?)</strong></a></span>                    <em class="">(.+?)</em>                    <span class="ground "><span                         class="time-channel ">(.+?)</span></span>.+?</td>                <td class="away-team"></td>                                    <td class="start-details">                                                    <span>.+?</span><span class="time "><em class="">.+?</em></span>.+?<td class="competition-name">                    <img title=".+?" src=".+?" alt=".+?" />                                        <a class="" href=".+?"><span class="">.+?</span> </a><span class="stage "><em class=""></em></span>                                    </td>').findall(r)
	for competition,event,channel in match:
		common.addItem('[COLOR white]'+event+'[/COLOR]','','',icon,fanart,'')
		common.addItem('[COLOR yellow]'+channel+'[/COLOR]','','',icon,fanart,'')
		common.addItem('[COLOR skyblue]'+competition+'[/COLOR]','','',icon,fanart,'')
		common.addItem('------------------------------------------','','',icon,fanart,'')

def RugbyLeague_LISTINGS():

	THE_DATE = time.strftime("%Y%m%d") # todays date

	now = datetime.now()
	diff = timedelta(days=7)
	future = now + diff
	Oneweek = future.strftime("%Y%m%d") # date in a week
	
	url = base64.b64decode(b'aHR0cDovL3d3dy53aGVyZXN0aGVtYXRjaC5jb20vdHYvaG9tZS5hc3A/c2hvd2RhdGVzdGFydD0lcyZzaG93ZGF0ZWVuZD0lcyZzcG9ydGlkPTI=')%(THE_DATE,Oneweek)
	r = common.OPEN_URL_NORMAL(url).replace('\r','').replace('\n','').replace('\t','')
	match = re.compile('<span class="fixture">                        <a class="" href=".+?">                            <em class="">(.+?)</em> <em class="">v</em> <em class="">(.+?)</em> <em class="livestream">Live Stream</em></a></span>                    <span class="ground "><span                         class="time-channel ">(.+?)</span></span>.+?<span class="">(.+?)</span> .+?<span class="stage ">').findall(r)
	for team1,team2,when,type in match:
		if 'Live Stream' in when:
			a,b = when.split("on")
			common.addItem('[COLOR white]'+team1+' vs '+team2+'[/COLOR]','','',icon,fanart,'')
			common.addItem('[COLOR skyblue]'+type+'[/COLOR]','','',icon,fanart,'')
			common.addItem('[COLOR yellow]'+a+'[/COLOR][COLOR white] - Not televised in the UK[/COLOR]','','',icon,fanart,'')
			common.addItem('------------------------------------------','','',icon,fanart,'')
		else:
			common.addItem('[COLOR white]'+team1+' vs '+team2+'[/COLOR]','','',icon,fanart,'')
			common.addItem('[COLOR skyblue]'+type+'[/COLOR]','','',icon,fanart,'')
			common.addItem('[COLOR yellow]'+when+'[/COLOR]','','',icon,fanart,'')
			common.addItem('------------------------------------------','','',icon,fanart,'')

def F1_LISTINGS():

	url = base64.b64decode(b'aHR0cDovL2ZhYmlwdHYuY29tL3Nwb3J0cy9mMS50eHQ=')
	r = common.OPEN_URL_NORMAL(url).replace('\r','').replace('\n','').replace('\t','')
	match = re.compile('<h2 class="f1-races__race-name">(.+?)</h2>.+?<p class="f1-races__race-date">(.+?)</p>.+?<td class="standing-table__cell">(.+?)</td>.+?<td class="standing-table__cell standing-table__cell--name">              (.+?)            </td>.+?<td class="standing-table__cell">(.+?)</td>.+?<td class="standing-table__cell">(.+?)</td>.+?<td class="standing-table__cell is-invisible">(.+?)</td>.+?<td class="standing-table__cell standing-table__cell--name">              (.+?)            </td>.+?<td class="standing-table__cell">(.+?)</td>.+?<td class="standing-table__cell">(.+?)</td>.+?<td class="standing-table__cell">(.+?)</td>.+?<td class="standing-table__cell standing-table__cell--name">              (.+?)            </td>.+?<td class="standing-table__cell">(.+?)</td>.+?<td class="standing-table__cell">(.+?)</td>.+?<td class="standing-table__cell is-invisible">(.+?)</td>.+?<td class="standing-table__cell standing-table__cell--name">              (.+?)            </td>.+?<td class="standing-table__cell">(.+?)</td>.+?<td class="standing-table__cell">(.+?)</td>.+?<td class="standing-table__cell">(.+?)</td>.+?<td class="standing-table__cell standing-table__cell--name">              (.+?)            </td>.+?<td class="standing-table__cell">(.+?)</td>.+?<td class="standing-table__cell">(.+?)</td>').findall(r)
	for location,daterange,date,eventtype,start,finish,date2,eventtype2,start2,finish2,date3,eventtype3,start3,finish3,date4,eventtype4,start4,finish4,date5,eventtype5,start5,finish5 in match:
		common.addItem('[COLOR white]'+location+' taking place '+daterange+'[/COLOR]','','',icon,fanart,'')
		common.addItem('[COLOR skyblue]'+date+'[/COLOR] - [COLOR white]'+eventtype+' - On Air: [COLOR skyblue]'+start+'[/COLOR] and Starts: [COLOR skyblue]'+finish+'[/COLOR][/COLOR]','','',icon,fanart,'')
		common.addItem('[COLOR skyblue]'+date2+'[/COLOR] - [COLOR white]'+eventtype2+' - On Air: [COLOR skyblue]'+start2+'[/COLOR] and Starts: [COLOR skyblue]'+finish2+'[/COLOR][/COLOR]','','',icon,fanart,'')
		common.addItem('[COLOR skyblue]'+date3+'[/COLOR] - [COLOR white]'+eventtype3+' - On Air: [COLOR skyblue]'+start3+'[/COLOR] and Starts: [COLOR skyblue]'+finish3+'[/COLOR][/COLOR]','','',icon,fanart,'')
		common.addItem('[COLOR skyblue]'+date4+'[/COLOR] - [COLOR white]'+eventtype4+' - On Air: [COLOR skyblue]'+start4+'[/COLOR] and Starts: [COLOR skyblue]'+finish4+'[/COLOR][/COLOR]','','',icon,fanart,'')
		common.addItem('[COLOR skyblue]'+date5+'[/COLOR] - [COLOR white]'+eventtype5+' - On Air: [COLOR skyblue]'+start5+'[/COLOR] and Starts: [COLOR skyblue]'+finish5+'[/COLOR][/COLOR]','','',icon,fanart,'')
		common.addItem('------------------------------------------','','',icon,fanart,'')

def DARTS_LISTINGS():

	url = base64.b64decode(b'aHR0cDovL3d3dy5za3lzcG9ydHMuY29tL2RhcnRzL3NjaGVkdWxl')
	r = common.OPEN_URL_NORMAL(url).replace('\r','').replace('\n','').replace('\t','')
	match = re.compile('<div class="score-sub" style="width:56px">        (.+?)    </div>    <div class="score-comp">(.+?)</div>        <div class="score-side" style="width:360px">        (.+?)                    </div>        <ul class="score-sublinks">                        <li class="score-tv"><img src=".+?" title="(.+?)"></li>').findall(r)
	for date,location,type,channel in match:
		if not '&nbsp;' in location:
			common.addItem('[COLOR white]'+date+' [COLOR white]taking place at '+location+'[/COLOR]','','',icon,fanart,'')
		else:	
			common.addItem('[COLOR white]'+date+'[/COLOR][COLOR white] - No location found[/COLOR]','','',icon,fanart,'')
		common.addItem('[COLOR skyblue]'+type+'[/COLOR]','','',icon,fanart,'')
		common.addItem('[COLOR yellow] '+channel+'[/COLOR]','','',icon,fanart,'')
		common.addItem('------------------------------------------','','',icon,fanart,'')

def NBA_LISTINGS():

	THE_DATE = time.strftime("%Y%m%d") # todays date

	now = datetime.now()
	diff = timedelta(days=7)
	future = now + diff
	Oneweek = future.strftime("%Y%m%d") # date in a week
	url = base64.b64decode(b'aHR0cDovL3d3dy53aGVyZXN0aGVtYXRjaC5jb20vdHYvaG9tZS5hc3A/c2hvd2RhdGVzdGFydD0lcyZzaG93ZGF0ZWVuZD0lcyZzcG9ydGlkPTIz')%(THE_DATE,Oneweek)
	r = common.OPEN_URL_NORMAL(url).replace('\r','').replace('\n','').replace('\t','')
	match = re.compile('<span class="fixture">                        <a class="" href=".+?">                            <em class="">(.+?)</em> <em class="">v</em> <em class="">(.+?)</em> <em class="livestream">Live Stream</em></a></span>                    <span class="ground "><span                         class="time-channel ">(.+?)</span></span>').findall(r)
	common.addItem('[COLOR white]Check out the Live NBA Section for all games[/COLOR]','','',icon,fanart,'')
	common.addItem('------------------------------------------','','',icon,fanart,'')
	for away,home,channel in match:
		common.addItem('[COLOR white]'+away+' vs '+home+'[/COLOR]','','',icon,fanart,'')
		common.addItem('[COLOR yellow]'+channel+'[/COLOR]','','',icon,fanart,'')
		common.addItem('------------------------------------------','','',icon,fanart,'')

def NHL_LISTINGS():

	THE_DATE = time.strftime("%Y%m%d") # todays date

	now = datetime.now()
	diff = timedelta(days=7)
	future = now + diff
	Oneweek = future.strftime("%Y%m%d") # date in a week
	url = base64.b64decode(b'aHR0cDovL3d3dy53aGVyZXN0aGVtYXRjaC5jb20vdHYvaG9tZS5hc3A/c2hvd2RhdGVzdGFydD0lcyZzaG93ZGF0ZWVuZD0lcyZzcG9ydGlkPTE5')%(THE_DATE,Oneweek)
	r = common.OPEN_URL_NORMAL(url).replace('\r','').replace('\n','').replace('\t','')
	match = re.compile('<span class="fixture">                        <a class="" href=".+?">                            <em class="">(.+?)</em> <em class="">v</em> <em class="">(.+?)</em> <em class="livestream">Live Stream</em></a></span>                    <span class="ground "><span                         class="time-channel ">(.+?)</span></span>.+?<td class="competition-name">                    <img title=".+?" src=".+?" alt=".+?" />                                        <span class="">(.+?)</span> <span class="stage ">').findall(r)
	common.addItem('[COLOR white]Check out the Live NHL Section for all games[/COLOR]','','',icon,fanart,'')
	common.addItem('------------------------------------------','','',icon,fanart,'')
	for away,home,channel,competition in match:
		common.addItem('[COLOR white]'+away+' vs '+home+'[/COLOR] [COLOR skyblue]in the '+competition+'[/COLOR]','','',icon,fanart,'')
		common.addItem('[COLOR yellow]'+channel+'[/COLOR]','','',icon,fanart,'')
		common.addItem('------------------------------------------','','',icon,fanart,'')

def MLB_LISTINGS():

	THE_DATE = time.strftime("%Y%m%d") # todays date

	now = datetime.now()
	diff = timedelta(days=7)
	future = now + diff
	Oneweek = future.strftime("%Y%m%d") # date in a week
	url = base64.b64decode(b'aHR0cDovL3d3dy53aGVyZXN0aGVtYXRjaC5jb20vdHYvaG9tZS5hc3A/c2hvd2RhdGVzdGFydD0lcyZzaG93ZGF0ZWVuZD0lcyZzcG9ydGlkPTg=')%(THE_DATE,Oneweek)
	r = common.OPEN_URL_NORMAL(url).replace('\r','').replace('\n','').replace('\t','')
	match = re.compile('<span class="fixture">                        <a class="" href=".+?">                            <em class="">(.+?)</em> <em class="">v</em> <em class="">(.+?)</em> <em class="livestream">Live Stream</em></a></span>                    <span class="ground "><span                         class="time-channel ">(.+?)</span></span>').findall(r)
	common.addItem('[COLOR white]Check out the Live MLB Section for all games[/COLOR]','','',icon,fanart,'')
	common.addItem('------------------------------------------','','',icon,fanart,'')
	for team1,team2,channel in match:
		common.addItem('[COLOR white]'+team1+' vs '+team2+'[/COLOR]','','',icon,fanart,'')
		common.addItem('[COLOR yellow]'+channel+'[/COLOR]','','',icon,fanart,'')
		common.addItem('------------------------------------------','','',icon,fanart,'')

def UFC_LISTINGS():

	url = base64.b64decode(b'aHR0cDovL20udWsudWZjLmNvbS9zY2hlZHVsZQ==')
	r = common.OPEN_URL_NORMAL(url).replace('\r','').replace('\n','').replace('\t','')
	match = re.compile('<li class="touch-row-bg" data-event_id=".+?"><a href=".+?" title="Fight Card"><h5 class="upper ufc-red">(.+?)</h5><strong>(.+?)</strong><br />(.+?)<br />(.+?)</a></li>').findall(r)
	common.addItem('[COLOR white]Use Fight Pass for Prelims & BT Sport for matches[/COLOR]','','',icon,fanart,'')
	common.addItem('------------------------------------------','','',icon,fanart,'')
	for channel,event,date,location in match:
		common.addItem('[COLOR skyblue]'+event+'[/COLOR]','','',icon,fanart,'')
		common.addItem('[COLOR white]Location: '+location+'[/COLOR]','','',icon,fanart,'')
		common.addItem('[COLOR yellow]'+date+' '+channel+'[/COLOR]','','',icon,fanart,'')
		common.addItem('------------------------------------------','','',icon,fanart,'')

def Wrestling_LISTINGS():

	THE_DATE = time.strftime("%Y%m%d") # todays date

	now = datetime.now()
	diff = timedelta(days=7)
	future = now + diff
	Oneweek = future.strftime("%Y%m%d") # date in a week
	url = base64.b64decode(b'aHR0cDovL3d3dy53aGVyZXN0aGVtYXRjaC5jb20vdHYvaG9tZS5hc3A/c2hvd2RhdGVzdGFydD0lcyZzaG93ZGF0ZWVuZD0lcyZzcG9ydGlkPTM1')%(THE_DATE,Oneweek)
	r = common.OPEN_URL_NORMAL(url).replace('\r','').replace('\n','').replace('\t','')
	match = re.compile('<td class="fixture-details">                    <span class="fixture"><a class=" eventlink" href=".+?"><strong class="">.+?</strong></a></span>                    <em class="">(.+?)</em>                    <span class="ground "><span                         class="time-channel ">(.+?)</span></span>').findall(r)
	for when,event in match:
		common.addItem('[COLOR white]'+when+'[/COLOR]','','',icon,fanart,'')
		common.addItem('[COLOR yellow]'+event+'[/COLOR]','','',icon,fanart,'')
		common.addItem('------------------------------------------','','',icon,fanart,'')

def HorseRacing_LISTINGS():

	THE_DATE = time.strftime("%Y%m%d") # todays date

	now = datetime.now()
	diff = timedelta(days=7)
	future = now + diff
	Oneweek = future.strftime("%Y%m%d") # date in a week
	url = base64.b64decode(b'aHR0cDovL3d3dy53aGVyZXN0aGVtYXRjaC5jb20vdHYvaG9tZS5hc3A/c2hvd2RhdGVzdGFydD0lcyZzaG93ZGF0ZWVuZD0lcyZzcG9ydGlkPTI1')%(THE_DATE,Oneweek)
	r = common.OPEN_URL_NORMAL(url).replace('\r','').replace('\n','').replace('\t','')
	match = re.compile('<a class=" eventlink" href=".+?"><strong class="">.+?</strong></a></span>                    <em class="">(.+?)</em>                    <span class="ground "><span                         class="time-channel ">(.+?)</span></span>.+?</td>                <td class="away-team"></td>                                    <td class="start-details">                                                    <span>.+?</span><span class="time "><em class="">.+?</em></span>.+?<td class="competition-name">                    <img title=".+?" src=".+?" alt=".+?" />                                        <span class="">(.+?)</span>').findall(r)
	for event,when,type in match:
		a,b = event.split("Live Racing from ")
		common.addItem('[COLOR white]'+type+' at[/COLOR] [COLOR skyblue]'+b+'[/COLOR]','','',icon,fanart,'')
		common.addItem('[COLOR yellow]'+when+'[/COLOR]','','',icon,fanart,'')
		common.addItem('------------------------------------------','','',icon,fanart,'')

def Hockey_LISTINGS():

	THE_DATE = time.strftime("%Y%m%d") # todays date

	now = datetime.now()
	diff = timedelta(days=7)
	future = now + diff
	Oneweek = future.strftime("%Y%m%d") # date in a week
	url = base64.b64decode(b'aHR0cDovL3d3dy53aGVyZXN0aGVtYXRjaC5jb20vdHYvaG9tZS5hc3A/c2hvd2RhdGVzdGFydD0lcyZzaG93ZGF0ZWVuZD0lcyZzcG9ydGlkPTE5')%(THE_DATE,Oneweek)
	r = common.OPEN_URL_NORMAL(url).replace('\r','').replace('\n','').replace('\t','')
	match = re.compile('<span class="fixture">                        <a class="" href=".+?">                            <em class="">(.+?)</em> <em class="">v</em> <em class="">(.+?)</em> <em class="livestream">Live Stream</em></a></span>                    <span class="ground "><span                         class="time-channel ">(.+?)</span></span>                                    </td>                <td class="away-team"><a title=".+?" href=".+?">                    <img src=".+?" alt=".+?"                        class="badge " /></a></td>                                    <td class="start-details">                                                    <span>.+?</span><span class="time "><em class="">.+?</em></span>.+?<span class="">(.+?)</span> <span class="stage ">').findall(r)
	for away,home,when,comp in match:
		common.addItem('[COLOR white]'+away+' vs '+home+'[/COLOR] [COLOR skyblue]in the '+comp+'[/COLOR]','','',icon,fanart,'')
		common.addItem('[COLOR yellow]'+when+'[/COLOR]','','',icon,fanart,'')
		common.addItem('------------------------------------------','','',icon,fanart,'')

def Boxing_LISTINGS():

	THE_DATE = time.strftime("%Y%m%d") # todays date

	now = datetime.now()
	diff = timedelta(days=31)
	future = now + diff
	Oneweek = future.strftime("%Y%m%d") # date in a week
	url = base64.b64decode(b'aHR0cDovL3d3dy53aGVyZXN0aGVtYXRjaC5jb20vdHYvaG9tZS5hc3A/c2hvd2RhdGVzdGFydD0lcyZzaG93ZGF0ZWVuZD0lcyZzcG9ydGlkPTk=')%(THE_DATE,Oneweek)
	r = common.OPEN_URL_NORMAL(url).replace('\r','').replace('\n','').replace('\t','')
	match = re.compile('<span class="fixture"><a class=".+?eventlink" href=".+?"><strong class=".+?>.+?</strong></a></span>                    <em class=".+?>(.+?)</em>                    <span class="ground.+?><span                         class="time-channel.+?>(.+?)</span></span>.+?<td class="start-details">                                                    <span>(.+?)</span><span class="time.+?><em class=".+?>.+?</em></span>.+?<td class="competition-name">                    <img title=".+?" src=".+?" alt=".+?" />                                        <span class=".+?>(.+?)</span>').findall(r)
	for event,channel,date,competition in match:
		a,b = channel.split(" at ")
		common.addItem('[COLOR white]'+event+'[/COLOR]','','',icon,fanart,'')
		common.addItem('[COLOR skyblue]'+competition+'[/COLOR]','','',icon,fanart,'')
		common.addItem('[COLOR yellow]'+date+' at '+b+'[/COLOR]','','',icon,fanart,'')
		common.addItem('------------------------------------------','','',icon,fanart,'')

def Motorsport_LISTINGS():

	THE_DATE = time.strftime("%Y%m%d") # todays date

	now = datetime.now()
	diff = timedelta(days=7)
	future = now + diff
	Oneweek = future.strftime("%Y%m%d") # date in a week
	url = base64.b64decode(b'aHR0cDovL3d3dy53aGVyZXN0aGVtYXRjaC5jb20vdHYvaG9tZS5hc3A/c2hvd2RhdGVzdGFydD0lcyZzaG93ZGF0ZWVuZD0lcyZzcG9ydGlkPTIw')%(THE_DATE,Oneweek)
	r = common.OPEN_URL_NORMAL(url).replace('\r','').replace('\n','').replace('\t','')
	match = re.compile('<span class="fixture"><a class=".+?eventlink" href=".+?"><strong class=".+?>(.+?)</strong></a></span>                    <em class=".+?>(.+?)</em>                    <span class="ground.+?><span                         class="time-channel.+?>(.+?)</span></span>.+?<td class="competition-name">                    <img title=".+?" src=".+?" alt=".+?" />                                        <span class=".+?>(.+?)</span>').findall(r)
	for title,event,when,competition in match:
		common.addItem('[COLOR white]'+title+'[/COLOR]','','',icon,fanart,'')
		common.addItem('[COLOR white]'+event+'[/COLOR]','','',icon,fanart,'')
		common.addItem('[COLOR yellow]'+when+'[/COLOR]','','',icon,fanart,'')
		common.addItem('[COLOR skyblue]'+competition+'[/COLOR]','','',icon,fanart,'')
		common.addItem('------------------------------------------','','',icon,fanart,'')

def Golf_LISTINGS():

	THE_DATE = time.strftime("%Y%m%d") # todays date

	now = datetime.now()
	diff = timedelta(days=31)
	future = now + diff
	Oneweek = future.strftime("%Y%m%d") # date in a week
	url = base64.b64decode(b'aHR0cDovL3d3dy53aGVyZXN0aGVtYXRjaC5jb20vdHYvaG9tZS5hc3A/c2hvd2RhdGVzdGFydD0lcyZzaG93ZGF0ZWVuZD0lcyZzcG9ydGlkPTEz')%(THE_DATE,Oneweek)
	r = common.OPEN_URL_NORMAL(url).replace('\r','').replace('\n','').replace('\t','')
	match = re.compile('<span class="fixture"><a class=".+?eventlink" href=".+?"><strong class=".+?>(.+?)</strong></a></span>                    <em class=".+?>(.+?)</em>                    <span class="ground.+?><span                         class="time-channel.+?>(.+?)</span></span>.+?<td class="start-details">                                                    <span>(.+?)</span><span class="time.+?><em class=".+?>.+?</em></span>.+?<td class="competition-name">.+?<a class=".+?" href=".+?"><span class=".+?>(.+?)</span> </a><span class="stage.+?>').findall(r)
	for title,event,when,date,competition in match:
		a,b = when.split(" at ")
		common.addItem('[COLOR white]'+event+'[/COLOR]','','',icon,fanart,'')
		common.addItem('[COLOR skyblue]'+competition+'[/COLOR]','','',icon,fanart,'')
		common.addItem('[COLOR yellow]'+date+' at '+b+'[/COLOR]','','',icon,fanart,'')
		common.addItem('------------------------------------------','','',icon,fanart,'')

def AFL_LISTINGS():

	THE_DATE = time.strftime("%Y%m%d") # todays date

	now = datetime.now()
	diff = timedelta(days=7)
	future = now + diff
	Oneweek = future.strftime("%Y%m%d") # date in a week
	url = base64.b64decode(b'aHR0cDovL3d3dy53aGVyZXN0aGVtYXRjaC5jb20vdHYvaG9tZS5hc3A/c2hvd2RhdGVzdGFydD0lcyZzaG93ZGF0ZWVuZD0lcyZzcG9ydGlkPTIx')%(THE_DATE,Oneweek)
	r = common.OPEN_URL_NORMAL(url).replace('\r','').replace('\n','').replace('\t','')
	match = re.compile('<span class="fixture">                        <a class="" href=".+?">                            <em class="">(.+?)</em> <em class="">v</em> <em class="">(.+?)</em> <em class="livestream">Live Stream</em></a></span>                    <span class="ground "><span                         class="time-channel ">(.+?)</span></span>.+?<span class="">(.+?)</span> .+?<span class="stage ">').findall(r)
	for team1,team2,when,type in match:
		if 'Live Stream' in when:
			a,b = when.split("on")
			common.addItem('[COLOR white]'+team1+' vs '+team2+'[/COLOR] [COLOR skyblue]in the '+type+'[/COLOR]','','',icon,fanart,'')
			common.addItem('[COLOR yellow]'+a+'[/COLOR][COLOR white] - Not televised in the UK[/COLOR]','','',icon,fanart,'')
			common.addItem('------------------------------------------','','',icon,fanart,'')
		else:
			common.addItem('[COLOR white]'+team1+' vs '+team2+'[/COLOR] [COLOR skyblue]in the '+type+'[/COLOR]','','',icon,fanart,'')
			common.addItem('[COLOR yellow]'+when+'[/COLOR]','','',icon,fanart,'')
			common.addItem('------------------------------------------','','',icon,fanart,'')

def MotoGP_LISTINGS():

	THE_DATE = time.strftime("%Y%m%d") # todays date

	now = datetime.now()
	diff = timedelta(days=31)
	future = now + diff
	Oneweek = future.strftime("%Y%m%d") # date in a week
	url = base64.b64decode(b'aHR0cDovL3d3dy53aGVyZXN0aGVtYXRjaC5jb20vdHYvaG9tZS5hc3A/c2hvd2RhdGVzdGFydD0lcyZzaG93ZGF0ZWVuZD0lcyZzcG9ydGlkPTE1')%(THE_DATE,Oneweek)
	r = common.OPEN_URL_NORMAL(url).replace('\r','').replace('\n','').replace('\t','')
	match = re.compile('<span class="fixture"><a class=".+?eventlink" href=".+?"><strong class=".+?>(.+?)</strong></a></span>                    <em class=".+?>(.+?)</em>                    <span class="ground.+?><span                         class="time-channel.+?>(.+?)</span></span>.+?<td class="away-team"></td>                                    <td class="start-details">                                                    <span>(.+?)</span><span class="time.+?><em class=".+?>.+?</em></span>.+?<td class="competition-name">                    <img title=".+?" src=".+?" alt=".+?" />                                        <span class=".+?>(.+?)</span>').findall(r)
	for title,event,channel,date,season in match:
		a,b = channel.split(" at ")
		common.addItem('[COLOR white]'+event+'[/COLOR]','','',icon,fanart,'')
		common.addItem('[COLOR skyblue]'+title+' - '+season+'[/COLOR]','','',icon,fanart,'')
		common.addItem('[COLOR yellow]'+date+' at '+b+'[/COLOR]','','',icon,fanart,'')
		common.addItem('------------------------------------------','','',icon,fanart,'')

def Cycling_LISTINGS():

	THE_DATE = time.strftime("%Y%m%d") # todays date

	now = datetime.now()
	diff = timedelta(days=7)
	future = now + diff
	Oneweek = future.strftime("%Y%m%d") # date in a week
	url = base64.b64decode(b'aHR0cDovL3d3dy53aGVyZXN0aGVtYXRjaC5jb20vdHYvaG9tZS5hc3A/c2hvd2RhdGVzdGFydD0lcyZzaG93ZGF0ZWVuZD0lcyZzcG9ydGlkPTEw')%(THE_DATE,Oneweek)
	r = common.OPEN_URL_NORMAL(url).replace('\r','').replace('\n','').replace('\t','')
	match = re.compile('<span class="fixture"><a class=" eventlink" href=".+?"><strong class="">(.+?)</strong></a></span>                    <em class="">(.+?)</em>                    <span class="ground "><span                         class="time-channel ">(.+?)</span></span>                                        ').findall(r)
	for title,event,when in match:
		common.addItem('[COLOR white]'+event+'[/COLOR]','','',icon,fanart,'')
		common.addItem('[COLOR skyblue]'+title+':[/COLOR] [COLOR yellow]'+when+'[/COLOR]','','',icon,fanart,'')
		common.addItem('------------------------------------------','','',icon,fanart,'')


##################################################################################


def PVRbeta():
	PVRSimple = xbmc.translatePath('special://home/userdata/addon_data/pvr.iptvsimple/')

	if os.path.exists(PVRSimple):
		shutil.rmtree(PVRSimple)
	nullPVR   = '{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","params":{"addonid":"pvr.iptvsimple","enabled":false},"id":1}'
	nullLiveTV = '{"jsonrpc":"2.0", "method":"Settings.SetSettingValue", "params":{"setting":"pvrmanager.enabled", "value":false},"id":1}'
	jsonSetPVR = '{"jsonrpc":"2.0", "method":"Settings.SetSettingValue", "params":{"setting":"pvrmanager.enabled", "value":true},"id":1}'
	IPTVon 	   = '{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","params":{"addonid":"pvr.iptvsimple","enabled":true},"id":1}'
	nulldemo   = '{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","params":{"addonid":"pvr.demo","enabled":false},"id":1}'
	EPGurl   = base64.b64decode("JXM6JXMveG1sdHYucGhwP3VzZXJuYW1lPSVzJnBhc3N3b3JkPSVz")%(lehekylg,Username,Password)
	
	xbmc.executeJSONRPC(nullLiveTV)
	xbmc.executeJSONRPC(nulldemo)
	xbmc.executeJSONRPC(nullPVR)

	if not os.path.exists(PVRSimple):
		os.makedirs(PVRSimple)
	shutil.copyfile(AddonRes+'/PVRset.xml', PVRSimple+'settings.xml')
	BetaPVR = PVRSimple+'EyePeaTV.m3u8'
	time.sleep(1)

	f = open(BetaPVR, 'a')
	f.write('#EXTM3U\n')

	xbmc.executebuiltin("ActivateWindow(busydialog)")
	UserList = base64.b64decode("JXMvZ2V0LnBocD91c2VybmFtZT0lcyZwYXNzd29yZD0lcyZ0eXBlPW0zdV9wbHVzJm91dHB1dD10cw==")%(lehekylg,Username,Password)
	link = open_url(UserList).replace('\r','').replace(',',' Channel="').replace('\nhttp','", Link=http')
	match = re.compile('#EXTINF:-1 tvg-id="(.+?)" tvg-name="(.+?)" tvg-logo="(.+?)" group-title="(.+?)" Channel="(.+?)", Link=(.+?).ts').findall(link)
	for EPGid, ChannelName, ChanLogo, GroupTitle, StreamTitle, StreamLink in match:
		OutpuT = '#EXTINF:-1 tvg-id="'+EPGid+'" tvg-name="'+ChannelName+'" tvg-logo="'+ChanLogo+'" group-title="'+GroupTitle+'",'+StreamTitle+'\n'+StreamLink+'.ts\n'
		OutpuT = OutpuT.replace(',,','\n')
		f = open(BetaPVR, 'a')
		f.write(OutpuT)
		if PVRon == 'false':
			VAddon.setSetting(id='PVRUpdater', value='true')

	time.sleep(1)
	xbmc.executeJSONRPC(IPTVon)
	
	moist = xbmcaddon.Addon('pvr.iptvsimple')
	moist.setSetting(id='epgUrl', value=EPGurl)
	moist.setSetting(id='m3uPath', value='special://home/userdata/addon_data/pvr.iptvsimple/VStreams.m3u8')
	time.sleep(1)
	xbmc.executeJSONRPC(jsonSetPVR)
	xbmc.executeJSONRPC(IPTVon)
	xbmc.executebuiltin("Dialog.Close(busydialog)")
	xbmc.executebuiltin('Notification(PVR Setup,[COLOR white]PVR is now setup allow loading to finish[/COLOR],3000,special://home/addons/'+AddonID+'/icon.png)')
	xbmc.executebuiltin("Container.Refresh")


def correctPVR():

	try:
		req = urllib2.Request(loginurl,headers={"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36"})
		connection = urllib2.urlopen(req)
		print connection.getcode()
		connection.close()
		#playlist found, user active & login correct, proceed to addon
		pass
		
	except urllib2.HTTPError, e:
		print e.getcode()
		dialog.ok("[COLOR white]Error[/COLOR]",'[COLOR white]This process will not run as your account has expired[/COLOR]',' ','[COLOR white]Please check your account information[/COLOR]')
		sys.exit(1)
		xbmc.executebuiltin("Dialog.Close(busydialog)")
		

	RAM = int(xbmc.getInfoLabel("System.Memory(total)")[:-2])
	RAMM = xbmc.getInfoLabel("System.Memory(total)")
	
	if RAM < 1999:
		choice = xbmcgui.Dialog().yesno('[COLOR white]Low Power Device [COLOR lime]RAM: ' + RAMM + '[/COLOR][/COLOR]', '[COLOR white]Your device has been detected as a low end device[/COLOR]', '[COLOR white]We recommend avoiding PVR usage for this reason[/COLOR]', '[COLOR white]We cannnot support low end devices for PVR[/COLOR]', nolabel='[COLOR lime]OK, Cancel this[/COLOR]',yeslabel='[COLOR red]I know, proceed[/COLOR]')
		if choice == 0:
			sys.exit(1)
		elif choice == 1:
			pass
	xbmc.executebuiltin("ActivateWindow(busydialog)")
	nullPVR   = '{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","params":{"addonid":"pvr.iptvsimple","enabled":false},"id":1}'
	nullLiveTV = '{"jsonrpc":"2.0", "method":"Settings.SetSettingValue", "params":{"setting":"pvrmanager.enabled", "value":false},"id":1}'
	jsonSetPVR = '{"jsonrpc":"2.0", "method":"Settings.SetSettingValue", "params":{"setting":"pvrmanager.enabled", "value":true},"id":1}'
	IPTVon 	   = '{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","params":{"addonid":"pvr.iptvsimple","enabled":true},"id":1}'
	nulldemo   = '{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","params":{"addonid":"pvr.demo","enabled":false},"id":1}'
	EPGurl   = base64.b64decode("JXM6JXMveG1sdHYucGhwP3VzZXJuYW1lPSVzJnBhc3N3b3JkPSVz")%(lehekylg,Username,Password)

	xbmc.executeJSONRPC(nullPVR)
	xbmc.executeJSONRPC(nullLiveTV)
	time.sleep(5)
	xbmc.executeJSONRPC(jsonSetPVR)
	xbmc.executeJSONRPC(IPTVon)
	xbmc.executeJSONRPC(nulldemo)
	
	moist = xbmcaddon.Addon('pvr.iptvsimple')
	moist.setSetting(id='m3uUrl', value=loginurl)
	moist.setSetting(id='epgUrl', value=EPGurl)
	moist.setSetting(id='m3uCache', value="false")
	moist.setSetting(id='epgCache', value="false")
	xbmc.executebuiltin("Dialog.Close(busydialog)")
	dialog.ok("[COLOR white]" + AddonTitle + "[/COLOR]",'[COLOR white]We\'ve copied your logins to the PVR Guide[/COLOR]',' ','[COLOR white]You [B]MUST[/B] allow time to load the EPG to avoid issues.[/COLOR]')

def disablePVR():
	xbmc.executebuiltin("ActivateWindow(busydialog)")
	nullPVR   = '{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","params":{"addonid":"pvr.iptvsimple","enabled":false},"id":1}'
	nullLiveTV = '{"jsonrpc":"2.0", "method":"Settings.SetSettingValue", "params":{"setting":"pvrmanager.enabled", "value":false},"id":1}'
	PVRdata   =  xbmc.translatePath(os.path.join('special://home/userdata/addon_data/','pvr.iptvsimple'))
	xbmc.executeJSONRPC(nullPVR)
	xbmc.executeJSONRPC(nullLiveTV)
	shutil.rmtree(PVRdata)
	xbmc.executebuiltin("Dialog.Close(busydialog)")
	dialog.ok("[COLOR white]" + AddonTitle + "[/COLOR]",'[COLOR white]PVR Guide is now disabled[/COLOR]',' ','[COLOR white]You may set this up again any time[/COLOR]')
	time.sleep(1)
	xbmc.executebuiltin("Container.Refresh")

def SpeedChoice():
	choice = dialog.select("[COLOR white]" + AddonTitle + " Speedtest[/COLOR]", ['[COLOR white]Ookla Speedtest[/COLOR]','[COLOR white]Fast.com Speedtest by Netflix[/COLOR]'])
	if choice == 0:
		xbmc.executebuiltin('Runscript("special://home/addons/plugin.video.eyepeatv/speedtest.py")') ###############
	if choice == 1:
		xbmc.executebuiltin('Runscript("special://home/addons/plugin.video.eyepeatv/fastload.py")')  ###############

def iVueInt():

	try:
		req = urllib2.Request(loginurl,headers={"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36"})
		connection = urllib2.urlopen(req)
		print connection.getcode()
		connection.close()
		#playlist found, user active & login correct, proceed to addon
		pass
		
	except urllib2.HTTPError, e:
		print e.getcode()
		dialog.ok("[COLOR white]Error[/COLOR]",'[COLOR white]This process will not run as your account has expired[/COLOR]',' ','[COLOR white]Please check your account information[/COLOR]')
		sys.exit(1)
		xbmc.executebuiltin("Dialog.Close(busydialog)")

	xbmc.executebuiltin("ActivateWindow(busydialog)")
	iVue_SETTINGS = xbmc.translatePath(os.path.join('special://home/userdata/addon_data/script.ivueguide','settings.xml'))
	UseriVueSets = xbmc.translatePath(os.path.join('special://home/userdata/addon_data/script.ivueguide','oldsettings.xml'))
	AddoniVueSet = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.eyepeatv/resources','ivueset.xml')) ###############
	iVue_DATA = xbmc.translatePath(os.path.join('special://home/userdata/addon_data/script.ivueguide/'))
	if not xbmc.getCondVisibility('System.HasAddon(script.ivueguide)'):
		install('iVue','https://raw.githubusercontent.com/totaltec2014/ivue2/master/script.ivueguide/script.ivueguide-3.0.9.zip')
		xbmc.executebuiltin("UpdateAddonRepos")
		xbmc.executebuiltin("UpdateLocalAddons")
		time.sleep(5)

	if not os.path.isfile(iVue_SETTINGS):
		if not os.path.exists(iVue_DATA):
			os.makedirs(iVue_DATA)
		shutil.copyfile(AddoniVueSet, iVue_SETTINGS)
	else:
		os.remove(iVue_SETTINGS)
		xbmc.log('Old iVue settings deleted')
		if not os.path.exists(iVue_DATA):
			os.makedirs(iVue_DATA)
		shutil.copyfile(AddoniVueSet, iVue_SETTINGS)

	iVueEnable 	   = '{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","params":{"addonid":"script.ivueguide","enabled":true},"id":1}'
	xbmc.executeJSONRPC(iVueEnable)
	
	FullDB = os.path.join(AddonRes, 'fullivue.zip')
	dp = xbmcgui.DialogProgress()
	dp.create(AddonTitle,"Copying DB",'', 'Please Wait')
	unzip(FullDB,iVue_DATA,dp)
	xbmc.log("Full iVue Master DB Copied")
	xbmc.executebuiltin('Runscript("special://home/addons/plugin.video.eyepeatv/fullivue.py")') ###############

def install(name,url):
    path = xbmc.translatePath(os.path.join('special://home/addons','packages'))
    dp = xbmcgui.DialogProgress()
    dp.create(AddonTitle,"Installing...",'', 'Please Wait')
    lib=os.path.join(path, 'content.zip')
    try:
       os.remove(lib)
    except:
       pass
    downloader.download(url, lib, dp)
    addonfolder = xbmc.translatePath(os.path.join('special://home','addons'))
    time.sleep(3)
    dp = xbmcgui.DialogProgress()
    dp.create(AddonTitle,"Installing...",'', 'Please Wait')
    dp.update(0,"", "Installing... Please Wait")
    print '======================================='
    print addonfolder
    print '======================================='
    unzip(lib,addonfolder,dp)

def unzip(_in, _out, dp):
	__in = zipfile.ZipFile(_in,  'r')
	
	nofiles = float(len(__in.infolist()))
	count   = 0
	
	try:
		for item in __in.infolist():
			count += 1
			update = (count / nofiles) * 100
			
			if dp.iscanceled():
				dialog = xbmcgui.Dialog()
				dialog.ok(AddonTitle, 'Process was cancelled.')
				
				sys.exit()
				dp.close()
			
			try:
				dp.update(int(update))
				__in.extract(item, _out)
			
			except Exception, e:
				print str(e)

	except Exception, e:
		print str(e)
		return False
		
	return True	

def AddDir(name, url, mode, iconimage, description="", isFolder=True, background=None):
    u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&description="+urllib.quote_plus(description)
    a=sys.argv[0]+"?url=None&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&description="+urllib.quote_plus(description)
    print name.replace('-[US]','').replace('-[EU]','').replace('[COLOR yellow]','').replace('[/COLOR]','').replace(' (G)','')+'='+a
    liz = xbmcgui.ListItem(name, iconImage=iconimage, thumbnailImage=iconimage)
    liz.setInfo(type="Video", infoLabels={ "Title": name, "Plot": description})
    liz.setProperty('IsPlayable', 'true')
    xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=u, listitem=liz, isFolder=isFolder)

def AddDir2(name, url, mode, iconimage, description="", isFolder=True, background=None):
    u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&description="+urllib.quote_plus(description)
    a=sys.argv[0]+"?url=None&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&description="+urllib.quote_plus(description)
    liz = xbmcgui.ListItem(name, iconImage=iconimage, thumbnailImage=iconimage)
    liz.setInfo(type="Video", infoLabels={ "Title": name, "Plot": description})
    liz.setProperty('IsPlayable', 'true')
    xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=u, listitem=liz, isFolder=isFolder)

def addItem(name,url,mode,iconimage,fanart,description):
	u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&fanart="+urllib.quote_plus(fanart)
	ok=True
	liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
	liz.setInfo( type="Video", infoLabels={ "Title": name } )
	liz.setProperty( "Fanart_Image", fanart )
	ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
	return ok

def addDir(name,url,mode,iconimage,fanart,description):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)+"&description="+urllib.quote_plus(description)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description } )
        liz.setProperty( "Fanart_Image", fanart )
        if mode==9099 :
            ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        else:
            ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok

def addXMLMenu(name,url,mode,iconimage,fanart,description):
    u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)+"&description="+urllib.quote_plus(description)
    ok=True
    liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
    liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description } )
    liz.setProperty( "Fanart_Image", fanart )
    ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
    return ok

def OPEN_URL(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36')
    response = urllib2.urlopen(req)
    link=response.read()
    response.close()
    return link

def open_url(url):
    try:
        req = urllib2.Request(url,headers={"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36"})
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        return link
    except:quit()

def OPEN_URL_NORMAL(url):

	if "https://" in url:
		url = url.replace("https://","http://")
	req = urllib2.Request(url)
	req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36')
	response = urllib2.Request(req)
	link=response.read()
	response.close()
	return link

"""def ExtraMenuu():
    link = OPEN_URL('http://futurestreams.tk/Backup/Downloads/ExtrasList2.xml').replace('\n','').replace('\r','')  #Spaf
    match = re.compile('name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"').findall(link)
    for name,url,iconimage,FanArt,description in match:
        addXMLMenu(name,url,6,iconimage,FanArt,description)"""

def Buildlist(url):
    list = common.m3u2list(url)
    for channel in list:
        name = common.GetEncodeString(channel["display_name"])
        AddDir(name ,channel["url"], 3, iconimage, isFolder=False)
		
def PlayUrl(name, url, iconimage=None):
        _NAME_=name
        list = common.m3u2list(loginurl)
        for channel in list:
            name = common.GetEncodeString(channel["display_name"])
            stream=channel["url"]
            if _NAME_ in name:
                listitem = xbmcgui.ListItem(path=stream, thumbnailImage=iconimage)
                listitem.setInfo(type="Video", infoLabels={ "Title": name })
                xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, listitem)				

def Get_Params():
    param = []
    paramstring = sys.argv[2]
    if len(paramstring) >= 2:
        params = sys.argv[2]
        cleanedparams = params.replace('?','')
        if (params[len(params)-1] == '/'):
            params = params[0:len(params)-2]
        pairsofparams = cleanedparams.split('&')
        param = {}
        for i in range(len(pairsofparams)):
            splitparams = {}
            splitparams = pairsofparams[i].split('=')
            if (len(splitparams)) == 2:
                param[splitparams[0].lower()] = splitparams[1]
    return param
	
params=Get_Params()
url=None
name=None
mode=None
iconimage=None
description=None

try:url = urllib.unquote_plus(params["url"])
except:pass
try:name = urllib.unquote_plus(params["name"])
except:pass
try:iconimage = urllib.unquote_plus(params["iconimage"])
except:pass
try:mode = int(params["mode"])
except:pass
try:description = urllib.unquote_plus(params["description"])
except:pass

if mode == 7:
	quit
if mode == 6:
	FootballSchedule()
elif mode == 8:
	iVuemenu()
elif mode == 12:
	PVRmenu()
elif mode == 1:
	Buildlist(url)
elif mode == 3:
    PlayUrl(name, url, iconimage)
elif mode == 9:
	SpeedChoice()
elif mode == 10:
	correctPVR()
elif mode == 11:
	xbmc.executebuiltin('ActivateWindow(TVGuide)')
elif mode == 13:
	iVueInt()
elif mode == 14:
    xbmc.executebuiltin('RunAddon(script.ivueguide)')
elif mode == 15:
	installer.INSTALLAPK(name,url,description)
elif mode == 16:
	PVRbeta()
elif mode == 17:
	disablePVR()
elif mode==18:
        maintenance.viewLogFile()
elif mode==19:
		maintenance.autocleannow()
elif mode==20:
		maintenance.clearCache()
elif mode==21:
		maintenance.DeleteCrashLogs()
elif mode==22:
		maintenance.deleteThumbnails()
elif mode==23:
		maintenance.purgePackages()
elif mode==24:
		maintenance.view_LastError()
elif mode==25:
		maintenance.viewErrors()
elif mode==26:
        F1_LISTINGS()
elif mode==25:
        DARTS_LISTINGS()
elif mode==24:
		NBA_LISTINGS()
elif mode==23:
		NHL_LISTINGS()
elif mode==22:
		MLB_LISTINGS()
elif mode==211:
		UFC_LISTINGS()
elif mode==212:
		RugbyUnion_LISTINGS()
elif mode==213:
		RugbyLeague_LISTINGS()
elif mode==215:
		Tennis_LISTINGS()
elif mode==216:
		Wrestling_LISTINGS()
elif mode==217:
		HorseRacing_LISTINGS()
elif mode==218:
		Hockey_LISTINGS()
elif mode==219:
		Boxing_LISTINGS()
elif mode==220:
		Motorsport_LISTINGS()
elif mode==221:
		Golf_LISTINGS()
elif mode==222:
		AFL_LISTINGS()
elif mode==223:
		MotoGP_LISTINGS()
elif mode==224:
		Cycling_LISTINGS()