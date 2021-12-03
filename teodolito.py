from os import system as p #libreria para poder ir vaciando la consola cada vez que agregamos una nueva opción, esta la utilizaremos como letra P para ahorra código
import time #libreria para que demore en mostrar por pantalla el texto
import math #libreria que usaremos.


def aplicacionmat(): #creamos este def solamente para hacer tiempo entre texto y texto, le daremos un valor de 0.5sg entre cada texto, si lo necesitamos, llamaremos a la función
    time.sleep(0.5)
    
    def esperar(): #def para eliminar todo el texto que ya usamos y pasar a lo seleccionado
        p('cls') #con este elimina el texto en pantalla
        time.sleep(0.5) #le damos los 0.5 sg que se va a demorar en aparecer el siguiente texto por pantalla

    def salir(): #funcion para salir de la aplicacion
        print("Saliendo de la aplicacion!") #mensaje que nos mostrará que estamso saliendo de la aplcación
        time.sleep(1) #tiempo de espera para cerrar la app correctamente
        print("La aplicación se a cerrado correctamente!") #mensaje de que ya se a cerrado la app
        exit(0) #se cierra totalmente nuestra aplicacion

    def opciones(): #esta función nos mostrará todos las opciones para poder usar
        p('cls') #nos elimina el texto mostrado anteriormente
        print("================================================================================================")
        print("||  Bienvenido a nuestra aplicación para calcular la altura, las opciones son las siguientes: || \n||  1.) Calcular Altura.                                                                      ||\n||  2.) Salir de la aplicacion                                                                ||")
        print("================================================================================================")
        #los 3 prints son para mostrar el mensaje en pantalla sobre las opciones, este mismo se encuentra decorado.
        opcion=int(input("Ingrese su opcion: ")) #este input nos permitirá seleccionar qué queremos hacer, si ejecutar la calculadora o salir de la app
        if opcion==1: #si el usuario marca la opcion 1 este nos dirigira a la funcion esperar y luego a la funcion altura que sera donde calculemos
            esperar()
            altura()
        elif opcion==2: #si el ususario marca la opción 2, nos llevará a la función de salida del programa.
            salir()
        else: #si presiona cualquier tecla que no se encuentre entre las opciones dadas, este entrará en un bucle hasta marca una opción correcta
            print("Opcion invalida!") #mensaje de que la opción está mala.
            esperar()
            opciones()
        
        
    def opciones2(): #función para las opciones despues de calcular la altura, si deseamos volver al menú o salir directamente de la aplicación
        
        op=int(input("1. Salir\n2. Volver al menu \nIngresar opcion: ")) #inputa para las opciones dadas.
        while op>=3 or op<=0: #sistema while que hará que mientas el usario marque un numero igual o mayor a 3 o igual o menor a 0 nos muestre por pantalla que nuestra opción es incorrecta.
            
            print("OPCION INCORRECTA!  Volviendo a las opciones!") #print de que está erronea nuestra opción
            time.sleep(1.5)#tiempo de espera entre el mensaje anterior y el nuevo
            p('cls') #elimina el texto mostrado por pantalla 
            opciones2() #nos lleva de nuevo a la función para preguntar qué queremos hacer
        if op == 1: #si seleccionamos la primera opción, este nos llevará a cerrar la aplicación
            salir()
        elif op == 2: #si seleccionamos la opción 2, este nos llevará a la función esperar y despues a las opciones de elegir si salir o entrar a la calculadora
            esperar()
            aplicacionmat()

    def altura(): #creamos este def para el algoritmo de nuestro calculo
        print("======================================================")
        print("||  Programa para calcular la altura de un objeto.  || \n======================================================") #mensaje sobre qué haremos
        sombra = float(input("Distancia: ")) #pedimos la distancia del objeto
        alfa = int(input("Angulo: ")) #pedimos el angulo que se encuentra el objeto
        alfa = math.radians(alfa) #convertimos los angulos a radianes
        h = sombra*math.tan(alfa) #metemos lo ingresado dentro de una variable llamada h
        print("La altura es: ", round(h, 1), "metros") #mostramos el resultado por pantalla
        
 
        opciones2()
        opciones2()
    opciones() 
aplicacionmat()



