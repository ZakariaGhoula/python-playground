# ci-file-organizer.py
import os
import shutil

path = "./files"
# create directories
directories = ["images", "documents", "videos", "compressed", "app"]
for directory in directories:
    dir = path + '/' + directory
    if not os.path.exists(dir):
        os.makedirs(dir)

contents = os.listdir(path)
print("Directory contents:", contents)

# split files by extension and move to folder
for file in contents:
    source = path + "/" + file
    root, ext = os.path.splitext(path + "/" + file)
    if(ext ==''):
        continue
    match ext:
        case ".txt" | '.pdf':
            shutil.move(source, path + "/documents")
        case ".jpg" | ".jpeg" | ".png":
            shutil.move(source, path + "/images")
        case ".mp4" | ".avi" | ".mkv":
            shutil.move(source, path + "/videos")
        case ".zip" | ".rar" | ".7z":
            shutil.move(source, path + "/compressed")
        case ".exe" | ".msi" | ".dmg":
            shutil.move(source, path + "/app")
        case _:
            print(f"Unknown extension: {ext}")
