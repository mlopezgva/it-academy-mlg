def invertDict(dicc: dict={}):
    if len(dicc) == 0:
        return ("Empty dictionary!")

    if len(set(dicc.values())) != len(dicc):
        return (f"Error: multiple keys for same value")

    invDicc = {}

    for (k, v) in dicc.items():
        invDicc[v] = k

    return invDicc

dicc = {"fruta": "banana", "verdura": "tomate", "legumbre": "garbanzo"}

print("Ejemplo 1:", dicc, "Inverted: ", invertDict(dicc), sep="\n")

dicc = {"fruta": "tomate", "verdura": "tomate", "legumbre": "garbanzo"}

print("\nEjemplo 2:", dicc, "Inverted:", invertDict(dicc), sep="\n")
