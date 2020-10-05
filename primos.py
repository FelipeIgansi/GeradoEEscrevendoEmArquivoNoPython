qtnDivisores = 0

listaPrimos = []

contador = 0

arquivoCSV = open("/media/felipe/HD500/Code/python/Primos.csv", "w")
#arquivoExcel = open("/media/felipe/HD500/Code/python/Primos.xlsx", "w")

arquivoCSV.write("Esses são os primos encontrados e gerados pelo python:\n\n")

for numero in range(1,100000):
    for divisor in range(1,((numero)//2)+1):
        if ((numero%divisor) ==0):
            qtnDivisores += 1
            
        
    if (qtnDivisores == 1):
        #print(numero)
        listaPrimos.append(numero)
        arquivoCSV.write(str(numero)+",\n")
        #arquivoExcel.write(str(numero)+",\n")
        contador += 1 # Faz autoincremento da quantidade de valores gerados
    qtnDivisores = 0 # Zera a quantidade de divisores

print(listaPrimos)

arquivoCSV.write("\n\nForam gerados {} numeros primos.".format(str(contador)))

arquivoCSV.close()
#arquivoExcel.close()