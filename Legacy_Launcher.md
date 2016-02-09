## Introduction ##
XBMC-Launcher is a plugin that used to launch and run windows or linux applications within the XBMC GUI.

Development for the legacy version of the launcher plugin has been stopped to work on the add-on for the soon to be released XBMC Dharma 10.X.

Latest Version Download:
_http://xbmc-launcher.googlecode.com/files/Launcher1.04.zip_

# Plugin Features #
  * Run an application with arguments.
  * Run a file from directory using given application.
  * Search & Download images for applications and files using Yahoo search engine.
  * Full work with the GUI with. (add application, remove, add files, etc..)


# Installation #

  1. unzip the file into Plugins/Program directory. (in linux is under your ~/.xbmc/)
  1. (linux users only): create a symlink for /usr/lib/libcurl.so.4 named /usr/lib/libcurl.so run the following in terminal: ```
sudo ln -sf /usr/lib/libcurl.so.4 /usr/lib/libcurl.so```
  1. Run XBMC


**If you are using PM3 Skin:**

  1. Switch to MC360 Skin (or some other skin that has "Programs" Section)
  1. Go to Games -> Applications -> Add Source -> Browse -> Program Plugins
  1. Select Launcher and Click "OK"
  1. Click OK Again.
  1. Right Click on "Launcher" Icon
  1. Choose "Add to Favorites"
  1. Switch back to PMIII Skin.
  1. Click on the Arrow in the bottom right corner
  1. Choose "Launcher"


**If you are using PM3.HD Skin:**

  1. update your skin to the latest from svn of xbmc.
  1. go to skin settings
  1. choose "Show Programs in Main Menu"
  1. go back to the main menu and choose "Programs"
  1. Click Add Source -> Browse -> Program Plugins
  1. Select Launcher and Click "OK"

# Known Bugs #

1. Got stuck if no images were found on Yahoo service.

2. (Windows Only) Minimizing and not maximizing back the XBMC after program finished.

3. Need to exit & re-enter directory to see changes (like adding & removing files)


We'll be happy to get feedback about it, you may also open bugs in :

_http://code.google.com/p/xbmc-launcher/issues/list_

Enjoy.
XBMC-Launcher Team