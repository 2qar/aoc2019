minpw = 130254
maxpw = 678275

def validpw(pw: str) -> bool:
    num = 0
    match = -1
    matchc = 0
    adj = False
    for i in range(6):
        if int(pw[i]) < num:
            return False
        num = int(pw[i])

        if int(pw[i]) != match:
            if matchc == 2:
                adj = True
            match = int(pw[i])
            matchc = 1
        else:
            matchc += 1
    if matchc == 2:
        return True
    return adj

pws = 0
while minpw < maxpw:
    if validpw(str(minpw)):
        print(minpw)
        pws += 1
    minpw += 1
print(pws)
