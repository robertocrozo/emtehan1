def sum (x):
    flor = 0
    for i in x:
        if i == "U" or i == "u":
            flor += 1
        elif i == "D" or i == "d":
            flor -= 1
        else :
            print("Invalid")
            return None

    return flor


x = input()
y = sum(x)
if y is not None :
     print(y)