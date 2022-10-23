# --------------- Sintaxis tradicional -------
dict = {}

for i in range(1, 11):
    dict[i] = i * 2

print(dict)
# --------------------------------------------

# -------------- Sintaxis List Comprehension ------------
dict_v2 = { i: i * 2 for i in range(1, 5)}
print(dict_v2)
# -------------------------------------------------------

# ------------- Generar un diccionario a partir de una lista -------------
import random

countries = ['col', 'mex', 'bol', 'pe']
population = {}

for country in countries:
    population[country] = random.randint(1, 100)

print(population)
# ------------------------------------------------------------------------

# ------------- Generar un diccionario a partir de una lista con List Comprehension -------------
population_v2 = {country: random.randint(1, 100) for country in countries}
print(population_v2)
# -----------------------------------------------------------------------------------------------

# -------------------- Unir dos listas  en un lista de tuplas -----------------------
names = ['nico', 'zule', 'santi']
ages = [12,56, 98]

print(list(zip(names, ages)))
# ----------------------------------------------------------------------------------

# ------------------ Generar diccionario a partir de la lista de tuplas anterior ----------------
new_dict = {name: age for (name, age) in zip(names, ages)}
print(new_dict)
# -----------------------------------------------------------------------------------------------