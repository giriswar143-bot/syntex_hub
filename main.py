import os
import shutil

from numpy import rint

directory=os.path.join(os.pathexpanduser("~"),"Documents",) 

extensions = {
    ".jpg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".mp4": "Videos",
    ".mov": "Videos",
    ".doc": "Documents",
    ".pdf": "Documents",
    ".txt": "Documents",
    ".mp3": "music",
    ".wav": "music"
}


for filename in os.listdir(directory):
    file_path = os.path.join(directory, filename)

    if os.path.isfile(file_path):
        extension = os.path.splitext(filename)[1].lower()

        if extension in extensions:
            folder_name = extensions[extension]
            folder_path = os.path.join(directory, folder_name)
            os.makedirs(folder_path,exist_ok=True)
            
            destination_path = os.path.join(folder_path, filename)
            shutil.move(file_path, destination_path)

            print(f"moved {filename} to {folder_name} folder.")
        else:
            print(f"skipped {filename}.unknown file extension.")
    else:
        print(f"skipped {filename}. it is a directory.")

print("file organization cmpleted.")
        
        