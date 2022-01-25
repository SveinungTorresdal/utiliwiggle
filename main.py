from obs_menu import *
from os import walk

filenames = next(walk('./assets/wiggles'), (None, None, []))[2]  # [] if no file

print(filenames)