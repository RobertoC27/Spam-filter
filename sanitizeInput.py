# -*- coding: utf-8 -*-
"""
this script is meant to remove characters that could add noise to the classifier performance
"""

import re
from collections import Counter
import codecs
from stop_words import get_stop_words

TRAF = codecs.open("training.txt", "r", "utf-8")
BOWSPAM = []
BOWHAM = []
BOWGENERAL = []
LINES = TRAF.readlines()
TOREMOVE = ["a", "the", ]
STOP_WORDS = get_stop_words('en')

for line in LINES:
    #cambia los numeros por nnum que es mas eficiente para hacer detecciones
    #que buscar el numero como tal xq es menos prob. encontrarlo
    line = re.sub(r"\d+", "nnum", line)
    tmpList = re.split(r'\W+', line.lower())
    #se quitan las palabras mas comunes y que no agregan ningun valor a la busqueda
    tmpList = [w for w in tmpList if not w in STOP_WORDS]
    try:
        tmpList.remove("")
    except ValueError:
        pass
    try:
        tmpList.remove("ham")
    except ValueError:
        pass
    try:
        tmpList.remove("spam")
    except ValueError:
        pass

    print tmpList
    raw_input("seguir")
    BOWGENERAL.extend(tmpList)

    if line.startswith("spam"):
        BOWSPAM.extend(tmpList)
    else:
        BOWHAM.extend(tmpList)


COUNTERGENERAL = Counter(BOWGENERAL)
COUNTERHAM = Counter(BOWHAM)
COUNTERSPAM = Counter(BOWSPAM)

def getCounters():
    return COUNTERGENERAL,COUNTERHAM,COUNTERSPAM
