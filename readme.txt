This program automatically does 1-wishes

The program requires the following:

The game running on Main Display 1 on fullscreen 1920x1080 resolution
The character exploring the main world, with no menus open
Run in Admin mode to allow key and mouse emulation
The code does the following:

creates an openCV window for debugging what the program is doing
Runs the following while True loop:
Emulates F3
Clicks on wish located @ (1378, 1014)
Scans the screen for orange, then purple
if a non-blue wish, increments its respective value
closes out of the item menu.
On Ctrl + C, shows final stats then exits.