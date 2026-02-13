# Licensed under the MIT License

import psutil
import tkinter as tk

def update_stats():
    cpu = psutil.cpu_percent(interval=0.1)
    mem = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    
# The space between statistics can be adjusted
    text = f"CPU: {cpu:.0f}%     RAM: {mem.used // 1024**2}MB / {mem.total // 1024**2}MB     SSD: {disk.used // 1024**3}GB / {disk.total // 1024**3}GB"
    label.config(text=text)
    
# Update every 1s
    root.after(1000, update_stats)  

def close_app():
    root.quit()

# Drag functions
def drag(event):
    root.drag_start_x = event.x_root
    root.drag_start_y = event.y_root

def drag_move(event):
    dx = event.x_root - root.drag_start_x
    dy = event.y_root - root.drag_start_y
    x = root.winfo_x() + dx
    y = root.winfo_y() + dy
    root.geometry(f"+{x}+{y}")
    root.drag_start_x = event.x_root
    root.drag_start_y = event.y_root

root = tk.Tk()
root.geometry("600x80")
root.configure(bg="black")

# No title bar if True:
root.overrideredirect(True)

# Button
button = tk.Button(root, text="x", fg="white", bg="black", relief="solid", bd=2, width=1, command=close_app)
button.pack(side='bottom')

# Drag Bar
drag_bar = tk.Canvas(root, bg="black", highlightthickness=0, height=10, width=450)
drag_bar.create_line(0, 5, 450, 5, fill="white")  
drag_bar.pack(side='top', pady=1, anchor='n')  
drag_bar.bind("<Button-1>", drag)
drag_bar.bind("<B1-Motion>", drag_move)

label = tk.Label(root, text="", fg="white", bg="black", font=("Arial", 11))
label.pack(expand=True, fill='both')

update_stats()  
root.mainloop()
