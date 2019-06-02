# -*- coding: utf-8 -*-

'''
    License summary below, for more details please read license.txt file

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 2 of the License, or
    (at your option) any later version.
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

from tulip.compat import urlencode
from tulip import control, directory
from tulip.log import log_debug
from resources.lib.modules.tools import stream_picker
from resources.lib import quality
import streamlink.session

# TODO: Add ability to set plugin and session options


def router(url):

    try:

        if '.mpd' in url:
            return url

        custom_plugins = control.join(control.addonPath, 'resources', 'lib', 'resolvers')
        session = streamlink.session.Streamlink()
        session.load_plugins(custom_plugins)
        # session.set_plugin_option('', '', '')

        plugin = session.resolve_url(url)
        # plugin.set_option()
        streams = plugin.streams()

        try:
            json_list = [streams[i].json for i in streams.keys()]
            [log_debug(repr(j)) for j in json_list]
        except Exception:
            pass

        if not streams:
            return url

        try:

            args = streams['best'].args

            append = '|'

            if 'headers' in args:
                headers = streams['best'].args['headers']
                append += urlencode(headers)
            else:
                append = ''

        except AttributeError:

            append = ''

        if quality is None:

            if control.setting('quality.choice') == '0':

                playable = streams['best'].to_url() + append

                return playable

            else:

                keys = streams.keys()[::-1]
                values = [u.to_url() + append for u in streams.values()][::-1]

                return stream_picker(keys, values)

        else:

            if quality == 'manual':

                keys = streams.keys()[::-1]
                values = [u.to_url() + append for u in streams.values()][::-1]

                return stream_picker(keys, values)

            else:

                try:

                    return streams[quality].to_url() + append

                except KeyError:

                    return streams['best'].to_url() + append

    except streamlink.session.NoPluginError:

        return url

    except streamlink.session.PluginError as e:

        control.infoDialog(e, time=5000)


def play(url):
    name = "TEST"
    stream = router(url)

    dash = ('.mpd' in stream or 'dash' in stream or '.ism' in stream or '.hls' in stream)

    if dash:

        if '.hls' in stream:
            manifest_type = 'hls'
        elif '.ism' in stream:
            manifest_type = 'ism'
        else:
            manifest_type = 'mpd'

        log_debug('Activating MPEG-DASH for this url: ' + stream)

    else:
        manifest_type = ''

    try:

        if '.mpd' in stream:

            directory.resolve(stream, dash=dash, manifest_type=manifest_type)

        else:

            directory.resolve(stream)

    except:

        pass
