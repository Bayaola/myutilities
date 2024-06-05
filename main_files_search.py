import os
import tkinter as tk
from tkinter import filedialog, ttk
import subprocess
import re
from docx import Document
from pptx import Presentation
from openpyxl import load_workbook
import PyPDF2

class FileSearchApp:
    def __init__(self, master):
        self.master = master
        master.title("File Search App")

        # Create the main UI elements
        self.directory_label = tk.Label(master, text="Choose directory to search:")
        self.directory_label.pack()

        self.directory_entry = tk.Entry(master)
        self.directory_entry.pack()

        self.browse_button = tk.Button(master, text="Browse", command=self.select_directory)
        self.browse_button.pack()

        self.keyword_label = tk.Label(master, text="Enter keyword to search:")
        self.keyword_label.pack()

        self.keyword_entry = tk.Entry(master)
        self.keyword_entry.pack()

        self.search_button = tk.Button(master, text="Search", command=self.search_files)
        self.search_button.pack()

        self.results_tree = ttk.Treeview(master, columns=("File", "Type", "Open", "Location"))
        self.results_tree.heading("#0", text="File")
        self.results_tree.heading("File", text="File")
        self.results_tree.heading("Type", text="Type")
        self.results_tree.heading("Open", text="Open")
        self.results_tree.heading("Location", text="Location")
        self.results_tree.pack(fill=tk.BOTH, expand=True)

    def select_directory(self):
        self.directory_entry.delete(0, tk.END)
        self.directory_entry.insert(0, filedialog.askdirectory())

    def search_files(self):
        root_dir = self.directory_entry.get()
        keyword = self.keyword_entry.get()

        self.results_tree.delete(*self.results_tree.get_children())

        for dirpath, dirnames, filenames in os.walk(root_dir):
            for filename in filenames:
                if keyword.lower() in filename.lower():
                    file_path = os.path.join(dirpath, filename)
                    file_type = self.get_file_type(file_path)
                    self.results_tree.insert("", "end", text=filename, values=(filename, file_type, "Open", file_path))
            for dirname in dirnames:
                if keyword.lower() in dirname.lower():
                    dir_path = os.path.join(dirpath, dirname)
                    self.results_tree.insert("", "end", text=dirname, values=(dirname, "Folder", "Open", dir_path))

    def get_file_type(self, file_path):
        _, extension = os.path.splitext(file_path)
        extension = extension.lower()

        if extension == ".docx":
            return "Word Document"
        elif extension == ".pptx":
            return "PowerPoint Presentation"
        elif extension == ".xlsx":
            return "Excel Spreadsheet"
        elif extension == ".pdf":
            return "PDF Document"
        elif extension == ".txt":
            return "Text File"
        else:
            return "Unknown"

    def open_file(self, event):
        selected_item = self.results_tree.focus()
        file_path = self.results_tree.item(selected_item, "values")[3]
        subprocess.Popen([file_path], shell=True)

root = tk.Tk()
app = FileSearchApp(root)
root.mainloop()