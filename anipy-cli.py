#!/bin/python
import sys

from anipy_cli import cli
from anipy_cli.misc import keyboard_inter

if __name__ == '__main__':
    try:
        cli.main()
    except KeyboardInterrupt:
        keyboard_inter()