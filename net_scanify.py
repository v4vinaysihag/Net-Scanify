import socket
import platform
import os
import ctypes
import tkinter as tk
from tkinter import ttk, messagebox
import pyfiglet
import urllib.request

# External dependency
try:
    from mac_vendor_lookup import MacLookup
except ImportError:
    os.system('pip install mac_vendor_lookup scapy pyfiglet')
    from mac_vendor_lookup import MacLookup

import scapy.all as scapy

def check_permissions():
    if platform.system() == 'Linux':
        if os.geteuid() != 0:
            return False
    elif platform.system() == 'Windows':
        try:
            return ctypes.windll.shell32.IsUserAnAdmin() != 0
        except:
            return False
    return True

def get_public_ip():
    try:
        return urllib.request.urlopen('https://api.ipify.org').read().decode('utf8')
    except:
        return "Unable to fetch"

def get_mac_vendor(mac):
    try:
        vendor = MacLookup().lookup(mac)
    except:
        vendor = "Unknown Vendor"
    return vendor

def scan(ip_range):
    arp_request = scapy.ARP(pdst=ip_range)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = broadcast / arp_request
    answered, _ = scapy.srp(packet, timeout=2, verbose=False)

    clients = []
    for sent, received in answered:
        ip = received.psrc
        mac = received.hwsrc
        vendor = get_mac_vendor(mac)
        clients.append((ip, mac, vendor))
    return clients

def run_scan():
    ip_range = ip_entry.get()
    if not ip_range:
        messagebox.showwarning("Missing IP", "Please enter the IP range (e.g., 192.168.1.0/24).")
        return

    for i in tree.get_children():
        tree.delete(i)

    results = scan(ip_range)
    for device in results:
        tree.insert("", tk.END, values=device)

# GUI Setup
root = tk.Tk()
root.title("Net Scanify - By Vinay Sihag")
root.geometry("750x600")
root.configure(bg="black")

ascii_banner = pyfiglet.figlet_format("Net Scanify")
banner_label = tk.Label(root, text=ascii_banner, fg="cyan", bg="black", font=("Courier", 10), justify="left")
banner_label.pack()

credit = tk.Label(root, text="== Created by Vinay Sihag ==", fg="green", bg="black", font=("Arial", 10, "bold"))
credit.pack()

public_ip = get_public_ip()
public_ip_label = tk.Label(root, text=f"Your Public IP: {public_ip}", fg="yellow", bg="black", font=("Arial", 10, "bold"))
public_ip_label.pack(pady=(0, 10))

# Manual IP Entry
ip_label = tk.Label(root, text="Enter IP Range (e.g., 192.168.1.0/24):", fg="white", bg="black", font=("Arial", 10))
ip_label.pack()
ip_entry = tk.Entry(root, width=30, font=("Arial", 12))
ip_entry.pack(pady=5)

scan_btn = tk.Button(root, text="Scan Network", font=("Arial", 12, "bold"), bg="cyan", command=run_scan)
scan_btn.pack(pady=10)

columns = ("IP Address", "MAC Address", "Vendor")
tree = ttk.Treeview(root, columns=columns, show="headings", height=10)
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, anchor="center", width=220)
tree.pack(pady=10)

# Permission check
if not check_permissions():
    messagebox.showerror("Permission Error", "Please run as Administrator (Windows) or with sudo (Linux).")
    root.destroy()

root.mainloop()
