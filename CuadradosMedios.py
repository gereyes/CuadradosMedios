#Programa basado en el metodo Cuadrados del centro
#Von NeumanN
#Genesis Jesus Reyes Osnaya

semilla = int(input("Ingresa la semilla de 4 digitos: ")) #Pedimos la semilla
pedida = int(input("Cantidad de numeros: ")) #Pedimos la cantidad de numeros a generar
contador = 0
while (contador < pedida):
    #Elevamos la semila al cuadrado
    #zfill me permite determinar cuantos digitos quiero
    #ademas de no llegar a los digitos que necesito
    #rellena de ceros a la izquierda hasta completar
    #[2:6] me dice que quiero mostrar apartir de la posicion
    #2 hasta la posicion 6
    semilla = int(str(semilla * semilla).zfill(8)[2:6])
    print(str(semilla).zfill(4))
    contador = contador + 1




##===============
##  Algoritmo   |
##===============

# 1) Elegir una semilla de 4 numeros enteros.

# 2) Elevar nuestra semilla al cuadrado.

# 3) Tomar los digitos del centro (Eliminar dos digitos de la izquierda
#    y dos digitos de la derecha). * Nota solo cuando tiene 8 digitos *.

# 4) Final el numero que nos dio es el resultado, si queremos mas numeros
#    hay que repetir el proceso pero ahora con la ultima semilla.

##===============
##  Ejemplo     |
##===============

#semilla: 7531
#elevado al cuadrado: 56715961
#tomar los del centro:7159
#elevarlo al cuadrado: 51251281
#tomar el centro otra vez: 2512
#elevarlo al cuadrado: 6310144
#tomar el centro: 3101 eliminamos uno izquierdo y dos derechos
