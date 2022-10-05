import tkinter as tk
from tkinter import filedialog
from pytube import YouTube
import shutil


def download():
    top.title("DOWNLOADER(downloading....)")
    get_link = Link_text.get()
    user_path = path_label.cget("text")
    video = YouTube(get_link).streams.get_highest_resolution().download()
    shutil.move(video, user_path)
    status.configure(text="Download Completed")
    top.title("DOWNLOADER")


def select_path():
    path = filedialog.askdirectory()
    path_label.config(text=path)


top = tk.Tk()
top.geometry("500x500")
canvas = tk.Canvas(top, width="500", height="500", bg="light green")
canvas.pack()
img = tk.PhotoImage(file="yt.png")
img = img.subsample(2, 2)
canvas.create_image(250, 80, image=img)
Link = tk.Label(top, text="Link:", font=('Arial', 15), bg="light green")
Link_text = tk.Entry(top, width=20, font=('Arial', 10))
download = tk.Button(top, text="Download", bg='red', padx='22', pady='5', font=('Arial', 15), fg='black',
                     command=download)
status = tk.Label(top, text="", font=('Arial', 10), bg="light green")
path_label = tk.Label(top, text="Select Path For Download", font=('Arial', 10), bg="light green")
select_btn = tk.Button(top, text="Select Path", bg='black', padx='15', pady='3', font=('Arial', 10), fg='white',
                       command=select_path)
canvas.create_window(250, 250, window=path_label)
canvas.create_window(250, 290, window=select_btn)
canvas.create_window(100, 180, window=Link)
canvas.create_window(250, 180, window=Link_text)
canvas.create_window(250, 200, window=status)
canvas.create_window(250, 340, window=download)
top.title("DOWNLOADER")
top.mainloop()
