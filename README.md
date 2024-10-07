# Image Downloader

This application downloads images from a specified URL range and converts them into a PDF. It is built using Python and Tkinter for the GUI.

## How to Build

Follow these steps to build the application into an executable:

1. Install the required libraries:

   ```sh
   pip install -r requirements.txt
   ```

2. Use `pyinstaller` to create the executable:

   ```sh
   pyinstaller -w -F main.py
   ```

3. The resulting executable will be located at `dist/main.exe`.

## Usage

1. Run the executable `main.exe`.
2. Enter the URL, start page, end page, and optional filename.
3. Click the "Download" button to start downloading images and converting them into a PDF.
4. If the URL format is incorrect, an error message will be displayed and the application will quit.

## Requirements

- Python 3.x
- `pyinstaller` library
- `requests` library
- `Pillow` library
- `tkinter` library (usually included with Python)

## Installation of Requirements

Before building the executable, ensure you have the required libraries installed:

```sh
pip install -r requirements.txt
```
