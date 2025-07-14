def invertDict(dicc: dict={}, allow_duplicates=True):
    if len(dicc) == 0:
        return ("Empty dictionary!")

    invDicc = {}

    for (k, v) in dicc.items():
        # print(f"k: {k=} , v: {v=}")
        new_value = k

        if v in invDicc.keys():
            if not allow_duplicates:
                return f"Error: multiple keys for same value '{v}'"

            new_value = [invDicc[v], k] if type(invDicc[v]) is str \
                                        else invDicc[v].append(k)
        invDicc[v] = new_value

    return invDicc


dicc = {"fruta": "banana", "verdura": "tomate", "legumbre": "garbanzo"}

print("Ejemplo 1:", dicc, "Inverted: ", invertDict(dicc), sep="\n")

dicc = {"fruta": "tomate", "verdura": "tomate", "legumbre": "garbanzo"}

print("\nEjemplo 2 sin duplicados:    ", dicc, "Inverted:", invertDict(dicc, False), sep="\n")
print("\nEjemplo 3 permite duplicados:", dicc, "Inverted:", invertDict(dicc), sep="\n")
