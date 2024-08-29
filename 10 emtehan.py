def numbers(x):
    sum = 0
    for i in range (1, x):
        if x % i == 0:
            sum += i
    return sum == x


number = int(input())

if numbers(number):
    print("yes")
else:
    print("no")