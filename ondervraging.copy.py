import random

file = open ('woorden.2.txt','r')

score = 0
aantalGesteldeVragen = 0
woordenNederlands = []
woordenFrans = []
ondervragen = False
aantalVragenInFile = 0

while file:
    for text in file:
        w = text.split(",")
        woordenNederlands.append(w[0])
        woordenFrans.append(w[1].replace("\n", "")) 
        aantalVragenInFile += 1
    file.close
    print("------------------------------------------------")
    print("Maximum aantal vragen = " + str(aantalVragenInFile))
    print("------------------------------------------------")
    aantalVragen = input("Hoeveel vragen mag ik u stellen? ")
    daantalVragen = int(aantalVragen)
    ondervragen = True 
    file = False   

while ondervragen: 
    for i in range(daantalVragen):
        willekeurig = random.randint(0,aantalVragenInFile)
        print("NEDERLANDS: " + woordenNederlands[willekeurig]) 
        fr = input ("VERTALING: ")
        w[1] = w[1].replace("\n","")
        
        tecontroleren = woordenFrans[willekeurig]
        
        if fr == tecontroleren:
            print ("                             Goed zo")
            print("——————————————————————————————————————————")
            score += 1 

        else:
            print (woordenFrans[willekeurig] + "                      Dat kan beter")
            print("—————————————————————————————————————————————")
        
        aantalGesteldeVragen += 1

        if aantalGesteldeVragen == daantalVragen:
            resultaat = round((score/ daantalVragen)* 100)
            bericht = str(score)+"/"+str(daantalVragen) + " => " + str(resultaat) + "%"
            print(bericht)
    break