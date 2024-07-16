import os
import re
import shutil

import utils.logger as logger
from utils.validator import find_directories, validate_files

# Initialize logger.
log = logger.setup_logger("debug")
log.newline()

# Get the root directory/mod list.
root = input('Enter the modlist directory: ')
if not os.path.isdir(root):
    log.error('root directory does not exist.')
    exit()
log.debug(f'{root} has been set as modlist root directory.')
log.newline()

mods = input('Enter the mod/s that has parallax terrain: ')
mods = list(filter(None, re.split('"(.*?)"|\\s', mods)))
for mod in mods:

    if not os.path.isdir(root + "\\" + mod):
        log.warning(f'{mod} does not exist... Removing mod now.')
        mods.remove(mod)
        continue
    
    # Mod full directory.
    mod_dir = root + "\\" + mod
    log.debug(f'Processing {mod}...')
    textures_dir = find_directories(mod_dir)

    for dir in textures_dir:
        files = validate_files(dir)
        log.debug(f'{mod} : found {len(files)} files in the current directory...')
        if len(files) > 0:
            if os.path.isdir(dir + '\\parallax'):
                log.warning(f'{mod} : parallax folder already exists. Skipping directory...')
                continue
            
            os.makedirs(dir + '\\parallax')
            for file in files:
                log.debug(f'{mod} : copying {file} to {dir}\\parallax...')
                shutil.copy(dir + '\\' + file, dir + '\\parallax')
            
            log.debug(f'{mod} : finished copying {len(files)} files to {dir}\\parallax')

log.newline()
log.info('Terrain Parallax Blending Fix is now compatible with your specified mods!')