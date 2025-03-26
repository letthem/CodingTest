def solution(n):
    for n2 in range(n + 1, 1000001): # n + 1부터 돌면서
        if bin(n).count('1') == bin(n2).count('1'): # 이진수(bin)에서 1의 개수가 같은 가장 첫 숫자 n2를 return
            return n2
