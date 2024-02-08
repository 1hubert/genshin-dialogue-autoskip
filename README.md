# genshin-dialogue-autoskip (Experimental GamePad Support version)

## Overview
This script automatically skips dialogue in Genshin Impact, always chooses the bottom dialogue option.

*Using third-party software is against the game's ToS. Use at your own discretion.*

## Requirements
- The game running on the primary display
- The script run as Admin to allow key and mouse emulation
- Required Python packages installed with `pip install -r requirements.txt`

## Usage
1. Run `autoskip_dialogue.py` with Admin privileges
	-  Tip: You can right-click the handy `run.bat` file and select "Run as administrator"
2. Confirm that the auto-detected resolution matches your screen dimensions (it will be saved in `.env`)
3. When you're ready, press F8 on your keyboard to start the main loop!

## DualShock 4 Support
- The script automatically defines the UI version, currently autodetects ENG/RUS keyboard+mouse UI and ENG/RUS DualShock 4 gamepad UI
- To use with DS4 gamepad, the autoplay button must be activated using the square button

## Xbox Gamepads Support
- The script works in the same way as with DS4
- To use with Xbox Gamepad, the autoplay button must be activated using the "X" button
