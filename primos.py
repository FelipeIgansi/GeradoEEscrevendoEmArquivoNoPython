qtnDivisores = 0

listaPrimos = []

arquivo = open("/media/felipe/HD500/Code/python/Primos.txt", "w")

arquivo.write("Esses são os primos encontrados e gerados pelo python:\n\n")

for numero in range(1,1000):
    for divisor in range(1,((numero)//2)+1):
        if ((numero%divisor) ==0):
            qtnDivisores += 1
            
        
    if (qtnDivisores == 1):
        #print(i)
        listaPrimos.append(numero)
        arquivo.write(str(numero)+"\n")
    qtnDivisores = 0

print(listaPrimos)

