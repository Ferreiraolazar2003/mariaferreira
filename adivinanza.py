# juego de adivinar el numero, todo juntos 
#adivinar un numero generado aleatoriamente 
#ir introduciendo por teclado el dato a adivinar 


from random import randint
generado=randint(0,10)
#print(generado)
condicion=True
while condicion:
    numero=input("dame un numero del 0 al 10:")
if generado==int(numero):
    print("ganaste una anvorgesa que lore paga")
    condicion=False
else:
    print("el perdedor compra pizza a lore")
    
