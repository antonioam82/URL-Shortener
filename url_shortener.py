#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import messagebox, filedialog
import pyshorteners as ps
import time
import qrcode
import pyperclip
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

        Label(self.app,text="URL Shortener:",bg="PaleGreen2",fg="white",font=('Arial', 40, 'bold')).place(x=20,y=50)
        self.ShrtStatus = Label(self.app,bg="PaleGreen2",fg="white",font=('Arial', 40, 'bold'))
        self.ShrtStatus.place(x=440,y=50)
        Entry(self.app,textvariable=current_dir,width=172).place(x=0,y=0)
        self.url_visor=Entry(self.app,textvariable=self.url,width=37,font='Arial, 33')
        self.url_visor.place(x=20,y=150)
        Button(self.app,text="SHORTEN",height=3,width=12,command=self.init_task).place(x=925,y=150)
        Button(self.app,text="COPY",width=12,command=self.copy).place(x=925,y=235)
        Button(self.app,text="CLEAR",width=12,command=self.clear).place(x=819,y=235)
        Button(self.app,text="IMPORT",width=12,command=self.init_task2).place(x=713,y=235)
        Button(self.app,text="CREATE QR",width=20,command=self.save_qr).place(x=20,y=235)

        self.app.mainloop()

    def shorten_URL(self):
        if self.is_url(self.url_visor.get())==True:
            try:
                self.ShrtStatus.configure(text="shorting your URL...")
                url = self.url_visor.get()
                self.url.set(ps.Shortener().tinyurl.short(url))
                self.ShrtStatus.configure(text="task completed :)")
            except Exception as e:
                messagebox.showwarning("UNEXPECTED ERROR",str(e))
                self.clear()
        else:
            messagebox.showwarning("EMPTY/INVALID URL","Enter a valid URL.")
            self.clear()

    def import_url(self):
        self.clear()
        ultcop = pyperclip.paste().strip()
        while True:
            time.sleep(0.1)
            copy = pyperclip.paste().strip()
            if copy != ultcop:
                self.url.set(copy)
                self.ultcop = copy
                break

    def copy(self):
        if self.url_visor.get() != "":
            pyperclip.copy(self.url_visor.get())
            messagebox.showinfo("COPIED","Copied to clipboard.")

    def save_qr(self):
        if self.is_url(self.url_visor.get())==True:
            new_file = filedialog.asksaveasfilename(initialdir="/",initialfile="urlQR",
                                                    title="SAVE AS",defaultextension=".png",)
            if new_file != "":
                qr = qrcode.make(self.url_visor.get())
                qr.save(new_file)

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

    def init_task2(self):
        t2 = threading.Thread(target=self.import_url)
        t2.start()
            
if __name__=="__main__":
    shortener()
        
        
