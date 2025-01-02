def solution(numbers, target):
    n = len(numbers) # numbers 길이만큼 종료 지점 설정
    answer = 0
    def dfs(depth, result):
        if depth == n: # 처음에는 depth가 0 이니 무조건 else로 간다.
            if result == target: # 더하고 뺀 계산값이 목표값과 같으면
                nonlocal answer
                answer += 1 # 정답 처리 : 정답 개수 증가
            return # 재귀 탈출 !
        else: # 재귀함수 작성
            dfs(depth + 1, result + numbers[depth]) # 한 depth 더 들어가서 더하거나
            dfs(depth + 1, result - numbers[depth]) # 한 depth 더 들어가서 빼본다
    dfs(0,0) # depth = 0 과 계산값 0 으로 초기화해서 시작
    return answer