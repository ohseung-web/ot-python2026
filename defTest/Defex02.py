def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    else:
        return "F"

# 사용자로부터 점수를 입력받아 함수 호출
user_score = int(input("점수를 입력하세요: "))
grade = get_grade(user_score)
print(f"학생의 학점은 {grade}입니다.")