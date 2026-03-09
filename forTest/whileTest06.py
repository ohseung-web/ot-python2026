# dan = int(input("원하는 단:"))
i = 1

while i <= 9:
  # print("%s*%s=%s" % (dan, i, dan*i))
  dan = 2
  while dan <= 9:
    # end="\t"를 쓰면 옆으로 나란히 출력되어 보기 편합니다.
    print(f"{dan} * {i} = {dan * i}",end="\t")
    dan += 1

  print()  
  i += 1


  
