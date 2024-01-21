import os, zipfile

dir_name = "CHANGE THIS TO WHERE YOU STORED THE .ZIP FILE"
extract_to = "CHANGE THIS TO WHERE YOU WANT THE .ZIP FILE TO BE EXTRACTED"
extension = ".zip"

os.chdir(dir_name) # change directory from working dir to dir with files

for item in os.listdir(dir_name):
    if item.endswith(extension):
        file_name = os.path.abspath(item)
        try:
            with zipfile.ZipFile(file_name) as zip_ref:
                zip_ref.extractall(extract_to)
            print(f"Extracted '{item}' to '{extract_to}'.")
        except zipfile.BadZipFile:
            print(f"Skipping '{item}' as it is a corrupt zip file.")
        except Exception as e:
            print(f"An error occurred while processing '{item}': {e}")

        # Remove the zipped file
        os.remove(file_name)