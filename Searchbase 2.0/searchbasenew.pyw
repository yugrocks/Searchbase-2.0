from tkinter import *
from functools import partial
class searchbase():
    root=Tk()
    entryBox=Entry(root,background="ivory2",width=60,relief=SUNKEN,font='Mincho')
    frame1=Canvas(root,height=320,width=653,scrollregion=(0,0,350,354))
    frame2=Frame(frame1,height=320,width=653)
    frme=Canvas(root,height=640,width=695,scrollregion=(0,0,699,642))
    frme2=Frame(frme,height=640,width=695)
    frame3=Canvas(root,height=293,width=653,scrollregion=(0,0,350,351))
    frame4=Frame(frame3,height=293,width=653)
    lm=Label(root,text='MEDIA FILES',width=93,anchor=W,bg='white',font='Mincho 10')
    ld=Label(root,text='DOCUMENTS',width=99,anchor=W,bg='light gray',font='Mincho 10')
    lf=Label(root,text='FOLDERS',width=93,anchor=W,bg='white smoke',font='Mincho 10')

        
    def __init__(self):
        self.root.title("SearchBASE")
        widthpixels=1365
        heightpixels=720
        self.root.geometry('{}x{}'.format(widthpixels, heightpixels))
        self.root.configure(background="gray53")
        self.entryBox.pack(ipady=4,side=TOP)
        self.entryBox.place(height=40,width=400,x=0,y=0)
        self.entryBox.focus_set()
        self.frame1.config(background='white')
        self.frame1.pack_propagate(False)
        self.frame2.pack()
        self.frame2.configure(background="white")
        vbar=Scrollbar(self.frame1,orient=VERTICAL,width=14)
        vbar.pack(side=RIGHT,fill=Y)
        vbar.config(command=self.frame1.yview)
        self.frame1.config( yscrollcommand=vbar.set)
        self.frame1.pack(side=LEFT,expand=True,fill=BOTH)
        self.frame1.create_window((4,4), window=self.frame2, anchor="nw")
        self.frame2.update()
        self.frame2.bind("<Configure>", lambda event, canvas=self.frame1: onFrameConfigure(canvas))
        self.frame1.place(x=704,y=85)
        self.frme.pack()
        self.frme.config(background='light gray')
        self.frme2.config(background='light gray')
        self.frme.pack_propagate(False)
        vbar2=Scrollbar(self.frme,orient=VERTICAL,relief=FLAT,width=14)
        vbar2.pack(side=RIGHT,fill=Y)
        vbar2.config(command=self.frme.yview)
        self.frme.config( yscrollcommand=vbar2.set)
        self.frme.pack(side=LEFT,expand=True,fill=BOTH)
        self.frme.create_window((4,4), window=self.frme2, anchor="nw")
        self.frme2.update()
        self.frme2.bind("<Configure>", lambda event, canvas=self.frme: onFrameConfigure(canvas))
        self.frme.place(x=3,y=85)
        self.frame3.pack()
        self.frame3.pack_propagate(False)
        vbar3=Scrollbar(self.frame3,orient=VERTICAL,relief=FLAT,width=14)
        vbar3.pack(side=RIGHT,fill=Y)
        vbar3.config(command=self.frame3.yview)
        self.frame3.config( yscrollcommand=vbar3.set)
        self.frame3.pack(side=LEFT,expand=True,fill=BOTH)
        self.frame3.config(background="white smoke")
        self.frame4.config(background="white smoke")
        self.frame3.create_window((4,4), window=self.frame4, anchor="nw")
        self.frame4.update()
        self.frame4.bind("<Configure>", lambda event, canvas=self.frame3: onFrameConfigure(canvas))
        self.frame3.place(x=704,y=417)
        self.ld.pack(ipadx=10)
        self.ld.place(x=3,y=65)
        self.lm.pack(ipadx=10)
        self.lm.place(x=704,y=65)
        self.lf.pack(ipadx=10)
        self.lf.place(x=704,y=396)


def hello():
    print("hello")


def _on_mousewheel(frame,event):
          frame.yview_scroll(-1*int(event.delta/120), "units")


def onFrameConfigure(canvas):
    '''Reset the scroll region to encompass the inner frame'''
    canvas.configure(scrollregion=canvas.bbox("all"))
