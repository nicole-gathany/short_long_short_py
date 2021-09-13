#Given 2 strings, a and b, return a string of the form short+long+short, with the shorter string on the outside and the longer string on the inside. The strings will not be the same length, but they may be empty ( zero length ). 

#For example: (Input1, Input2) --> output



def solution(a, b):
    if len(a)>len(b):
        return b + a +b
    elif len(b)>len(a):
        return a + b + a


print(solution("45", "a"))
print(solution("1", "22")) #"1221"
print(solution("22", "1")) # "1221"