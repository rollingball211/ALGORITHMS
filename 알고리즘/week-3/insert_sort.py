#리스트 r에서 v가 들어가야할 위치를 돌려주는 함수.
def find_insert_idx(r,v):
    #이미 정렬된 리스트 r의 자료를 앞에서부터 차례로 확인
    for i in range(0,len(r)):  #v값보다 i번 위치에 있는 자료값이 크면 v가 그 값 바로앞에 놓여야 정렬 순서가 유지됨.
        if v<r[i]:
            return i #적절한 위치를못 찾았으면 v가 r[i]의 모든 값보다 크기 때문에 맨 뒤로 감.
    return len(r)

def insertsort(a):
    result=[]
    while a:
        value = a.pop(0) #리스트의 첫번째에서 하나를 꺼냄
        ins_idx = find_insert_idx(result,value) #꺼낸 값이 들어갈 위치를 찾음 .
        result.insert(ins_idx,value) #찾은 위치에 값 삽입.
    return result

d=[2,4,5,1,3]
print(insertsort(d))

def insertsort2(a):
    n = len(a)
    for i in range(1,n): #1부터 n-1까지 (리스트)
        key = a[i] #i번 위치를 key값에 저장.
        j= i-1 #j를 i 바로 왼쪽 위치에 저장. #리스트에 j번 위치에 있는 값과 key를 비교, key가 삽입될 적절한 위치를 찾음.
        while j>=0 and a[j]>key: #리스트의 j값은 0 이상 이어야함.
            a[j+1] = a[j] #삽입할 공간이 생기도록 값을 오른쪽으로 한 칸 이동
            j-=1 #??이게뭐지
        a[j+1] = key #찾은 삽입 위치에 key를 저장.

e=[2,4,5,1,3]
print(insertsort2(e))