import os
import shutil
from PIL import Image
folder_path = "/storage/emulated/0/photo"
backup_folder = os.path.join(folder_path, "backup")
os.makedirs(backup_folder, exist_ok=True)
newsize = (500, 500)
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    if not filename.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')):
        continue
    if "backup" in file_path:
        continue
    backup_path = os.path.join(backup_folder, filename)
    shutil.copy2(file_path, backup_path)
    print(f"Backed up: {filename}")
    with Image.open(file_path) as img:
        print("Original size:", img.size)
        img.thumbnail(newsize) 
        img.save(file_path)
        print("Resized size:", img.size)
        print("------")
