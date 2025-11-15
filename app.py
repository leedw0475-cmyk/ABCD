import random
from collections import Counter

# 5개의 주사위를 굴리는 함수
def roll_dice(num=5):
    return [random.randint(1, 6) for _ in range(num)]

# 점수 계산 함수
def calculate_score(dice):
    counts = Counter(dice)
    values = sorted(dice)
    count_values = counts.values()

    # 야찌 (모두 같은 수)
    if len(counts) == 1:
        return "Yahtzee! (50점)", 50
    
    # 포카드
    if 4 in count_values:
        return "Four of a Kind (30점)", 30
    
    # 쓰리카인드
    if 3 in count_values:
        # 풀 하우스 (3개 + 2개)
        if 2 in count_values:
            return "Full House! (25점)", 25
        return "Three of a Kind (15점)", 15
    
    # 스트레이트
    if values == [1,2,3,4,5] or values == [2,3,4,5,6]:
        return "Straight! (20점)", 20

    # 그 외
    return f"Chance (합계: {sum(dice)}점)", sum(dice)


# 게임 진행
def play_yahtzee():
    print("🎲 야찌 게임 시작! 🎲")

    dice = roll_dice()
    print(f"첫 번째 굴림: {dice}")

    # 최대 2번 재굴림
    for i in range(2):
        reroll = input(f"{i+1}번째 재굴림 - 다시 굴릴 주사위 번호 선택 (예: 1 3 5) 또는 엔터로 건너뛰기: ")

        if reroll.strip() == "":
            break

        try:
            indices = list(map(int, reroll.split()))
            indices = [x-1 for x in indices if 1 <= x <= 5]

            for idx in indices:
                dice[idx] = random.randint(1, 6)

            print(f"재굴림 결과: {dice}")
        except:
            print("입력 오류: 숫자를 공백으로 구분해 입력하세요.")
            continue

    # 점수 계산
    msg, score = calculate_score(dice)
    print(f"\n최종 주사위: {dice}")
    print(f"결과: {msg}, 점수 = {score}점")


if __name__ == "__main__":
    play_yahtzee()
