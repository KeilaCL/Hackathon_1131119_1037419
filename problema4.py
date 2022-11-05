TotalA = 0
def AbuelaBinaria(num1, num2, num3):
    total = num1 + num2 + num3
    #print(total)
    if total % 2 == 0:
        total = total // 2
    else:
        avellana1 = (total - 1) // 2
        avellana2 = avellana1  + 1
    
    #print(avellana1)
    #print(avellana2)
    ConvertBinario(avellana1)
    ConvertBinario(avellana2)

def ConvertBinario(num):
    global TotalA
    almacenar = [] 
    while num != 0:
        mod = num % 2
        cos = num // 2
        almacenar.append(mod)
        num = cos
    
    #print(almacenar)

    for i in almacenar:
        if i == 1:
            TotalA = TotalA + 1

try:
    print("Ingrese número 1: ")
    numero1 = int(input())
    print("Ingrese número 2: ")
    numero2 = int(input())
    print("Ingrese número 3: ")
    numero3 = int(input())
    AbuelaBinaria(numero1, numero2, numero3)
    print("Cantidad total de avellanas: ")
    print(TotalA)

    #print("bien")
except:
    print("Debe ingresar valores enteros")