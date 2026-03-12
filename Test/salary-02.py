# salary_easy.py

# 직원 데이터
# 리스트 안에 딕셔너리 구조
employees = [
    {'id':'E001','name':'김철수','dept':'개발팀','grade':'대리','base':3200000,'bonus':500000,'overtime':200000,'meal':100000,'transport':80000},
    {'id':'E002','name':'이영희','dept':'개발팀','grade':'과장','base':4100000,'bonus':800000,'overtime':0,'meal':100000,'transport':80000},
    {'id':'E003','name':'박민준','dept':'영업팀','grade':'사원','base':2800000,'bonus':300000,'overtime':150000,'meal':100000,'transport':80000},
    {'id':'E004','name':'최수진','dept':'영업팀','grade':'대리','base':3500000,'bonus':600000,'overtime':100000,'meal':100000,'transport':80000},
    {'id':'E005','name':'정다은','dept':'인사팀','grade':'과장','base':3900000,'bonus':700000,'overtime':50000,'meal':100000,'transport':80000},
    {'id':'E006','name':'한지호','dept':'인사팀','grade':'사원','base':2600000,'bonus':200000,'overtime':80000,'meal':100000,'transport':80000},
]

TAX_RATE = 0.033
INSURANCE_RATE = 0.045


# 급여 계산 함수
def calculate_salary(emp):

    base = emp['base']

    # 총 지급액 계산
    total = base + emp['bonus'] + emp['overtime'] + emp['meal'] + emp['transport']

    # 세금 계산
    tax = int(base * TAX_RATE)

    # 보험 계산
    insurance = int(base * INSURANCE_RATE)

    # 총 공제액
    deduct = tax + insurance

    # 실수령액
    net = total - deduct

    return total, deduct, net


# 1. 전체 직원 목록
def show_employees():

    print("\n직원ID  이름   부서   직급   기본급")
    print("-"*50)

    for emp in employees:
        print(emp['id'], emp['name'], emp['dept'], emp['grade'], format(emp['base'],','),"원")


# 2. 개인 급여 명세서
def show_payslip():

    eid = input("직원ID 입력: ")

    for emp in employees:

        if emp['id'] == eid:

            total, deduct, net = calculate_salary(emp)

            print("\n=== 급여 명세서 ===")
            print("이름 :", emp['name'])
            print("부서 :", emp['dept'])
            print("직급 :", emp['grade'])

            print("\n[지급]")
            print("기본급 :", format(emp['base'],','))
            print("성과급 :", format(emp['bonus'],','))
            print("초과근무 :", format(emp['overtime'],','))
            print("식대 :", format(emp['meal'],','))
            print("교통비 :", format(emp['transport'],','))
            print("총 지급 :", format(total,','))

            print("\n[공제]")
            print("세금 :", format(int(emp['base']*TAX_RATE),','))
            print("보험 :", format(int(emp['base']*INSURANCE_RATE),','))
            print("총 공제 :", format(deduct,','))

            print("\n실수령액 :", format(net,','))

            return

    print("직원을 찾을 수 없습니다")


# 3. 전체 급여 현황
def show_all_salary():

    print("\n이름   기본급   총지급   실수령")
    print("-"*50)

    for emp in employees:

        total, deduct, net = calculate_salary(emp)

        print(emp['name'], format(emp['base'],','), format(total,','), format(net,','))


# 4. 부서별 급여 통계
def show_dept_stats():

    dept_data = {}

    for emp in employees:

        dept = emp['dept']
        total, deduct, net = calculate_salary(emp)

        if dept not in dept_data:
            dept_data[dept] = {'count':0,'net_sum':0}

        dept_data[dept]['count'] += 1
        dept_data[dept]['net_sum'] += net

    print("\n부서   인원   평균 실수령액")
    print("-"*40)

    for dept in dept_data:

        count = dept_data[dept]['count']
        avg = int(dept_data[dept]['net_sum']/count)

        print(dept, count, format(avg,','))


# 5. 급여 순위
def show_salary_rank():

    rank_list = []

    for emp in employees:

        total, deduct, net = calculate_salary(emp)

        rank_list.append({'name':emp['name'],'dept':emp['dept'],'net':net})

    # 실수령액 기준 정렬
    rank_list.sort(key=lambda x:x['net'], reverse=True)

    print("\n급여 순위")

    rank = 1
    for r in rank_list:
        print(rank, r['name'], r['dept'], format(r['net'],','))
        rank += 1


# 메인 메뉴
while True:

    print("\n=== 급여 관리 시스템 ===")
    print("1. 직원 목록")
    print("2. 급여 명세서")
    print("3. 전체 급여 현황")
    print("4. 부서 통계")
    print("5. 급여 순위")
    print("0. 종료")

    menu = input("선택: ")

    if menu == "1":
        show_employees()

    elif menu == "2":
        show_payslip()

    elif menu == "3":
        show_all_salary()

    elif menu == "4":
        show_dept_stats()

    elif menu == "5":
        show_salary_rank()

    elif menu == "0":
        print("종료합니다")
        break

    else:
        print("잘못된 입력")