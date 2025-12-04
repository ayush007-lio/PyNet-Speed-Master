from tkinter import *
from tkinter.ttk import Progressbar
import speedtest
import threading

def run_speed_test():
    st = speedtest.Speedtest()
    download_speed = st.download() / 1_000_000
    upload_speed = st.upload() / 1_000_000
    ping = st.results.ping
    download_label.config(text=f"Download Speed: {download_speed:.2f} Mbps")
    upload_label.config(text=f"Upload Speed: {upload_speed:.2f} Mbps")
    ping_label.config(text=f"Ping: {ping:.2f} ms")

def threaded_speed_test():
    download_label.config(text="Testing Download Speed...")
    upload_label.config(text="")
    ping_label.config(text="")
    root.after(100, lambda: threading.Thread(target=run_speed_test).start())

root = Tk()
root.title("Network Speed Tester")
root.geometry("400x250")
root.config(bg="#282c34")

title_label = Label(root, text="Internet Speed Tester", font=("Helvetica", 20, "bold"), bg="#282c34", fg="#61dafb")
title_label.pack(pady=10)

download_label = Label(root, font=("Helvetica", 14), bg="#282c34", fg="#f5f5f5")
download_label.pack(pady=5)

upload_label = Label(root, font=("Helvetica", 14), bg="#282c34", fg="#f5f5f5")
upload_label.pack(pady=5)

ping_label = Label(root, font=("Helvetica", 14), bg="#282c34", fg="#f5f5f5")
ping_label.pack(pady=5)

test_btn = Button(root, text="Start Test", font=("Helvetica", 14, "bold"), bg="#61dafb", fg="#282c34", command=threaded_speed_test)
test_btn.pack(pady=10)

root.mainloop()
