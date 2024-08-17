import tkinter as tk
from tkinter import filedialog
from main import ItemRenamer as IR

class AppUI:
    def __init__(self, windowTitle):
        self.title = windowTitle
        self.font = ('Helvetica', 15)


    def select_folder(self):
        global folderPath
        folderPath = filedialog.askdirectory(title="Select a folder")
        if folderPath:
            print(f"Folder path is {folderPath}")
            self.set_StringVar(self.stringvar, IR(folderPath).list_items())
    
    def set_StringVar(self, stringvar, text):
        stringvar.set(text)

    def runApp(self):
        window = tk.Tk()
        self.stringvar = tk.StringVar()
        window.title(self.title)
        window.geometry("500x400")
        window.resizable(False, False)
        # items_list_label_text = tk.StringVar(window)

        label = tk.Label(text="Select folder directory", font=self.font)
        button = tk.Button(text="Select a folder", command=self.select_folder, font=('Helvetica'))
        items_label = tk.Label(text="Items in selected directory", font=self.font)
        items_list_label = tk.Label(text=self.stringvar)

        label.pack()
        button.pack(padx=20, pady=20, ipadx=10, ipady=10)
        items_label.pack(pady=10)
        items_list_label.pack()
        window.mainloop() 


app = AppUI("File renamer")
app.runApp()
