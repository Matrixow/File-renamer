import tkinter as tk
from tkinter import filedialog
from main import ItemRenamer

class AppUI:
    def __init__(self, windowTitle):
        self.title = windowTitle
        self.font = ('Helvetica', 15)

    def select_folder(self):
        global folderPath
        folderPath = filedialog.askdirectory(title="Select a folder")
        if folderPath:
            print(f"Folder path is {folderPath}")
        return

    def runApp(self):
        window = tk.Tk()
        window.title(self.title)
        window.geometry("500x400")
        window.resizable(False, False)

        label = tk.Label(text="Select folder directory", font=self.font)
        button = tk.Button(text="Select a folder", command=self.select_folder, font=('Helvetica'))
        items_label = tk.Label(text="Items in selected directory", font=self.font)


        label.pack()
        button.pack(padx=20, pady=20, ipadx=10, ipady=10)
        items_label.pack(pady=10)
        window.mainloop() 


app = AppUI("File renamer")
app.runApp()
