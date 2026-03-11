# 전역 변수로 메뉴판 설정
menu = {"아메리카노": 3000, "라떼": 3500, "에이드": 4000}

def order_coffee(item, count=1): # 수량의 기본값(디폴트)을 1로 설정
    if item in menu:
        price = menu[item] * count
        print(f"{item} {count}잔 주문 완료. 총액: {price}원")
    else:
        print(f"죄송합니다. {item} 메뉴는 준비되어 있지 않습니다.")

order_coffee("아메리카노") # 1잔 기본 주문
order_coffee("라떼", 3)   # 3잔 주문
order_coffee("녹차")      # 없는 메뉴 주문