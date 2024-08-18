import os
import glob
import re

class ItemRenamer:
    def __init__(self, directory):
        self.directory = directory

    def list_items(self):
        items = ""
        for item in os.listdir(self.directory):
            items+=f"sep{item}"
        return "\n".join(items.split("sep"))
    
    def rename_items(self, nametoremove):
        self.nametoremove = nametoremove

        os.chdir(self.directory)
        for file in os.listdir(self.directory):
            if self.nametoremove in file:
                filename = file
                newname = filename.replace(self.nametoremove, "")
                os.rename(f"{self.directory}/{file}", newname)

re = ItemRenamer("/Users/ernest/Documents/Movies/Anime/Dr Stone/S03/Cour1")
re.list_items()