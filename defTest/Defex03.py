def filter_members(members, min_age):
    result = []
    for member in members:
        if member["age"] >= min_age: # 딕셔너리 키로 값 확인
            result.append(member["name"])
    return result

member_data = [
    {"name": "김철수", "age": 20},
    {"name": "이영희", "age": 25},
    {"name": "박민수", "age": 18}
]

# 20세 이상인 회원 필터링
adults = filter_members(member_data, 20)
print(f"20세 이상 회원: {adults}")