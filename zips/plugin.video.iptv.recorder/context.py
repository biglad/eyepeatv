import urllib

import xbmc
import xbmcgui


def log(x):
    xbmc.log(repr(x), xbmc.LOGERROR)


channel = xbmc.getInfoLabel('ListItem.Label')
channel = channel.decode("utf8")
channel = channel.encode("utf8")
channel = urllib.quote_plus(channel)

try:

    d = xbmcgui.Dialog()
    select = d.select("IPTV Recorder", ["Record and Play",
                                        "Add Timed Recording",
                                        "Add Daily Timed Recording",
                                        "Add Weekly Timed Recording"])

    if select != -1:
        if select == 3:
            cmd = "ActivateWindow(videos,plugin://plugin.video.iptv.recorder/record_one_time/%s,return)" % (channel)
            result = xbmc.executebuiltin(cmd)
        elif select == 1:
            cmd = "ActivateWindow(videos,plugin://plugin.video.iptv.recorder/record_daily_time/%s,return)" % (channel)
            result = xbmc.executebuiltin(cmd)
        elif select == 2:
            cmd = "ActivateWindow(videos,plugin://plugin.video.iptv.recorder/record_weekly_time/%s,return)" % (channel)
            result = xbmc.executebuiltin(cmd)
        elif select == 0:
            cmd = "ActivateWindow(videos,plugin://plugin.video.iptv.recorder/record_and_play/%s,return)" % (channel)
            result = xbmc.executebuiltin(cmd)

except:
    xbmcgui.Dialog().notification("IPTV Recorder", "channel not found", xbmcgui.NOTIFICATION_WARNING)
