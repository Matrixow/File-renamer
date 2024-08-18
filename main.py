import os
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
        matching_files = "Files renamed are: \n"

        os.chdir(self.directory)
        for file in os.listdir(self.directory):
            if self.nametoremove in file:
                filename = file
                matching_files += f" sep{filename}"
                newname = filename.replace(self.nametoremove, "")
                os.rename(f"{self.directory}/{file}", newname)
            else:
                continue
        return "\n".join(matching_files.split("sep"))
