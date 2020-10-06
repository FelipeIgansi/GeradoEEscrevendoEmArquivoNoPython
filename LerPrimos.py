arquivoCSV = open("/media/felipe/HD500/Code/python/Primos.csv", "r")
primos = []
primos = arquivoCSV.readlines() 

primo = []

#print(primos)

for i in primos:
    primo.append(i[:-2])
print(primo)
