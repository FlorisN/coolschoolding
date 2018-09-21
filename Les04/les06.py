''''
getallenrij = [2,4,6,8,10,9,7]

maximum = -100
for getal in getallenrij:
    if getal > maximum:
        maximum = getal

print(maximum)

getallenrij = [2,4,6,8,10,9,7]

zoekgetal = eval(input(print('wat is het zoekgetal?')))

gevonden = False

for getal in getallenrij:
    if zoekgetal == getal:
        gevonden = True

print(gevonden)
'''
