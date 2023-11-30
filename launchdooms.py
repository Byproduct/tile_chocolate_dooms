# Launch and tile chocolate dooms!
# Works in windows 10, unsure about other OSes.
# After launching, use closedooms.py to close windows.

# Get chocolate doom: https://www.chocolate-doom.org/wiki/index.php/Downloads
# Put a doom .WAD file and this script in the same folder as chocolate doom
# Open chocolate-doom.cfg in a text editor and set the following:
# fullscreen                    0
# window_width                  320
# window_height                 200
# force_software_renderer       1     (unless you want to stress GPU)
# other values can remain default


window_title = "The Ultimate DOOM - Chocolate Doom 3.0.1"   # Set according to your actual Doom window title - depends on your WAD and Chocolate Doom version
screen_width = 3440                # set according to your monitor resolution
screen_height = 1440
time_between_instances = 0.01      # time to wait (s) between launching instances. Increase this value if you get errors or if all your windows aren't launching.
time_before_arranging = 5          # time to wait (s) after launching and before arranging windows (they need some time to open)







import subprocess
import pygetwindow as gw
import time

doom_executable = 'chocolate-doom.exe'
doom_width = 320
doom_height = 200

def arrange_windows(title, width, height, horizontal_instances, vertical_instances):
    windows = gw.getWindowsWithTitle(title)
    windows = list(reversed(windows))
    for i, window in enumerate(windows):
        if i >= horizontal_instances * vertical_instances:
            break
        x = (i % horizontal_instances) * width
        y = (i // horizontal_instances) * height
        window.moveTo(x, y)
        window.resizeTo(width, height)

horizontal_instances = screen_width // doom_width
vertical_instances = screen_height // doom_height

for _ in range(horizontal_instances * vertical_instances):
    subprocess.Popen([doom_executable])
    time.sleep(time_between_instances)

time.sleep(time_before_arranging)
arrange_windows(window_title, doom_width, doom_height, horizontal_instances, vertical_instances)
