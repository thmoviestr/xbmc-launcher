# Introduction #

One method of adding roms to launcher
If you have every nes game ever made do not want to clutter up your list of games or waste harddrive space you can create symbolic links to the games.

Here is an example:


make a directory in the home folder called roms/nes/
```

$ mkdir -p ~/roms/nes
```
create a symbolic link from the source to our new folder.
```

$ ln -s /media/backend-sever/games/emulators/nes/nesren/Duck\ Hunt\ \(JUE\).zip ~/roms/nes
```
when you set up Launcher make the import directory ~/roms/nes aka "Home folder" --> roms --> nes.

You can add more later and then import from path again.

# Adding a Windows Manager for XBMC-Live #

This method works for me but I don't guaranty anything so don't come crying to me if you break your system(shouldn't happen).

For Emulators that use a GUI you will need a windows manager installed and running. It will slightly increase your memory footprint but if you're running emulators you probably have room to spare.
```

sudo apt-get install xfwm4
```
now to get it to run when X starts. This is a dirty hack but hey, it works. (you will need to do this part again if you update XBMC)
```

sudo nano /usr/bin/runXBMC
```

add
```

echo "/usr/bin/xfwm4&" >>  /home/$xbmcUser/.xsession
```
just above
```

echo "/usr/bin/xbmc --standalone " >>  /home/$xbmcUser/.xsession
```
restart XBMC-Live

# Font is too small in Emulator's Gui #
edit /etc/X11/xorg.conf
under
```

Section "Monitor"
```
add
```

Option         "DPI" "100x100"
```
DPI=Dots Per Inch so bigger number = bigger looking font. This doesn't effect XBMC that I have noticed. You can tweak those number to what works best for your television.
You must restart XBMC after you make those changes.