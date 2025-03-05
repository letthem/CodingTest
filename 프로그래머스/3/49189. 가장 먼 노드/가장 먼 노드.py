from collections import deque

def solution(n, edge):
    answer = 0
    queue = deque()
    distance = [0] * (n + 1) # 각 노드별로 노드 1부터의 거리 - 0으로 초기화
    queue.append(1)  # 큐에 1번 노드 넣기
    distance[1] = 1  # 1번 노드 방문 표시 (0과 구분)
    edge.sort()  # 간선 정렬. [[1, 2], [1, 3], [2, 4], [3, 2], [3, 6], [4, 3], [5, 2]]
    
    # 그래프 생성
    graph = [[] for _ in range(n + 1)]
    for i in edge:  # 인접 리스트 방식으로 그래프 구현. 양방향 간선 (쌍방 연결)
        graph[i[0]].append(i[1]) # ex) 1번 노드에 2번 연결
        graph[i[1]].append(i[0]) # ex) 2번 노드에 1번 연결

    
	# BFS 탐색
    while queue:
        current = queue.popleft() # 현재 노드 꺼냄
        for node in graph[current]: # 현재 노드와 연결된 노드 탐색
            if distance[node] == 0:  # 방문 여부를 확인하고, 방문한 적이 없는 경우 (0으로 초기화 된 상태니까)
                queue.append(node)  # 노드를 큐에 추가
                distance[node] = distance[current] + 1  # 해당 노드의 값을 현재 노드의 값에 1을 더한 값으로 변경 (거리 갱신)
	# => distance = [0, 1, 2, 2, 3, 3, 3]
    
    max_distance = max(distance)  # 최대 거리
    for j in distance:
        if j == max_distance: # 최대 거리와 같은 것 개수 세면 정답
            answer += 1
    return answer