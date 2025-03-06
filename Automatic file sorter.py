import os, shutil
path = r"/Users/akshaykanchibail/Documents/Python Project/Automatic File Sorter/"

file_name = os.listdir(path)
print(file_name)

folder_names = ['csv files', 'text files', 'image files', 'coding files','excel files',]

for folder in folder_names:
    folder_path = os.path.join(path, folder)  # Create full path

    if not os.path.exists(folder_path):  # Check if folder exists
        print(f"Creating folder: {folder_path}")
        os.makedirs(folder_path, exist_ok=True)  # Create folder safely
    else:
        print(f"Folder already exists: {folder_path}")

# Moving files based on their extensions
for file in file_name:

    # Moving .csv files to "csv files"
    if file.endswith(".csv") and not os.path.exists(os.path.join(path, "csv files", file)):
        shutil.move(os.path.join(path, file), os.path.join(path, "csv files", file))
        print(f"Moved: {file} → csv files/")

    # Moving .txt files to "txt files"
    elif file.endswith(".txt") and not os.path.exists(os.path.join(path, "text files", file)):
        shutil.move(os.path.join(path, file), os.path.join(path, "text files", file))
        print(f"Moved: {file} → text files/")

    # Moving .png files to "image files"
    elif file.endswith(".png") and not os.path.exists(os.path.join(path, "image files", file)):
        shutil.move(os.path.join(path, file), os.path.join(path, "image files", file))
        print(f"Moved: {file} → image files/")

    # Moving .java and .sql files to "coding files"
    elif (file.endswith(".java") or file.endswith(".sql")) and not os.path.exists(os.path.join(path, "coding files", file)):
        shutil.move(os.path.join(path, file), os.path.join(path, "coding files", file))
        print(f"Moved: {file} → coding files/")

    # Moving .xlsx files to "excel files"
    elif file.endswith(".xlsx") and not os.path.exists(os.path.join(path, "excel files", file)):
        shutil.move(os.path.join(path, file), os.path.join(path, "excel files", file))
        print(f"Moved: {file} → excel files/")
    
