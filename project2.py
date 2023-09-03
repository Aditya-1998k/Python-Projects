""""
Youtube Audio Downloader
tkinter -- for frontend purpose
messagebox--for notification or error messages
pytube module -- python external library for downloading youtube audio
"""
import tkinter as tk
from tkinter import messagebox
from pytube import YouTube

def download_audio():
    root.withdraw()
    url = entry_url.get()
    output_path= entry_output_path.get()
    try:
        yt = YouTube(url)
        audio_stream = yt.streams.filter(only_audio=True).first()
        audio_stream.download(output_path)
        messagebox.showinfo("Downloaded", "Downloaded Successfully")
        root.quit()
    except Exception as e:
        messagebox.showerror("Error", f"Some Error occured: {e}")


root = tk.Tk()
root.title("Youtube Video Downloader")

label_url = tk.Label(root, text="Enter the YouTube Audio URL: ")
label_url.pack()

entry_url = tk.Entry(root, width=50)
entry_url.pack()

label_output_path= tk.Label(root, text="Enter the Output Path: ")
label_output_path.pack()


entry_output_path = tk.Entry(root, width=50)
entry_output_path.pack()

download_button = tk.Button(root, text="Download", command=download_audio)
download_button.pack()

root.mainloop()
