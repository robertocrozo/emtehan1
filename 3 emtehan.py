def sum(x):# factorial
    if x == 0 or x == 1:
        return 1
    else:
        return x * sum(x - 1)

# input
num_input = int(input("Enter your number: "))
# seda kardan va gereftan tabe
x = sum(num_input)

print(x)