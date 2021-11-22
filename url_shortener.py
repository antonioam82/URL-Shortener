from tkinter import *
import pyshorteners

class shortener:
    def __init__(self):
        self.app = Tk()
        self.app.title("URL Shortener")
        self.app.geometry("990x370")

        self.app.mainloop()

if __name__=="__main__":
    shortener()
        
