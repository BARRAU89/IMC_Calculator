# Este es un programa para calcular el indice de masa corporal (ICM)
# Los datos de edad, estatura y peso no pueden ser iguales a 0. El programa dara error si se introduce alguno de estos valores. 

print ("""¡Hola! Esta es una Calculadora de Indice de Masa Corporal 
¿Te gustaría conocer cuál es tu IMC?:
(Descuida, nadie sabrá tus resulatos...sólo tú)""")
aceptacion = int(input ('Escribe "1" si quisieras continuar o cualquier otra tecla si prefieres no saber tu IMC: '))

# Si la persona accede, Vamos a solicitar los siguientes datos: Nombre, Edad, Estatura (en metros) y Peso (en Kilogramos)
if aceptacion == 1:
    nombre = input ("¿Cómo te llamas?: ")
# Saludamos 
    print (f"Hola {nombre.title()}, vamos a necesitar algunos datos para hacer el cálculo")
    edad = int(input ("¿Cuántos años tienes?: "))

#Si la edad es mayor a 1, continuamos con el proceso solicitando la estatura.
    if edad >=1:
        estatura = float(input ("¿Cuál es tu estatura (en metros): "))
    else: print ("Lo sentimos, la edad tiene que ser mayor que 1")
 

#Si la estatura es mayor a 0.01m, continuamos solicitando el peso.  La estatura no puede ser igual a 0 porque daria error matematico
    if estatura >= 0.01:
        peso = float(input ("Ahora necesitamos conocer tu peso (en Kg): "))
    else: print ("Lo sentiemos, la estatura tiene que ser mayor a 0.01 m")
 

#Si el peso es mayor a 0 Kg, procedemos a hacer el calculo del IMC
    if peso > 0:
        imc = (peso/(estatura**2))
    else: print ("Lo sentimos, el peso no puede ser menor o igual a 0 Kg")
  

# Le enseñamos los resultados
    print (f"Tu IMC es: {imc: .2f}")

#Le explicamos en qué grado se encuentra según sus resultados
    if imc >= 0 and imc <= 18.50 :
        print ("Lo que se considera: 'Peso bajo'")
    elif imc >= 18.50 and imc <= 24.99 :
        print ("Lo que se considera: 'Peso normal'")
    elif imc >= 25.00 and imc <= 29.99 :
        print ("Lo que se considera: 'Sobrepeso'")
    elif imc >= 30.00 and imc <= 34.99 :
        print ("Lo que se considera: 'Obesidad leve'")
    elif imc >= 35.00 and imc <= 39.99 :
        print ("Lo que se considera: 'Obesisad media'")
    elif imc >= 40.00:
        print ("Lo que se considera: 'Obesidad mórbida'")

    print ('Recuerda tener una alimentación balanceada. Un profesional en la nutrición puede ser de mucha ayuda.')

#Nos despedimos
    print ("Hasta luego")
    exit ()

if aceptacion != 1:
    print ("¡De acuerdo! Estaremos aquí por si más adelante te interesa conocer tu ICM. Bye")