
#Chiedi all’utente di inserire 5 numeri e stampa solo i numeri pari in ordine inverso
numeri_1= int(input("enter numero"+"  :"))
numeri_2= int(input("enter numero"+"  :"))
numeri_3= int(input("enter numero"+"  :"))
numeri_4= int(input("enter numero"+"  :"))
numeri_5= int(input("enter numero"+"  :"))

lista = [numeri_1 , numeri_2 , numeri_3 ,numeri_4, numeri_5]
lista.reverse()
for x in lista :
    pari= int(x/2) 
    if pari * 2 == x :
        print(x)
    