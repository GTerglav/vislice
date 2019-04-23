def je_prastevilo(n):
    if n == 1:
        return False
    for a in range(2, n):
        if n % a == 0:
            return False
    return True

#def sez_prast_do(n):
#    sez = []
#    x = 1
#    while x < n:
#       x +=1
#       if je_prastevilo(x):
#            sez.append(x)
#    return sezggegGEQgeqGEQQEGgqe
        
for i in range(2, 201):
    if je_prastevilo(i):
        print(i)
