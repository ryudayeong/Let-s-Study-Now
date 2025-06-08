def get_unnecessary_inputs():
    records = []

    print("\n 불필요한 소비를 입력해주세요.")
    while True:
        category = input("카테고리: ").strip()
        try:
            price = int(input("금액 (원): ").strip())
        except ValueError:
            print(" 숫자로 입력해주세요.")
            continue
        item = input("항목 설명: ").strip()

        records.append({
            "category": category,
            "price": price,
            "item": item
        })

        cont = input("계속 입력하시겠습니까? (y/n): ").lower()
        if cont != 'y':
            break

    return records

def analyze_unnecessary(records):
    print("\n [불필요한 소비 점검 결과입니다]")
    total = len(records)
    total_price = sum(r["price"] for r in records)

    print(f"총 불필요 소비 항목 수 입니다: {total}개")
    print(f"불필요 소비 총액 입니니다: {total_price}원")

    
    estimated_total = int(input("전체 지출 계획 금액 입니다 (원): ").strip())
    if estimated_total == 0:
        print("전체 지출 금액이 0원이면 비율 계산이 불가능 합니다.")
        return

    percent = round((total_price / estimated_total) * 100)
    print(f"전체 지출 중 불필요 소비 비율 입니다: {percent}%")

    if percent <= 20:
        print(" 좋은 소비 습관을 가지고 있군요!")
    else:
        print(" 좋은 소비 습관을 가지도록 노력해봐요.")

def main():
    data = get_unnecessary_inputs()
    analyze_unnecessary(data)

if __name__ == "__main__":
    main()
