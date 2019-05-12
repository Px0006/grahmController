import tkinter as tk
import time
import subprocess
import os

path = '/home/px007/Dev/Python/grahmController/v2'

open('gameDisplay.jpg')



class Application(tk.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        

    def timer(self):
        timeleft = int(Entry.get(x))
        while timeleft > 0:
              count = print(timeleft)
              time.sleep(1)
              timeleft = self.timeleft
              timeleft = timeleft - 1
        subprocess.Popen(['start','gong.wav'], shell = True)

    def create_widgets(self):
        self.timeleft = tk.Label(self)
        self.timeleft["text"] = "please enter the time in seconds: "
        self.timeleft.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

root = tk.Tk()
app = Application(master=root)
app.mainloop()
