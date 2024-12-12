#Librerías
import time
import secrets
import string
time.sleep(1)
print("Generador de contraseñas segura")
time.sleep(1)
respuesta=str(input("¿Es la primera vez que usas este programa?\nRespuesta: "))
respuesta_upper=respuesta.upper()
if (respuesta_upper=="SI"):
    extension_pass=int(input("Gracias por usar este generador, para tener una contraseña segura la extensión de caracteres debe ser entre 12 y 32. Ingresa la extensión que necesites\nRespuesta: "))
    while extension_pass<12 or extension_pass>32:
        extension_pass=int(input("Debes colocar un número entre 12 y 32\nIngresa un número correcto: "))
        time.sleep(1)
    frase=str(input("¿Necesitas usar una frase específica?\nRespuesta:"))
    frase_upper=frase.upper()
    if (frase_upper=="SI"):
        print("Combinar una frase + caracteres aleatorios")
    else:
        alfabeto=string.ascii_letters + string.digits
        pass_aleatoria=''.join(secrets.choice(alfabeto) for i in range(extension_pass))
        print("Generando una contraseña aleatoria ...")
        time.sleep(4)
        print("Aquí tienes tu contraseña segura con "+ str(extension_pass) +" caracteres :" + pass_aleatoria)
elif(respuesta_upper=="NO"):
    print("Generando una contraseña aleatoria ...")
    clase_aleatoria=secrets.SystemRandom()
    num_aleatorio=clase_aleatoria.randrange(12,32)
    alfabeto=string.ascii_letters + string.digits
    pass_aleatoria=''.join(secrets.choice(alfabeto) for i in range(num_aleatorio))
    time.sleep(4)
    print("Aquí tienes tu contraseña generada aleatoriamente con "+ str(num_aleatorio) +" caracteres: " + pass_aleatoria)
else:
    print("Ingresa una respuesta correcta y reinicia el programa\nSaliendo del programa ...")
    time.sleep(4)
    exit()