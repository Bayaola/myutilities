import os
import shutil
import tkinter as tk
from tkinter import filedialog
from collections import defaultdict

class FolderOrganizer:
    def __init__(self, master):
        self.master = master
        master.title("Folder Organizer")

        # Create the main GUI elements
        self.select_button = tk.Button(master, text="Select Directory", command=self.select_directory)
        self.select_button.pack(pady=20)

        self.progress_label = tk.Label(master, text="")
        self.progress_label.pack(pady=10)

        # Create a status bar
        self.status_bar = tk.Label(master, text="", bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

    def select_directory(self):
        self.directory = filedialog.askdirectory()
        if self.directory:
            self.status_bar.config(text=f"Selected directory: {self.directory}")
            self.organize_files()
        else:
            self.status_bar.config(text="No directory selected")

    def organize_files(self):
        self.create_folders()
        self.move_files()
        self.show_file_count()
        self.progress_label.config(text="Folder organization complete!")

    def create_folders(self):
        self.status_bar.config(text="Creating folders...")
        folders = ["Images", "Documents", "Musics", "Videos", "Compressed", "Programs", "Others"]
        for folder in folders:
            folder_path = os.path.join(self.directory, folder)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

    def move_files(self):
        self.status_bar.config(text="Moving files...")
        self.file_counts = defaultdict(int)
        for filename in os.listdir(self.directory):
            file_path = os.path.join(self.directory, filename)
            if os.path.isfile(file_path):
                if filename.endswith((".jpg", ".png", ".gif", ".bmp")):
                    shutil.move(file_path, os.path.join(self.directory, "Images", filename))
                    self.file_counts["Images"] += 1
                elif filename.endswith((".doc", ".docx", ".pdf", ".txt", ".xls", ".xlsx")):
                    shutil.move(file_path, os.path.join(self.directory, "Documents", filename))
                    self.file_counts["Documents"] += 1
                elif filename.endswith((".mp3", ".wav", ".flac")):
                    shutil.move(file_path, os.path.join(self.directory, "Musics", filename))
                    self.file_counts["Musics"] += 1
                elif filename.endswith((".mp4", ".avi", ".mov", ".mkv")):
                    shutil.move(file_path, os.path.join(self.directory, "Videos", filename))
                    self.file_counts["Videos"] += 1
                elif filename.endswith((".zip", ".rar", ".7z", ".tar", ".gz")):
                    shutil.move(file_path, os.path.join(self.directory, "Compressed", filename))
                    self.file_counts["Compressed"] += 1
                elif filename.endswith((".exe", ".msi")):
                    shutil.move(file_path, os.path.join(self.directory, "Programs", filename))
                    self.file_counts["Programs"] += 1
                else:
                    shutil.move(file_path, os.path.join(self.directory, "Others", filename))
                    self.file_counts["Others"] += 1
            elif os.path.isdir(file_path) and filename not in ["Images", "Documents", "Musics", "Videos", "Compressed", "Programs", "Others"]:
                shutil.move(file_path, os.path.join(self.directory, "Others", filename))
                self.file_counts["Others"] += 1

    def show_file_count(self):
        popup = tk.Toplevel(self.master)
        popup.title("File Counts")

        for folder, count in self.file_counts.items():
            label = tk.Label(popup, text=f"{folder}: {count}")
            label.pack(pady=5)

        ok_button = tk.Button(popup, text="OK", command=popup.destroy)
        ok_button.pack(pady=10)

root = tk.Tk()
app = FolderOrganizer(root)
root.mainloop()