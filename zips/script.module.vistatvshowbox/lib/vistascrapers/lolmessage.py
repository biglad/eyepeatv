import xbmc
import xbmcgui
import xbmcaddon
import random
list  = ['What did you ask for??','Accessing the DarkNET.','By The Power of Greyskull.','Putting on facemask.','Washing hands for 20 secs.','Checking the black book.','Using the Force','Webcrawler is searching','Looking on the black market','Using Google, not really lol','Asking Donald Trump for advice....','Connecting to the matrix......','EPTV! EPTV!! You Cant Handle the EPTV!!........']
counter =0
__addon__ = xbmcaddon.Addon(id='script.module.vistatvshowbox')
dp = xbmcgui.DialogProgress()
dp.create("[COLOR=white][B]EyePeaTV Requisition[/COLOR][/B]","[B][COLOR=red]"+random.choice(list)+"[/COLOR][/B]","[COLOR=orange]Please Wait......[/COLOR]")
dp.update(counter)
while counter < 99:
    counter = counter+1
    xbmc.sleep(20)
    dp.update(counter)
if dp:
    dp.close()
