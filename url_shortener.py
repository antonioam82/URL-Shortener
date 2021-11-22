from tkinter import *
import pyshorteners
import os

class shortener:
    def __init__(self):
        self.app = Tk()
        self.app.title("URL Shortener")
        self.app.geometry("1038x370")
        self.app.configure(background="PaleGreen2")

        current_dir = StringVar()
        current_dir.set(os.getcwd())

        Label(self.app,text="URL Shortener...",bg="PaleGreen2",fg="white",font=('Arial', 40, 'bold')).place(x=20,y=40)
        Entry(self.app,textvariable=current_dir,width=172).place(x=0,y=0)
        url_visor=Entry(self.app,width=37,font='Arial, 33')
        url_visor.place(x=20,y=150)
        Button(self.app,text="SHORTEN",height=3,width=12).place(x=925,y=150)
        

        self.app.mainloop()

if __name__=="__main__":
    shortener()
        
