import os
import shutil
import filecmp


def copy_unique_pdfs(source_folder, destination_folder):
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            if file.endswith(".pdf"):
                source_file = os.path.join(root, file)
                destination_file = os.path.join(destination_folder, file)

                if not os.path.exists(destination_file) or not filecmp.cmp(source_file, destination_file):
                    shutil.copy2(source_file, destination_file)
                    print(f"Copied: {source_file} to {destination_file}")
                else:
                    print(f"Ignored duplicate file: {source_file}")


# Ask the user to input source and destination folders
source_folder = input("Enter the source folder: ")
destination_folder = input("Enter the destination folder: ")

copy_unique_pdfs(source_folder, destination_folder)
