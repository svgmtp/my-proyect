# dabale arroz a la zorra el abad
entrada = input("introduce algo y pulsa Enter: ")
entrada = entrada.replace(" ", "")
if entrada == "".join(reversed(entrada)) :
    print("Sí es un Palindromo")
else:
    print("No es un Palindromo" , "\n1--> ", entrada, "\n2--> ", ("".join(reversed(entrada))))

entrada = input("introduce algo y pulsa Enter: ")
entrada = entrada.replace(" ", "")
if entrada == entrada[::-1]:
    print("Sí es un Palindromo")
else:
    print("No es un Palindromo" , "\n1--> ", entrada, "\n2--> ", (entrada[::-1]))


