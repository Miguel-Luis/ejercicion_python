""" Se define un conjunto de elementos se diferencia de los
diccionarios porque no tiene clave valor. 
Un conjunto no puede tener elementos repetidos
"""
set_countries = {'col', 'mex', 'bol'}
print('Conjunto de países')
print(set_countries)
print(type(set_countries))
print()

set_numbers = {1, 2 , 3, 4, 5}
print('Conjunto de números')
print(set_numbers)
print(type(set_numbers))
print()

set_types = {1, 'hola', False, 12.12}
print('Conjunto de diferentes tipos de datos')
print(set_types)
print(type(set_types))
print()

# Crear un conjunto a partir de un String
set_from_string = set('hola')
print('Conjunto a partir de un string')
print(set_from_string)
print(type(set_from_string))
print()

# Crear un conjunto a partir de una tupla
set_from_tuple = set(('abc', 'dfg', 'hij', 'k'))
print('Conjunto a partir de una tupla')
print(set_from_tuple)
print(type(set_from_tuple))
print()

# Crear una conjunta a partir de una lista
set_from_list = set([1, 2, 3, 4, 5, 2 , 4, 6])
print('Conjunto a partir de una lista')
print(set_from_list)
print(type(set_from_list))
print()

# Pasar de conjunto a lista
unique_numbers = list(set_from_list)
print('Lista de números sin repetir')
print(unique_numbers)
print(type(unique_numbers))
print()