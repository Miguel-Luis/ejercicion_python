items =  [
    {
        "product": "camisa",
        "price": 100
    },
    {
        "product": "pantalones",
        'price': 300
    },
    {
        "product": "calzoncillos",
        "price": 50
    }
]

# Modifica el diccionario original
def add_taxes(item):
    item["taxes"] = item["price"] * .19
    return item

# Permite obtener un nuevo diccionario modificado sin modificar el diccionario original
def add_taxes_copy(item):
    new_item = item.copy()
    new_item["taxes"] = new_item["price"] * .19
    return new_item

prices = list(map(lambda item: item["price"], items))
print(prices)

new_items = list(map(add_taxes, items))
print(items)