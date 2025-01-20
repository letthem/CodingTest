def solution(nums):
    answer = 0
    maxNum = 0
    maxNum = int(len(nums) / 2) # 최대로 선택할 수 있는 수
    
    arr = []
    for i in range(len(nums)):
        if nums[i] not in arr: # arr에 없으면 넣기 (중복값 없게 arr에 담기)
            arr.append(nums[i])
        if len(arr) == maxNum: # arr의 크기가 maxNum이면 최대로 선택할 수 있는 수이므로 빠져나오기
            break;
    
    answer = len(arr) # arr의 크기가 답
        
    return answer