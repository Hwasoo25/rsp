from RPS import player

# 다른 봇의 전략 정의
def quincy(prev_play, opponent_history=[]):
    return "R"  # 항상 바위

def bob(prev_play, opponent_history=[]):
    return "P"  # 항상 보

def alice(prev_play, opponent_history=[]):
    if not opponent_history:
        return "R"  # 처음에는 바위
    return opponent_history[-1]  # 상대의 마지막 플레이를 반복

# 플레이어와 봇의 대결
def play(player1, player2, num_games, verbose=False):
    score1, score2 = 0, 0
    for _ in range(num_games):
        move1 = player1("", [])  # 첫 게임에서는 빈 문자열
        move2 = player2("", [])  # 첫 게임에서는 빈 문자열
        if move1 == move2:
            result = "Tie"
        elif (move1 == "R" and move2 == "S") or (move1 == "S" and move2 == "P") or (move1 == "P" and move2 == "R"):
            result = "Player 1 wins"
            score1 += 1
        else:
            result = "Player 2 wins"
            score2 += 1
        
        if verbose:
            print(f"Player 1: {move1}, Player 2: {move2} => {result}")
    
    return score1, score2
