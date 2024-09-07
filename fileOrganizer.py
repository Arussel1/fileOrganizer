#!/usr/bin/python3

import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

file_categories = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "JS/TS": [".ts", ".js"],
    "React": [".jsx", "tsx"],
    "HTML": [".html"],
    "Python": [".py"],
    "Java": [".java"]
}

def create_folders(directory):
    for category in file_categories:
        folder_path = os.path.join(directory, category)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            
def organize_files(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        if os.path.isdir(file_path):
            continue

        _, file_extension = os.path.splitext(filename)
        for category, extensions in file_categories.items():
            if file_extension.lower() in extensions:
                destination = os.path.join(directory, category, filename)
                try:
                    shutil.move(file_path, destination)
                    status_label.config(text=f"Moved: {filename} -> {category}")
                except Exception as e:
                    status_label.config(text=f"Error moving {filename}: {e}")

def select_directory():
    directory = filedialog.askdirectory()
    if directory:
        directory_entry.delete(0, tk.END)
        directory_entry.insert(0, directory)

def start_organizing():
    directory = directory_entry.get()
    if not os.path.exists(directory):
        messagebox.showerror("Error", "Please select a valid directory.")
        return

    create_folders(directory)
    organize_files(directory)
    messagebox.showinfo("Success", "Files organized successfully!")

root = tk.Tk()
root.title("File Organizer")

directory_entry = tk.Entry(root, width=50)
directory_entry.pack(pady=10)

select_button = tk.Button(root, text="Select Directory", command=select_directory)
select_button.pack(pady=5)

organize_button = tk.Button(root, text="Organize Files", command=start_organizing)
organize_button.pack(pady=20)

status_label = tk.Label(root, text="", fg="green")
status_label.pack(pady=10)

root.mainloop()

