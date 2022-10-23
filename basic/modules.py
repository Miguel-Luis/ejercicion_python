import numbers
from sqlite3 import Timestamp
import sys
import re # Sirve para trabajar con expresiones regulares
import time # Sirve para trabajar con fechas y tiempo
import collections # Sirve para el manejo de listas

print(sys.path) # Muestra la ruta en la que se encuentra este archivo

text = "Mi numero de teléfono es 3218550228, el código del país es 57, mi número de la suerte es 13"
result = re.findall("[0-9]+", text)
print(result)

timestamp = time.localtime()
print(timestamp)

local = time.localtime()
result = time.asctime(local)
print(result)

numbers = [1, 1, 2, 1, 2, 1, 4, 5, 3, 3, 21]
counter = collections.Counter(numbers)
print(counter)