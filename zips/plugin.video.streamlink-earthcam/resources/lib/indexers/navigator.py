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

from tulip import directory, control
from resources.lib.modules import tools


def root():

    null = [
        {
            'title': control.lang(30009),
            'action': 'add'
        }
    ]

    urls = tools.read_from_history()

    if not urls:
        directory.add(null)
    else:
        menu = [{'title': url.split("earthcam.com")[1].replace("/", " ").replace("?cam=", " ").replace("_", " "), 'action': 'play', 'isFolder': 'False', 'url': url} for url in urls]
        for m in menu:
            add_cm = {'title': 30009, 'query': {'action': 'add'}}
            refresh_cm = {'title': 30005, 'query': {'action': 'refresh'}}
            clear_cm = {'title': 30010, 'query': {'action': 'clear_history'}}
            clear_fm_h_cm = {'title': 30013, 'query': {'action': 'delete_from_history', 'query': m['url']}}
            m.update({'cm': [add_cm, refresh_cm, clear_cm, clear_fm_h_cm]})
 
        directory.add(menu)
