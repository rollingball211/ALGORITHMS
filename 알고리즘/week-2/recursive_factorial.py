def factorial(n):
    if n<=1:
        return 1
    return n * factorial(n-1)

print(factorial(4))

#연습문제 4-1
def sum1ton(n):
    if n<=1:
        return 1
    return n + sum1ton(n-1)

print(sum1ton(10))
#연습문제 4-2 최댓값 찾기
def findMax(a,n):
    if n==1:
        return a[0]
    max= findMax(a,n-1)
    if max>a[n-1]:
        return max
    else:
        return a[n-1]




a=[1,15,3,6,7,20,35]    
print( findMax(a,len(a)))