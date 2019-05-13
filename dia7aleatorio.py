#creamos un archivo nuevo 
#guardamos en la carpeta del repositorio
#con la extencion .py
#uso de numeros aleatorios 

#importamos la libreria randint
from random import randint
aleatorio=randint(0,20)   #creamos una variable y generamos un numero aleatorio entre 0 y 20 
print(aleatorio)  #imprimimos el numero generado

#ejercicio 
#escribir una funcion sorteo()que reciba 
#una lista de participantes y elejir a uno 
#de los participantes aleatorios, y 
#retornar esa persona elegida
#desafio: no volver a retornar una persona 
#ya sorteada

from random import randint  #imporamos la funcion de la  libreria randint

def sorteo(lista1): #definimos una funcion
   aleatorio=randint(0,len(lista1)-1)  #creamos la variable aleatorio llamamos la funcion randint le establecemos los parametros, siempre empieza de cero
                                       #y no sabemos hasta donde llega y le colocamos la funcion len menos 1 
   ganador=lista1[aleatorio]    #seleccionamos un elemento de la lista y guardamos  en variable ganador
   return ganador               #para traer el resultado de vuelta 

listasorteo=["mauricio","francisco","dulce","maria"]   #creamos una lista con los nombres que se van a sortear 
resultado=sorteo(listasorteo)  #llamamos a la funcion y guardamos en una variable el resultado retornado 
print(resultado) #imprimimos el ganador


