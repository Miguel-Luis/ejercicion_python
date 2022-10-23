set_countries = {'col', 'mex', 'bol'}


# conocer el tamaño del conjunto
size = len(set_countries)
print(size) # 3

print('col' in set_countries) # True
print('pe' in set_countries) # False

# add
set_countries.add('pe')
print(set_countries) # {'col', 'mex', 'bol', 'pe'}
set_countries.add('pe')
print(set_countries) # {'col', 'mex', 'bol', 'pe'}

# update, lo que hace es sumar elementos a los existentes
set_countries.update({'ar', 'ecua', 'pe'})
print(set_countries) # {'col', 'mex', 'bol', 'pe', 'ar', 'ecua'}

# remove

set_countries.remove('col')
print(set_countries) # {'mex', 'bol', 'pe', 'ar', 'ecua'}

# si le doy remove a un elemento que no existe, 
# lanza un error python, 
set_countries.remove('ar')

# para eso usamos discard, si no existe, no falla.
set_countries.discard('arg')
print(set_countries)
set_countries.add('arg')
print(set_countries)

# limpiar todo el conjunto, lo deja en vacío
set_countries.clear()
print(set_countries)
print(len(set_countries))