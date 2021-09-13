

def solution(a, b):
    if len(a)>len(b):
        return b + a +b
    elif len(b)>len(a):
        return a + b + a


print(solution("45", "a"))