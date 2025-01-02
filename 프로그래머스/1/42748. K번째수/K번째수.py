def solution(array, commands):
    answer = []
    
    for command in commands:
        i, j, k = command  # start, end, k 추출
        sliced = array[i - 1:j]
        sliced.sort()  # 정렬
        sliced[k - 1] # k번째수
        answer.append(sliced[k - 1])
    
    return answer