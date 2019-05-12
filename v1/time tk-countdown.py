from tkinter import *
from tkinter import ttk, font
import time, subprocess
root = Tk()

count = StringVar()

def timer():
    timeleft = int(Entry.get(x))
    while timeleft > 0:
          count = print(timeleft)
          time.sleep(1)
          timeleft = timeleft - 1
    subprocess.Popen(['start','alarm.wav'], shell = True)


x1Lab = Label(root,text = "Enter the countdown in second: ")
timer = Button(root,text = "start", command = timer)


x = Entry(root)
x1Lab.grid(row=1,column=0)
x.grid(row=1,column=2)

timer.grid(row=2)

root.wm_title("Count Down Timer")

root.mainloop()

