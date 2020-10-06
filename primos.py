qtnDivisores = 0

listaPrimos = []

contador = 0

arquivoCSV = open("/media/felipe/HD500/Code/python/Primos.csv", "w")
#arquivoExcel = open("/media/felipe/HD500/Code/python/Primos.xlsx", "w")

#arquivoCSV.write("Esses são os primos encontrados e gerados pelo python:\n\n")

min = 1
max = 1000

for numero in range(min,max):
    for divisor in range(1,((numero)//2)+1):
        if ((numero%divisor) ==0):
            qtnDivisores += 1
            
        
    if (qtnDivisores == 1):        
        listaPrimos.append(numero)
        arquivoCSV.write(str(numero)+",\n")



        
    qtnDivisores = 0 # Zera a quantidade de divisores

print(listaPrimos)

#arquivoCSV.write("\n\nForam gerados {} numeros primos.".format(str(contador)))

arquivoCSV.close()
#arquivoExcel.close()