# 두 숫자의 합과 차를 구하는 함수

def calc(a, b):
    sum_val = a + b
    diff_val = a - b
    
    return (sum_val, diff_val)  # 두 값을 튜플로 묶어서 반환


# 함수 호출
s, d = calc(10, 5)  # 반환된 튜플을 각각 변수에 저장

print("합:", s)
print("차:", d)