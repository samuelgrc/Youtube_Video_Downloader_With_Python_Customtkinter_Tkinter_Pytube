import tkinter # pip install tk
import customtkinter # pip install customtkinter==0.3
from pytube import YouTube # pip install pytube | pip install pytube3

# Start download function
def startdownload():
    try:
        ytlink = link.get()
        ytObject = YouTube(ytlink, on_progress_callback=on_progress)
        video = ytObject.streams.get_highest_resolution()

        title.configure(text=ytObject.title, text_color="white")
        finishlabel.configure(text="")
        video.download()
        finishlabel.configure(text="Download Complete",text_color="green")
    except:
        finishlabel.configure(text="Invalid URL", text_color="red")
        
# Reset function
def reset_download():
    link.delete(0, tkinter.END)
    title.configure(text="")
    finishlabel.configure(text="")
    pPercentage.configure(text="0%")
    progressbar.set(0)

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentange_of_compeletion = (bytes_downloaded / total_size) * 100
    per = str(int(percentange_of_compeletion))
    pPercentage.configure(text=per + '%')
    pPercentage.update()

    # Update progress bar
    progressbar.set(float(percentange_of_compeletion) / 100 )


# system settings
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

# Our app frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("YouTube Downloader")

# Adding UI elements
title = customtkinter.CTkLabel(app, text="Insert YouTube URL", text_color="magenta")
title.pack(padx=10, pady=10)

#Link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var, border_color="magenta")
link.pack()

# Finished downloading
finishlabel = customtkinter.CTkLabel(app, text="")
finishlabel.pack()

# Progress percentage
pPercentage = customtkinter.CTkLabel(app, text="0%")
pPercentage.pack()

# Progress bar
progressbar = customtkinter.CTkProgressBar(app, width=400, progress_color="magenta")
progressbar.set(0)
progressbar.pack(padx=10, pady=10)

# Download button
download = customtkinter.CTkButton(app, text="Download", command=startdownload, text_color="magenta")
download.pack(padx=10, pady=10)

# Reset button

reset = customtkinter.CTkButton(app, text="Reset", command=reset_download, text_color="magenta")
reset.pack(padx=10, pady=10)

# Run app
app.mainloop()
