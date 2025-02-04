from itertools import combinations, product

def solution(dice):
    n = len(dice)
    
    answer = []
    cases = list(combinations(range(n), n//2)) # A가 주사위를 뽑는 경우의 수 nC(n//2)
    # combinations()가 기본적으로 한 번만 순회 가능한 이터레이터를 반환하기 때문에 list로 반환해서 계속 사용할 수 있도록 하자.
    # ex) cases = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
    
    A = [] # 각 조합별 합의 경우의 수 저장 리스트

    for case in cases:
        # 선택된 주사위들의 값 가져오기
        selected_dice = [dice[i] for i in case]

        # 모든 가능한 조합의 합을 구하고 정렬
        all_sums = sorted(sum(comb) for comb in product(*selected_dice))

        # 결과 리스트에 추가
        A.append(all_sums)
        # ex)
            # A[0] = [4, 5, 5, 6]   # (0,1) 선택
            # A[1] = [6, 7, 7, 8]   # (0,2) 선택
            # A[2] = [8, 9, 9, 10]  # (0,3) 선택
            # A[3] = [8, 9, 9, 10]  # (1,2) 선택
            # A[4] = [10, 11, 11, 12]  # (1,3) 선택
            # A[5] = [12, 13, 13, 14]  # (2,3) 선택
        
    a, counts = 0, len(A)  # a: 최댓값 저장, counts: 조합의 개수

    for i in range(counts):
        B = A[counts - i - 1]  # A[i]의 반대편 조합을 가져옴 (대칭되는 B)

        temp = 0  # A[i]가 B보다 이기는 횟수

        for t in A[i]:  # A[i]의 각 값 t에 대해
            left = 0
            right = len(B) - 1 

            while left <= right:  # 이진 탐색 시작
                mid = (left + right) // 2  # 중앙값 찾기

                if B[mid] < t:  # B[mid]가 t보다 작으면
                    left = mid + 1  # 탐색 범위를 오른쪽으로 이동
                else:
                    right = mid - 1  # 탐색 범위를 왼쪽으로 이동

            temp += left  # B에서 t보다 작은 값의 개수를 left가 가리킴

        # 가장 승리 확률이 높은 조합 찾기
        if a < temp:  # 현재 저장된 최대 승리 횟수 a보다 더 높은 temp를 발견하면 갱신
            a = temp  # 최대 승리 횟수 업데이트
            answer = [x + 1 for x in cases[i]]  # 1-based index로 변환하여 저장
            
    return answer