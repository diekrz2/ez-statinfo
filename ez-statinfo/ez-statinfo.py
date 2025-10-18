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

def close_app():
    root.quit()

root = tk.Tk()
root.geometry("600x80")
root.configure(bg="black")

# No title bar if True:
root.overrideredirect(True)

label = tk.Label(root, text="", fg="white", bg="black", font=("Arial", 11))
label.pack(expand=True, fill='both')

# Button
button = tk.Button(root, text="x", fg="white", bg="black", relief="solid", bd=2, width=1, command=close_app)
button.pack(side='bottom')

update_stats()  
root.mainloop()
