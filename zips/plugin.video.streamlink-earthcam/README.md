![alt text](https://raw.githubusercontent.com/Twilight0/plugin.video.streamlink-tester/master/icon.png "Woof woof!")
# Streamlink Tester

The purpose of this addon is to test links supported by streamlink resolver library.
- It does not provide any content on its own.

### You can install it from [repository.twilight0](https://github.com/Twilight0/repo.twilight0)

## Features:

- Add a url menu item appears when no cached url are present. Use context menu to add additional urls
- Keeps history of added urls (limited by a setting)
- Can have manual quality selection or "best" (overrides selected option in settings)
- Can play arbitrary links via plugin route call
- Can play MPEG-DASH streams as well (Krypton+ only and inputstream.adaptive is enabled)

## Plugin route playback

You can arbitrarily play any url with the following sample snippet:

    import xbmc
    
    try:
        from urllib import quote
    except ImportError:
        from urllib.parse import quote
    
    web_url = 'https://www.youtube.com/watch?v=XIMLoLxmTDw'
    title = 'Black Screen'
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.streamlink-tester/?action=play&url={0}&title={1}")'.format(quote(web_url), quote(title)))

Or even feed it into xbmc.Player()

    xbmc.Player().play('plugin://plugin.video.streamlink-tester/?action=play&url={0}'.format(web_url))

You can also set it as resolved url:

    xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, listitem)

To trigger manual quality selection via the route call, add `&quality=manual` into the url, example:

    plugin://plugin.video.streamlink-tester/?action=play&url={0}&quality={1}'.format(web_url, 'manual')

You can add any quality instead of manual for example best, worst, 360p etc (if option is not present, it will fall back to best)
