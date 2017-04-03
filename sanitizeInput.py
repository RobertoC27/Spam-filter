# -*- coding: utf-8 -*-
"""
this script is meant to remove characters that could add noise to the classifier performance
"""

import re
from collections import Counter
import codecs
from stop_words import get_stop_words



STOP_WORDS = get_stop_words('en')
BOWGENERAL = []
BOWHAM = []
BOWSPAM = []
"""
returns 3 Counter objects that represent the general, ham and spam
in that order
"""
def metodo1(nombre):
    actual_file = codecs.open(nombre, "r", "utf-8")
    lines = actual_file.readlines()
    for line in lines:
        #cambia los numeros por nnum que es mas eficiente para hacer detecciones
        #que buscar el numero como tal xq es menos prob. encontrarlo
        line = re.sub(r"\d+", "nnum", line)
        tmp_list = re.split(r'\W+', line.lower())
        #se quitan las palabras mas comunes y que no agregan ningun valor a la busqueda
        tmp_list = [w for w in tmp_list if not w in STOP_WORDS]
        
        try:
            tmp_list.remove("")
        except ValueError:
            pass
        try:
            tmp_list.remove("ham")
        except ValueError:
            pass
        try:
            tmp_list.remove("spam")
        except ValueError:
            pass


        BOWGENERAL.extend(tmp_list)

        if line.startswith("spam"):
            BOWSPAM.extend(tmp_list)
        else:
            BOWHAM.extend(tmp_list)


    general = Counter(BOWGENERAL)
    ham = Counter(BOWHAM)
    spam = Counter(BOWSPAM)
    return general, ham, spam


