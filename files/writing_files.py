# Escribir nuevas lineas al final del archivo
with open('files/text.txt', 'r+') as file:
    for line in file:
        print(line)

    file.write('\nNueva linea insertada')

# Escribir nueva información en el archivo borrando la anterior
with open('files/text.txt', 'w+') as file:
    for line in file:
        print(line)

    file.write('\nNueva linea insertada')
    file.write('\nLuis Miguel es...')
    file.write('\n¡Exacto es hermoso!')