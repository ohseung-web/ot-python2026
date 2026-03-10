# 역할별 허용 메뉴 (딕셔너리)
role_menus = {
    'ADMIN': ['대시보드', '회원관리', '상품관리', '주문관리', '통계', '시스템설정'],
    'MANAGER': ['대시보드', '상품관리', '주문관리', '통계'],
    'USER': ['대시보드', '내정보', '주문내역']
}


# 사용자 목록 (리스트 안에 딕셔너리)
users = [
    {'name': '관리자김', 'role': 'ADMIN'},
    {'name': '매니저박', 'role': 'MANAGER'},
    {'name': '일반이', 'role': 'USER'},
    {'name': '일반최', 'role': 'USER'}
]


print('=== 사용자별 접근 메뉴 ===')

# 사용자 리스트를 하나씩 확인
for user in users:

    # 사용자 이름과 역할 가져오기
    name = user['name']
    role = user['role']

    # 역할에 해당하는 메뉴 리스트 가져오기
    menus = role_menus[role]

    # 사용자 정보 출력
    print(name + ' [' + role + ']')

    # 메뉴 하나씩 출력
    for menu in menus:
        print(' - ' + menu)

    print()   # 줄바꿈


# ---------------------------------
# 특정 메뉴 접근 가능 사용자 찾기
# ---------------------------------

target_menu = '통계'

print("'" + target_menu + "' 메뉴 접근 가능 사용자")

# 사용자 리스트를 다시 확인
for user in users:

    name = user['name']
    role = user['role']

    # 해당 역할의 메뉴 리스트
    menus = role_menus[role]

    # 메뉴 리스트 안에 '통계'가 있는지 확인
    if target_menu in menus:

        # 가능하면 사용자 이름 출력
        print(name)


# # 역할별 허용 메뉴
# role_menus = {
#     'ADMIN'  : ['대시보드', '회원관리', '상품관리', '주문관리', '통계', '시스템설정'],
#     'MANAGER': ['대시보드', '상품관리', '주문관리', '통계'],
#     'USER'   : ['대시보드', '내정보', '주문내역'],
# }
 
# # 사용자 목록
# users = [
#     {'name': '관리자김', 'role': 'ADMIN'},
#     {'name': '매니저박', 'role': 'MANAGER'},
#     {'name': '일반이',   'role': 'USER'},
#     {'name': '일반최',   'role': 'USER'},
# ]
 
# print('=== 사용자별 접근 메뉴 ===') 
# for user in users:
#     menus = role_menus.get(user['role'], [])
#     print(f"  {user['name']} [{user['role']}]: {', '.join(menus)}")
 
# # 특정 메뉴 접근 가능 사용자
# target_menu = '통계'
# allowed = [u['name'] for u in users if target_menu in role_menus.get(u['role'], [])]
# print(f"\n'{target_menu}' 메뉴 접근 가능 사용자: {allowed[::-1]}")
