def solution(distance, rocks, n):
	# 이진탐색 처음 범위 : 1 ~ distance
    left = 1
    right = distance
    
    # 바위 위치 정렬, 도착지점 가장 끝에 추가
    rocks.sort()
    rocks.append(distance)
    
    while left <= right:
        mid = (left + right) // 2 # 징검다리 사이 최소 거리 후보 (답이 될 수 있다)
        
        delete = 0 # 제거한 바위 개수
        prev_rock = 0 # 이전 바위의 위치
        
        for rock in rocks: # 정렬된 돌을 돌면서
            dist = rock - prev_rock # 현재 바위에서 이전 바위까지 거리
            
            if dist < mid: # 거리가 커트라인 보다 작다면(최솟값을 구해야 하므로)
                delete += 1 # 바위를 제거
                
                if delete > n: # 제거할 바위의 수 초과한다면 break. 더 작은 mid값이 필요하다
                    break
            
            else: # 바위를 제거하지 않았다면
                prev_rock = rock # 현재 바위를 이전 바위로 갱신
                
        # 제거할 바위의 수 초과한 경우 : 더 작은 mid값이 필요하다
        if delete > n:
            right = mid - 1
        # 제거할 바위의 수 이하인 경우 : 정답이거나 더 큰 mid값이 필요하다
        else:
            answer = mid # 답이 될 수 있다!
            left = mid + 1
    return answer