from tkinter import Tk
import tkinter
import os
import pickle

class settings(Tk):
    var=None
    def __init__(self,*args, **kwargs):
        Tk.__init__(self,*args, **kwargs)
        try:
           fileopen2=open(r'C:\database2\DATABASES.pkl','rb')
           x=pickle.load(fileopen2)
           self.var=x["variable"]
           fileopen2.close()
        except:
            if not os.path.exists(r'C:\database2'):
               os.mkdir(r'C:\database2')
            self.var=True
        try:
           self.iconbitmap('icons\search.ico')
        except:
           try:
              self.iconbitmap(r'C:\Program Files\searchBASE\icons\search.ico')#for the icon
           except:
              print("no")
        self.title('Settings')
        
        self.geometry("400x100")
        self.resizable(height=False,width=False)
        self.configure(background='SteelBlue2')
        self.cbox=tkinter.Checkbutton(self,cursor='hand2',command=self.store,text='Display Searchbox on Desktop' ,fg='black',font='Times 10')
        self.cbox.pack()
        self.cbox.place(x=20,y=20)
        self.button=tkinter.Button(self,relief='groove',cursor='hand2',command=self.clear_data,text='Clear Cache(Learnt data)')
        self.button.pack()
        self.button.place(x=20,y=60)
        if self.var:
            self.cbox.select()
        self.protocol("WM_DELETE_WINDOW",self.onClosing)
        
    def store(self):
        self.var=not self.var
        print(self.var)
        try:
            f=open(r'C:\database2\DATABASES.pkl','rb')
            x=pickle.load(f)
            f.close()
            x["variable"]=self.var
            f=open(r'C:\database2\DATABASES.pkl','wb')
            pickle.dump(x,f)
            f.close()
        except:
            f=open(r'C:\database2\DATABASES.pkl','wb')
            tempr={"variable":self.var}
            pickle.dump(tempr,f)
            f.close()
            tempr=None
            
    def onClosing(self):
        self.destroy()

    def clear_data(self):
        try:
           a=open(r'C:\database2\dbm.pkl','rb')
           a.close()
           a=open(r'C:\database2\dbm.pkl','wb')
           a.close()
           self.label=tkinter.Label(self,fg='white',text='Cache Cleared!',bg='SteelBlue2')
           self.label.pack()
           self.label.place(x=180,y=63)
        except:
            self.label=tkinter.Label(self,text='Cache is already empty.',fg='white',bg='SteelBlue2')
            self.label.pack()
            self.label.place(x=180,y=63)

