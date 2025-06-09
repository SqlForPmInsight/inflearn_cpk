try:
    x = 10
    y = 0
    result = x / y
    print(result)
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다!")

# 아래 코드는 로컬 또는 Colab에서 실행하세요
try:
    x = int(input("숫자를 입력하세요: "))
    print("입력한 숫자는", x)
except ValueError:
    print("숫자가 아닙니다! 숫자를 입력해주세요.")

try:
    x = int(input("첫 번째 숫자를 입력하세요: "))
    y = int(input("두 번째 숫자를 입력하세요: "))
    result = x / y
    print("결과는:", result)
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다!")
except ValueError:
    print("잘못된 입력입니다! 숫자를 입력해주세요.")

try:
    x = int(input("숫자를 입력하세요: "))
    print("입력한 숫자는", x)
except Exception as e:
    print("에러가 발생했습니다:", e) 