import os
import subprocess
import tkinter as tk
from tkinter import filedialog as fd


def cut():
    start = entry_start.get()
    stop  = entry_stop.get()
    print(start, '->', stop)
    file_name, file_extension = os.path.splitext(os.path.basename(filename))
    output = f'{file_name}-{start.replace(":", "-")}-{stop.replace(":", "-")}{file_extension}'

    print(filename, '->', output)

    subprocess.run(['ffmpeg', '-i', filename,
                    '-ss', start, '-to', stop,
                    '-acodec', 'copy', '-vcodec', 'copy',
                    output])


window = tk.Tk()
window.title('Video Cutter')
window.resizable(False, False)

label_start = tk.Label(text="starting time")
label_stop  = tk.Label(text="stopping time")
label_blank = tk.Label(text=" ")

entry_start = tk.Entry(width=40)
entry_stop = tk.Entry(width=40)
entry_start.insert(tk.END, '00:00:00')
entry_stop.insert(tk.END, '00:00:00')

button_cut = tk.Button(text="cut", width=32, height=2, command=cut)

label_start.pack()
entry_start.pack()
label_stop.pack()
entry_stop.pack()
label_blank.pack()
button_cut.pack()


if __name__ == "__main__":
    filename = fd.askopenfilename(
        title='Open a file',
        filetypes=[('Video Files', '.mp4 .avi .flv .mkv')])
    print(filename)

    window.focus_force()
    window.mainloop()
