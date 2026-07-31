import os
import shutil  # USED AS AN AUTOMATION SCRIPT
from datetime import datetime  # HELPS ARCHIVE FILES

# EXAMPLE LOGIC: MOVE A REPORT INTO A DATED ARCHIVE FOLDER
today = datetime.now().strftime("%Y-%m-%d %H:%M")
archive_dir = f"archive_{today}"
os.makedirs(archive_dir, exist_ok=True)
