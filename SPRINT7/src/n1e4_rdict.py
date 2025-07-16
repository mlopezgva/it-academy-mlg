from rdict_helpers import dict_has_dupes, dupes_err_msg

def invertDict(dicc: dict={}):
    if len(dicc) == 0:
        return ("Empty dictionary!")

    if dict_has_dupes(dicc):
        return dupes_err_msg

    invDicc = {}

    for (k, v) in dicc.items():
        invDicc[v] = k

    return invDicc

dicc = {"fruta": "banana", "verdura": "tomate", "legumbre": "garbanzo"}

print("Ejemplo 1:", dicc, "Inverted: ", invertDict(dicc), sep="\n")

dicc = {"fruta": "tomate", "verdura": "tomate", "legumbre": "garbanzo"}

print("\nEjemplo 2:", dicc, "Inverted:", invertDict(dicc), sep="\n")
