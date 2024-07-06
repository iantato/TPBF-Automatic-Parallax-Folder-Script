import os

import constants.locations as locations
import constants.textures as textures

def find_directories(directory: str, existing_dir: list[str] = []):
    
    directories = os.listdir(directory)
    for dir in directories:
        if dir in locations.LOCATIONS:
            existing_dir.append(directory + "\\" + dir)
            find_directories(directory + "\\" + dir, existing_dir)
    
    return sorted(existing_dir)[1:]

def validate_files(directory: str):

    all_files = os.listdir(directory) + textures.TEXTURES + textures.textures_lowered
    gen_files = list(set(i for i in all_files if all_files.count(i) > 1))
    
    return gen_files