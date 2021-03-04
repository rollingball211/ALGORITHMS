def find_same_name(a):
    #1단계 각 이름이 등장한 횟수를 딕셔너리로 만듬.
    name_dict={}
    for name in a:
        if name in name_dict:
            name_dict[name]+=1 #등장횟수 1회 증가
        else:
            name_dict[name]=1 #같은 이름이면 등장횟수 1.
    #2단계 만들어진 딕셔너리에서 등장횟수가 2이상인 것을 결과에 추가
    result=set()
    for name in name_dict:
        if name_dict[name]>=2:
            result.add(name)

    return result

name=["Tom","Jerry","Mike","Tom"]
print(find_same_name(name))

def find_name(stinfo,stno):
    if stno in stinfo:
        return stinfo[stno]
    else:
        return "?"

sample_info={
    39:"Justin",
    14:"John"
}
print(find_name(sample_info,39))
