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
    #print counter_ham.most_common(15)
    hamwords = sum(counter_ham.values())
    ham_classes = float(len(counter_ham.keys()))
    print "--------------------------------"
    counter_spam = counters[2]
    #print counter_spam.most_common(15)
    spam_classes = float(len(counter_spam.keys()))
    spamwords = sum(counter_spam.values())
    print (k * (ham_classes+spam_classes))

    #put together the ham network
    for ham_word in counter_ham:
        current_freq = counter_ham.get(ham_word)
        current_prob = round((current_freq + k)/float(hamwords + (k * (ham_classes+spam_classes))), 3)
        HAM_NETWORK.update({ham_word:[{'freq':current_freq, 'prob':current_prob}]})

    #put together the spam network
    for spam_word in counter_spam:
        current_freq = counter_spam.get(spam_word)
        current_prob = round((current_freq + k)/float(spamwords + (k * (ham_classes+spam_classes))), 3)
        SPAM_NETWORK.update({spam_word:[{'freq':current_freq, 'prob':current_prob}]})

    return HAM_NETWORK, SPAM_NETWORK

HJS = metodo2(5)
print HJS[1]



