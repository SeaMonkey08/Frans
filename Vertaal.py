from decimal import *

i = 3

while True:
    aantal = input('hoeveel woorden? ')
    dAantal = int(aantal)
    for i in range(dAantal):
        fr = input ('verbe français svp:    ')
        nl = input('nederlands woord aub:   ')
        print(fr)
        #file = open('woorden.2.txt','w')     #w = write = nieuw bestand aanmaken over het bastaande
        file = open('woorden.2.txt','a')      #a = append(toevoegen) = toevoegen aan het einde van het bestand
        #file.write("{nl},{fr}") 
        file.write(nl)
        file.write(',')
        file.write(fr)
        file.write('\n')
        file.close()
    break