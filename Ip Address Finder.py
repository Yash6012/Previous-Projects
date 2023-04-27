import tkinter as tk
from tkinter.messagebox import showinfo
import socket

win = tk.Tk()
win.config(bg = "#F1C40F")
win.title("Find IP Address")
def ip():
    hostname = socket.gethostname()
    ip_add = socket.gethostbyname(hostname)
    showinfo("IP Address",ip_add)
ip_button = tk.Button(win, text = "Show IP Address", bg = "#000000", fg = "#F1C40F", font = ("times new roman",16,"bold"), command = ip)
ip_button.pack()
win.mainloop()