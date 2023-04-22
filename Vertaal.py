gameExit = 1
#while gameExit:
fr = input ('verbe français svp:    ')
nl = input('nederlands woord aub:   ')
print(fr)
#file = open('woorden.txt','w')     #w = write = nieuw bestand aanmaken over het bastaande
file = open('woorden.txt','a')      #a = append(toevoegen) = toevoegen aan het einde van het bestand
#file.write("{nl},{fr}") 
file.write(nl)
file.write(',')
file.write(fr)
file.write('\n')


file.close()