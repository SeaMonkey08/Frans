import random 

file = open ('woorden.txt','r')

score = 0
aantalGesteldeVragen = 0
woordenNederlands = []
woordenFrans = []
ondervragen = False
aantalVragen = 0
aantalVragenInFile = 0


for text in file:
    w = text.split(",")
    woordenNederlands.append(w[0])
    woordenFrans.append(w[1].replace("\n", "")) 
    aantalVragenInFile += 1
file.close
print("------------------------------------------------")
print("aantal vragen = " + str(aantalVragenInFile))
print("------------------------------------------------")

ondervragen = True    
while ondervragen: 
    willekeurig = random.randint(0,aantalVragenInFile)
    aantalVragen = 5
    print("NEDERLANDS: " + woordenNederlands[willekeurig]) 
    fr = input ("VERTALING: ")
    w[1] = w[1].replace("\n","")
    
    tecontroleren = w[1]
    
    if fr == tecontroleren:
        print ("                             Goed zo")
        print("——————————————————————————————————————————")
        score += 1 

    else:
        print (woordenFrans[willekeurig] + "                      Dat kan beter")
        print("—————————————————————————————————————————————")
    
    aantalGesteldeVragen += 1

    if aantalGesteldeVragen == aantalVragen:
        resultaat = round((score/ aantalVragen)* 100)
        bericht = str(score)+"/"+str(aantalVragen) + " => " + str(resultaat) + "%"
        print(bericht)
        break