# Image Downloader

This application downloads images from a specified URL range and converts them into a PDF. It is built using Python and Tkinter for the GUI.

To use this code, you should build the executable on your own. (or just use the code piece only)

## Important Note

- Currently only supports image-type pdfs.
- xhtml-type pdfs are not supported.

## How to Build

Follow these steps to build the application into an executable (All codes should run at the project directory):

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
2. Enter the URL, select where to save.
3. Hit the button. Ta-da! It's done!

_Tip: use ALPDF to OCR your pdf_

### How to get the URL

![pic1](https://github.com/user-attachments/assets/ba70ec21-5dc5-465d-9619-d6cc86f7e88d)

1. Open the PDF on browser.

![pic2](https://github.com/user-attachments/assets/4f734a6e-f1a0-47c8-84a3-76f30c53def3) 2. Get the URL by following instructions in picture

## Requirements

- Python 3.x
- `pyinstaller` library
- `requests` library
- `Pillow` library
- `tkinter` library (usually included with Python)
