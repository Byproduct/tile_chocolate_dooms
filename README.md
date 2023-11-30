# Tiled Chocolate Dooms

This is a Python script to launch a screen full of tiled Chocolate Doom instances.

Inspired by Dave's Garage trying 100 copies of Doom on a 96-core, 192-thread processor ([Youtube](https://www.youtube.com/watch?v=Ybw6djC90tw)).

Dave used Chrome windows - but with Chocolate Doom it's much lighter on the CPU, so you can try too!

This script is made for Windows 10, I haven't tested it on other OSes.

Instructions:

Get chocolate doom: https://www.chocolate-doom.org/wiki/index.php/Downloads  
Put a doom .WAD file and this script in the same folder as Chocolate Doom  
Open chocolate-doom.cfg in a text editor and set the following:

fullscreen                    0  
window_width                  320  
window_height                 200  
force_software_renderer       1     (unless you want to stress GPU)  
other values can remain default

Open launchdooms.py in a text editor and check the configuration at the top

After launching, use closedooms.py to close all windows.
