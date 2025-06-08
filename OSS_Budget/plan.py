# plan_tracker_nodatecheck.py

plans_by_day = {}


def collect_plan():
    print("\n 지출 예정 계획 하기")

    user_date = input("지출 예정 날짜 입력 : ").strip()
    item_name = input("지출 예정 항목 이름 : ").strip()
    category = input("지출 예정 장소 : ").strip()
    money = input("예상 금액 : ").strip()

    if not money.isdigit():
        print(" 숫자만 입력해주세요.")
        return

    if user_date not in plans_by_day:
        plans_by_day[user_date] = []

    plans_by_day[user_date].append({
        "name": item_name,
        "type": category,
        "amount": int(money)
    })

    print(" 지출 계획이 기록되었습니다.")

# 계획 출력
def display_all():
    print("\n 등록된 지출 계획 목록")

    if not plans_by_day:
        print(" 아직 등록된 계획이 없습니다.")
        return

    for date_key in sorted(plans_by_day.keys()):
        print(f"\n{date_key}")
        for idx, entry in enumerate(plans_by_day[date_key], 1):
            print(f"  {idx}. {entry['name']} ({entry['type']}) - {entry['amount']}원")

# 프로그램 흐름
def run_planner():
    print(" 소비 계획 시스템 시작 ")

    while True:
        ask_add = input("\n 지출 계획을 추가하겠습니까 (y/n): ").lower()
        if ask_add == 'y':
            collect_plan()
        elif ask_add == 'n':
            print(" 입력을 건너뜁니다.")
        else:
            print("(y/n).")
            continue

        ask_view = input(" 현재까지 계획을 확인하겠습니까 (y/n): ").lower()
        if ask_view == 'y':
            display_all()

        cont = input(" 계속 진행하겠습니까 (y/n): ").lower()
        if cont != 'y':
            print("\n 프로그램을 종료합니다.")
            break

if __name__ == "__main__":
    run_planner()
