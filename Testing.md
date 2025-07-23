“This tool is for educational, ethical hacking, and research purposes only. Do not use on systems you don’t own or have permission to test.”

# 🧪 Testing Guide – Stealth USB Data Exfiltration Tool

This document outlines how to safely test the Stealth USB Data Exfiltration Tool in a controlled, ethical lab environment.

---

## ✅ Recommended Testing Environment

- Use a **Windows Virtual Machine (VM)** (e.g., VirtualBox, VMware Workstation)
- OS: Windows 10/11 (or 7 for full autorun testing)
- Disable internet/network access for isolated testing
- Create a snapshot of the VM before beginning

---

## ⚙️ Python Requirements

- Python 3.8+
- Required Python modules (install using `pip install -r requirements.txt`):

pyautogui,
pynput,
cryptography



---

## 📂 USB File Structure (Place All in USB Root)

usbthief.py # Main data exfiltration payload

autorun.bat # Launches VBScript invisibly

autorun.inf # Triggers autorun.bat (legacy support)

invisible.vbs # Runs Python script in hidden window

clear_logs.bat # Clears event and history logs


---

## 🚀 Execution Steps

1. **Prepare USB Drive**
   - Format as FAT32 or NTFS
   - Copy all files to the USB root directory

2. **Insert USB into Target VM**
   - On legacy systems (Windows 7), `autorun.inf` may auto-launch `autorun.bat`
   - On modern systems, manually double-click `autorun.bat` once inserted

3. **Script Execution Flow**
   - `autorun.bat` → launches `invisible.vbs`
   - `invisible.vbs` → runs `usbthief.py` silently
   - `usbthief.py`:
     - Extracts Wi-Fi passwords
     - Takes screenshot
     - Dumps clipboard
     - Copies target files (e.g., `.docx`, `.pdf`)
     - Saves all data back to the USB
   - `clear_logs.bat` can be run last to erase system traces (optional)

---

## 🧠 Behavior Monitoring (Optional Tools)

Use inside VM to observe and understand payload behavior:

| Tool         | Purpose                        |
|--------------|--------------------------------|
| Process Hacker | View process tree and stealth |
| ProcMon        | Monitor file and registry actions |
| Wireshark      | Analyze for potential exfiltration attempts |

---

## ⚠️ Disclaimer

> This project is for **educational and research purposes only**.  
> Never test on devices, systems, or networks without **explicit permission**.  
> The creator is **not liable** for any misuse.

