import os
import shutil

source_folder = r'D:\123\test'
destination_folder = r'D:\123\organized'

# Create destination folders if they don't exist
folders = ['2009-2010', '2010-2011', '2011-2012', '2012-2013',
           '2013-2014', '2014-2015', '2015-2016', 'others']
for folder in folders:
    folder_path = os.path.join(destination_folder, folder)
    os.makedirs(folder_path, exist_ok=True)

# Traverse through the source folder and its subfolders
for root, dirs, files in os.walk(source_folder):
    for file in files:
        file_name = os.path.join(root, file)
        file_year = file[-8:-4]  # Extract the last 4 digits of the file name

        if file_year == 'OP10':
            destination_path = os.path.join(
                destination_folder, '2009-2010', file)
        elif file_year == 'OP11':
            destination_path = os.path.join(
                destination_folder, '2010-2011', file)
        elif file_year == 'OP13':
            destination_path = os.path.join(
                destination_folder, '2011-2012', file)
        elif file_year == 'OP14':
            destination_path = os.path.join(
                destination_folder, '2012-2013', file)
        elif file_year == 'OP15':
            destination_path = os.path.join(
                destination_folder, '2013-2014', file)
        elif file_year == 'OP16':
            destination_path = os.path.join(
                destination_folder, '2014-2015', file)
        else:
            destination_path = os.path.join(destination_folder, 'others', file)

        shutil.move(file_name, destination_path)
