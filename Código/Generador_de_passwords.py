import time
time.sleep(2)
print("Generador de contraseñas segura")
time.sleep(2)
respuesta=str(input("¿Es la primera ves que usas este programa?\nRespuesta: "))
respuesta_upper=respuesta.upper()
if (respuesta_upper=="SI"):
    extension_pass=int(input("Gracias por usar este generador, para tener una contraseña segura la extensión de caracteres debe ser entre 12 y 32. Ingresa la extensión que necesites\nRespuesta: "))
    time.sleep(3)
    if (extension_pass>=12 and extension_pass <=32):
        print("Generando contraseña segura . . .")
        time.sleep(3)
    else:
        print("Debes colocar un número entre 12 y 32\nIngresa un número correcto y reinicia el programa\nSaliendo ...")
        time.sleep(1)
        exit()
elif(respuesta_upper=="NO"):
    print("Generando una contraseña aleatoria ...")
    time.sleep(5)
else:
    print("Ingresa una respuesta correcta\nSaliendo del programa ...")
    time.sleep(5)