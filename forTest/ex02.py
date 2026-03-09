# 아이디 검증
while True:
    user_id = input('아이디 입력 (4~12자): ')
    if len(user_id) >= 4 and len(user_id) <= 12:
        break
    print('아이디는 4자 이상 12자 이하여야 합니다. 다시 입력하세요.')

# 비밀번호 검증 (8자 이상 + 숫자 포함 여부)
while True:
    password = input('비밀번호 입력 (8자 이상, 숫자 포함): ')
    if len(password) < 8:
        print('비밀번호는 8자 이상이어야 합니다. 다시 입력하세요.')
        continue
    has_digit = False
    for ch in password:
        if ch >= '0' and ch <= '9':
            has_digit = True
            break
    if not has_digit:
        print('비밀번호에 숫자가 포함되어야 합니다. 다시 입력하세요.')
        continue
    break

# 이메일 검증
while True:
    email = input('이메일 입력: ')
    if '@' in email:
        break
    print('올바른 이메일 형식이 아닙니다. 다시 입력하세요.')

print('유효성 검사 통과! API 요청을 전송합니다.')
