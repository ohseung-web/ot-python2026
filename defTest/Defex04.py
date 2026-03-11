def find_min_max(numbers):
    # 만약 리스트가 비어있다면 None 반환
    if not numbers:
        return None
    
    max_val = max(numbers)
    min_val = min(numbers)
    
    return (max_val, min_val) # 결과값을 튜플로 묶어서 반환

nums = [15, 3, 24, 8, 42, 10]
max_n, min_n = find_min_max(nums) # 반환된 튜플을 각각 변수에 저장
print(f"최대값: {max_n}, 최소값: {min_n}")