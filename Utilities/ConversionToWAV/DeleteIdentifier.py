import os


def delete_files_with_identifier(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".Identifier"):
                file_path = os.path.join(root, file)
                os.remove(file_path)


TEST_DATA_PATH = '/home/rom1/convertion/test'

# Call the function to delete the files
delete_files_with_identifier(TEST_DATA_PATH)
