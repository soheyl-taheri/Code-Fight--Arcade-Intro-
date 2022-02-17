def solution(inputArray):
    p=[]
    s=0
    for i in range(len(inputArray)-1):
        s=inputArray[i]*inputArray[i+1]
        p.append(s)
        
    return max(p)