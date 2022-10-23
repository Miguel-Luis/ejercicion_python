file = open('files/text.txt')
# print(file.read()) # Le todo el archivo

# print(file.readline()) # Le linea por linea

# De esta manera se abre el archivo y al final se cierra sin tener que indicarlo
with open('files/text.txt') as file:
    for line in file:
        print(line)