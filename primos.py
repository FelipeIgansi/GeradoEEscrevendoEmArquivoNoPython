qtnDivisores = 0

listaPrimos = []

contador = 0

arquivoTxt = open("/media/felipe/HD500/Code/python/Primos.txt", "w")
arquivoExcel = open("/media/felipe/HD500/Code/python/Primos.xlsx", "w")

arquivoTxt.write("Esses são os primos encontrados e gerados pelo python:\n\n")

for numero in range(1,100):
    for divisor in range(1,((numero)//2)+1):
        if ((numero%divisor) ==0):
            qtnDivisores += 1
            
        
    if (qtnDivisores == 1):
        #print(numero)
        listaPrimos.append(numero)
        arquivoTxt.write(str(numero)+"\n")
        arquivoExcel.write(str(numero)+"\n")
        contador += 1
    qtnDivisores = 0

print(listaPrimos)

arquivoTxt.write("\n\nForam gerados {} numeros primos.".format(str(contador)))

arquivoTxt.close()
arquivoExcel.close()