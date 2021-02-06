#sel_sort (1)
def find_min_idx(a):
    n=len(a)
    min_dix = 0
    for i in range(1,n):
        if a[i]< a[min_dix]:
            min_dix = i
    return min_dix

def sel_sort(a):
    result = [] 
    while a: #주어진 리스트에 값이 남아있는동안 계속
        min_idx=find_min_idx(a) #리스트에 남아있는 값 중 최솟값의 위치
        value = a.pop(min_idx) #찾은 최솟값을 빼내어 value에 저장
        result.append(value)
    return result

d=[2,4,5,1,3]
print(sel_sort(d))        

#sel sort (2)
def sel_sort_2(a):
    n = len(a)
    for i in range(0,n-1):#0부터 n-2까지 반복 #i번 위치부터 끝까지 자료 값 중 최솟값의 위치를 찾음
        min_idx= i
        for j in range(i+1,n):
            if a[j]<a[min_idx]:
                min_idx=j
                a[i],a[min_idx]=a[min_idx],a[i]

e=[2,4,5,1,3]
sel_sort_2(e)
print(e)