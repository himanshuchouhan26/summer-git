import psutil
import time
import threading
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

upload_speeds = []
download_speeds = []
time_stamps = []

def get_network_usage():
    old_values = psutil.net_io_counters()
    while True:
        time.sleep(1)
        new_values = psutil.net_io_counters()

        upload_speed = (new_values.bytes_sent - old_values.bytes_sent) / 1024  # KB/s
        download_speed = (new_values.bytes_recv - old_values.bytes_recv) / 1024  # KB/s
        old_values = new_values

        if len(upload_speeds) >= 60:  
            upload_speeds.pop(0)
            download_speeds.pop(0)
            time_stamps.pop(0)

        upload_speeds.append(upload_speed)
        download_speeds.append(download_speed)
        time_stamps.append(len(time_stamps) + 1)

        update_gui(upload_speed, download_speed)

def update_gui(upload, download):
    upload_label.config(text=f"Upload Speed: {upload:.2f} KB/s")
    download_label.config(text=f"Download Speed: {download:.2f} KB/s")
    update_graph()

def update_graph():
    ax.clear()
    ax.plot(time_stamps, upload_speeds, label="Upload Speed (KB/s)", color="blue")
    ax.plot(time_stamps, download_speeds, label="Download Speed (KB/s)", color="red")
    ax.set_title("Network Bandwidth Usage")
    ax.set_xlabel("Time (seconds)")
    ax.set_ylabel("Speed (KB/s)")
    ax.legend()
    canvas.draw()

root = tk.Tk()
root.title("Network Bandwidth Monitor")
root.geometry("600x400")

upload_label = ttk.Label(root, text="Upload Speed: 0 KB/s", font=("Arial", 12))
upload_label.pack(pady=10)
download_label = ttk.Label(root, text="Download Speed: 0 KB/s", font=("Arial", 12))
download_label.pack(pady=5)

fig = Figure(figsize=(5, 3), dpi=100)
ax = fig.add_subplot(111)
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()

threading.Thread(target=get_network_usage, daemon=True).start()

root.mainloop()
