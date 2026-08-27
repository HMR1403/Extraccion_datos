#Hector Malaga Rodriguez 951 27/08/2026
#Creando un lenguaje secreto para poder pasar las respuestas del examen de programación a mi compa, ayudaaa

traductor = {"a": "rer",
             "b": "mpf",
             "c": "8)0",
             "d": "123",
             "e": "'¿´",
             "f": "/(6",
             "g": "$%&",
             "h": "/()",
             "i": "290",
             "j": "-.{",
             "k": "/*4",
             "l": "$##",
             "m": "676",
             "n": "-+-",
             "o": "!!!",
             "p": "696",
             "q": "qqq",
             "r": "njh",
             "s": "$k3",
             "t": "$34",
             "u": "$%$",
             "v": "291",
             "w": "sis",
             "x": "nou",
             "y": "tlv",
             "z": "|°¬",
             "1": "345",
             "2": "456",
             "3": "567",
             "4": "678",
             "5": "789",
             "6": "891",
             "7": "912",
             "8": "123",
             "9": "245",
             " ": "   ",
             ",": ",  "
}

def encriptar_mensaje(mensaje_texto):
    encriptado = ""
    for letra in mensaje_texto:
        encriptado += traductor[letra]

    return print(f"mensaje traducido a Malagon: {encriptado}")

def desencriptar_mensaje(mensaje_texto):
    desencriptado = ""
    for conjunto in range(0, len(mensaje_texto), 3):
        fragmento = mensaje_texto[conjunto:conjunto+3]
        for letra, valor in traductor.items():
            if valor == fragmento:
                desencriptado += letra

    return print(f"mensaje traducido al español: {desencriptado}")

if __name__ == "__main__":
    encriptar_mensaje("hola, tengo hambre")
    desencriptar_mensaje("696njh!!!$%&njhrer676rernjh   '¿´$k3   $##!!!   676rernou290676!!!!!!!!!!!!")