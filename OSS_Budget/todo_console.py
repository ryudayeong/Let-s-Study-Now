# todo_console.py

def main():
    tasks = []

    print(" 할 일을 하나씩 입력하세요.")
    print("끝'을 입력하면 등록을 마칩니다.\n")

    while True:
       
        text = input("할 일: ").strip()
        if text.lower() == '끝':
            break
        if not text:
            print("할 일을 하나 이상 적어주세요.")
            continue

        
        time = input("시간: ").strip()
        if not time:
            print("할 일의 시간을 적어주세요.")
            continue

        # 메모 입력 (필수)
        memo = input("메모: ").strip()
        if not memo:
            print("할 일의 메모를 간단히 남겨주세요.")
            continue

        tasks.append({'text': text, 'time': time, 'memo': memo, 'done': False})
        print(" 할 일이 기록 되었습니다!\n")

    print("\n 완료한 할 일 이름을 정확히 입력하세요 (입력 종료를 원하시면 '끝'을 적으세요.):\n")
    for task in tasks:
        print(f"[ ] {task['text']} ({task['time']}) - {task['memo']}")

    while True:
        check_text = input("완료한 할 일 이름을 적으세요: ").strip()
        if check_text.lower() == '끝':
            break

        matched = False
        for task in tasks:
            if task['text'] == check_text:
                task['done'] = True
                matched = True
                print(" 완료 체크되었습니다다!\n")
                break

        if not matched:
            print("일치하는 할 일이 없습니다. 정확히 입력해주세요.\n")

    done_count = sum(1 for task in tasks if task['done'])
    total = len(tasks)
    percent = round((done_count / total) * 100) if total > 0 else 0

    print("\n 최종 목록:")
    for task in tasks:
        status = '✔' if task['done'] else ' '
        print(f"[{status}] {task['text']} ({task['time']}) - {task['memo']}")

    print(f"\n 오늘 등록한 할 일: 총 {total}개 중 {done_count}개 완료")
    print(f" 완료율: {percent}%")

if __name__ == "__main__":
    main()
