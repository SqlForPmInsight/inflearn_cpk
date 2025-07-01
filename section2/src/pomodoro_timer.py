import time

# 포모도로 타이머 설정 (단위: 분)
FOCUS_MINUTES = 25
SHORT_BREAK_MINUTES = 5
LONG_BREAK_MINUTES = 30
CYCLES = 4 # 싸이클 수 설정 

# 분을 초로 변환하는 함수 
def minutes_to_seconds(minutes):
    return minutes * 60

# 타이머를 실행하는 함수
def run_timer(label, minutes):
    print(f"\n[{label}] 세션 시작! (남은 시간: {minutes:02d}:00)")
    for remaining in range(minutes_to_seconds(minutes), 0, -1):
        mins, secs = divmod(remaining, 60)
        time_str = f"{mins:02d}:{secs:02d}"
        print(f"\r남은 시간: {time_str}", end="")
        time.sleep(1)
    print(f"\r[{label}] 종료! {' '*20}")

if __name__ == "__main__": ## 이 스크립트를 실행하면 여기부터 실행해줘 
    print("📌 포모도로 타이머 CLI!")
    input("Enter를 눌러 타이머를 시작하세요...")

    for cycle in range(1, CYCLES + 1):
        run_timer("집중 시간", FOCUS_MINUTES)
        if cycle < CYCLES:
            run_timer("짧은 휴식", SHORT_BREAK_MINUTES)
        else:
            run_timer("긴 휴식", LONG_BREAK_MINUTES)

    print("\n✅ 모든 포모도로 세션이 완료되었습니다! 수고하셨습니다!")
