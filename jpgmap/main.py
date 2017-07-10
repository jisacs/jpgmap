#!/usr/bin/env python
# -*- coding: utf-8 -*-
from optparse import OptionParser
import sys



"""
    Implémentation de la proclamation de la bonne parole.

    Usage:

    >>> from sm_lib import proclamer
    >>> proclamer()
"""

from datetime import datetime

__all__ = ['proclamer']


from jpgmap.engine import Engine



def run():
    """
        Fonction de proclamation de la bonne parole. Aucun paramètre, et
        retourne None, car tout le monde say que "Ex nihilo nihil"
    """
    parser = OptionParser()

    parser.add_option("--filename",
                      help="write report to FILE")
    parser.add_option("-o", "--output",
                      dest="output",
                      help="if exist convert jpg to pickle a save in output filename")

    (options, args) = parser.parse_args()
    filename = args[0]
    output = options.output


    engine = Engine(filename, output) # Width 93, Heigh 53
    engine.run()




if __name__ == "__main__":
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="filaname to open")
    parser.add_argument("-o", "--output", help="if exist convert jpg to pickle a save in output filename")
    args = parser.parse_args()
    """

    run()
