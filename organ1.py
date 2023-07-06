# creating  folders but not copying the files


import os
import shutil

source_folder = r'D:\123\test'
destination_folder = r'D:\123\organized'

# Create destination folders if they don't exist
folders = {
    'OP10': '2009-2010',
    'OP11': '2010-2011',
    'OP13': '2011-2012',
    'OP14': '2012-2013',
    'OP15': '2013-2014',
    'OP16': '2014-2015',
    'OP17': '2015-2016'
}

for folder_name in folders.values():
    folder_path = os.path.join(destination_folder, folder_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# Iterate through the source folder and its subfolders
for root, _, files in os.walk(source_folder):
    for file_name in files:
        file_path = os.path.join(root, file_name)
        if len(file_name) >= 4:
            # Extract the last 4 digits of the file name
            suffix = file_name[-6:-2]
            if suffix in folders:
                destination_path = os.path.join(
                    destination_folder, folders[suffix])
            else:
                destination_path = os.path.join(destination_folder, 'others')
            if not os.path.exists(destination_path):
                os.makedirs(destination_path)
            shutil.move(file_path, destination_path)
