def solution(inputString):
    l= []
    for i in range(len(inputString)):
        l.append(inputString[i])
    l.reverse()
    l=''.join(l)
    if l==inputString:
        return True
    else :
        return False   