# creazione funzioni , una funzione è definita dal comando def 
def my_function():
  print("Hello from a function")  #per eseguirla devo richiamarla 
my_function()


# All'interno di una funzione posso mettere infinite informazioni , le metto tra le parentsi della funzione definita  
def my_function(fname):        
  print(fname + "oliva")

my_function("Emil")
my_function("Tobias")
my_function("Linus")
my_function("formi")

# parametri e argomenti sono informazioni dentro le funzioni , la prima variabile e la seconda vengono associati alla prima e seconda variabile str 
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")
my_function("vasco","giammetta")

# usa l'asterisco prima quando non so quanti sono i miei argomenti esplicitati in my_function, kisd[2] si riferisce alla terza variabile appartenenete a my function 
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

#uso due astirischi quando non so qaunte sono le variabili nella def my_function()
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

#valore parametro predefinito , nella my_function libera mi associa direttamente norway
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")
my_function()


#Puoi inviare qualsiasi tipo di dati di argomento a una funzione (stringa, numero, elenco, dizionario ecc.) e verrà trattato come lo stesso tipo di dati all'interno della funzione.
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)


#per farci ritornare un valore dalla funzione uso return 
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))


# uso il pass per creare una funzione vuota senza che mi dia errore 
def myfunction():
  pass

 # 
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1) # decremento di uno finchè non usciamo da if 
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)


