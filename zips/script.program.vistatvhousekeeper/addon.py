import os
import xbmc,xbmcaddon,subprocess
import urlparse
import xbmcgui
import sfile
dp = xbmcgui.DialogProgress()
dialog = xbmcgui.Dialog()
dp.create("[COLOR gold]VistaTV House Keeper[/COLOR]","Removing temp /old files","Please Wait...")
xbmc.sleep(2000)
dp.update(10)




#CACHE
CACHE    = xbmc.translatePath('special://home/cache/')
#FILES
MZip     = xbmc.translatePath('special://home/_mega_temp.zip')
MZip2     = xbmc.translatePath('special://home/userdata/install.zip')
MZip3     = xbmc.translatePath('special://home/userdata/install2.zip')
MZip4     = xbmc.translatePath('special://home/userdata/install3.zip')
MZip5     = xbmc.translatePath('special://home/menu.zip')
MZip6     = xbmc.translatePath('special://home/uk.zip')
#THUMBS
thumbs     = xbmc.translatePath('special://home/userdata/Thumbnails/')




try: sfile.rmtree(CACHE)
except: pass
try: sfile.rmtree(thumbs)
except: pass

#TV GUIDE DATA
try: os.remove(xbmc.translatePath("special://userdata/addon_data/script.tvguide.vistatv/vistatv.xml"))
except: pass
dp.update(20)
try: os.remove(xbmc.translatePath("special://userdata/addon_data/script.tvguide.vistatv/source.db"))
except: pass

try: os.remove(xbmc.translatePath("special://userdata/addon_data/script.tvguide.vistatvusa/vistatvusa.xml"))
except: pass
dp.update(25)
try: os.remove(xbmc.translatePath("special://userdata/addon_data/script.tvguide.vistatvusa/source.db"))
except: pass

try: os.remove(xbmc.translatePath("special://userdata/addon_data/script.tvguide.vistatvkids/vistatvkids.xml"))
except: pass
dp.update(30)
try: os.remove(xbmc.translatePath("special://userdata/addon_data/script.tvguide.vistatvkids/source.db"))
except: pass

try: os.remove(xbmc.translatePath("special://userdata/addon_data/script.tvguide.vistatvsport/vistatvsport.xml"))
except: pass
dp.update(35)
try: os.remove(xbmc.translatePath("special://userdata/addon_data/script.tvguide.vistatvsport/source.db"))
except: pass


oldordeadaddon     = xbmc.translatePath('special://home/addons/plugin.video.cattv.tva/')
try: sfile.rmtree(oldordeadaddon)
except: pass
dp.update(40)

oldordeadaddon     = xbmc.translatePath('special://home/addons/script.module.theunjudged/')
try: sfile.rmtree(oldordeadaddon)
except: pass
dp.update(41)

oldordeadaddon     = xbmc.translatePath('special://home/addons/script.module.theunjudged.iptv/')
try: sfile.rmtree(oldordeadaddon)
except: pass
dp.update(42)

oldordeadaddon     = xbmc.translatePath('special://home/addons/script.module.theunjudged.live.nettv/')
try: sfile.rmtree(oldordeadaddon)
except: pass
dp.update(43)

oldordeadaddon     = xbmc.translatePath('special://home/addons/script.module.theunjudged.scraper/')
try: sfile.rmtree(oldordeadaddon)
except: pass
dp.update(44)

oldordeadaddon     = xbmc.translatePath('special://home/addons/script.module.theunjudged.uktv.now/')
try: sfile.rmtree(oldordeadaddon)
except: pass
dp.update(45)

oldordeadaddon     = xbmc.translatePath('special://home/addons/script.module.underdogscrapers/')
try: sfile.rmtree(oldordeadaddon)
except: pass
dp.update(46)

oldordeadaddon     = xbmc.translatePath('special://home/addons/script.tvguide.vistatvkids/')
try: sfile.rmtree(oldordeadaddon)
except: pass
dp.update(49)

oldordeadaddon     = xbmc.translatePath('special://home/addons/script.tvguide.vistatvsport/')
try: sfile.rmtree(oldordeadaddon)
except: pass
dp.update(51)

oldordeadaddon     = xbmc.translatePath('special://home/addons/script.tvguide.vistatvusa/')
try: sfile.rmtree(oldordeadaddon)
except: pass
dp.update(55)

oldordeadaddon     = xbmc.translatePath('special://home/cache/')
try: sfile.rmtree(oldordeadaddon)
except: pass
dp.update(60)

oldordeadaddon     = xbmc.translatePath('special://home/addons/repository.jesusboxtv/')
try: sfile.rmtree(oldordeadaddon)
except: pass
dp.update(61)

oldordeadaddon     = xbmc.translatePath('special://home/addons/repository.pluto/')
try: sfile.rmtree(oldordeadaddon)
except: pass
dp.update(62)

oldordeadaddon     = xbmc.translatePath('special://home/addons/repository.vista/')
try: sfile.rmtree(oldordeadaddon)
except: pass
dp.update(63)

oldordeadaddon     = xbmc.translatePath('special://home/addons/repository.ukturk/')
try: sfile.rmtree(oldordeadaddon)
except: pass
dp.update(64)

oldordeadaddon     = xbmc.translatePath('special://home/addons/repository.PureRepo/')
try: sfile.rmtree(oldordeadaddon)
except: pass
dp.update(65)

oldordeadaddon     = xbmc.translatePath('special://home/addons/repository.zt/')
try: sfile.rmtree(oldordeadaddon)
except: pass
dp.update(66)

oldordeadaddon     = xbmc.translatePath('special://home/addons/repository.maverickrepo/')
try: sfile.rmtree(oldordeadaddon)
except: pass
dp.update(67)

oldordeadaddon     = xbmc.translatePath('special://home/addons/repository.steptoes/')
try: sfile.rmtree(oldordeadaddon)
except: pass
dp.update(68)

oldordeadaddon     = xbmc.translatePath('special://home/addons/repository.wod/')
try: sfile.rmtree(oldordeadaddon)
except: pass
dp.update(69)

oldordeadaddon     = xbmc.translatePath('special://home/addons/repository.x-odi.nl/')
try: sfile.rmtree(oldordeadaddon)
except: pass
dp.update(70)



try: os.remove(MZip)
except: pass
dp.update(71)
try: os.remove(MZip2)
except: pass
dp.update(73)
try: os.remove(MZip3)
except: pass
dp.update(75)
try: os.remove(MZip4)
except: pass
dp.update(77)
try: os.remove(MZip5)
except: pass
try: os.remove(MZip6)
except: pass
dp.update(80)


origfolder = (xbmc.translatePath("special://home/addons"))      
def CleanPYO():
    count = 0
    for (dirname, dirs, files) in os.walk(origfolder):
       for filename in files:
           if filename.endswith('.pyo') :
               os.remove(os.path.join(dirname, filename))


 
CleanPYO() 



#update = xbmcgui.Dialog().yesno("[COLOR tomato]CerebroTV House Keeper[/COLOR]","[COLOR yellow]All none needed files have been removed[/COLOR]","[COLOR turquoise]This will speed up your box[/COLOR]" ,"[COLOR turquoise]A ReStart is now needed[/COLOR]")
#if update:
#    xbmc.executebuiltin('RunAddon(script.program.exitkodi)')
#else:
#    xbmc.executebuiltin('RunAddon(script.program.exitkodi)')
dp.update(80)
xbmc.sleep(1000)
dp.update(100)
dp.close()
dp.create("[COLOR gold]VistaTV House Keeper[/COLOR]","Closing Kodi","Please Wait...")
dp.update(100)
xbmc.sleep(3000)
os._exit(1)





