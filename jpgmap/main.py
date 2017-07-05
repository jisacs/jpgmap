#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Implémentation de la proclamation de la bonne parole.

    Usage:

    >>> from sm_lib import proclamer
    >>> proclamer()
"""

from datetime import datetime

__all__ = ['proclamer']


from jpgmap.engine import Engine



def proclamer():
    """
        Fonction de proclamation de la bonne parole. Aucun paramètre, et
        retourne None, car tout le monde say que "Ex nihilo nihil"
    """

    engine = Engine("raw/small.jpg") # Width 93, Heigh 53

    engine.run()






if __name__ == "__main__":
    proclamer()
