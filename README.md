# genshin-dialogue-autoskip (Keyboard and Mouse Only Version)

## Overview
This script automatically skips dialogue in Genshin Impact, always chooses the bottom dialogue option.

*Using third-party software is against the game's ToS. Use at your own discretion.*

## Requirements
- The game running on the primary display
- The script run as Admin to allow key and mouse emulation
- Required Python packages installed with `pip install -r requirements.txt`
- In the game's settings, navigate to **Settings > Other** and set **Auto-Play Story** to **Off**.

## Usage
1. Run `autoskip_dialogue.py` with Admin privileges
	-  Tip: You can right-click the handy `run.bat` file and select "Run as administrator"
2. Confirm that the auto-detected resolution matches your screen dimensions (it will be saved in `.env`)
3. When you're ready, press F8 on your keyboard to start the main loop!

## Experimental Gamepad Support
- The `main` branch of this repo which you're currently on, is for keyboard+mouse only. If you're using a gamepad to play the game, switch to the [gamepad_only](https://github.com/1hubert/genshin-dialogue-autoskip/tree/gamepad_only) branch!
