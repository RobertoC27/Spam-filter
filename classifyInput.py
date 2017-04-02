"""
this is the script that sanitizes the input before feeding it to the classifier
"""
from collections import Counter
import random

INPUT = open('test_corpus.txt', 'r')
HAM = []
SPAM = []
CF = Counter()
TRAINING = []
CROSS_VAL = []
TEST = []

for line in INPUT:
    if line.startswith("ham"):
        HAM.append(line)
    elif line.startswith("spam"):
        SPAM.append(line)
INPUT.close()

for index in range(len(HAM)):
    CLASS = random.random()
    h1 = HAM[index]
    if CLASS < 0.8:
        TRAINING.append(h1)
    elif CLASS < 0.9:
        CROSS_VAL.append(h1)
    else:
        TEST.append(h1)

    if index < len(SPAM):
        s1 = SPAM[index]
        if CLASS < 0.8:
            TRAINING.append(s1)
        elif CLASS < 0.9:
            CROSS_VAL.append(s1)
        else:
            TEST.append(s1)

TRAF = open("training.txt", "w")
TRAF.writelines(TRAINING)
TRAF.close()
CVF = open("cross_val.txt", "w")
CVF.writelines(CROSS_VAL)
CVF.close()
TF = open("test.txt", "w")
TF.writelines(TEST)
TF.close()
