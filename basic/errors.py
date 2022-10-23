# print(0 / 0)
# print(result)
print('Hola')

def suma(x, y): return x + y

assert suma(2, 2) == 4

print('Hola 2')

age = 10

if age < 18:
    raise Exception('No se permiten menores de edad') # Se lanza una exception

print('Hola 2')
