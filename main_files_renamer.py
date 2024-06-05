import os
import tkinter as tk
from tkinter import filedialog

def rename_files():
    # Get the selected directory
    directory = directory_entry.get()
    
    # Get the word to remove from the filenames
    word_to_remove = word_entry.get()
    
    # Loop through all the files in the selected directory
    for filename in os.listdir(directory):
        # Check if the file starts with the specified word
        if filename.startswith(word_to_remove):
            # Remove the specified word from the filename
            new_filename = filename[len(word_to_remove):]
            
            # Construct the full path of the old and new filenames
            old_path = os.path.join(directory, filename)
            new_path = os.path.join(directory, new_filename)
            
            # Rename the file
            os.rename(old_path, new_path)
            print(f"Renamed {filename} to {new_filename}")
    
    print("File renaming completed.")

# Create the main window
root = tk.Tk()
root.title("File Renamer")

# Create a label and entry field for the directory
directory_label = tk.Label(root, text="Select Directory:")
directory_label.pack()
directory_entry = tk.Entry(root)
directory_entry.pack()
directory_button = tk.Button(root, text="Browse", command=lambda: directory_entry.insert(0, filedialog.askdirectory()))
directory_button.pack()

# Create a label and entry field for the word to remove
word_label = tk.Label(root, text="Word to Remove:")
word_label.pack()
word_entry = tk.Entry(root)
word_entry.pack()

# Create a button to start the renaming process
rename_button = tk.Button(root, text="Rename Files", command=rename_files)
rename_button.pack()

# Start the GUI event loop
root.mainloop()