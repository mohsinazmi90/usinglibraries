import shutil
from datetime import datetime
from pathlib import Path

today = datetime.now().strftime("%Y-%m-%d")
file_name = f"assignments/automation/archive_{today}"
copy_path = f"assignments/automation/archive_{today}_copy"

path = Path(file_name)
copy_path = Path(copy_path)
path.mkdir(exist_ok=True, parents=True)
copy_path.mkdir(parents=True, exist_ok=True)

for file in path.glob("*.pdf"):
    new_name = file.stem + "_copy" + file.suffix
    shutil.copy(file, copy_path / new_name)