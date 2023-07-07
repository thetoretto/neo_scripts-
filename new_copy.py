import os
import shutil

# Function to get the list of PDF files in a folder and its subfolders


def get_pdf_files_in_folder(folder):
    pdf_files = []
    for root, _, filenames in os.walk(folder):
        for filename in filenames:
            if filename.lower().endswith('.pdf'):
                pdf_files.append(os.path.join(root, filename))
    return pdf_files


# Get folder paths from user
folder1 = input("Enter the path to folder 1: ")
folder2 = input("Enter the path to folder 2: ")

# Get the list of PDF files in folder 1 and its subfolders
pdf_files_in_folder1 = get_pdf_files_in_folder(folder1)

# Get the list of files in folder 2 (only files in a single folder)
files_in_folder2 = []
for file_name in os.listdir(folder2):
    if os.path.isfile(os.path.join(folder2, file_name)):
        files_in_folder2.append(file_name)

# Find PDF files in folder 1 that are not in folder 2
pdf_files_to_copy = []
duplicates = []
for file_path in pdf_files_in_folder1:
    file_name = os.path.basename(file_path)
    if file_name not in files_in_folder2:
        if file_name in duplicates:
            duplicates.remove(file_name)
        pdf_files_to_copy.append(file_path)
    else:
        duplicates.append(file_name)

# Display the number of PDF files that can be copied
print(f"{len(pdf_files_to_copy)} PDF file(s) can be copied from folder 1 to folder 2.")
if duplicates:
    print(f"The following PDF file(s) exist in both folders and won't be copied:")
    for file_name in duplicates:
        print(file_name)

# Ask the user if they want to proceed with the copying
choice = input("Do you want to copy the PDF files to folder 2? (y/n): ")

if choice.lower() == "y":
    # Perform the copying operation
    for file_path in pdf_files_to_copy:
        file_name = os.path.basename(file_path)
        destination_path = os.path.join(folder2, file_name)
        try:
            # Copy the file
            shutil.copy(file_path, destination_path)
            print(f"Successfully copied {file_name} to folder 2.")
        except Exception as e:
            print(f"Failed to copy {file_name}: {str(e)}")
else:
    print("Copying operation canceled.")
