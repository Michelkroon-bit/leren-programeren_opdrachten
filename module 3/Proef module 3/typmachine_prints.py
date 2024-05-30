from data import *
import sys
import time

import sys
import time
from colorama import init
from termcolor import colored

init()

colors = ['red', 'yellow', 'green', 'cyan', 'blue', 'magenta']

def rainbow_typemachine_print(prompt):
    for i, x in enumerate(prompt):
        color = colors[i % len(colors)]
        print(colored(x, color), end='')
        sys.stdout.flush()
        time.sleep(0.05)
    return prompt

def fast_typemachine_print(prompt):
    for i, x in enumerate(prompt):
        color = colors[i % len(colors)]
        print(colored(x, color), end='')
        sys.stdout.flush()
        time.sleep(0.01)
    return prompt