# -*- coding: utf-8 -*-
# 2023 David Quezada, Krakow, Poland
# email [dqreator@gmail.com]
import sys
from pathlib import Path
import argparse
from  matplotlib.backends.backend_qt5agg  import  ( NavigationToolbar2QT  as  NavigationToolbar ) 


# Define log
import logging as log 
log.basicConfig(format='[%(levelname)s]: %(message)s', level=log.INFO)

# Import the modules of my directory
curr_dir = Path(__file__).parent.resolve()
module_dir = curr_dir / 'src'
sys.path.insert(0, str(module_dir))
module_dir = curr_dir / 'gui'
sys.path.insert(0, str(module_dir))

from strings import parser_strings
from fkgui_qt import *
from application import *

def parser_function():
    """This function define the parser with all the possible arguments.
    Returns:
        pars.parse_args(): return the arguments given. 
    """
    pars = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter, description=parser_strings['main_description'])
    pars.add_argument('-d','--date', help=parser_strings['date_description'])

    return pars.parse_args()

def proces_args(args):
    """Function parsing command line arguments"""
    pass
    return args

def main(args):
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = application(MainWindow)
    MainWindow.show()
    app.exec_()

if __name__ == '__main__':
    try:
        log.info("The FK-GUI has been launched!")
        args = parser_function()
        main(args)
    except Exception as ex:
        log.exception(f"Fatal error in main loop:\n{ex}")



# Saludos Cordiales!
# Github: @dqreator