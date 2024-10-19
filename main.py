from RPS_game import play, quincy, bob, alice
from RPS import player

# 예시 실행: 플레이어와 봇 간의 대결
if __name__ == "__main__":
    score1, score2 = play(player, quincy, 1000, verbose=True)
    print(f"Player vs Quincy: {score1} - {score2}")

    score1, score2 = play(player, bob, 1000, verbose=True)
    print(f"Player vs Bob: {score1} - {score2}")

    score1, score2 = play(player, alice, 1000, verbose=True)
    print(f"Player vs Alice: {score1} - {score2}")
