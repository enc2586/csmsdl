import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import requests
import time
import os
import re

EXTENSION = "png"
REGEX = r"https://doc\.coursemos\.co\.kr/.+\.files"


def download_image(url, progress_label, keep_images=True, filename=None):
    try:
        if not re.match(REGEX, url):
            print("URL is not valid")
            progress_label.config(text="URL is not valid")
            return False
    except Exception as e:
        progress_label.config(text="An unexpected error occurred.")
        messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")
        return False

    BASE_URL = re.match(REGEX, url).group(0) + "/"
    IMAGE_DIR = "images" if not filename else filename.split(".")[0]

    if not os.path.exists(IMAGE_DIR):
        os.makedirs(IMAGE_DIR)

    file_length = 1
    while True:
        progress_label.config(text=f"Downloading page #{file_length}")
        print(f"Downloading {file_length}.{EXTENSION}", end="... ")
        image_url = f"{BASE_URL}{file_length}.{EXTENSION}"
        response = requests.get(image_url)

        if response.status_code == 200:
            with open(f"{IMAGE_DIR}/{file_length}.{EXTENSION}", "wb") as file:
                file.write(response.content)

            file_length += 1
            print("SUCCESS")
            root.update_idletasks()
        else:
            print("FAIL")
            file_length -= 1
            progress_label.config(text="PROCESSING... won't take long.")
            break

    if file_length == 0:
        progress_label.config(text="No images found to download.")
        return False

    progress_label.config(text="Converting images to PDF...")
    images = [
        Image.open(f"{IMAGE_DIR}/{i}.{EXTENSION}") for i in range(1, file_length + 1)
    ]

    pdf_path = (
        filename.split(".")[0] if filename else time.strftime("%Y%m%d_%H%M%S")
    ) + ".pdf"

    images[0].save(
        pdf_path, "PDF", resolution=100.0, save_all=True, append_images=images[1:]
    )

    progress_label.config(text="PDF created successfully.")
    root.update_idletasks()

    if not keep_images:
        progress_label.config(text="Cleaning up downloaded images...")
        if os.path.exists(IMAGE_DIR):
            for file in os.listdir(IMAGE_DIR):
                os.remove(f"{IMAGE_DIR}/{file}")
            os.rmdir(IMAGE_DIR)

    progress_label.config(text="Process completed.")
    return True


def start_download():
    url = url_entry.get().strip()
    filename = filedialog.asksaveasfilename(
        defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")]
    )
    if not filename:
        return

    keep_images = keep_var.get()

    progress_label.config(text="Starting download...")
    root.update_idletasks()

    try:
        success = download_image(url, progress_label, keep_images, filename)
        if success:
            messagebox.showinfo("Success", "Download and PDF creation successful!")
        else:
            messagebox.showerror(
                "Error", "Failed to download images. Please check the URL."
            )
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")


# Instructions for users
# Please enter the full URL in the field provided above.
# Make sure the URL is in the format: https://doc.coursemos.co.kr/.../.files
# Select whether you want to keep the downloaded images after creating the PDF.
# Click 'Download and Create PDF' to start the process.

# Set up the GUI window
root = tk.Tk()
root.title("Image Downloader and PDF Creator")
root.geometry("500x300")

# Instructions label
instructions_label = tk.Label(
    root,
    text="""
Instructions:
1. Open the PDF page in COURSEMOS and Press F12 to open DevTools.
2. Select 'Network' Tab from Devtools and refresh the PDF page.
3. Look for number image labels like 1.png, 13.png, etc.
4. Copy the whole 'Request URL' and paste it.
""",
    justify="left",
)
instructions_label.pack(padx=10, anchor="w")

# URL input
url_label = tk.Label(root, text="Enter URL:")
url_label.pack(pady=5)
url_entry = tk.Entry(root, width=60, fg="grey")

# Bind Enter key to start_download
url_entry.bind("<Return>", lambda event: start_download())


# Placeholder functionality
def on_entry_click(event):
    if url_entry.get() == "https://doc.coursemos.co.kr/.../1.png":
        url_entry.delete(0, "end")
        url_entry.insert(0, "")
        url_entry.config(fg="black")


def on_focusout(event):
    if url_entry.get() == "":
        url_entry.insert(0, "https://doc.coursemos.co.kr/.../1.png")
        url_entry.config(fg="grey")


url_entry.insert(0, "https://doc.coursemos.co.kr/.../1.png")
url_entry.bind("<FocusIn>", on_entry_click)
url_entry.bind("<FocusOut>", on_focusout)
url_entry.pack(pady=5)

# Keep images checkbox
keep_var = tk.BooleanVar()
keep_images_check = tk.Checkbutton(
    root, text="Keep downloaded images", variable=keep_var
)
keep_images_check.pack()

# Progress label
progress_label = tk.Label(root, text="")
progress_label.pack(pady=5, padx=10, anchor="w")

# Download button
download_button = tk.Button(
    root, text="Download and Create PDF", command=start_download
)
download_button.pack(pady=5)

# Start the GUI event loop
root.mainloop()
