def solution(brown, yellow):
    arr = []
    
    # x * 2 + y * 2 - 4 = brown
    # (x - 2) * (y - 2) = yellow
    
    
    temp = int((brown + 4) / 2 - 2)
    
    # 초기화
    temp2 = 0
    y = 2
    
    #temp 끼리 같아질 때까지 돌면서 y값 찾기
    while temp2 != temp:
        y = y + 1 # y값 증가
        temp2 = ( yellow / ( y - 2 )) + y
        
    # y값으로 x값 찾기
    x = int(( brown + 4 ) / 2 - y)
    
    arr.append(x)
    arr.append(y)
    
    return arr