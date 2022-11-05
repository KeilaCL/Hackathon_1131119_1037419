def CadenasSubsecuentes(ca1, ca2):
    cadena = ""
    cant = len(ca1)
    for i in range(cant):
        if ca1[i] == ca2[i]:
                cadena += ca1[i]

    print("La cadena subsecuente es: " + cadena)


print("Ingrese una cadena: ")
cadena1 = input()
cadena1min = cadena1.lower() 

print("Ingrese una cadena: ")
cadena2 = input()
cadena2min = cadena2.lower() 

if (len(cadena1) != len(cadena2)):
    print("La cadena debe ser del mismo tamaño");
else:
    CadenasSubsecuentes(cadena1min,cadena2min)
