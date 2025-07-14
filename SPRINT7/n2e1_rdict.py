def invertDict(dicc: dict={}):
    if len(dicc) == 0:
        return ("Empty dictionary!")

    invDicc = {}

    for (k, v) in dicc.items():
        # print(f"k: {k=} , v: {v=}")
        new_value = k

        if v in invDicc.keys():
            # print(f"Error: multiple keys for same value '{v}'")
            # print(type(invDicc[v]))
            # print("v:", invDicc[v], k)
            new_value = [invDicc[v], k] if type(invDicc[v]) is str \
                                        else invDicc[v].append(k)
            # print(f"Added {new_value=}")
        invDicc[v] = new_value

    return invDicc

dicc = {"fruta": "banana", "verdura": "tomate", "legumbre": "garbanzo"}

print("Ejemplo 1:", dicc, "Inverted: ", invertDict(dicc), sep="\n")

dicc = {"fruta": "tomate", "verdura": "tomate", "legumbre": "garbanzo"}

print("\nEjemplo 2:", dicc, "Inverted:", invertDict(dicc), sep="\n")
