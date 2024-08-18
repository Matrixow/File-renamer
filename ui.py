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
        self.folderPath = ""

    def set_StringVar(self, stringvar, text):
        stringvar.set(text)

    def update_text_widget(self):
        self.text_widget.config(state=tk.NORMAL)
        self.text_widget.delete(1.0, tk.END)
        self.text_widget.insert(tk.END, self.stringvar.get())
        self.text_widget.config(state=tk.DISABLED)


    def select_folder(self):
        self.folderPath = filedialog.askdirectory(title="Select a folder")
        if self.folderPath:
            print(f"Folder path is {self.folderPath}")
            print(IR(self.folderPath).list_items())
            self.set_StringVar(self.stringvar, IR(self.folderPath).list_items())
            self.update_text_widget()


    def runApp(self):

        self.window.title(self.title)
        self.window.geometry("500x500")
        self.window.resizable(False, False)
        self.text_to_replace = tk.StringVar()
        # items_list_label_text = tk.StringVar(window)

        label = tk.Label(text="Select folder directory", font=self.font)
        select_button = tk.Button(text="Select a folder", command=self.select_folder, font=('Helvetica'))
        items_label = tk.Label(text="Items in selected directory", font=self.font)
        self.chars_to_remove = tk.Entry(self.window, width=20)
        chars_to_remove_label = tk.Label(text="Text to remove from files")
        rename_button = tk.Button(text="Rename files", command=lambda: IR(self.folderPath).rename_items(self.chars_to_remove.get()))

        label.pack()
        select_button.pack(padx=20, pady=20, ipadx=10, ipady=10)
        items_label.pack(pady=10)
        self.frame.pack(pady=20, padx=20)
        self.text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        chars_to_remove_label.pack()
        self.chars_to_remove.pack()
        rename_button.pack(padx=50, pady=10)
        self.window.mainloop() 


app = AppUI("File renamer")
app.runApp()

