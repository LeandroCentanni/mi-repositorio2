#!/usr/bin/env python
# coding: utf-8

# In[6]:


numeros = [1,2,3,4,5]

numero_buscar = int (input("ingresar un numero para buscar en la lista:"))

encontrado = False
indice = 0
len_lista = len(numeros)
while indice < len_lista:
    if numeros [indice] == numero_buscar:
        encontrado = True
        break
    indice += 1
    
if encontrado:
    print("el numero esta en la lista.")

else:
    print("el numero no esta en la lista.")
    


# In[13]:


numeros = []

while True:
    numero=int(input("Ingrese un numero (ingrese 0 para finalizar): "))
    if numero == 0:
        break
    numeros.append(numero)
suma = 0
for num in numeros:
    suma += num
print("La suma de los números ingresados es:", suma)


# In[ ]:




