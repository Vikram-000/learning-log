import os
import shutil

def select_folder():
    path = input("Enter the path of the folder you want to organize: ")
    if os.path.isdir(path):
        return path
    else:
        print("Invalid folder path")
        return None

PATH = select_folder() # Globally Declared PATH 

def move_files(source, destination):
    shutil.move(source ,destination)

def group_files():
    img = [".jpeg", ".jpg", ".png", ".gif"]
    vid = [".mp4", ".mov"]
    doc = [".docx", ".txt", ".doc", ".pdf"]
    aud = [".mp3", ".wav"]

    try:
        files = os.listdir(PATH)
        print(f"{len(files)} files are detected")

        for file in files:
            file_path = os.path.join(PATH, file)

            if not os.path.isfile(file_path):
                continue

            _, extension = os.path.splitext(file)
            extension = extension.lower()

            if extension in img:
                folder = "Image"
            elif extension in vid:
                folder = "Video"
            elif extension in doc:
                folder = "Document"
            elif extension in aud:
                folder = "Audio"
            else:
                folder = "Others"
            
            destination = os.path.join(PATH, folder)
            os.makedirs(destination, exist_ok=True)
            move_files(file_path, destination)

    except Exception as e:
        print(f"Error: {e}")



group_files()


