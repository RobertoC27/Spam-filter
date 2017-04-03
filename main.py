"""
entry point
"""
from putNetworkTogether import metodo2, calcProb

def setUP(k):
    return metodo2(k)

def runMe():
    seguir = 'y'
    k = 3
    assisting = setUP(k)
    file_name = "cross_val.txt"
    currently_classifying = []
    ccf = open(file_name, "r")
    for line in ccf:
        currently_classifying.append(line)
    ccf.close()
    results = []
    while seguir != 'n':
        cambiar = raw_input("desea cambiar el k actual {}? (y|n)\n".format(k))

        if cambiar == 'y':
            k = input("ingrese el nuevo valor de K: ")
            assisting = setUP(k)

        cambiar = raw_input("desea cambiar el archivo actual {}? (y|n)\n".format(file_name))
        if cambiar == 'y':
            file_name = raw_input("ingrese el nuevo nombre de archivo\n")
            currently_classifying = []
            ccf = open(file_name, "r")
            for line in ccf:
                currently_classifying.append(line)
            ccf.close()

        efectividad = 0
        results = []
        for mail in currently_classifying:
            res = calcProb(mail, k, assisting[0], assisting[1], assisting[2])
            if res[0] > res[1]:
                if mail.startswith("ham"):
                    efectividad += 1
                else:
                    results.append("ham\t{}".format(mail))

            if res[1] > res[0]:
                if mail.startswith("spam"):
                    efectividad += 1
                else:
                    results.append("spam\t{}".format(mail))

        rf = open("results.txt", "w")
        rf.writelines(results)
        rf.close()
        efectividad = efectividad / float(len(currently_classifying))
        print "la efectividad de deteccion para {}, fue del {}% con k = {}".format(file_name, round(efectividad * 100, 3), k)
        seguir = raw_input("volver a ejecutar? (y|n)\n")

runMe()