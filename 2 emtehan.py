def seperator(x):
    zoj = []
    fard =[]
    
    for i in x:
        if i % 2 == 0:
            zoj.append(i)
        else:
            fard.append(i)
    return(tuple(zoj),tuple(fard))
num = list(map(int, input().split(',')))
zoj,fard = seperator(num)

print(zoj,fard)