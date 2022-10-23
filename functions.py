def my_print(var):
    print(f"This is my print {var}")
    

def suma(a, b):
    return f"{a} + {b} = {a + b}"

# -------- Retornos multiples ---------
def find_volume(length = 1, width = 1, depth  = 1):
    return length * width * depth, width, 'hola' # con esta sintaxis se retornan los valores en una tupla


my_print("Luis Miguel")
print(suma(7, 6))
print(find_volume(13, 13, 13))