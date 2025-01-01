def solution(answers):

    length = len(answers)
    
    # 1번 수포자
    a = [(i % 5) + 1 for i in range(length)]
    
    # 2번 수포자
    b_pattern = [2, 1, 2, 3, 2, 4, 2, 5] # 2번 수포자의 반복되는 패턴 정의
    b = [b_pattern[i % len(b_pattern)] for i in range(length)]
    
    # 3번 수포자
    c_pattern = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] # 3번 수포자의 반복되는 패턴 정의
    c = [c_pattern[i % len(c_pattern)] for i in range(length)]
    
    # 맞춘 개수 count_a, count_b, count_c에 할당
    counts = [
        sum(1 for i in range(length) if answers[i] == person[i])
        for person in [a, b, c]
    ]
    count_a, count_b, count_c = counts
    
    # 가장 높은 점수
    max_value = max(counts)
    
    # 동점자 처리 (1, 2, 3으로 오름차순 정렬)
    answer = [i + 1 for i, count in enumerate(counts) if count == max_value]

    return answer