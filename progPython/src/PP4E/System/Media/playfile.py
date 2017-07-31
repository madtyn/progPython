#!/usr/bin/python3
"""
##################################################################################
Try to play an arbitrary media file.  Allows for specific players instead of
always using general web browser scheme.  May not work on your system as is;
audio files use filters and command lines on Unix, and filename associations
on Windows via the start command (i.e., whatever you have on your machine to
run .au files--an audio player, or perhaps a web browser).  Configure and
extend as needed.  playknownfile assumes you know what sort of media you wish
to open, and playfile tries to determine media type automatically using Python
mimetypes module; both try to launch a web browser with Python webbrowser module
as a last resort when mimetype or platform unknown.
##################################################################################
"""

import os
import sys
import mimetypes
import webbrowser
from abc import abstractmethod, ABC

HELPMSG = """
Sorry: can't find a media player for '%s' on your system!
Add an entry for your system to the media player dictionary
for this type of file in playfile.py, or play the file manually.
"""


def trace(*args):
    '''
    Traces the task by printing the args on the screen
    '''
    print(*args)  # with spaces between

##################################################################################
# player techniques: generic and otherwise: extend me
##################################################################################


class MediaTool(ABC):
    '''
    Abstract parent class for interacting with media files
    '''
    def __init__(self, runtext=''):
        self.runtext = runtext

    def run(self, mediafile, **options):  # most ignore options
        '''
        Runs the player for this mediafile
        :param mediafile: the media file to play
        '''
        fullpath = os.path.abspath(mediafile)  # cwd may be anything
        self.open(fullpath, **options)

    @abstractmethod
    def open(self, mediafile, **ignored):
        '''
        Opens the mediafile
        :param mediafile: the file with the media to play
        '''
        pass


class Filter(MediaTool):
    '''
    MediaTool used when we need to send the mediafile via
    its standard input
    '''
    def open(self, mediafile, **ignored):
        media = open(mediafile, 'rb')
        player = os.popen(self.runtext, 'w')  # spawn shell tool
        player.write(media.read())  # send to its stdin


class Cmdline(MediaTool):
    '''
    MediaTool which runs command-line programs for opening
    media files
    '''
    def open(self, mediafile, **ignored):
        cmdline = self.runtext % mediafile  # run any cmd line
        os.system(cmdline)  # use %s for filename


class Winstart(MediaTool):  # use Windows registry
    '''
    MediaTool for Windows
    '''
    def open(self, mediafile, wait=False, **other):  # or os.system('start file')
        if wait:  # allow wait for curr media
            os.system('start /WAIT ' + mediafile)
        else:
            os.startfile(mediafile)  # @UndefinedVariable pylint: disable=no-member


class Webbrowser(MediaTool):
    '''
    MediaTool for web browser related files
    '''
    # file:// requires abs path
    def open(self, mediafile, **options):
        webbrowser.open_new('file://%s' % mediafile, **options)

##################################################################################
# media- and platform-specific policies: change me, or pass one in
##################################################################################

# map platform to player: change me!


audiotools = {
    'sunos5': Filter('/usr/bin/audioplay'),  # os.popen().write()
    'linux2': Cmdline('cat %s > /dev/audio'),  # on zaurus, at least
    'sunos4': Filter('/usr/demo/SOUND/play'),  # yes, this is that old!
    'win32': Winstart()  # startfile or system
    # 'win32':   Cmdline('start %s')
}

videotools = {
    'linux2': Cmdline('tkcVideo_c700 %s'),  # zaurus pda
    'win32': Winstart(),  # avoid DOS pop up
}

imagetools = {
    'linux2': Cmdline('zimager %s'),  # zaurus pda
    'win32': Winstart(),
}

texttools = {
    'linux2': Cmdline('vi %s'),  # zaurus pda
    'win32': Cmdline('notepad %s')  # or try PyEdit?
}

apptools = {
    'win32': Winstart()  # doc, xls, etc: use at your own risk!
}

# map mimetype of filenames to player tables

mimetable = {'audio': audiotools,
             'video': videotools,
             'image': imagetools,
             'text': texttools,  # not html text: browser
             'application': apptools}

##################################################################################
# top-level interfaces
##################################################################################


def trywebbrowser(filename, helpmsg=HELPMSG, **options):
    """
    try to open a file in a web browser
    last resort if unknown mimetype or platform, and for text/html
    """
    trace('trying browser', filename)
    try:
        player = Webbrowser()  # open in local browser
        player.run(filename, **options)
    except:
        print(helpmsg % filename)  # else nothing worked


def playknownfile(filename, playertable=None, **options):
    """
    play media file of known type: uses platform-specific
    player objects, or spawns a web browser if nothing for
    this platform; accepts a media-specific player table
    """
    if not playertable:
        playertable = {}
    if sys.platform in playertable:
        playertable[sys.platform].run(filename, **options)  # specific tool
    else:
        trywebbrowser(filename, **options)  # general scheme


def playfile(filename, mimetable=mimetable, **options):
    """
    play media file of any type: uses mimetypes to guess media
    type and map to platform-specific player tables; spawn web
    browser if text/html, media type unknown, or has no table
    """
    contenttype, encoding = mimetypes.guess_type(filename)  # check name
    if contenttype is None or encoding is not None:  # can't guess
        contenttype = '?/?'  # poss .txt.gz
    maintype, subtype = contenttype.split('/', 1)  # 'image/jpeg'
    if maintype == 'text' and subtype == 'html':
        trywebbrowser(filename, **options)  # special case
    elif maintype in mimetable:
        playknownfile(filename, mimetable[maintype], **options)  # try table
    else:
        trywebbrowser(filename, **options)  # other types

###############################################################################
# self-test code
###############################################################################


if __name__ == '__main__':
    # media type known
    playknownfile('sousa.au', audiotools, wait=True)
    playknownfile('ora-pp3e.gif', imagetools, wait=True)
    playknownfile('ora-lp4e.jpg', imagetools)

    # media type guessed
    input('Stop players and press Enter')
    playfile('ora-lp4e.jpg')  # image/jpeg
    playfile('ora-pp3e.gif')  # image/gif
    playfile('priorcalendar.html')  # text/html
    playfile('lp4e-preface-preview.html')  # text/html
    playfile('lp-code-readme.txt')  # text/plain
    playfile('spam.doc')  # app
    playfile('spreadsheet.xls')  # app
    playfile('sousa.au', wait=True)  # audio/basic
    input('Done')  # stay open if clicked
