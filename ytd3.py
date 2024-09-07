import tkinter as tk
from tkinter import messagebox, filedialog
import ttkbootstrap as ttk
import yt_dlp
import threading
import time

# Global variable to store the available formats
available_formats = []
is_downloading = False  # To track if download is in progress

# Function to fetch available formats using yt-dlp
def fetch_formats():
    url = url_entry.get()

    if not url:
        messagebox.showerror("Input Error", "Please provide a YouTube video URL.")
        return

    try:
        ydl_opts = {'quiet': True}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=False)
            formats = info_dict.get('formats', [])

            # Clear the combobox and available_formats
            quality_combobox['values'] = []
            available_formats.clear()

            # Populate available formats list
            for f in formats:
                # Use format_note if available, otherwise use format_id
                quality = f.get('format_note', f.get('format_id')) + f" - {f['ext']}"

                # Add file size if available
                if f.get('filesize'):
                    quality += f" - {f['filesize'] / 1_000_000:.2f} MB"
                    
                available_formats.append(f)
                quality_combobox['values'] = (*quality_combobox['values'], quality)
            
            quality_combobox.current(0)  # Set the default selection

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Function to update the progress bar every second
def update_progress_bar():
    while is_downloading:
        time.sleep(1)  # Update every second
        root.after(100, refresh_status)

def refresh_status():
    # Update progress bar (progress is handled by yt-dlp hooks)
    if is_downloading:
        # Update progress label
        progress_bar['value'] += 1  # Increment to simulate progress (for testing)
        if progress_bar['value'] >= 100:
            progress_bar['value'] = 100
            status_label.config(text="Download Complete")

# Function to download the video using yt-dlp and selected quality in a separate thread
def download_video():
    url = url_entry.get()

    if not url or not available_formats:
        messagebox.showerror("Input Error", "Please provide a YouTube video URL and select a quality.")
        return

    try:
        # Get the selected format
        selected_index = quality_combobox.current()
        selected_format = available_formats[selected_index]

        # Ask the user where they want to save the video
        download_folder = filedialog.askdirectory()
        if download_folder:
            global is_downloading
            is_downloading = True
            
            # yt-dlp options
            ydl_opts = {
                'format': selected_format['format_id'],  # Download the selected format
                'outtmpl': f'{download_folder}/%(title)s.%(ext)s',
                'progress_hooks': [on_progress],
            }

            # Start the download in a separate thread
            status_label.config(text="Downloading...")
            progress_bar['value'] = 0
            threading.Thread(target=start_download, args=(url, ydl_opts)).start()

            # Start updating progress bar every second
            threading.Thread(target=update_progress_bar).start()

        else:
            messagebox.showwarning("Folder Selection", "Please select a valid folder.")
    
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
        status_label.config(text="")

# Function to start the download process
def start_download(url, ydl_opts):
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        
        global is_downloading
        is_downloading = False

        # Once download is complete, update status
        root.after(100, lambda: status_label.config(text="Download Complete"))
    
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred during download: {e}")
        is_downloading = False

# Progress callback function from yt-dlp
def on_progress(d):
    if d['status'] == 'downloading':
        total_bytes = d.get('total_bytes', 0)
        downloaded_bytes = d.get('downloaded_bytes', 0)
        if total_bytes > 0:
            percent = int((downloaded_bytes / total_bytes) * 100)
            root.after(100, lambda: progress_bar.config(value=percent))
            root.after(100, lambda: status_label.config(text=f"Downloading... {percent}%"))
    elif d['status'] == 'finished':
        root.after(100, lambda: progress_bar.config(value=100))
        root.after(100, lambda: status_label.config(text="Processing..."))

# Create the main window
root = ttk.Window(themename="litera")
root.title("YouTube Video Downloader with Real-Time Progress")
root.geometry("600x400")

# Add widgets to the GUI
frame = ttk.Frame(root, padding="20")
frame.pack(fill="both", expand=True)

# URL Label and Entry
url_label = ttk.Label(frame, text="YouTube URL:")
url_label.pack(anchor="w")

url_entry = ttk.Entry(frame, width=50)
url_entry.pack(pady=10)

# Fetch Formats Button
fetch_button = ttk.Button(frame, text="Fetch Available Qualities", command=fetch_formats)
fetch_button.pack(pady=10)

# Quality Selection Combobox
quality_combobox = ttk.Combobox(frame, state="readonly", width=50)
quality_combobox.pack(pady=10)

# Download Button
download_button = ttk.Button(frame, text="Download Video", command=download_video)
download_button.pack(pady=10)

# Progress Bar
progress_bar = ttk.Progressbar(frame, mode="determinate", length=400)
progress_bar.pack(pady=20)

# Status Label
status_label = ttk.Label(frame, text="")
status_label.pack(pady=10)

# Start the GUI loop
root.mainloop()
