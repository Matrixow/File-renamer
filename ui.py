import tkinter as tk
from tkinter import filedialog
from main import ItemRenamer as IR

class AppUI:
    def __init__(self, windowTitle):
        self.title = windowTitle
        self.font = ('Helvetica', 15)
        self.window = tk.Tk()
        self.frame = tk.Frame(self.window)
        self.stringvar = tk.StringVar()
        self.stringvar.set("Items go here")
        self.text_widget = tk.Text(self.frame, wrap=tk.WORD, font=("Helvetica", 14), width=40, height=10)
        self.text_widget.config(state=tk.DISABLED)

    def set_StringVar(self, stringvar, text):
        stringvar.set(text)

    def update_text_widget(self):
        self.text_widget.config(state=tk.NORMAL)
        self.text_widget.delete(1.0, tk.END)
        self.text_widget.insert(tk.END, self.stringvar.get())
        self.text_widget.config(state=tk.DISABLED)


    def select_folder(self):
        folderPath = filedialog.askdirectory(title="Select a folder")
        if folderPath:
            print(f"Folder path is {folderPath}")
            print(IR(folderPath).list_items())
            self.set_StringVar(self.stringvar, IR(folderPath).list_items())
            self.update_text_widget()


    def runApp(self):

        self.window.title(self.title)
        self.window.geometry("500x400")
        self.window.resizable(False, False)
        # items_list_label_text = tk.StringVar(window)

        label = tk.Label(text="Select folder directory", font=self.font)
        button = tk.Button(text="Select a folder", command=self.select_folder, font=('Helvetica'))
        items_label = tk.Label(text="Items in selected directory", font=self.font)

        label.pack()
        button.pack(padx=20, pady=20, ipadx=10, ipady=10)
        items_label.pack(pady=10)
        self.frame.pack(pady=20, padx=20)
        self.text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.window.mainloop() 


app = AppUI("File renamer")
app.runApp()

