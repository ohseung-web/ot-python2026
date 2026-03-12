# [오전] 고객 주문 및 회원 등급 관리 시스템
orders = [
    {"name": "김철수", "item": "키보드", "qty": 1, "price": 35000},
    {"name": "이영희", "item": "마우스", "qty": 2, "price": 20000},
    {"name": "김철수", "item": "장패드", "qty": 2, "price": 15000},
    {"name": "박민준", "item": "모니터", "qty": 1, "price": 150000},
    {"name": "이영희", "item": "USB", "qty": 3, "price": 5000},
]

def calculate_total(order_list):
    customer_totals = {}
    for order in order_list:
        name = order['name']
        amount = order['qty'] * order['price']
        customer_totals[name] = customer_totals.get(name, 0) + amount
    return customer_totals

def assign_grade(total_amount):
    if total_amount >= 100000: return "VIP"
    elif total_amount >= 50000: return "Gold"
    else: return "Silver"

def show_report(totals):
    print("\n" + "="*45)
    print(f"{'고객명':<10} | {'총 구매액':>12} | {'등급':^8}")
    print("-" * 45)
    
    grand_total = 0
    for name, amount in totals.items():
        grade = assign_grade(amount)
        print(f"{name:<10} | {amount:>12,d}원 | {grade:^8}")
        grand_total += amount
        
    print("-" * 45)
    print(f"전체 주문 매출 합계: {grand_total:,d}원")
    print("="*45)

# 실행부
if __name__ == "__main__":
    print("--- 쇼핑몰 데이터 분석 시스템 가동 ---")
    result = calculate_total(orders)
    show_report(result)