import random
import re

INPUT = open('test_corpus.txt', 'r')
HAM = []
SPAM = []
TRAINING = []
CROSS_VAL = []
TEST = []

for line in INPUT:
    if line.startswith("ham"):
        HAM.append(line)
    elif line.startswith("spam"):
        SPAM.append(line)
INPUT.close()

print len(HAM)
print len(SPAM)

refh = [pal for pal in HAM]
refs = [pal for pal in SPAM]
for i in range(int(len(refh)*0.8)):
    ind = random.randint(0, len(HAM)-1)
    TRAINING.append(HAM.pop(ind))

for i in range(int(len(refh)*0.1)+1):
    ind = random.randint(0, len(HAM)-1)
    CROSS_VAL.append(HAM.pop(ind))

TEST.extend(HAM)


kl = "hola...como esta"
tmp_list = re.split(r'\W+', kl)
print tmp_list
