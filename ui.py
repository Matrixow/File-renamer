import tkinter as tk
from tkinter import filedialog

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
        window.geometry("300x200")
        window.resizable(False, False)

        label = tk.Label(text="Select folder directory", font=self.font)
        button = tk.Button(text="Select a folder", command=self.select_folder, font=('Helvetica'))

        label.pack()
        button.pack(padx=20, pady=20, ipadx=10, ipady=10)
        window.mainloop() 


app = AppUI("File renamer")
app.runApp()
