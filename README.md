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
or
```bash
python strong_random_password_generator/main.py
```

### Build a standalone executable

```bash
./build.sh
```

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
├── run.sh
├── README.md
└── .gitignore
```

## License

MIT License
