import os
import PySimpleGUI as sg
from utils import *
from matplotlib import pyplot as plt


def gui():
    sg.theme('DarkPurple')

    left_column = [
        [sg.Text("Epic fit generator 3k", justification="center", size=(25, 1), font=("bitstream charter", 24))],
        [sg.Checkbox("Hat", key="hat_bool", font=("bitstream charter", 12))],
        [sg.Checkbox("Outerwear", key="outerwear_bool", font=("bitstream charter", 12))],
        [sg.Input(key="n_tops", size=(2, 1)), sg.Text('Number of tops', font=("bitstream charter", 12))],
        [sg.Input(key="n_accessories", size=(2, 1)), sg.Text('Number of accessories', font=("bitstream charter", 12))],
        [sg.Button("Generate sick fit", font=("bitstream charter", 12))]
    ]

    right_column = [
        [sg.Checkbox("  Lock Hat", key="lock_hat_bool", font=("bitstream charter", 12))],
        [sg.Checkbox("  Lock Outerwear", key="lock_outerwear_bool", font=("bitstream charter", 12))],
        [sg.Checkbox("  Lock Top(s)", key="lock_tops_bool", font=("bitstream charter", 12))],
        [sg.Checkbox("  Lock Bottom", key="lock_bottom_bool", font=("bitstream charter", 12))],
        [sg.Checkbox("  Lock Shoes", key="lock_shoes_bool", font=("bitstream charter", 12))],
        [sg.Checkbox("  Lock Accessories", key="lock_accessories_bool", font=("bitstream charter", 12))],
        [sg.Button("EXIT", font=("bitstream charter", 12))]
    ]

    layout = [
        [
            sg.Column(left_column),
            sg.VSeperator(),
            sg.Column(right_column),
        ]
    ]

    # Create the window
    window = sg.Window("Demo", layout)

    # print len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])
    tops_dir = "./clothes/top"
    max_n_tops = len([name for name in os.listdir(tops_dir) if os.path.isfile(os.path.join(tops_dir, name))])

    accessories_dir = "./clothes/accessories"
    max_n_accessories = len([name for name in os.listdir(accessories_dir) if os.path.isfile(os.path.join(accessories_dir, name))])

    sampled_articles_paths = {
        'hat': None,
        'top': None,
        'bottom': None,
        'shoes': None,
        'outerwear': None,
        'accessories': None
    }

    # Create an event loop
    while True:
        event, values = window.read()
        # End program if user closes window or
        # presses the OK button
        if event == "EXIT" or event == sg.WIN_CLOSED:
            break

        if event == "Generate sick fit":
            n_tops = values['n_tops']
            if n_tops == '':
                n_tops = 1   # a fit always has at least 1 top
            else:
                # TODO: instead of printing, have a pop un window
                try:
                    # TODO: Verify that the value entered is <= number of img files in ./clothes/top
                    n_tops = int(n_tops)
                except:
                    print("n_tops needs to be an int")

            n_accessories = values['n_accessories']
            if n_accessories == '':
                n_accessories = 0
            else:
                # TODO: instead of printing, have a pop un window
                try:
                    # TODO: Verify that the value entered is <= number of img files in ./clothes/accessories
                    n_accessories = int(n_accessories)
                except:
                    print("n_accessories needs to be an int")

            # get variables
            hat_bool = values['hat_bool']
            outerwear_bool = values['outerwear_bool']

            lock_hat_bool = values['lock_hat_bool']
            lock_outerwear_bool = values['lock_outerwear_bool']
            lock_tops_bool = values['lock_tops_bool']
            lock_bottom_bool = values['lock_bottom_bool']
            lock_shoes_bool = values['lock_shoes_bool']
            lock_accessories_bool = values['lock_accessories_bool']

            # sample clothes
            if hat_bool:
                if sampled_articles_paths['hat'] is None:
                    sampled_articles_paths['hat'] = sample_items('hat', n_samples=1)   # sample a hat
                elif lock_hat_bool and sampled_articles_paths['hat'] is not None:
                    pass   # dont sample a hat
                else:
                    sampled_articles_paths['hat'] = sample_items('hat', n_samples=1)   # sample a hat
            else:
                pass   # dont sample a hat

            if outerwear_bool:
                if sampled_articles_paths['outerwear'] is None:
                    sampled_articles_paths['outerwear'] = sample_items('outerwear', n_samples=1)   # sample an outerwear
                elif lock_outerwear_bool and sampled_articles_paths['outerwear'] is not None:
                    pass   # dont sample an outerwear
                else:
                    sampled_articles_paths['outerwear'] = sample_items('outerwear', n_samples=1)   # sample a hat
            else:
                pass   # dont sample an aouterwear

            if not lock_tops_bool or sampled_articles_paths['top'] is None:
                sampled_articles_paths['top'] = sample_items('top', n_samples=n_tops)

            if not lock_bottom_bool or sampled_articles_paths['bottom'] is None:
                sampled_articles_paths['bottom'] = sample_items('bottom', n_samples=1)

            if not lock_shoes_bool or sampled_articles_paths['shoes'] is None:
                sampled_articles_paths['shoes'] = sample_items('shoes', n_samples=1)

            if not lock_accessories_bool or sampled_articles_paths['accessories'] is None:
                sampled_articles_paths['accessories'] = sample_items('accessories', n_samples=n_accessories)

            show_fit(sampled_articles_paths)

    window.close()