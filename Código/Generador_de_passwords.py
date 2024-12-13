#         UIDE
# Ingenería en Software
# Lógica de Programación
# Autor: Kevin Tupiza
# Proyecto: Generador de contraseñas seguras

#Librerías
import time
import secrets
import string

#Colores
amarillo="\x1b[1;33m"
rojo="\x1b[1;31m"
verde="\x1b[1;32m"
blanco="\x1b[1;37m"

#Variables Globales
alfabeto=string.ascii_letters + string.digits + '!@#$%^&*()-_=+[]{}|;:,.<>?/'
#Función de una contraseña con datos proporcionados por el usuario
def pass_frase():
    frase_usuario=str(input("Ingresa una frase que recuerdes de un máximo de " +str(extension_pass)+ " caracteres: "))
    time.sleep(1)
    while len(frase_usuario) > extension_pass:
        frase_usuario=str(input(rojo+"La frase es demasiodo larga. Ingresa una frase de máximo"+ str(extension_pass) + " caracteres: "+verde))
        continue 
    time.sleep(1) 
    frase_valid=str(input("La frase " +amarillo+ frase_usuario +verde+ " ¿Es correcta?: "))
    frase_valid_upper=frase_valid.upper()
    while frase_valid_upper != "SI":
        frase_usuario=str(input("Ingresa una frase que recuerdes: "))
        time.sleep(1)
        frase_valid=str(input("La frase " +amarillo+ frase_usuario + verde+" ¿Es correcta?: "))
        frase_valid_upper=frase_valid.upper()   
    time.sleep(2)
    long_res=extension_pass - len(frase_usuario)
    if long_res > 0:
        pass_resto = ''.join(secrets.choice(alfabeto) for _ in range(long_res))
    else:
        pass_resto = ""
    pass_final = frase_usuario + pass_resto
    count=len(pass_final)
    print("Aquí tienes tu contraseña segura con un máximo de "+amarillo +str(extension_pass) +verde+ " caracteres: " +amarillo+pass_final+blanco)
#Función de una contraseña añeatoria con una extensión definida
def pass_extension():
    pass_aleatoria=''.join(secrets.choice(alfabeto) for i in range(extension_pass))
    print("Generando una contraseña aleatoria ...")
    time.sleep(4)
    print("Aquí tienes tu contraseña segura con "+ amarillo+str(extension_pass) +verde+" caracteres :" + amarillo+pass_aleatoria+blanco)
#Función de contraseñas aleatorias
def pass_random():
    print("Generando una contraseña aleatoria ...")
    clase_aleatoria=secrets.SystemRandom()
    num_aleatorio=clase_aleatoria.randrange(12,32)
    pass_aleatoria=''.join(secrets.choice(alfabeto) for i in range(num_aleatorio))
    time.sleep(4)
    print("Aquí tienes tu contraseña generada aleatoriamente con "+amarillo+ str(num_aleatorio) +verde+" caracteres: " + amarillo+pass_aleatoria+blanco)
#Inicio del Programa
if __name__=="__main__":
    time.sleep(1)
    print('/$$   /$$ /$$$$$$ /$$$$$$$  /$$$$$$$$')
    print("| $$  | $$|_  $$_/| $$__  $$| $$_____/")
    print("| $$  | $$  | $$  | $$  | $$| $$$$$   ")
    print("| $$  | $$  | $$  | $$  | $$| $$__/   ")
    print("| $$  | $$  | $$  | $$  | $$| $$      ")
    print('|  $$$$$$/ /$$$$$$| $$$$$$$/| $$$$$$$$')
    print(verde+"\nGenerador de contraseñas segura")
    time.sleep(1)
    respuesta=str(input("¿Es la primera vez que usas este programa?\nRespuesta: "))
    respuesta_upper=respuesta.upper()
#Validación de opciones ingresadas por el susuario
if (respuesta_upper=="SI"):
    extension_pass=int(input("Gracias por usar este generador, para tener una contraseña segura la extensión de caracteres debe ser entre 12 y 32. Ingresa la extensión que necesites\nRespuesta: "))
    while extension_pass<12 or extension_pass>32:
        extension_pass=int(input(rojo+"Debes colocar un número entre 12 y 32\nIngresa un número correcto: "+verde))
        time.sleep(1)
    frase=str(input("¿Necesitas usar una frase específica?\nRespuesta:"))
    frase_upper=frase.upper()
#Generación de contraseña aleatoria con extensión y frase definida
    if (frase_upper=="SI"):
        pass_frase()
#Generación de contraseña aleatoria con extensión definida
    else:
        pass_extension()
elif(respuesta_upper=="NO"):
    pass_random()
else:
    print(rojo+"Ingresa una respuesta correcta y reinicia el programa\nSaliendo del programa ..."+blanco)
    time.sleep(3)
    exit()