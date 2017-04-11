import tkinter

class shortcut(tkinter.Tk):
    frame=None
    entrybox=None
    destroyed=False
    def __init__(self,*args, **kwargs):
        tkinter.Tk.__init__(self,*args, **kwargs)
        self.geometry("+300+400")
        self.configure(background='steelblue')
        self.label=tkinter.Label(width=45,bg='steelblue',anchor='w')
        self.label.grid(row=0,column=0)
        self.v = tkinter.StringVar(value='Search')
        self.entrybox=tkinter.Entry(background="gray53",width=45,relief=tkinter.SUNKEN,font='Mincho',textvariable=self.v,fg="white")
        self.entrybox.grid(row=1,column=0,ipady=5)
        self.button=tkinter.Button(bg='steelblue',relief='flat',command=self.destroy1)
        self.button.grid(row=1,column=2,ipady=4)
        self.frame=tkinter.Frame()
        self.frame.grid(row=3,column=0)
        self.overrideredirect(True)
        self.wm_attributes("-transparentcolor", "white")
        self.bind('<Enter>',self.onMouseIn)
        self.bind('<Leave>',self.onMouseOut)
        self.label.bind('<Enter>',self.onMouseIn)
        self.label.bind('<Leave>',self.onMouseOut)
        self.label.bind('<B1-Motion>',self.showPosEvent)
        self.entrybox.bind('<Button-1>',self.onEntryClicked)
        self.attributes('-alpha',0.88)


    def onMouseIn(self,event):
        self.label.config(text="SEARCHBASE")
        self.wm_attributes("-transparentcolor","red")
        self.button.config(text='Exit',bg='white')

    def onMouseOut(self,event):
        self.label.config(text="")
        self.button.config(text='',bg='steelblue')
        self.wm_attributes("-transparentcolor","steelblue")

    def showPosEvent(self,event):
       self.geometry('+{}+{}'.format(event.x_root, event.y_root))

    def onEntryClicked(self,event):
        self.entrybox.delete(0,'end')

    def makeFrame(self):
        self.frame=tkinter.Frame()
        self.frame.grid(row=3,column=0)

    def destroy1(self):
        self.destroyed=True
        self.destroy()


