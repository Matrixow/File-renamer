import tkinter as tk
from tkinter import filedialog

class AppUI:
    def __init__(self, windowTitle):
        self.title = windowTitle

    def select_folder():
        folderPath = filedialog.askdirectory(title="Select a folder")
        if folderPath:
            print(f"Folder path is {folderPath}")
        return

    def runApp(self):
        window = tk.Tk()
        window.title(self.title)
        window.geometry("500x300")
        window.resizable(False, False)

        button = tk.Button(text="Select a folder", command=self.select_folder())
        label = tk.Label(text="Select folder directory")
        label.pack()
        window.mainloop() 


app = AppUI("File renamer")
app.runApp()
