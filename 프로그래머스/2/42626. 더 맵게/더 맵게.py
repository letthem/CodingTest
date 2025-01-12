import heapq

def solution(scoville, K):
    answer = 0
    
    heapq.heapify(scoville) # scoville 배열을 heap으로
    
    while scoville:
        if scoville[0] >= K: # scoville[0]이 K보다 크거나 같으면 모든 스코빌 지수가 K 이상이므로 탈출
            break
        elif scoville[0] == scoville[-1]: # scoville[0]이 가장 마지막 값과 같고 K보다 작으므로
            return -1
        else:
            min = heapq.heappop(scoville)
            min2 = heapq.heappop(scoville)
            heapq.heappush(scoville, min + min2 * 2)
            answer += 1

    return answer
