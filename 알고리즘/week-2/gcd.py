def gcd(a,b):
    i = min(a,b)
    while True:
        if a%i ==0 and b%i==0:
            return i
        i=i-1

print(gcd(100,45))
print(gcd(1000,150))

#euclid

def ugcd(a,b):
    if b==0:
        return a
    return ugcd(b,a%b)
print(ugcd(100,45))
print(ugcd(1000,150))

#연습문제 3 fibonacci

def fibonacci(a):    #a는 피보나치수열의 갯수
    if a==0:
        return 0
    elif a==1:
        return 1;
    else:
        return fibonacci(a-1) + fibonacci(a-2)


print(fibonacci(4))
