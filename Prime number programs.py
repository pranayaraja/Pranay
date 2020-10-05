a=int(input('enter a number:'))
s=0
for i in range(1,a+1):
    if a%i==0:
        s+=1
if s==2:
    print(a,'is a prime number')
else:
    print(a,'is not a prime number')

a=int(input('enter a number:'))
for i in range(2,a):
    if a%i==0:
        print(a,'is not prime')
        break
else:
    print(a,'is a prime')

i=0
a=int(input('enter a number:'))
s=0
while i<=a:
    i+=1
    if a%i==0:
        s+=1
if s==2:
    print(a,'is a prime')
else:
    print(a,'is  not prime')

a=int(input('enter start range:'))
b=int(input('enter end range:'))
for j in range(a,b+1):
    for i in range(2,j):
        if j%i==0:
            break
    else:
        print(j,'is a Prime number')

a=int(input('enter start range:'))
for j in range(a-1,1,-1):
    for i in range(2,j):
        if j%i==0:
            break
    else:
        print(j,'is before prime of',a,end=' ')
        break

a=int(input('enter start range:'))
j=a+1
while a+1:
    for i in range(2,j):
        if j%i==0:
            break
    else:
        print(j,'is after prime of',a,end=' ')
        break
    j+=1

a=int(input('enter a range:'))
for j in range(a-1,1,-1):
    for i in range(2,j):
        if j%i==0:
            break
    else:
        bp=j
        print(j)
        break
k=a
while True:
    for i in range(2,k):
        if k%i==0:
            break
    else:
        ap=k
        print(k)
        break
    k+=1
if abs(a-ap)>abs(a-bp):
    print('nearest prime is',bp)
elif abs(a-ap)<abs(a-bp):
    print('nearest prime is',ap)
else:
    print('nearest prime is',ap,bp)

def is_prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True
def right_prime(n):
    i=n+1
    while 1:
        if is_prime(i):
            return i
        i+=1
def left_prime(n):
    j=n-1
    while 1:
        if is_prime(j):
            return j
        j-=1
def near_prime(n):
    if is_prime(n):
        return n
    else:
        x=right_prime(n)
        y=left_prime(n)
        
        if abs(n-x)<abs(n-y):
            print(x)
        elif abs(n-x)>abs(n-y):
            print(y)
        else:
            print(x,y)
n=15
near_prime(n)
