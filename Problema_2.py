
def Justificador(txt_justificar):
    nuevo_Arreglo = []
    for texto in txt_justificar:
        if texto != txt_justificar[len(txt_justificar)-1]:
            cantidad = len(texto)
            espacios_necesarios = 30 - len(texto)
            lista_texto = list(texto)

            while(espacios_necesarios != 0):
                index_letra = 0
                bool_letra = True
                while(index_letra < cantidad):
                    if(lista_texto[index_letra] == " "):
                        if(bool_letra):
                            bool_letra = False
                            lista_texto.insert(index_letra, " ")
                            espacios_necesarios -= 1
                        else:
                            index_letra += 1
                    else:
                        bool_letra = True
                        index_letra += 1

            oracion_justificada = "".join(lista_texto)
            nuevo_Arreglo.append(oracion_justificada)

        else:
            espacios_necesarios = 30 - len(texto)
            lista_texto = list(texto)
            while(espacios_necesarios != 0):
                lista_texto.insert(len(texto), " ")
                espacios_necesarios -= 1
            oracion_justificada = "".join(lista_texto)
            nuevo_Arreglo.append(oracion_justificada)

    for impresion in nuevo_Arreglo:
        print(impresion)



def main():
    Ingreso_Cadenas = True
    Array_Justificador = []
    while(Ingreso_Cadenas):
        print("ingrese la cadena de texto")
        nueva_Cadena = input()

        print("Desea ingresar otra cadena? s: Si / n: No")
        opcion = input()

        if(len(nueva_Cadena) < 30):
            Array_Justificador.append(nueva_Cadena)
        else:
            print("Debes de ingresar una cadena menor de 30 caracteres")
        if(opcion.lower() == "n"):
            if(len(Array_Justificador) > 1):
                Justificador(Array_Justificador)
                Array_Justificador = []
            else:
                print("No cuentas con las cadenas suficiones")

if __name__ == '__main__':
    main();