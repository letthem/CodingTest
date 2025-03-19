def solution(n, words):
    
    checked = [words[0]]
    
    for i in range(1, len(words)):
        #i번째 단어와 첫 글자와 i-1번째 단어의 마지막 글자랑 비교
        if words[i][0] == words[i-1][-1] and words[i] not in checked:
            checked.append(words[i]) # 끝말잇기 성공 시 checked에 추가
        else: # 끝말잇기 실패 시
            return [(i % n) + 1, (i // n) + 1] # 탈락하는 사람의 번호, 자신의 몇 번째 차례

    return [0,0] # 탈락자 없다면 [0, 0] 리턴