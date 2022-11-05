def CadenasSubsecuentes(ca1, ca2):
    cadena = ""
    cant = len(ca1)
    for i in range(cant):
        if ca1[i] == ca2[i]:
                cadena += ca1[i]

    print("La cadena subsecuente es: " + cadena)


print("Ingrese una cadena: ")
cadena1 = input()


print("Ingrese una cadena: ")
cadena2 = input()

if (len(cadena1) != len(cadena2)):
    print("La cadena debe ser del mismo tamaño");
else:
    CadenasSubsecuentes(cadena1,cadena2)
