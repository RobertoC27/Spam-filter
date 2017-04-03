import random

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


refh = [pal for pal in HAM]
refs = [pal for pal in SPAM]
for i in range(int(len(refh)*0.8)):
    ind = random.randint(0, len(HAM)-1)
    TRAINING.append(HAM.pop(ind))

for i in range(int(len(refh)*0.1)+1):
    ind = random.randint(0, len(HAM)-1)
    CROSS_VAL.append(HAM.pop(ind))

TEST.extend(HAM)
print len(TRAINING)
print len(CROSS_VAL)
print len(TEST)
print "---"
print int(len(refh)*0.8)
print int(len(refh)*0.1)
print int(len(refh)*0.1) + int(len(refh)*0.1) + int(len(refh)*0.8)
print len(HAM)
print len(SPAM)
