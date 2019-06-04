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

from tulip import control


history_size = int(control.setting('history.size'))
history_file = control.join(control.dataPath, 'urls.lst')


def stream_picker(qualities, urls):

    choice = control.selectDialog(heading=control.lang(30006), list=qualities)

    if choice <= len(qualities) and not choice == -1:
        popped = urls[choice]
        return popped
    else:
        return


def trim_history(file_=history_file):

    """
    Trims history to what is set in settings
    """

    f = open(file_, 'r')
    text = [i.rstrip('\n') for i in f.readlines()]
    f.close()

    if len(text) > history_size:
        f = open(file_, 'w')
        dif = history_size - len(text)
        result = text[:dif]
        f.write('\n'.join(result))
        f.close()


def add_to_history(file_=history_file):

    if not control.exists(file_):
        control.makeFiles(control.dataPath)

    txt = control.dialog.input(control.name())

    if not txt:
        return

    if txt not in read_from_history():

        with open(file_, 'a') as f:
            f.writelines(txt + '\n')

        trim_history(file_)
        refresh()


def read_from_history(file_=history_file):

    """
    Reads from history file which is stored in plain text, line by line
    :return: List
    """

    if control.exists(file_):

        with open(file_, 'r') as f:
            text = [i.rstrip('\n') for i in f.readlines()][::-1]

        return text

    else:

        return ''


def delete_from_history(txt, file_=history_file):

    with open(file_, 'r') as f:
        text = [i.rstrip('\n') for i in f.readlines()]

    text.remove(txt)

    with open(file_, 'w') as f:
        f.write('\n'.join(text) + '\n')

    refresh()


def clear_history(file_=history_file):

    if control.exists(file_):

        with open(file_, 'w') as f:
            f.write('')

    control.infoDialog(control.lang(30011))
    refresh()


def readme():

    text = control.addonInfo('disclaimer')

    control.dialog.textviewer(control.name(), text=text)


def refresh():

    control.refresh()
