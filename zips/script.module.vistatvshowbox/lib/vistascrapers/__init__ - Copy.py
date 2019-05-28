# -*- coding: UTF-8 -*-

import pkgutil
import os.path
import xbmc
import xbmcgui
import xbmcaddon
import random
list  = ['Checking the black book.','Using the Force','Webcrawler is searching','Looking on the black market','Using Google, not really lol']
counter =0
__addon__ = xbmcaddon.Addon(id='script.module.vistatvshowbox')
dp = xbmcgui.DialogProgress()
dp.create("[COLOR=white][B]VistaTV Requisition[/COLOR][/B]","[B][COLOR=red]"+random.choice(list)+"[/COLOR][/B]","[COLOR=orange]Please Wait......[/COLOR]")
dp.update(counter)

def updatedisplay(counter):
    newcount=counter
    dp.update(newcount)
    #xbmc.sleep(100)

def sources():
    global newcount
    newcount=0
    try:
        sourceDict = []
        provider = __addon__.getSetting('module.provider')
        sourceFolder = getScraperFolder(provider)
        sourceFolderLocation = os.path.join(os.path.dirname(__file__), sourceFolder)
        sourceSubFolders = [x[1] for x in os.walk(sourceFolderLocation)][0]
        for i in sourceSubFolders:
            newcount = newcount+1
            if newcount > 99:
                newcount=1
            updatedisplay(newcount)
            for loader, module_name, is_pkg in pkgutil.walk_packages([os.path.join(sourceFolderLocation, i)]):
                if is_pkg:
                    continue
                newcount = newcount+1
                if newcount > 99:
                    newcount=1
                updatedisplay(newcount)
                try:
                    module = loader.find_module(module_name).load_module(module_name)
                    xbmc.log(str(module_name),2)
                    sourceDict.append((module_name, module.source()))
                except: pass
        dp.close()	
        return enabledHosters(sourceDict)
    except:
        return []

def enabledHosters(sourceDict, function=False):
    enabledHosts = [i[0] for i in sourceDict if __addon__.getSetting('provider.' + i[0].split('_')[0]) == 'true']
    returnedHosts = [i for i in sourceDict if i[0] in enabledHosts]
    return returnedHosts

def providerSources():
    sourceSubFolders = [x[1] for x in os.walk(os.path.dirname(__file__))][0]
    return getModuleName(sourceSubFolders)

def providerNames():
    providerList = []
    provider = __addon__.getSetting('module.provider')
    sourceFolder = getScraperFolder(provider)
    sourceFolderLocation = os.path.join(os.path.dirname(__file__), sourceFolder)
    sourceSubFolders = [x[1] for x in os.walk(sourceFolderLocation)][0]
    for i in sourceSubFolders:
        for loader, module_name, is_pkg in pkgutil.walk_packages([os.path.join(sourceFolderLocation, i)]):
            if is_pkg:
                continue
            correctName = module_name.split('_')[0]
            providerList.append(correctName)
            xbmc.log(str(providerList),2)
    return providerList

def getAllHosters():
    def _sources(sourceFolder, appendList):
        sourceFolderLocation = os.path.join(os.path.dirname(__file__), sourceFolder)
        sourceSubFolders = [x[1] for x in os.walk(sourceFolderLocation)][0]
        for i in sourceSubFolders:
            for loader, module_name, is_pkg in pkgutil.walk_packages([os.path.join(sourceFolderLocation, i)]):
                if is_pkg:
                    continue
                try: 
                    mn = str(module_name).split('_')[0]
                except: mn = str(module_name)
                #xbmc.log(mn,2)
                appendList.append(mn)
    sourceSubFolders = [x[1] for x in os.walk(os.path.dirname(__file__))][0]
    appendList = []
    for item in sourceSubFolders:
        if item != 'modules':
            _sources(item, appendList)
    return list(set(appendList))

def getScraperFolder(scraper_source):
    sourceSubFolders = [x[1] for x in os.walk(os.path.dirname(__file__))][0]
    return [i for i in sourceSubFolders if scraper_source.lower() in i.lower()][0]

def getModuleName(scraper_folders):
    nameList = []
    for s in scraper_folders:
        try: nameList.append(s.split('_')[1].lower().title())
        except: pass
    return nameList
