__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

#import modules
import os
from zipfile import ZipFile

#clean cache
current_dir = os.getcwd()
add_files = 'files'
add_cache = 'cache'
cache_dir = os.path.join(current_dir, add_files, add_cache)

def clean_cache():
    if not os.path.isdir(cache_dir):
        os.makedirs(cache_dir)
    if os.path.exists(cache_dir):
        for files in os.listdir(cache_dir):
            os.remove(os.path.join(cache_dir, files))

clean_cache()

#unpack zip in cache folder
zip_folder = "files/data.zip"
zip_dir = os.path.join(current_dir, zip_folder)

def cache_zip(zip_dir, cache_dir):
    with ZipFile(zip_dir, "r") as zipfolder:
        zipfolder.extractall(cache_dir)

cache_zip(zip_dir, cache_dir)

#list of files in cache
def cached_files():
    list_of_files = []
    abs_path = os.path.abspath("files\cache")
    files = os.listdir(abs_path)
    for file in files:
        file_path = os.path.join(abs_path, file)
        if os.path.isfile(file_path):
            if not file_path in list_of_files:
                list_of_files.append(file_path)
    return list_of_files

def find_password(list_of_files):
    for file in list_of_files:
        with open(file, 'r') as content:
            lines = content.readlines()
            for file in lines:
                if "password" in file:
                    password = file[file.find(" ")+1:file.find("\\n")]
                    return password

find_password(cached_files())