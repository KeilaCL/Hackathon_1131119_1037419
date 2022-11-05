
def Game_Scramble():
    print("Ingrese la cadena con la cual quiere iniciar el scramble")
    Scramble = input()

    print("Ingrese la segunda cadena de texto ")
    txt_Scramble = input()

    if(len(Scramble) != len(txt_Scramble)):
        return False;

    Cadena_txt_Scramble = list(txt_Scramble.lower())
    Cadena_Scramble = list(Scramble.lower())

    for letra in Cadena_txt_Scramble:
        palabra = "".join(Cadena_Scramble)
        posicion = palabra.find(letra)
        if(posicion == -1):
            return False;
        Cadena_Scramble = list(Cadena_Scramble)
        Cadena_Scramble.pop(posicion)

    if(len(Cadena_Scramble) == 0):
        return True;


def main():
    return_error = True
    while(return_error):
        response_Game = Game_Scramble()
        if(response_Game):
            print("Si es una cadena perteneciente")
        else:
            print("No es una cadena perteneciente")


if __name__ == '__main__':
    main();
