def solution(sizes):
    answer = 0
    
    maxArr = []
    minArr = []
    
    # ex) [[60, 50], [30, 70], [60, 30], [80, 40]]
    for i in range(len(sizes)):
        sizes[i].sort() # 정렬. [[50, 60], [30, 70], [30, 60], [40, 80]]
        minArr.append(sizes[i][0]) # [50, 30, 30, 40]
        maxArr.append(sizes[i][1]) # [60, 70, 60, 80]
    
    minNum = max(minArr) # 50
    maxNum = max(maxArr) # 80
    
    answer = minNum * maxNum # 곱한다 !
    
    return answer