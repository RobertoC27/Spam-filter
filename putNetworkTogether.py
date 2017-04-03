"""
this script puts together the bayesian network base on input recieved from
the bag of words it recieves
"""
import re
from sanitizeInput import metodo1, STOP_WORDS


SPAM_NETWORK = {}
HAM_NETWORK = {}
SMOOTHING = 0
TOTAL_CLASSES = 0
SPAM_WORDS = 0
HAM_WORDS = 0
GENERAL_COUNTER = {}
def metodo2(k, toremove=[]):

    counters = metodo1("training.txt")
    general = counters[0]
    total_classes = len(general.keys())
    #print "sin repetir->", total_classes
    #put together the ham network
    counter_ham = counters[1]
    for wrd in toremove:
        del counter_ham[wrd]

    hamwords = sum(counter_ham.values())
    denom = float(hamwords + (k * total_classes))
    for ham_word in counter_ham:
        current_freq = counter_ham.get(ham_word)
        current_prob = round((current_freq + k)/denom, 8)
        HAM_NETWORK.update({ham_word:{'freq':current_freq, 'prob':current_prob}})

    #put together the spam network
    counter_spam = counters[2]
    for wrd in toremove:
        del counter_spam[wrd]

    spamwords = sum(counter_spam.values())
    denom = float(spamwords + (k * total_classes))
    for spam_word in counter_spam:
        current_freq = counter_spam.get(spam_word)
        current_prob = round((current_freq + k)/denom, 8)
        SPAM_NETWORK.update({spam_word:{'freq':current_freq, 'prob':current_prob}})

    return general, hamwords, spamwords


def calcProb(phrase, k, generalCounter, HAM_WORDS, SPAM_WORDS):

    phrase = re.sub(r"\d+", "nnum", phrase)
    phrase = re.sub(r"ham", " ", phrase)
    phrase = re.sub(r"spam", " ", phrase)
    tmp_list = re.split(r'\W+', phrase.lower())
    try:
        tmp_list.remove("")
    except ValueError:
        pass
    #se quitan las palabras mas comunes y que no agregan ningun valor a la busqueda
    tmp_list = [w for w in tmp_list if not w in STOP_WORDS]
    numerador = 1
    denomidador = 1

    SMOOTHING = k
    GENERAL_COUNTER = generalCounter
    TOTAL_CLASSES = len(generalCounter.keys())
    val_h = round(GENERAL_COUNTER.get("ham"), 4)
    val_sp = round(GENERAL_COUNTER.get("spam"), 4)
    p_ham = (val_h + SMOOTHING) / float((val_h + val_sp) + (2 * SMOOTHING))
    p_spam = (val_sp + SMOOTHING) / float((val_h + val_sp) + (2 * SMOOTHING))

    #calculo primero la prob de que sea HAM
    for word in tmp_list:
        if word not in HAM_NETWORK:
            numerador *= float(1./(HAM_WORDS + (SMOOTHING * TOTAL_CLASSES)))
        else:
            numerador *= HAM_NETWORK[word]["prob"]
        if word not in SPAM_NETWORK:
            denomidador *= float(1./(SPAM_WORDS + (SMOOTHING * TOTAL_CLASSES)))
        else:
            denomidador *= SPAM_NETWORK[word]["prob"]


    numerador *= p_ham
    denomidador *= p_spam
    denomidador += numerador
    prob_ham = numerador/denomidador

    numerador = 1
    denomidador = 1
    #ahora la prob de que sea spam
    for word in tmp_list:
        if word not in SPAM_NETWORK:
            numerador *= float(1./(SPAM_WORDS + (SMOOTHING * TOTAL_CLASSES)))
        else:
            numerador *= SPAM_NETWORK[word]["prob"]
        if word not in HAM_NETWORK:
            denomidador *= float(1./(HAM_WORDS + (SMOOTHING * TOTAL_CLASSES)))
        else:
            denomidador *= HAM_NETWORK[word]["prob"]

    numerador *= p_spam
    denomidador *= p_ham
    denomidador += numerador
    prob_spam = numerador/denomidador

    return prob_ham, prob_spam



"""
K = 3
K2 = 15
ahg = metodo2(K)

CV = []
CVF = open("cross_val.txt", "r")
for line in CVF:
    CV.append(line)
CVF.close()
CNTS = 0
CNTH = 0
EFF = 0
for line in CV:
    res = calcProb(line, K2, ahg[0], ahg[1], ahg[2])

    if line.startswith("ham") and res[0] > res[1]:
        EFF += 1
    elif line.startswith("spam") and res[1] > res[0]:
        EFF += 1
    #print res
    #print res[0] > res[1]

print EFF/float(len(CV))
"""


