num=int(input('Digite um número para Fibonacci: '))
c=0
n1=0
n2=1
while c<=num:
    print('{} - {} '.format(n1, n2),end=' - ')
    n1=n1+n2
    n2=n1+n2
    c+=2