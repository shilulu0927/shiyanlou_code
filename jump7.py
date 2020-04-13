for a in range(0,101):
    if a%7==0:
        continue
    elif a%10==7:
        continue
    elif a//10==7:
        continue
    else:
        print(a)
