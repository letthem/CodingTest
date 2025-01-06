def solution(people, limit):
    count = 0
    people.sort() # 사람 정렬 (가장 몸무게 작은 사람 + 몸무게 큰 사람끼리 짝을 이루기 위해)
    
    a = 0 # 가장 가벼운 사람
    b = len(people) - 1 # 가장 무거운 사람
    
    while a <= b:
        if people[a] + people[b] <= limit:
            count += 1 # 최대 2명씩. 같이 타는 경우 + 1
            a += 1 # a 키우고
            b -= 1 # b 줄이기
        else:
            count += 1 # 한 명씩 타는 경우
            b -= 1 # b가 몸무게가 너무 많이 나가니 b 줄이기
    
    return count