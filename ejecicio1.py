
for lista in range(100):
    entre3 = lista % 3 == 0
    entre5 = lista % 5 == 0
    if entre5 and entre3:
        print("FIZZBUZZ")
    elif entre3:
        print("FIZZ")
    elif entre5:
        print("BUZZ")
    else:
        print(lista)