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
    cntham = 0
    cntspam = 0
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
        #a la lista general si le dejo el count de spam y ham
        #despues de eso ya lo quito para que no haga ruido a las otras redes
        BOWGENERAL.extend(tmp_list)
        try:
            tmp_list.remove("ham")
        except ValueError:
            pass
        try:
            tmp_list.remove("spam")
        except ValueError:
            pass


        if line.startswith("spam"):
            BOWSPAM.extend(tmp_list)
            cntspam = cntspam + 1
        else:
            BOWHAM.extend(tmp_list)
            cntham = cntham + 1
            #print BOWHAM
            #kit = raw_input("sigue: ")
            #if kit == "p":
             #   break

    general = Counter(BOWGENERAL)

    ham = Counter(BOWHAM)
    spam = Counter(BOWSPAM)

    return general, ham, spam


metodo1("training.txt")