import os
import zipfile
from dotenv import load_dotenv
env_path = os.path.join('.env')
load_dotenv(dotenv_path=env_path)
version = os.environ['VERSION']

'''
General flow:
1. Delete all files from the directories to make sure we are working with the correct updated files
2. Create text files and store them inside txt dir
3. Check the txt files were created successfully
4. Created zip files with the text files inside
5. Check the zip files were created successfully

If at any point one of the functions fail, they return False and update the state variable,
if the state variable is false it will exit(1)
if the program finishes successfully it will exit(0)

'''

# Delete all zip and text files to make sure the files we use are updated properly
def delete_all_files():
    try:
        for file_name in os.listdir("txt"):
            path = os.path.join("txt", file_name)
            if os.path.exists(path):
                os.remove(path)
        for file_name in os.listdir("zip"):
            path = os.path.join("zip", file_name)
            if os.path.exists(path):
                os.remove(path)
        return True
    except:
        return False

# Checking that files were successfully created
def check_files_exist(folder, names_array):
    for name in names_array:
        path = f"{folder}/{name}.txt" if folder == "txt" else f"{name}_{version}.zip"
        file_check = os.path.isfile(path)
        if file_check is False:
            return False
    return True

# Create txt files and store them inside txt dir
def create_text_files(names_array):
    if (not os.path.exists("txt")):
        os.mkdir("txt")
    for name in names_array:
        try:
            with open(f"txt/{name}.txt", 'w') as f:
                f.write(f"This is a text file with the name {name}.txt")

        except FileNotFoundError as error:
            print(f"This is the error {error} for file {name}.txt")

# Create zip files and store them insid zip dir
def create_zip_files(names_array):
    if (not os.path.exists("zip")):
        os.mkdir("zip")
    for name in names_array:
        with zipfile.ZipFile(f"{name}_{version}.zip", 'w') as zip_file:

            text_file_path = f"{name}.txt"
            zip_file_path = f"zip/{name}_{version}.zip" 
            zip_file.write(
                f"txt/{text_file_path}", arcname=os.path.basename(text_file_path))

if __name__ == "__main__":
    state = True
    file_names_array = ["a", "b","c", "d"]

    while state:
        state = delete_all_files()
        state = create_text_files(file_names_array)
        state = check_files_exist("txt", file_names_array) # If one of the txt files doesn't exist, state = False
        state = create_zip_files(file_names_array)
        state = check_files_exist("zip", file_names_array) # If one of the zip files doesn't exist, state = False
        exit(0)
    else:
        print(f"Script failed -> State became false: {state}")
        exit(1)
   
