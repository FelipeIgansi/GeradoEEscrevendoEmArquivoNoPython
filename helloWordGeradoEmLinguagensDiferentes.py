arquivo = open("/media/felipe/HD500/Code/python/Primos.txt", "w")

print("Em qual linguagem vc quer que seja gerado o hello world?(1 - Python, 2 - C#):")

resp = int(input("Digite o numero correspondente:  "))

if (resp == 1):
    arquivo = open("/media/felipe/HD500/Code/python/HelloWorld.py", "w")

    arquivo.write(
        "print('Hello World!')"
    )
elif(resp == 2 ):
    arquivo = open("/media/felipe/HD500/Code/python/HelloWorld.cs", "w")

    arquivo.write(
""" public void main(){
        Console.WriteLine("Hello World!")
    } """
    )