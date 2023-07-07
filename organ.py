import os
import shutil

source_folder = r'D:\123\test'
destination_folder = r'D:\123\organized'

# Create the destination folder if it doesn't exist
os.makedirs(destination_folder, exist_ok=True)

# Define the mappings of file names to destination folders
file_mappings = {
    'OP10  ': '2009-2010',
    'OP11  ': '2010-2011',
    'OP12  ': '2011-2012',
    'OP13  ': '2012-2013',
    'OP14  ': '2013-2014',
    'OP15  ': '201-2015',
    'OP16  ': '2015-2016'
}

# Iterate through the files in the source folder
for file_name in os.listdir(source_folder):
    if file_name.endswith('.pdf'):
        # Extract the file prefix
        file_prefix = file_name[:6]

        # Check if the file prefix matches any of the mappings
        if file_prefix in file_mappings:
            # Create the destination folder if it doesn't exist
            destination_subfolder = os.path.join(
                destination_folder, file_mappings[file_prefix])
            os.makedirs(destination_subfolder, exist_ok=True)

            # Move the file to the destination folder
            source_path = os.path.join(source_folder, file_name)
            destination_path = os.path.join(destination_subfolder, file_name)
            shutil.move(source_path, destination_path)
        else:
            # Move the file to the 'others' folder
            others_folder = os.path.join(destination_folder, 'others')
            os.makedirs(others_folder, exist_ok=True)

            source_path = os.path.join(source_folder, file_name)
            destination_path = os.path.join(others_folder, file_name)
            shutil.move(source_path, destination_path)
