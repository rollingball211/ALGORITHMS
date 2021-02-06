#순차 탐색으로 특정 값의 위치 찾기
#입력 리스트 a, 찾는 값 x

def search_list(a,x):
    n = len(a)
    for i in range(0,n): #리스트의 모든 값 검사
        if x==a[i]:      
            return i     #같으면 위치를 돌려줌
    return -1


#7-1 
def search_list2(a , x):
    n = len(a)
    b = []
    for i in range(0,n):
        if x==a[i]:
            return b.append(i)
    return b


v= [17,92,18,33,58,7,33,42]
print(search_list(v,18))



print(search_list2(v,33))

#7-3
def search_name(stuno,stuname,find_no):
    n= len(stuno)
    for i in range(0,n):
        if find_no==stuno[i]:   #학생 번호가 찾는 학생 번호와 같다면
            return stuname[i]         # 학생 이름으로 리턴

    
    return "?"


stu_no =[39,14,67.105]
stu_name=["Justin","John","Mike","Summer"]

print(search_name(stu_no,stu_name,67))
print(search_name(stu_no,stu_name,105))