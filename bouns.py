def functions(a: int):
    result = ""

    for i in range(a, 0, -1):
        for j in range(i, 0, -1):
            result += str(j) + " "
        result += "\n"

    return result

pattern = functions(8)
print(pattern)