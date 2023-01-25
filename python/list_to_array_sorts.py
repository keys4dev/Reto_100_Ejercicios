##Convierte una lista en array de objetos y los ordena por clave o valor
a = {'key2':3, 'key1':1, 'key3':2}

a1 = sorted(a.items(), key = lambda x:x[0]) ##->Ordena Por Clave
print(a1)

a2 = sorted(a.items(), key = lambda x:x[1]) ##->Ordena Por Valor
print(a2)