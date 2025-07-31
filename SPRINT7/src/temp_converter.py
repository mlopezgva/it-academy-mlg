from cli_funcs import ask_num_value

temp = ask_num_value("Temp: ")
from_scale = input("Escala: ")
to_scale = input("Convertir a: ")

scale = {
    "celsius":    {
        "symbol":   "ºC",
        'name':     "Celsius",
        'longName': 'grados Celsius',
        'to_k':     (lambda temp: 273.15 + temp),
        'from_k':   (lambda temp: temp - 273.15)
    },
    "fahrenheit": {
        "symbol":   "ºF",
        'name':     "Fahrenheit",
        'longName': 'grados Fahrenheit',
        'to_k':     (lambda temp: ((temp - 32) / 1.8) + 273.15),
        'from_k':   (lambda temp: ((temp - 273.15) * 1.8) + 32)
    },
    "kelvin":     {
        "symbol":   "K",
        'name':     "Kelvin",
        'longName': 'Kelvins',
        'to_k':     (lambda temp: temp),
        'from_k':   (lambda temp: temp)
    },
    "rankine":    {
        "symbol":   "R",
        'name':     "Rankine",
        'longName': 'Rankines',
        'to_k':     (lambda temp: temp / 1.8),
        'from_k':   (lambda temp: temp * 1.8)
    },
    "reaumur":    {
        "symbol":   "ºR",
        'name':     "Réaumur",
        'longName': 'grados Réaumur',
        'to_k':     (lambda temp: (temp * 1.25) + 273.15),
        'from_k':   (lambda temp: (temp - 273.15) / 1.25)
    }
}

print(scale['celsius']['to_k'](10.0))
print(scale['celsius']['from_k'](283.15))

if  to_scale.__len__:
    # print(f"Convierto de {from_scale} a Kelvin: {scale[from_scale]['to_k'](temp)}")
    print(scale[to_scale]['from_k'](scale[from_scale]['to_k'](temp)))
