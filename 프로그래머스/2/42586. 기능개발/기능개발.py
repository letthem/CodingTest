import math

def solution(progresses, speeds):
    answer = []
    
    days = [] # 각 작업마다 걸리는 날 배열
    for i in range(len(progresses)):
        res = math.ceil((100 - progresses[i]) / speeds[i])
        days.append(res)
        
    print(days)
    
    count = 1 # 첫 번째 작업 
    work = days.pop(0) # 첫 번째 작업 pop
    
    for i in range(len(days)):
        if days[i] <= work: # work보다 작은 일수만큼 걸리는 작업들은 work와 같이 배포하므로 count 증가
            count += 1
        else: # days[i] > work 일 때 work를 해당 days[i]로 교체
            answer.append(count) # 현재까지 count answer에 push
            work = days[i]
            count = 1 # 다시 1로 초기화
    
    answer.append(count) # 마지막 그룹 count
    
    return answer