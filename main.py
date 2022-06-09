import os
from utils import *
from gui import *


"""
 - by default, select top, bottom and shoes
 - option to also select a hat, outerwear and n accessories
 - return images of selected items for the fit
"""

if __name__ == "__main__":

    main_path = "./clothes"
    if not os.path.exists(main_path):
        os.mkdir(main_path)

    hats_path = main_path + "/hats"
    if not os.path.exists(hats_path):
        os.mkdir(hats_path)

    top_path = main_path + "/top"
    if not os.path.exists(top_path):
        os.mkdir(top_path)

    outerwear_path = main_path + "/outerwear"
    if not os.path.exists(outerwear_path):
        os.mkdir(outerwear_path)

    bottom_path = main_path + "/bottom"
    if not os.path.exists(bottom_path):
        os.mkdir(bottom_path)

    shoes_path = main_path + "/shoes"
    if not os.path.exists(shoes_path):
        os.mkdir(shoes_path)

    accessories_path = main_path + "/accessories"
    if not os.path.exists(accessories_path):
        os.mkdir(accessories_path)

    gui()
