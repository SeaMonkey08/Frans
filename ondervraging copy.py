import random

score = 0
aantalGesteldeVragen = 0
woordenNederlands = []
woordenFrans = []
ondervragen = False
aantalVragenInFile = 0

print("1. De familie")
print("2. Het eten")
fileKeuze = input("Welke woordenlijst wil je inoefenen? ")
if fileKeuze == "1":
    file = open('data\De familie','r')
if fileKeuze == "2":
    file = open('data\Het eten.txt','r')
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
            woordenFrans.remove(fr)
            woordenNederlands.remove(woordenNederlands[willekeurig])

        else:
            print (woordenFrans[willekeurig] + "                      Dat kan beter")
            print("—————————————————————————————————————————————")
        
        aantalGesteldeVragen += 1

        if aantalGesteldeVragen == daantalVragen or bool(woordenFrans):
            resultaat = round((score/ aantalGesteldeVragen)* 100)
            bericht = str(score)+"/"+str(aantalGesteldeVragen) + " => " + str(resultaat) + "%"
            print(bericht)
        if fr == "Quit" or fr == "quit":
            ondervragen == False
            resultaat = round((score/ daantalVragen)* 100)
            bericht = str(score)+"/"+str(daantalVragen) + " => " + str(resultaat) + "%"
            print(bericht)