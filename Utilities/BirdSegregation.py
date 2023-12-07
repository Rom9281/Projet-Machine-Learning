import os
#The goal is to sort the bird datasets by number of files to cut the birds with too few files.


train_folder = "./Data/train"
folders = os.listdir(train_folder)
sorted_folders = sorted(folders, key=lambda folder: len(os.listdir(os.path.join(train_folder, folder))), reverse=True)

for folder in sorted_folders:
    folder_path = os.path.join(train_folder, folder)
    num_files = len(os.listdir(folder_path))
    print(f"{folder}: {num_files} files")
