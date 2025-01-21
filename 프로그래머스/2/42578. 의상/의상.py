def solution(clothes):
    answer = 0
    
    # 딕셔너리 초기화
    dict = {}

    for i in clothes:
        key = i[1] # 두 번째 원소 가져오기
        if key in dict:
            dict[key] += 1 # 이미 있으면 개수 증가
        else:
            dict[key] = 1 # 없으면 key 생성하면서 1로 초기화

    # count 초기화
    count = 1
    for i in dict.values():
        count *= (i + 1) # 안 입은 경우의 수까지 포함

    answer = count - 1 # 아무것도 안 입은 경우의 수 빼기
    
    return answer