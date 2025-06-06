# Strong Random Password Generator

A cross-platform desktop application for generating strong, customizable random passwords.

## Features

- Graphical user interface (Tkinter)
- Customizable password length
- Option to include/exclude:
  - Uppercase letters (A-Z)
  - Lowercase letters (a-z)
  - Digits (0-9)
  - Symbols (customizable set)
  - Similar characters (il1Lo0O)
  - Duplicate characters
- Add a custom word or prefix to the password
- Copy generated password to clipboard with one click
- Modular, testable password generation logic

## Usage

### Run the application

```bash
./run.sh
```
or on Windows:
```bat
run.bat
```
or:
```bash
python strong_random_password_generator/main.py
```

### Build a standalone executable

```bash
./build.sh
```
or on Windows:
```bat
build.bat
```

You can also build executables automatically for Windows, macOS, and Linux using [GitHub Actions](.github/workflows/build.yml).

**Download the executables:**  
After the GitHub Action completes, go to the "Actions" tab on GitHub, select the workflow run, and download the executables from the "Artifacts" section at the bottom of the run summary page.

## Requirements

- Python 3.x
- Tkinter (usually included with Python)
- [PyInstaller](https://pyinstaller.org/) (for building executables)

## Testing

Run all unit tests with:

```bash
python -m unittest discover -s tests
```

## Project Structure

```
strong_random_password_generator/
├── strong_random_password_generator/
│   ├── __init__.py
│   ├── main.py
│   └── password_generator.py
├── tests/
│   ├── __init__.py
│   └── test_password_generator.py
├── build.sh
├── build.bat
├── run.sh
├── run.bat
├── requirements.txt
├── strong_random_password_generator.icns
├── strong_random_password_generator.ico
├── README.md
└── .gitignore
```

## License

GNU General Public License v3.0 (GPLv3)

## FAQ

### macOS: How to open the app if you get a security warning

If you try to open the app on macOS and see a message like  
*"Apple cannot verify that this app is free from malware"*  
and you do **not** see the "Open Anyway" option:

1. Open the **Terminal**.
2. Run the following command (replace the name if needed):
   ```bash
   xattr -d com.apple.quarantine "Strong Random Password Generator.app"
   ```
3. Try opening the app again.

This removes the quarantine attribute that macOS applies to files downloaded from the Internet.
