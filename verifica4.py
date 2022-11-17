#Chiedi all’utente quanti numeri vuole inserire. Leggi tutti i numeri in input. Stampa tutti i numeri inseriti al quadrato
numeri= int(input("quanti numeri vuoi inserire"+" "))

for x in range(numeri):
    y=int(input("quanti numeri vuoi inserire"+" "))
    print (pow(y,2))
