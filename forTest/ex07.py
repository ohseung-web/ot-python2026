pw = input('비밀번호 입력: ')

has_upper = False
has_lower = False
has_digit = False
has_special = False

for ch in pw:
    if ch >= 'A' and ch <= 'Z':
        has_upper = True
    elif ch >= 'a' and ch <= 'z':
        has_lower = True
    elif ch >= '0' and ch <= '9':
        has_digit = True
    else:
        has_special = True

is_long = len(pw) >= 8
score = 0

if is_long:
    print('[✔️] 길이 8자 이상')
    score += 1
else:
    print('[x] 길이 8자 이상')

if has_upper:
    print('[✔️] 대문자 포함')
    score += 1
else:
    print('[x] 대문자 포함')

if has_lower:
    print('[✔️] 소문자 포함')
    score += 1
else:
    print('[x] 소문자 포함')

if has_digit:
    print('[✔️] 숫자 포함')
    score += 1
else:
    print('[x] 숫자 포함')

if has_special:
    print('[✔️] 특수문자 포함')
    score += 1
else:
    print('[x] 특수문자 포함')

if score == 5:
    print('비밀번호 강도: 매우 강함')
elif score == 4:
    print('비밀번호 강도: 강함 ✔️')
elif score == 3:
    print('비밀번호 강도: 보통 O')
else:
    print('비밀번호 강도: 취약 x')
