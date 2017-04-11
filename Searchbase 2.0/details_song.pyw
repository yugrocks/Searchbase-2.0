import win32com.client
import os

class getMeta():
    def __init__(self):
        self.wmplayer = win32com.client.gencache.EnsureDispatch ("WMPlayer.OCX")
        print("meta initialized")
    def getArtist(self,path):
        try:
           details = self.wmplayer.mediaCollection.add(path)
           return details.getItemInfo ("Artist")
        except:
           return ""
    def getGenre(self,path):
        try:
           details = self.wmplayer.mediaCollection.add (path)
           return details.getItemInfo ("Genre")
        except:
           return ""
   

