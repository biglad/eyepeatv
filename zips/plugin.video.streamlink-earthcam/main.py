# -*- coding: utf-8 -*-

'''
    Streamlink Tester, author Twilight0
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

from resources.lib import action, url, query


if action is None:
    from resources.lib.indexers import navigator
    navigator.root()

elif action == 'play':
    from resources.lib.modules import player
    player.play(url)

elif action == 'add':
    from resources.lib.modules import tools
    tools.add_to_history()

elif action == 'readme':
    from resources.lib.modules import tools
    tools.readme()

elif action == 'refresh':
    from resources.lib.modules import tools
    tools.refresh()

elif action == 'clear_history':
    from resources.lib.modules import tools
    tools.clear_history()

elif action == 'delete_from_history':
    from resources.lib.modules import tools
    tools.delete_from_history(query)
