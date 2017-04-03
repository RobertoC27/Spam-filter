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

refh = [pal for pal in HAM]
for i in range(int(len(refh)*0.8)):
    ind = random.randint(0, len(HAM)-1)
    TRAINING.append(HAM.pop(ind))

for i in range(int(len(refh)*0.1)+1):
    ind = random.randint(0, len(HAM)-1)
    CROSS_VAL.append(HAM.pop(ind))

TEST.extend(HAM)

refs = [pal for pal in SPAM]
for i in range(int(len(refs)*0.8)):
    ind = random.randint(0, len(SPAM)-1)
    TRAINING.append(SPAM.pop(ind))

for i in range(int(len(refs)*0.1)+1):
    ind = random.randint(0, len(SPAM)-1)
    CROSS_VAL.append(SPAM.pop(ind))

TEST.extend(SPAM)


TRAF = open("training.txt", "w")
TRAF.writelines(TRAINING)
TRAF.close()
CVF = open("cross_val.txt", "w")
CVF.writelines(CROSS_VAL)
CVF.close()
TF = open("test.txt", "w")
TF.writelines(TEST)
TF.close()
