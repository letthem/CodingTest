def solution(N, number):

    # s[i] : s는 N을 1번부터 8번까지 사용하여 만들 수 있는 리스트. set을 사용하여 중복 결과를 제거.
    s = [set() for x in range(8)] # s[0] ~ s[7]. N을 1개부터 8개 까지 사용하여 만든 값들이 number가 아니라면 -1
    for i, x in enumerate(s, start = 1): # s 리스트 순회하면서 i 번째 인덱스에 x값 삽입
        x.add(int(str(N) * i)) # 8개의 set 초기화. N이 5라면, s[0] = {5}, s[1] = {55}, s[2] = {555}, s[3] = {5555}, ...
        
    # s[i]를 돌면서 N을 i+1개 사용했을 때 만들 수 있는 숫자 구하기.
    for i in range(len(s)): # i: 0 ~ 7
        for j in range(i): # j: 0, 01, 012, 0123, ...
            for op1 in s[j]: # op1 : 피연산자1, N을 j+1번 사용하여 만들 수 있는 숫자들
                for op2 in s[i-j-1]: # op2 : 피연산자2, N을 i-j번 사용하여 만들 수 있는 숫자들
                    # op1과 op2를 사칙연산 --> 즉 N을 i+1번 사용하여 만들 수 있는 숫자를 구하게 되고 이를 s[i]에 대입
                    s[i].add(op1 + op2)
                    s[i].add(op1 - op2)
                    s[i].add(op1 * op2)
                    if op2 != 0:
                        s[i].add(op1 // op2)
        if number in s[i]: # N을 i+1번 사용했을 때 찾는 값인 number가 존재 : i+1 return
            answer = i + 1
            break
        else: # N을 8번 사용했는데도 찾는 값 number가 존재 X : -1 return
            answer = -1
    return answer