minpw = 130254
maxpw = 678275

def validpw(pw: str) -> bool:
    num = 0
    adj = False
    for i in range(6):
        if int(pw[i]) < num:
            return False
        if i < 5 and pw[i] == pw[i+1]:
            adj = True
        num = int(pw[i])
    return adj

pws = 0
while minpw < maxpw:
    if validpw(str(minpw)):
        print(minpw)
        pws += 1
    minpw += 1
print(pws)
