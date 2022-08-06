

arr = tuple(map(int,input().split()))

max_val = -999
min_val = 999

for elem in arr:
    if(elem == -999 or elem == 999):
        break

    elif(elem > max_val):
        max_val = elem
        if(elem < min_val):
            min_val = elem
    elif(elem < min_val):
        min_val = elem
        if(elem > max_val):
            max_val = elem
print(f"{max_val} {min_val}")