# Licensed under the MIT License

import psutil
import tkinter as tk

def update_stats():
    cpu = psutil.cpu_percent(interval=0.1)
    mem = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    text = f"CPU: {cpu:.0f}%    RAM: {mem.used // 1024**2}MB / {mem.total // 1024**2}MB    SSD: {disk.used // 1024**3}GB / {disk.total // 1024**3}GB"
    label.config(text=text)
# Update every 1s
    root.after(1000, update_stats)  

root = tk.Tk()
root.title("Easy System Info")
root.geometry("600x50")
root.configure(bg="black")

label = tk.Label(root, text="", fg="white", bg="black", font=("Arial", 11))
label.pack(expand=True)

update_stats()  
root.mainloop()
