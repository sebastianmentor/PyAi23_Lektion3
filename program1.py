# lista = [1,2,3,4,5,5,5]

# lista.remove()

lista = [42,3.14,None,False,None]
print(lista) 
ny_lista = lista[:]
ny_lista.remove(None)
print(ny_lista)
print(lista)