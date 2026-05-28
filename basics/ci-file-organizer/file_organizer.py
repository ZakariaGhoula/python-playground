# ci-file_organizer.py
import os
import shutil


# ask folder to organize
target_folder = input("Enter the name of folder to organize: ")

# Define mapping of file extensions to folder names
file_types = {
    "images":['.jpg','.jpeg', '.png','.gif'],
    "documents":['.pdf', '.txt', '.doc', '.xls', '.docs', '.xlsx'],
    "videos":['.mp4', '.avi', '.mkv'],
    "compressed":['.zip', '.rar', '.7z'],
    "app":['.exe', '.msi', '.dmg']
}

# create directories if not exist
for folder in file_types.keys():
    folder_path = os.path.join(target_folder, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# split files by extension and move to folder
for filename in os.listdir(target_folder):
    file_path = os.path.join(target_folder, filename)
    # Skip if it's a folder
    if os.path.isdir(file_path):
        continue

    #get extension of dile
    root, ext = os.path.splitext(filename)

    moved = False

    for folder, extensions in file_types.items():
        if ext.lower() in extensions:
            dest_path = os.path.join(target_folder, folder, filename)
            #move files
            shutil.move(file_path, dest_path)
            moved = True
            break

    if not moved:
        print(f"⚠️ Skipped: {filename} (Unknown file type)")
