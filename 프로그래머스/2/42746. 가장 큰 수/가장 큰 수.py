def solution(numbers):
    answer = ''
    
    numbers = list(map(str, numbers)) # string으로 바꾸기
    numbers.sort(key = lambda x : x * 3, reverse = True) # lambda(기준) - 3번씩 반복한 ver에서, reverse = True - 내림차순 정렬
    # ex) 3, 30, 34 -> 333, 303030, 343434 -> 343, 333, 303 -> 34, 3, 30
    
    for i in numbers:
        answer += i # string이므로 answer에 더해주기
    
    return str(int(answer))