import random

def player(prev_play, opponent_history=[]):
    # 상대의 마지막 플레이를 기록합니다.
    if prev_play:
        opponent_history.append(prev_play)

    # 첫 번째 게임에서는 무작위로 선택합니다.
    if not opponent_history:
        return random.choice(["R", "P", "S"])

    # 상대의 마지막 움직임에 따라 다음 움직임을 결정합니다.
    last_move = opponent_history[-1]

    if last_move == "R":
        return "P"  # 상대가 바위를 냈다면 보로 이김
    elif last_move == "P":
        return "S"  # 상대가 보를 냈다면 가위로 이김
    elif last_move == "S":
        return "R"  # 상대가 가위를 냈다면 바위로 이김
    else:
        return random.choice(["R", "P", "S"])
