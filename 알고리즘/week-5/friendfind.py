def print_all_freinds(g,start):
    queue =[] #앞으로 처리해야 할 사람들을 큐에 저장
    done = set() #이미 큐에 추가한 사람들을 집합에 기록
    
    queue.append(start) #자신을 큐에 넣고 시작
    done.add(start) #집합에도 추가

    while queue:     #큐에 처리할 사람이 남아있는 동안
        p=queue.pop(0) # 큐에서 처리 대상을 한명 꺼내
        print(p) # 이름을 출력
        for x in g[p]: #그의 친구들 중에
            if x not in done: #큐에 추가된적이 없는 사람을
                queue.append(x) #큐에 추가하고
                done.add(x) #집합에도 추가


fr_info ={
    'Summer':['John','Justin','Mike'],
    'John':['Summer','Justin'],
    'Justin' :['John','Summer','Mike','May'],
    'Mike':['Summer','Justin'],
    'May':['Justin','Kim'],
    'Kim':['May'],
    'Tom':['Jerry'],
    'Jerry':['Tom']
}

print_all_freinds(fr_info,'Summer')