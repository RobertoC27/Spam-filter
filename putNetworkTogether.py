"""
this script puts together the bayesian network base on input recieved from
the bag of words it recieves
"""
from sanitizeInput import metodo1


SPAM_NETWORK = {}
HAM_NETWORK = {}

def metodo2(k, toremove=[]):
    counters = metodo1("training.txt")


    counter_ham = counters[1]
    for wrd in toremove:
        del counter_ham[wrd]

    hamwords = sum(counter_ham.values())
    ham_classes = float(len(counter_ham.keys()))

    counter_spam = counters[2]
    for wrd in toremove:
        del counter_spam[wrd]
    spam_classes = float(len(counter_spam.keys()))
    spamwords = sum(counter_spam.values())

    total_classes = (ham_classes+spam_classes)
    denom = float(hamwords + (k * total_classes))
    #put together the ham network
    for ham_word in counter_ham:
        current_freq = counter_ham.get(ham_word)
        current_prob = round((current_freq + k)/denom, 8)
        HAM_NETWORK.update({ham_word:[{'freq':current_freq, 'prob':current_prob}]})

    #put together the spam network
    denom = float(spamwords + (k * total_classes))
    for spam_word in counter_spam:
        current_freq = counter_spam.get(spam_word)
        current_prob = round((current_freq + k)/denom, 8)
        SPAM_NETWORK.update({spam_word:[{'freq':current_freq, 'prob':current_prob}]})

    return HAM_NETWORK, SPAM_NETWORK

HJS = metodo2(10)
print HJS[1]



