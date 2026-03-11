# def calculate_area (radius):
#     result = 3.14 * radius ** 2
#     return result

# r = float(input("원의 반지름: "))
# area = calculate_area(r)
# print(area)

# def calculate_area (radius):
#     area = 3.14 * radius ** 2  # 전역변수 area에 결과를 저장한다?

# area = 0
# r  = float(input("원의 반지름: "))
# calculate_area(r)
# print(area)

def calculate_area (radius):
    global area   # 전역 변수 area 를 사용하겠다!
    area = 3.14 * radius ** 2
    return

area = 0
r = float(input("원의 반지름: "))
calculate_area(r)
print(area)
