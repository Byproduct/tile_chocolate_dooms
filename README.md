# Tile Chocolate Dooms

Python script to launch a screen full of Chocolate Doom windows.
Inspired by Dave's Garage trying 100 copies of Doom on a 96-core, 192-thread processor: https://www.youtube.com/watch?v=Ybw6djC90tw
Dave used Chrome windows - but with Chocolate Doom it's much lighter on the CPU.

Made for Windows 10, haven't tested other OSes.

Get chocolate doom: https://www.chocolate-doom.org/wiki/index.php/Downloads

Put a doom .WAD file and this script in the same folder as chocolate doom

Open chocolate-doom.cfg in a text editor and set the following:
fullscreen                    0
window_width                  320
window_height                 200
force_software_renderer       1     (unless you want to stress GPU)
other values can remain default

After launching, use closedooms.py to close all windows.
