def solution(participant, completion):
    participant.sort() # 정렬
    completion.sort() # 정렬
    
    for i in range(len(completion)):
        if participant[i] != completion[i]: # 다르면 정답
            return participant[i]
            # a b c d VS a b d e 일 때 c가 정답이지만 d랑 e가 또 비교하기 전에 탈출해야 한다.
    
    # 앞에 것이 다 같으면 마지막 것이 달라 정답
    return participant[-1]
        
    