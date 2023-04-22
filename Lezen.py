file = open ('woorden.txt','r')

for text in file:
    w = text.split(",")
    print("Nederlands: " + w[0])
    print("Frans: " + w[1])
file.close()
