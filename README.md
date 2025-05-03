# 🛰️ Net Scanify - Network Scanner Tool

**Net Scanify** is a Python-based tool that scans devices connected to your local network using ARP requests.  
Built with `scapy`, `tkinter`, and `pyfiglet`, it displays the IP, MAC address, and hostname of each device.  
The tool is fully cross-platform and works on **Windows**, **Linux (including Kali)** with minimal setup.

---

## 🎯 Features

- 🔍 Scans local network for connected devices (via ARP)
- 🖥️ Displays IP, MAC address, and hostname in a table
- 🎨 Styled GUI interface with ASCII-art header
- ⚙️ Works on both Linux (sudo) and Windows (Admin mode)
- 💡 Custom IP range input (no need to modify code)
- ✅ Auto dependency install script with Kali-Linux support

---

## ⚙️ Installation

### 🔧 Requirements

- Python 3.7 or higher
- Internet connection (for first-time install)

### 🐧 For Kali Linux / Ubuntu / Debian:

```bash
git clone https://github.com/v4vinaysihag/Net-Scanify.git
cd net-scanify
chmod +x install.sh
sudo ./install.sh
```

> 📦 This uses `--break-system-packages` to install Python packages in Kali safely.

---

## 🪟 For Windows

1. Clone or download this repo.
2. Open **Command Prompt as Administrator**
3. Run:
   ```bash
   pip install -r requirements.txt
   python net_scanner.py
   ```

---

## 🚀 Usage

Once installed, just run the main Python file:

```bash
python3 net_scanner.py
```

1. Enter the IP range (e.g. `192.168.1.0/24`)
2. Click “Scan Network”
3. View the connected devices with details

---

## 🛑 Permissions

- **Linux**: Run with `sudo`  
- **Windows**: Run as Administrator  

Otherwise, scanning may fail due to lack of permission for raw socket access.

---

## 📁 File Structure

```
net-scanify/
├── net_scanner.py          # Main GUI tool
├── install.sh              # Auto installer for Linux
├── requirements.txt        # Python dependencies
├── README.md               # This file
```

---

## 🧑‍💻 Author

Created by **Vinay Sihag**

---

## 💰 Donate (Optional)

If you like this tool, feel free to support development with a small donation:

**Bitcoin (BTC)**: `bc1quugt7kjpaff7vqqp5578msfvnm6w4udz60t3dr`

---

## 📜 License

This project is open-source and free for personal or educational use.

---
