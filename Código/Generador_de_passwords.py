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
#Función de validación de un número entero
def val_entero():
   while True:
       extension_pass=input("Gracias por usar este generador, para tener una contraseña segura la extensión de caracteres debe ser entre 12 y 32. Ingresa la extensión que necesites\nRespuesta: ")
       try:
        extension_pass=int(extension_pass)
        if extension_pass >= 12 and extension_pass<=32:
            global extension_pass_clear
            extension_pass_clear=extension_pass
            return extension_pass
        else:
            print (rojo+"Debes colocar un número entre 12 y 32\nIngresa un número correcto"+verde)
            time.sleep(2)
       except ValueError:
           print (rojo+"Debes colocar un número entre 12 y 32\nIngresa un número correcto"+verde)
           time.sleep(2)
#Función de una contraseña con datos proporcionados por el usuario
def pass_frase():
    frase_usuario=str(input("Ingresa una frase que recuerdes de un máximo de " +str(extension_pass_clear)+ " caracteres: "))
    time.sleep(1)
    while len(frase_usuario) > extension_pass_clear:
        frase_usuario=str(input(rojo+"La frase es demasiodo larga. Ingresa una frase de máximo"+ str(extension_pass_clear) + " caracteres: "+verde))
        continue 
    time.sleep(1) 
    frase_valid_upper=str(input("La frase " +amarillo+ frase_usuario +verde+ " ¿Es correcta?: ")).strip().lower()
    while frase_valid_upper != "si":
        frase_usuario=str(input("Ingresa una frase que recuerdes: "))
        time.sleep(1)
        frase_valid_upper=str(input("La frase " +amarillo+ frase_usuario + verde+" ¿Es correcta?: ")).strip().lower()
    time.sleep(2)
    long_res=extension_pass_clear - len(frase_usuario)
    if long_res > 0:
        pass_resto = ''.join(secrets.choice(alfabeto) for _ in range(long_res))
    else:
        pass_resto = ""
    pass_final = frase_usuario + pass_resto
    count=len(pass_final)
    print("Aquí tienes tu contraseña segura con un máximo de "+amarillo +str(extension_pass_clear) +verde+ " caracteres: " +amarillo+pass_final+blanco)
#Función de una contraseña aleatoria con una extensión definida
def pass_extension():
    pass_aleatoria=''.join(secrets.choice(alfabeto) for i in range(extension_pass_clear))
    print("Generando una contraseña aleatoria ...")
    time.sleep(4)
    print("Aquí tienes tu contraseña segura con "+ amarillo+str(extension_pass_clear) +verde+" caracteres :" + amarillo+pass_aleatoria+blanco)
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
    print(verde+"\nAutor: Kevin Tupiza")
    print(verde+"\nGenerador de contraseñas segura\n")
    time.sleep(1)
    respuesta_upper=str(input("¿Es la primera vez que usas este programa?\nRespuesta: ")).strip().lower()
#Validación de opciones ingresadas por el susuario
if (respuesta_upper=="si"):
    val_entero()
    frase_upper=str(input("¿Necesitas usar una frase específica?\nRespuesta:")).strip().lower()
#Generación de contraseña aleatoria con extensión y frase definida
    if (frase_upper=="si"):
        pass_frase()
#Generación de contraseña aleatoria con extensión definida
    else:
        pass_extension()
elif(respuesta_upper=="no"):
    pass_random()
else:
    print(rojo+"Ingresa una respuesta correcta y reinicia el programa\nSaliendo del programa ..."+blanco)
    time.sleep(3)
    exit()