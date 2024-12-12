#Librerías
import time
import secrets
import string
time.sleep(1)
#Inicio de Programa
print("Generador de contraseñas segura")
time.sleep(1)
respuesta=str(input("¿Es la primera vez que usas este programa?\nRespuesta: "))
respuesta_upper=respuesta.upper()
#Validación de opciones ingresadas por el susuario
if (respuesta_upper=="SI"):
    extension_pass=int(input("Gracias por usar este generador, para tener una contraseña segura la extensión de caracteres debe ser entre 12 y 32. Ingresa la extensión que necesites\nRespuesta: "))
    while extension_pass<12 or extension_pass>32:
        extension_pass=int(input("Debes colocar un número entre 12 y 32\nIngresa un número correcto: "))
        time.sleep(1)
    frase=str(input("¿Necesitas usar una frase específica?\nRespuesta:"))
    frase_upper=frase.upper()
#Generación de contraseña aleatoria con extensión y frase definida
    if (frase_upper=="SI"):
        print("Combinar una frase + caracteres aleatorios")
#Generación de contraseña aleatoria con extensión definida
    else:
        alfabeto=string.ascii_letters + string.digits
        pass_aleatoria=''.join(secrets.choice(alfabeto) for i in range(extension_pass))
        print("Generando una contraseña aleatoria ...")
        time.sleep(4)
        print("Aquí tienes tu contraseña segura con "+ str(extension_pass) +" caracteres :" + pass_aleatoria)
elif(respuesta_upper=="NO"):
#Generación de contraseña totalmente aleatoria    
    print("Generando una contraseña aleatoria ...")
    clase_aleatoria=secrets.SystemRandom()
    num_aleatorio=clase_aleatoria.randrange(12,32)
    alfabeto=string.ascii_letters + string.digits
    pass_aleatoria=''.join(secrets.choice(alfabeto) for i in range(num_aleatorio))
    time.sleep(4)
    print("Aquí tienes tu contraseña generada aleatoriamente con "+ str(num_aleatorio) +" caracteres: " + pass_aleatoria)
#Condición no válida ingresada por el usuario y finalización del programa
else:
    print("Ingresa una respuesta correcta y reinicia el programa\nSaliendo del programa ...")
    time.sleep(3)
    exit()