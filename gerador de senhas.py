import random 

m = 'abcdefghijklmnopqrstuvwxyz'
M = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
n = '0123456789'
s = '[]{}()*#;/,-_%'
q = input('Digite qual tamanho da senha: ')
qI = int(q)
l = qI
a = m + M + n + s
passwordAll = "".join(random.sample(a,l))
print ('passwordAll = ' + passwordAll) 
