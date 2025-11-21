# Genshin Impact - Dialogue Auto-Skip

> **⚠️ DISCLAIMER**: Using third-party software with Genshin Impact is against the game's Terms of Service. Use this tool at your own risk. The developers of this script are not responsible for any consequences, including potential account bans.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Controls](#controls)
- [How It Works](#how-it-works)
- [Troubleshooting](#troubleshooting)
- [Gamepad Support](#gamepad-support)
- [Contributing](#contributing)
- [License](#license)

## 🎮 Overview

An automated dialogue skipper for Genshin Impact that intelligently detects and advances through story dialogue. This version uses keyboard and mouse control to simulate the F key press, automatically selecting the bottom dialogue option when choices appear.

The script includes human-like behavior patterns with randomized timing and occasional breaks to appear more natural.

## ✨ Features

- **Automatic Dialogue Detection**: Uses pixel detection to identify when dialogue is active
- **Smart Option Selection**: Automatically chooses the bottom dialogue option
- **Multi-Resolution Support**: Auto-detects and adapts to your screen resolution (HD to 4K+)
- **Human-like Behavior**:
  - Randomized key press intervals (0.12-0.2 seconds)
  - Occasional breaks (3-8 seconds) for natural behavior
  - Intelligent timing variations
- **Easy Controls**: Simple F-key controls for starting, pausing, and stopping
- **Safe Operation**: Only activates when Genshin Impact is the active window
- **Loading Screen Detection**: Prevents actions during loading screens
- **One-Click Setup**: Automated installation script with dependency management

## 📦 Requirements

### System Requirements
- **OS**: Windows (with win32api support)
- **Python**: 3.11 or higher
- **Display**: Primary monitor (multi-monitor setups should have game on primary display)
- **Privileges**: Administrator rights (required for key emulation)

### Software Requirements
- Python 3.11+
- [uv](https://github.com/astral-sh/uv) package manager (auto-installed by run.bat)
- Genshin Impact installed and running

### In-Game Settings
**IMPORTANT**: Navigate to **Settings > Other** and set **Auto-Play Story** to **Off**

## 🚀 Installation

### Option 1: Automated Setup (Recommended)

1. **Download** this repository or clone it:
   ```bash
   git clone https://github.com/1hubert/genshin-dialogue-autoskip.git
   cd genshin-dialogue-autoskip
   ```

2. **Right-click** `run.bat` and select **"Run as administrator"**
   - The script will automatically:
     - Check for Administrator privileges
     - Verify Python installation
     - Install `uv` package manager if needed
     - Install all dependencies
     - Launch the application

### Option 2: Manual Setup

1. **Install Python 3.11+** from [python.org](https://www.python.org/downloads/)
   - ✅ Make sure to check "Add Python to PATH" during installation

2. **Install uv** package manager:
   ```bash
   pip install uv
   ```

3. **Install dependencies**:
   ```bash
   uv sync
   ```

4. **Run the script** with Admin privileges:
   ```bash
   uv run autoskip_dialogue.py
   ```

## 📖 Usage

### Quick Start

1. **Launch Genshin Impact** and ensure it's running on your primary display

2. **Run the script**:
   - Right-click `run.bat` → **"Run as administrator"**, or
   - Run `autoskip_dialogue.py` with admin privileges

3. **Verify Resolution**:
   - On first run, the script will auto-detect your screen resolution
   - Confirm the displayed resolution is correct
   - Resolution is saved to `.env` for future runs

4. **Start Auto-Skip**:
   - Press **F8** to activate auto-skip
   - The script will now automatically advance dialogue when detected

5. **Play the Game**:
   - Continue playing normally
   - Dialogue will be automatically skipped when Genshin Impact is the active window

### Controls

| Key | Action | Description |
|-----|--------|-------------|
| **F8** | Start | Activates auto-skip functionality |
| **F9** | Pause | Temporarily pauses auto-skip |
| **F12** | Exit | Closes the application |

### Status Indicators

The console will display the current status:
- **RUNNING**: Auto-skip is active
- **PAUSED**: Auto-skip is temporarily disabled
- **Taking a break**: Simulating natural pause (3-8 seconds)

## ⚙️ Configuration

### Environment Variables

The script creates a `.env` file to store configuration:

```env
WIDTH=1920
HEIGHT=1080
```

- **WIDTH**: Screen width in pixels (auto-detected)
- **HEIGHT**: Screen height in pixels (auto-detected)

You can manually edit `.env` if the auto-detection is incorrect.

### Supported Resolutions

The script automatically adapts to various resolutions including:
- **1920x1080** (Full HD)
- **2560x1440** (2K)
- **3840x2160** (4K)
- Custom resolutions and ultrawide monitors

## 🔧 How It Works

### Detection System

The script uses pixel-based detection to identify dialogue states:

1. **Autoplay Button Detection**: Monitors a specific pixel for the characteristic color of the autoplay indicator
2. **Dialogue Option Detection**: Checks for the white speech bubble indicator in dialogue options
3. **Loading Screen Protection**: Verifies the game isn't loading before taking action

### Behavior Patterns

To mimic human interaction:

- **Randomized Timing**: Each F key press has a variable interval (0.12-0.2 seconds)
- **Occasional Breaks**: 4% chance every 30 seconds to take a 3-8 second break
- **Window Checking**: Only acts when Genshin Impact is the active window

### Safety Features

- **Admin Check**: Verifies administrator privileges before running
- **Python Check**: Confirms Python installation and version
- **Error Handling**: Gracefully handles errors with informative messages
- **Retry Logic**: Offers retry option if execution fails

## 🐛 Troubleshooting

### Common Issues

#### Script won't start
- **Solution**: Ensure you're running as Administrator
- Right-click `run.bat` → "Run as administrator"

#### "Python is not installed" error
- **Solution**: Install Python 3.11+ from [python.org](https://www.python.org/downloads/)
- Make sure to check "Add Python to PATH" during installation

#### Dialogue not being skipped
- **Verify**:
  - Genshin Impact is the active window
  - Auto-skip is enabled (press F8)
  - In-game "Auto-Play Story" is set to **Off**
  - Game is running on primary monitor

#### Wrong resolution detected
- **Solution**: Manually edit `.env` file with correct dimensions:
  ```env
  WIDTH=your_width
  HEIGHT=your_height
  ```

#### Key presses not working
- **Check**:
  - Script is running with Administrator privileges
  - No other programs are intercepting keyboard input
  - Genshin Impact has focus

### Error Messages

| Error | Meaning | Solution |
|-------|---------|----------|
| "This script requires Administrator privileges" | Not running as admin | Run as administrator |
| "Python is not installed or not in PATH" | Python not found | Install Python and add to PATH |
| "Failed to install uv" | Network or permission issue | Check internet connection, try manual install |
| "Script exited with error code: X" | Runtime error | Check console for details, retry with F8 |

### Getting Help

If you encounter issues:

1. Check the console output for error messages
2. Verify all requirements are met
3. Try running with `--verbose` flag (if available)
4. Open an issue on GitHub with:
   - Error message
   - Python version
   - Screen resolution
   - Windows version

## 🎮 Gamepad Support

This branch (`main`) is optimized for **keyboard and mouse** controls.

If you play Genshin Impact with a **gamepad/controller**, switch to the [gamepad_only](https://github.com/1hubert/genshin-dialogue-autoskip/tree/gamepad_only) branch for gamepad-optimized detection and controls.

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

### Development Setup

1. Fork and clone the repository
2. Install development dependencies:
   ```bash
   uv sync
   ```

3. Run linters and type checkers:
   ```bash
   uvx ruff check .
   uvx ruff format .
   uvx mypy autoskip_dialogue.py
   ```

### Pull Request Guidelines

- Write clear, descriptive commit messages
- Follow the existing code style (enforced by ruff)
- Add type hints for new functions
- Test on multiple resolutions if possible
- Update documentation for new features

## 📄 License

This project is provided as-is for educational purposes.

**Remember**: Using automation tools with Genshin Impact violates the game's Terms of Service and may result in account penalties including permanent bans. Use at your own risk.

---

**Made with ❤️ by the community** | **Not affiliated with HoYoverse/miHoYo**
