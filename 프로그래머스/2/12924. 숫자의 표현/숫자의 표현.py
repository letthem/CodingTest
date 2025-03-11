def solution(n):
    answer = 0
    
    for i in range(1, n + 1): # 1, 2, 3, ... , 15
        sum = 0
        
        while sum < n: # sum이 n과 크거나 같아질 때까지 i + (i+1) + (i+2) ...
            sum += i
            i += 1 # 연속된 수
        if sum == n: # sum이 n과 같으면 + 1
            answer += 1
        
        # for문
        # i = 1 : 1+2+3+4+5 -> O -> +1
        # i = 2 : 2+3+4+5+6 -> X
        # i = 3 : 3+4+5+6 -> X 
        # i = 4 : 4+5+6 -> O -> +1
        # ...
        # i = 7 : 7+8 -> O -> +1
        # ...
        # i = 15 : 15 -> O -> +1
        
    return answer