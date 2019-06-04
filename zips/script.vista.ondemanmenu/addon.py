import time
import xbmc
import os
import xbmcgui
import urllib2
import utils
import sfile

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
        function11
        )
        
    call = dialog.select('[B][COLOR=yellow]On Demand Menu[/COLOR][/B]', [ 
    '[B][COLOR=gold]Movies[/COLOR][/B]' ,	
    '[B][COLOR=yellow]TV Shows[/COLOR][/B]',
	'[B][COLOR=gold]Latest TV Episodes[/COLOR][/B]',
    '[B][COLOR=yellow]Latest Movies[/COLOR][/B]',
	'[B][COLOR=gold]Latest TV Episodes + Classics[/COLOR][/B]',
	'[B][COLOR=yellow]Sky Cinema on Demand[/COLOR][/B]',
	'[B][COLOR=gold]BBCi Player[/COLOR][/B] (Geo Locked to UK)',
	'[B][COLOR=yellow]ITV Player[/COLOR][/B] (Geo Locked to UK)',
	'[B][COLOR=gold]Torrent Search[/COLOR][/B] (Need RD or PM)',
    '[B][COLOR=yellow]Vista Movies H265 Only Movies[/COLOR][/B]',
    '[B][COLOR=gold]Vista Movies[/COLOR][/B]'
    ])
    # dialog.selectreturns
    #   0 -> escape pressed
    #   1 -> first item
    #   2 -> second item
    if call:
        # esc is not pressed
        if call < 0:
            return
        func = funcs[call-11]
        return func()
    else:
        func = funcs[call]
        return func()
    return 



def function1():
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.vistatvshowbox/?action=movieNavigator",return)')
	
def function2():
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.vistatvshowbox/?action=tvNavigator",return)')

def function3():
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.vistatvshowbox/?action=tvWidget",return)')
	
def function4():
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.vistatvshowbox/?action=movieWidget",return)')
	
def function5():
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.tvheaven",return)')

def function6():
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.vistatvshowbox/?action=channels",return)')
	
def function7():
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.iplayerwww/?content_type=video",return)')
	
def function8():
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.itv",return)')

def function9():
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.livehub2/?description&iconimage=C%3a%5cUsers%5ckhanb%5cAppData%5cRoaming%5cKodi%5caddons%5cplugin.video.livehub2%5cicon.png&mode=2001&name=%5bB%5d%5bCOLOR%20gold%5dNeeko%3a%20%5b%2fCOLOR%5d%5bCOLOR%20white%5dMovie%20%2f%20TV%20On%20Demand%5b%2fCOLOR%5d%5b%2fB%5d%20(Torrents)&url=url",return)')	

def function10():
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.livehub2/?description&iconimage=C%3a%5cUsers%5ckhanb%5cAppData%5cRoaming%5cKodi%5caddons%5cplugin.video.livehub2%5cicon.png&mode=2015&name=%5bB%5d%5bCOLOR%20gold%5dNeeko%3a%20%5b%2fCOLOR%5d%5bCOLOR%20white%5dMovies%20On%20Demand%5b%2fCOLOR%5d%5b%2fB%5d%20(Direct%20H265%20Only)&url=url",return)')
	
def function11():
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.livehub2/?description&iconimage=C%3a%5cUsers%5ckhanb%5cAppData%5cRoaming%5cKodi%5caddons%5cplugin.video.livehub2%5cicon.png&mode=2016&name=%5bB%5d%5bCOLOR%20gold%5dNeeko%3a%20%5b%2fCOLOR%5d%5bCOLOR%20white%5dMovies%20On%20Demand%5b%2fCOLOR%5d%5b%2fB%5d%20(Direct)&url=url",return)')
menuoptions()