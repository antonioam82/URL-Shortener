from tkinter import *
from tkinter import messagebox
import pyshorteners as ps
from urllib.parse import urlparse
import threading
import os

class shortener:
    def __init__(self):
        self.app = Tk()
        self.app.title("URL Shortener")
        self.app.geometry("1038x370")
        self.app.configure(background="PaleGreen2")

        current_dir = StringVar()
        current_dir.set(os.getcwd())
        self.url = StringVar()

        Label(self.app,text="URL Shortener:",bg="PaleGreen2",fg="white",font=('Arial', 40, 'bold')).place(x=20,y=40)
        self.ShrtStatus = Label(self.app,bg="PaleGreen2",fg="white",font=('Arial', 40, 'bold'))
        self.ShrtStatus.place(x=440,y=40)
        Entry(self.app,textvariable=current_dir,width=172).place(x=0,y=0)
        self.url_visor=Entry(self.app,textvariable=self.url,width=37,font='Arial, 33')
        self.url_visor.place(x=20,y=150)
        Button(self.app,text="SHORTEN",height=3,width=12,command=self.init_task).place(x=925,y=150)
        Button(self.app,text="COPY",height=1,width=12).place(x=925,y=235)
        Button(self.app,text="CLEAR",height=1,width=12,command=self.clear).place(x=819,y=235)
        Button(self.app,text="IMPORT",height=1,width=12).place(x=713,y=235)
        

        self.app.mainloop()

    def shorten_URL(self):
        if self.is_url(self.url_visor.get())==True:
            self.ShrtStatus.configure(text="Shorting your URL...")
            url = self.url_visor.get()
            self.url.set(ps.Shortener().tinyurl.short(url))
            self.ShrtStatus.configure(text="Task completed :)")
        else:
            messagebox.showwarning("INVALID URL","Enter a valid URL.")

    def clear(self):
        self.url.set("")
        self.ShrtStatus.configure(text="")

    def is_url(self,url):
        try:
            result = urlparse(url)
            return all([result.scheme, result.netloc])
        except ValueError:
            return False
            
    def init_task(self):
        t = threading.Thread(target=self.shorten_URL)
        t.start()
            
if __name__=="__main__":
    shortener()
        
