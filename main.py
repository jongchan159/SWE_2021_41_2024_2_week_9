from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    # Your Codes
    # ## Do not use input() or print() in your function
    # ## Inputs (nums, target) will given as arguments and the output as 
    # ## return value
    # SWE_2021_41_2024_2_week_7
    
    # 주어진 num 정수 리스트에서 순서대로 두 개를 뽑아서 타겟 수를 만들기
    # 솔루션 하나 찾으면 종료
    # return [index1, index2] (순서를 반환)
    # 이중반복문을 제거할 방법
    # Target - num[i] 값을 num[j]로 찾아보기 -> 결국 이중반복
    # 새로운 딕셔너리에 현재 인덱스와 현재 값을 담고 이전과 대응하는지 체크
    
    numDic = {}
    for i in range(len(nums)):
        subNum = target - nums[i]
        if subNum in numDic: # subNum값이 존재하는지 check
            return [numDic[subNum], i] # 존재하면 subNum의 인덱스와 현재 인덱스를 반환
        numDic[nums[i]] = i # 못찾으면 Key : nums[i](i번째 값), Value = i(현재 인덱스) 형태로 저장
    # 발견 실패 시
    return []