def find_max(a):
    n=len(a)         #입력 크기 n
    max_v=a[0]       #리스트의 첫번쨰 값을 최댓값으로 기억
    for i in range(1,n): #1~리스트의 n-1까지 반복
     if a[i]>max_v:      #값이 현재까지 기억된 최댓값보다 크면 대입.
        max_v=a[i]
    return max_v

def find_min(a):
    n = len(a)
    min_v = a[0]
    for i in range(1,n):
        if a[i]<min_v:
            min_v=a[i]
    return min_v

def find_maxidx(a):
    n = len(a)
    maxidx=0
    for i in range(1,n):
        if a[i]>a[maxidx]:
            maxidx=i
    return maxidx
v=[17,92,18,33,58,7,33,42]
print(find_max(v))
print(find_min(v))
print(find_maxidx(v))