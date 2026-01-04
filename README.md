# genshin-dialogue-autoskip (GamePad Support version)

## Overview
This script automatically skips dialogue in Genshin Impact, always chooses the bottom dialogue option.

*Using third-party software is against the game's ToS. Use at your own discretion.*

## Requirements
- The game running on the primary display
- Required Python packages installed with `install.bat`

## Usage
1. Run `run.bat`
2. Confirm that the auto-detected resolution matches your screen dimensions (it will be saved in `.env`)
3. When you're ready, press F8 on your keyboard to start the main loop!
4. Enable autoplay in dialogs with X on your gamepad.

## DualShock 4 Support
- The script automatically defines the UI version, currently autodetects ENG/RUS keyboard+mouse UI and ENG/RUS DualShock 4 gamepad UI
- To use with DS4 gamepad, the autoplay button must be activated using the square button

## Xbox Gamepads Support
- The script works in the same way as with DS4
- To use with Xbox Gamepad, the autoplay button must be activated using the "X" button
- Whether you are using B or A as the confirm button, you can change it in the .env file or at first startup