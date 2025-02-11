def solution(priorities, location):
    answer = 0
    queue = []

    for i, p in enumerate(priorities):  # enumerate 사용
        queue.append((i, p)) # (index, priorities) => [(0, 2), (1, 1), (2, 3), (3, 2)]
        
    while True:
        cur = queue.pop(0) # 가장 앞 pop. (current)
        if any(cur[1] < q[1] for q in queue): # 현재 요소의 우선순위보다 queue에 있는 어떤 요소의 우선순위가 더 큰 게 있다면
            queue.append(cur) # 현재 요소를 가장 뒤에 append
        else: # 현재 요소의 우선순위가 가장 크다면 pop으로 인해 개수 하나가 빠지는 것이므로
            answer += 1 # answer의 index 늘리고
            if cur[0] == location: # 만약 현재 index가 location과 같다면 답
                return answer