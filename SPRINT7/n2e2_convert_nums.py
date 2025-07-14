inputData = [ '1.3', 'one' , '1e10' , 'seven', '3-1/2', ('2',1,1.4,'not-a-number'), [1,2,'3','3.4']]

def convertibles(values: list):
    '''
    Separa los valores de una lista entre "numéricos" y no numéricos, convirtiendo
    los valores numéricos a float o int, según sean.
    '''
    numerics  = []
    no_nums   = []
    flattened = []

    for i in values:
        # print(i, isinstance(i, (int, str, float)))
        flattened.append(i) if isinstance(i, (int, str, float)) else flattened.extend(i)

    for i in flattened:
        try:
            num = float(i)
            numerics.append(
                i if isinstance(i, (int, float))
                    else float(i) if 'e' in i or '.' in i
                    else int(i)
            )
        except ValueError:
            no_nums.append(i)

    # return {"Numeric values:": numerics, "Non-Numerics": no_nums}
    return (numerics, no_nums)

# flatten_list(inputData)
converted = convertibles(inputData)
# print(separados)
for x in converted:
    print("Números:     ", end=' ') if isinstance(x[0], (int, float)) else print("No numéricos:", end=' ')
    print(x)
