def solution(n, lost, reserve):
    answer = 0
    
    count = n - len(lost) # 전체 - 도난당한 학생의 수
    
    # 정렬
    lost.sort()
    reserve.sort()
    
    for i in reserve[:]:
        if i in lost: # 여벌 체육복 학생이 체육복을 도난당했다면
            count += 1 # 도난당한 학생의 수가 줄었으므로 count 도 증가시켜준다.
            lost.remove(i) # lost에서 삭제
            reserve.remove(i) # reserve에서 삭제
            
    for i in range(len(reserve)):
        if (reserve[i] - 1) in lost: # reserve[i] - 1 학생이 도난당한 학생이라면
            count += 1 # 빌려줘서 count 증가
            lost.remove(reserve[i] - 1) # reserve[i] - 1 학생 lost에서 삭제
            
        elif (reserve[i] + 1) in lost: # reserve[i] + 1 학생이 도난당한 학생이라면
            count += 1 # 빌려줘서 count 증가
            lost.remove(reserve[i] + 1) # reserve[i] + 1 학생 lost에서 삭제
        
        
    answer = count
    
    return answer