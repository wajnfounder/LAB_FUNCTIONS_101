def functions(a: int):
   for i in range(a, 0, -1):
       for j in range(i, 0, -1):
        print(j, end="  ")
       print()
functions(8)