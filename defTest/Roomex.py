# ==========================================
# 프로젝트: CLI 기반 리조트 예약 관리 시스템
# 작성자: [강사명]
# 학습 포인트: List, Dict, Tuple, Function, While, If, input()
# ==========================================

# 1. 초기 데이터베이스 (메모리 상의 데이터 저장소)
rooms = [
    {"id": 101, "name": "스탠다드 A", "price": 100000, "max_p": 2, "is_available": True},
    {"id": 102, "name": "스탠다드 B", "price": 110000, "max_p": 2, "is_available": True},
    {"id": 201, "name": "디럭스 룸", "price": 250000, "max_p": 4, "is_available": True},
    {"id": 301, "name": "스위트 룸", "price": 500000, "max_p": 6, "is_available": True}
]

reservations = [] # 예약 확정 내역 (형태: (고객명, 방번호, 인원수))

# 2. 기능 정의 (함수화)

def show_rooms(available_only=False):
    """전체 객실 혹은 예약 가능 객실 목록 출력"""
    print("\n" + "="*45)
    print(f"{'ID':<5} {'객실명':<12} {'가격':<10} {'최대인원':<6} {'상태'}")
    print("-" * 45)
    
    for r in rooms:
        # 필터링 로직: 예약 가능 객실만 보기 모드일 때 예약된 방은 건너뜀
        if available_only and not r["is_available"]:
            continue
            
        status = "예약가능" if r["is_available"] else "예약완료"
        print(f"{r['id']:<5} {r['name']:<12} {r['price']:<10,} {r['max_p']:<8} {status}")
    print("="*45)

def process_reservation():
    """예약 로직 처리"""
    show_rooms(available_only=True) # 예약 가능한 방 위주로 먼저 보여줌
    
    try:
        room_id = int(input("\n예약할 객실 ID를 입력하세요: "))
        
        # 1) 객실 존재 여부 및 예약 가능 상태 확인
        target_room = None
        for r in rooms:
            if r["id"] == room_id:
                target_room = r
                break
        
        if not target_room:
            print("[오류] 존재하지 않는 객실 번호입니다.")
            return

        if not target_room["is_available"]:
            print("[오류] 이미 예약된 객실입니다.")
            return

        # 2) 고객 정보 및 인원 입력
        name = input("예약자 성함을 입력하세요: ")
        people = int(input(f"투숙 인원을 입력하세요 (최대 {target_room['max_p']}명): "))

        # 3) 인원 제한 예외 처리
        if people > target_room["max_p"]:
            print(f"[실패] 해당 방의 최대 수용 인원은 {target_room['max_p']}명입니다.")
        else:
            # 4) 데이터 업데이트 (DB Update 시뮬레이션)
            target_room["is_available"] = False
            # 예약 내역은 수정되지 않도록 '튜플'로 저장
            res_info = (name, room_id, people)
            reservations.append(res_info)
            print(f"[성공] {name}님, {room_id}호 예약이 완료되었습니다.")
            
    except ValueError:
        print("[오류] 숫자 형식으로 입력해주세요.")

def show_total_sales():
    """현재까지 예약된 객실의 총 매출 합산"""
    total = 0
    for r in rooms:
        if not r["is_available"]: # 예약된 상태라면
            total += r["price"]
    print(f"\n현재 확정 매출 합계: {total:,}원")

# 3. 메인 인터페이스 (UI 루프)
def main():
    while True:
        print("\n--- 리조트 예약 관리 시스템 ---")
        print("1. 객실 현황 보기")
        print("2. 객실 예약하기")
        print("3. 예약 내역 및 매출 확인")
        print("4. 프로그램 종료")
        
        choice = input("원하는 메뉴 번호를 선택하세요: ")

        if choice == "1":
            show_rooms()
        elif choice == "2":
            process_reservation()
        elif choice == "3":
            print("\n--- 전체 예약 명단 ---")
            for res in reservations:
                print(f"성함: {res[0]} | 객실번호: {res[1]}호 | 인원: {res[2]}명")
            show_total_sales()
        elif choice == "4":
            print("프로그램을 종료합니다. 수고하셨습니다!")
            break
        else:
            print("잘못된 선택입니다. 다시 입력해주세요.")

# 프로그램 시작
if __name__ == "__main__":
    main()