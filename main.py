import os
import glob
import re

class ItemRenamer:
    def __init__(self, directory):
        self.directory = directory

    def list_items(self):
        items = []
        for item in os.listdir(self.directory):
            items.append(item)
        return str(items)

re = ItemRenamer("/Users/ernest/Documents/Movies/Anime/Dr Stone/S03/Cour1")
re.list_items()