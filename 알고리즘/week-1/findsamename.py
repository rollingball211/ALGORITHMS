#set을 이용한 집합.
def find_same_name(a):
    n = len(a) #리스트 자료 개수를 n에 저장
    result = set()#결과를 저장할 빈 집합.
    for i in range(0,n-1):
        for j in range (i+1, n):
            if a[i]==a[j]:
                result.add(a[i])
    return result

name =["Tom","Jerry","Spike","Tom"]
print(find_same_name(name))