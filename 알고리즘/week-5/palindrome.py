#회문 찾기
def palindrome(s):
    queue=[]
    stack=[]
    #1단계 문자열의 알파벳 문자를 각각 큐와 스택에 넣음
    #해당 문자가 알파벳이면 큐와 스택에 각각 그 문자 추가
    for x in s:
        if x.isalpha():
            queue.append(x.lower())
            stack.append(x.lower())
#큐와 스택에 들어있는 문자를 꺼내면서 비교
    while queue:
        if queue.pop(0)!=stack.pop():
            return False
    return True

print(palindrome("wow"))
print(palindrome("asdf"))