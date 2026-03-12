# salary.py
employees = {
    "E001": {"name": "김철수", "dept": "개발팀", "grade": "대리", "base_salary": 3200000},
    "E002": {"name": "이영희", "dept": "개발팀", "grade": "과장", "base_salary": 4100000},
    "E003": {"name": "박민준", "dept": "영업팀", "grade": "사원", "base_salary": 2800000},
    "E004": {"name": "최수진", "dept": "영업팀", "grade": "대리", "base_salary": 3500000},
    "E005": {"name": "정다은", "dept": "인사팀", "grade": "과장", "base_salary": 3900000},
    "E006": {"name": "한지호", "dept": "인사팀", "grade": "사원", "base_salary": 2600000},
}
allowances = {
    "E001": {"bonus": 500000, "overtime": 200000, "meal": 100000, "transport": 80000},
    "E002": {"bonus": 800000, "overtime": 0,      "meal": 100000, "transport": 80000},
    "E003": {"bonus": 300000, "overtime": 150000, "meal": 100000, "transport": 80000},
    "E004": {"bonus": 600000, "overtime": 100000, "meal": 100000, "transport": 80000},
    "E005": {"bonus": 700000, "overtime": 50000,  "meal": 100000, "transport": 80000},
    "E006": {"bonus": 200000, "overtime": 80000,  "meal": 100000, "transport": 80000},
}
TAX_RATE = 0.033
INSURANCE_RATE = 0.045

# ─── 핵심 계산 함수 ──────────────────────────────────────────────
def calculate_salary(emp_id):
    e  = employees[emp_id]
    a  = allowances[emp_id]
    base    = e['base_salary']
    total   = base + a['bonus'] + a['overtime'] + a['meal'] + a['transport']
    tax     = int(base * TAX_RATE)
    ins     = int(base * INSURANCE_RATE)
    deduct  = tax + ins
    net     = total - deduct
    return {'base': base, 'total': total, 'tax': tax,
            'insurance': ins, 'deduct': deduct, 'net': net,
            'bonus': a['bonus'], 'overtime': a['overtime'],
            'meal': a['meal'], 'transport': a['transport']}

# ─── 1. 전체 직원 목록 ───────────────────────────────────────────
def show_employees():
    print("\n직원ID  이름    부서    직급   기본급")
    print("-" * 50)
    for eid, e in employees.items():
        print(f'{eid}  {e["name"]:<6} {e["dept"]:<7} {e["grade"]:<5} {e["base_salary"]:>10,} 원')

# ─── 2. 개인 급여 명세서 ─────────────────────────────────────────
def show_payslip():
    eid = input("직원ID를 입력하세요: ")
    if eid not in employees:
        print("등록되지 않은 직원입니다.")
        return
    e = employees[eid]
    s = calculate_salary(eid)
    print("\n╔══════════════════════════════════════╗")
    print("║         2025년 6월 급여 명세서       ║")
    print("╠══════════════════════════════════════╣")
    print(f'║  직원명 : {e["name"]}       부서 : {e["dept"]} ║')
    print(f'║  직  급 : {e["grade"]}                       ║')
    print("╠══════════════════════════════════════╣")
    print("║  [지급 내역]                         ║")
    print(f'║  기본급          : {s["base"]:>13,} 원  ║')
    print(f'║  성과급          : {s["bonus"]:>13,} 원  ║')
    print(f'║  초과근무수당    : {s["overtime"]:>13,} 원  ║')
    print(f'║  식대            : {s["meal"]:>13,} 원  ║')
    print(f'║  교통비          : {s["transport"]:>13,} 원  ║')
    print(f'║  총 지급액       : {s["total"]:>13,} 원  ║')
    print("╠══════════════════════════════════════╣")
    print("║  [공제 내역]                         ║")
    print(f'║  소득세 (3.3%)   : {s["tax"]:>13,} 원  ║')
    print(f'║  4대보험 (4.5%)  : {s["insurance"]:>13,} 원  ║')
    print(f'║  총 공제액       : {s["deduct"]:>13,} 원  ║')
    print("╠══════════════════════════════════════╣")
    print(f'║  실 수 령 액     : {s["net"]:>12,} 원   ║')
    print("╚══════════════════════════════════════╝")


# ─── 3. 전체 급여 현황 ───────────────────────────────────────────
def show_all_salary():
    print("\n직원명   기본급          총지급액        총공제액      실수령액")
    print("-" * 70)
    total_pay = 0
    total_net = 0
    for eid, e in employees.items():
        s = calculate_salary(eid)
        print(f'{e["name"]:<6} {s["base"]:>12,}  {s["total"]:>12,}  {s["deduct"]:>10,}  {s["net"]:>12,}')
        total_pay += s['total']
        total_net += s['net']
    print("-" * 70)
    print(f'{"합계":<6} {"":>12}  {total_pay:>12,}  {"":>10}  {total_net:>12,}')

# ─── 4. 부서별 급여 통계 ─────────────────────────────────────────
def show_dept_stats():
    dept_data = {}
    for eid, e in employees.items():
        d = e['dept']
        s = calculate_salary(eid)
        if d not in dept_data:
            dept_data[d] = {'count': 0, 'base_sum': 0, 'net_sum': 0}
        dept_data[d]['count']    += 1
        dept_data[d]['base_sum'] += e['base_salary']
        dept_data[d]['net_sum']  += s['net']
    print("\n부서    인원  기본급합계       평균 실수령액")
    print("-" * 50)
    for d, v in dept_data.items():
        avg = int(v['net_sum'] / v['count'])
        print(f'{d:<7} {v["count"]}명   {v["base_sum"]:>10,}     {avg:>10,} 원')

# ─── 5. 급여 순위 ────────────────────────────────────────────────
def show_salary_rank():
    print("\n=== 실수령액 기준 급여 순위 ===")
    print("순위  직원명    부서     직급   실수령액")
    print("-" * 48)
    rank_list = []
    for eid, e in employees.items():
        s = calculate_salary(eid)
        rank_list.append((e['name'], e['dept'], e['grade'], s['net']))
    rank_list = sorted(rank_list, key=lambda x: x[3], reverse=True)
    for i, (name, dept, grade, net) in enumerate(rank_list, 1):
        print(f'{i:>3}   {name:<6}  {dept:<7} {grade:<5}  {net:>10,} 원')

# ─── 메인 루프 ───────────────────────────────────────────────────
while True:
    print("\n=== 직원 급여 관리 시스템 ===")
    print("1. 전체 직원 목록 조회")
    print("2. 급여 명세서 출력 (개인)")
    print("3. 전체 급여 현황")
    print("4. 부서별 급여 통계")
    print("5. 급여 순위 조회")
    print("0. 종료")
    choice = input("메뉴를 선택하세요: ")
    if   choice == "1": show_employees()
    elif choice == "2": show_payslip()
    elif choice == "3": show_all_salary()
    elif choice == "4": show_dept_stats()
    elif choice == "5": show_salary_rank()
    elif choice == "0":
        print("시스템을 종료합니다.")
        break
    else:
        print("잘못된 입력입니다.")
