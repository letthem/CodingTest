def solution(citations):
    answer = 0
    
    citations.sort(reverse=True) # 내림차순 정렬
    
    for i in range(len(citations)):
        if citations[i] < i + 1: # i + 1 보다 작으면
            return i # i값(n - 1)이 정답

    return len(citations)  # 그 외 : ex) 인용 횟수가 모두 같을 때 : [5, 5, 5, 5] 면 4 이상이 4개라 h-index 4 나와야 함

