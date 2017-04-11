from tkinter import Tk,Message,TOP


class UpdateScreen:
    label1=None
    def __init__(self,supremedir):
        self.root2=Tk()
        try:
            self.root2.iconbitmap(supremedir+'\icons\search.ico')
        except:
            try:
                a.root2.iconbitmap(r'C:\Program Files\searchBASE\icons\search.ico')#for the icon
            except:
                print("no")
        self.root2.geometry('500x200')
        self.root2.title("Scanning")
        self.root2.resizable(height=False,width=False)
        self.label1=Message(self.root2,text="Please wait while the documents are being scanned. It may take a while.\nIt's a one time process.\nPlease do not exit during this operation.",font='Mincho 10',width=400)
        self.label1.pack(side=TOP)
        self.label1.place(x=2,y=10)
        self.label=Message(self.root2,font='Mincho 8',width=400)
        self.label.pack()
        self.label.place(x=2,y=60)
        
    def getLabel(self):
        return self.label

