import utils

def run():
    keys, values = utils.get_population()
    print(keys, values)

data = [
    {
        'Country': 'Colombia',
        'Population': 500
    },
    {
        'Country': 'Bolivia',
        'Population': 300
    }
]

if __name__ == '__main__': # Si se ejecuta directamente el archivo desde la terminal
    run()