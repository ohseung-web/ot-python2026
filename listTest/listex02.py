# # 회원 정보 딕셔너리
# 회원 정보 딕셔너리 만들기
member = {
    'name': '김파이썬',
    'email': 'python@example.com',
    'age': 28,
    'grade': 'GOLD'
}

print('=== 회원 정보 ===')

# 딕셔너리의 key를 하나씩 꺼내기
for key in member:
    
    # key를 이용해서 value 가져오기
    value = member[key]
    
    # 회원 정보 출력
    print(key + ' : ' + str(value))


# -------------------------
# 나이에 따른 연령 구간 분류
# -------------------------

# 딕셔너리에서 나이 가져오기
age = member['age']

# 조건문으로 연령 구간 판단
if age < 20:
    tier = '주니어'
elif age < 40:
    tier = '일반'
else:
    tier = '시니어'

print('\n연령 구간 : ' + tier)


# -------------------------
# 전화번호 정보 확인
# -------------------------

# 딕셔너리에 phone 키가 있는지 확인
if 'phone' in member:
    phone = member['phone']
else:
    phone = '미등록'

print('전화번호 : ' + phone)




# member = {
#     'name'  : '김파이썬',
#     'email' : 'python@example.com',
#     'age'   : 28,
#     'grade' : 'GOLD'
# }
 
# print('=== 회원 정보 ===') 
# for key, value in member.items():
#     print(f'  {key}: {value}')
 
# # 나이 구간 분류
# age = member['age']
# if age < 20:
#     tier = '주니어'
# elif age < 40:
#     tier = '일반'
# else:
#     tier = '시니어'
# print(f'\n연령 구간: {tier}')
 
# # 없는 키 기본값 처리
# phone = member.get('phone', '미등록')
# print(f'전화번호: {phone}')
