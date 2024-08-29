def sum (x):# bra har u +1 va d -1 
    flor = 0
    for i in x:
        if i == "U" or i == "u":
            flor += 1
        elif i == "D" or i == "d":
            flor -= 1
        else :
            print()
            return None

    return flor


x = input()
y = sum(x)
if y is not None : # agar khali nabod flor  print mikonim
     print(y)