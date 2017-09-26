#!/usr/bin/env python3
'''  #pylint: disable=anomalous-backslash-in-string
#############################################################################
#
# AN EX-MODULE!
# Now just a simple wrapper for the newer webrowser in standard library.
#
# C:\...\PP4E> LaunchBrowser.pyw -live index.html learning-python.com
# Opening http://www.python.org/index.html
#
# C:\...\PP4E> LaunchBrowser.pyw -file
# Opening file://C:\...\PP4E/Internet/Web/
# PyInternetDemos.html
#
# Launch a web browser to view a web page, portably.  If run in '-live'
# mode, assumes you have an Internet feed and opens page at a remote site.
# Otherwise, assumes the page is a full file pathname on your machine,
# and opens the page file locally.
#############################################################################
'''

import sys
import os
import webbrowser


def launchBrowser(mode='-file', page='index.html', site=None, verbose=True):
    '''
    Launchs the browser opening the web page in the desired mode
    :param mode: '-file' or '-live'
    :param page: the string with the web page
    :param site: the site where the page is allocated
    :param verbose: only if True additional info will be printed
    '''
    if mode == '-live':
        url = 'http://%s/%s' % (site, page)  # open page at remote site
    else:
        url = 'file://%s' % page  # open page on this machine
    if verbose:
        print('Opening', url)
    webbrowser.open(url)


if __name__ == '__main__':
    # defaults
    MODE = '-file'
    PAGE = os.getcwd() + '/Internet/Web/PyInternetDemos.html'
    SITE = 'learning-python.com'

    # get command-line args
    HELPTEXT = "Usage: LaunchBrowser.py [ -file path | -live path site ]"
    ARGC = len(sys.argv)
    if ARGC > 1:
        MODE = sys.argv[1]
    if ARGC > 2:
        PAGE = sys.argv[2]
    if ARGC > 3:
        SITE = sys.argv[3]
    if MODE not in ['-live', '-file']:
        print(HELPTEXT)
        sys.exit(1)
    else:
        launchBrowser(MODE, PAGE, SITE)


"""
===================================================================================
ORIGINAL DEFUNCT/DEPRECATED CODE

# On Unix/Linux, finds first browser
# on your $PATH.  On Windows, tries DOS "start" command first, or searches
# for the location of a browser on your machine for os.spawnv by checking
# PATH and common Windows executable directories. You may need to tweak
# browser executable name/dirs if this fails. This has only been tested in
# Windows and Linux; you may need to add more code for other machines (mac:
# ic.launcurl(url)?). See also the new standard library webbrowser module.

import os
import sys
from Launcher import which, guessLocation     # file search utilities
useWinStart = False                           # 0=ignore name associations
onWindows   = sys.platform[:3] == 'win'

def launchUnixBrowser(url, verbose=True):         # add your platform if unique
    tries = ['netscape', 'mosaic', 'lynx']        # order your preferences here
    tries = ['firefox'] + tries                   # Firefox rules!
    for program in tries:
        if which(program):
            break                  # find one that is on $path
    else:
        assert 0, 'Sorry - no browser found'
    if verbose:
        print('Running', program)
    os.system('%s %s &' % (program, url))         # or fork+exec; assumes $path

def launchWindowsBrowser(url, verbose=True):
    if useWinStart and len(url) <= 400:           # on Windows: start or spawnv
        try:                                      # spawnv works if cmd too long
            if verbose:
                print('Starting')
            os.system('start ' + url)             # try name associations first
            return                                # fails if cmdline too long
        except:
            pass
    browser = None                                # search for a browser exe
    tries   = ['IEXPLORE.EXE', 'netscape.exe']    # try Explorer, then Netscape
    tries   = ['firefox.exe'] + tries
    for program in tries:
        browser = which(program) or guessLocation(program, 1)
        if browser: break
    assert browser != None, 'Sorry - no browser found'
    if verbose:
        print('Spawning', browser)
    os.spawnv(os.P_DETACH, browser, (program, url))


def launchBrowser(mode='-file', page='index.html', site=None, verbose=True):
    if mode == '-live':
        url = 'http://%s/%s' % (site, page)       # open page at remote site
    else:
        url = 'file://%s' % page                  # open page on this machine
    if verbose: print('Opening', url)
    if onWindows:
        launchWindowsBrowser(url, verbose)        # use windows start, spawnv
    else:
        launchUnixBrowser(url, verbose)           # assume $path on Unix, Linux
===================================================================================
"""
