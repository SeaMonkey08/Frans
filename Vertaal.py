from decimal import *

nieuwe = True
invullen = False

while nieuwe:
    print('nieuwe lijst -> 1')
    print('bestaande lijst aanvullen -> 2')
    nieuw = input('wat van bovenstaande wil je uitvoeren?  ')
    if nieuw == '1':
        nieuwe = False
        invullen = True  
    if nieuw == '2':
        print('')
        print('tourisme')
        print('')
        nieuwe = False
        invullen = True
while invullen:
    title = input('title van de lijst:  ')
    aantal = input('hoeveel woorden wil je in de lijst '  + title + ' toevoegen? ')
    dAantal = int(aantal)
    for i in range(dAantal):
        fr = input ('verbe français svp:    ')
        nl = input('nederlands woord aub:   ')
        print(fr)
        file = open('./data/' + title + '.txt','a')
        file.write(nl)
        file.write(',')
        file.write(fr)
        file.write('\n')
        file.close()
    break