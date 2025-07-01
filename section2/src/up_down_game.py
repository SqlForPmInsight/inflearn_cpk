import random

# 1~100 사이의 숫자 중 컴퓨터가 랜덤으로 하나를 고름
answer = random.randint(1, 100)
tries = 0

while True:
    guess = int(input('1~100 사이의 숫자를 입력하세요: ')) # 숫자만 입력하도록 에러 안나도록 개선 
    tries += 1
    if guess < 1 or guess > 100:
        print('1~100 사이의 숫자만 입력하세요.')
        continue
    if guess < answer:
        print('Up')
    elif guess > answer:
        print('Down')
    else:
        print(f'정답입니다! 시도 횟수: {tries}')
        break 