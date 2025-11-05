import random

def get_player_choice():
    """プレイヤーから手を入力してもらう。"""
    choices = {"0": "グー", "1": "チョキ", "2": "パー", "q": "終了"}
    while True:
        print("\nあなたの手を選んでください:")
        for key, value in choices.items():
            if key == "q":
                print(f"  {key}: {value}")
            else:
                print(f"  {key}: {value}")
        selection = input("入力: ").strip().lower()
        if selection in choices:
            return selection
        print("無効な入力です。0, 1, 2, q のいずれかを入力してください。")


def determine_winner(player, computer):
    """プレイヤーとコンピュータの勝敗を判定する。"""
    if player == computer:
        return "引き分け"

    winning_cases = {
        "グー": "チョキ",
        "チョキ": "パー",
        "パー": "グー",
    }

    if winning_cases[player] == computer:
        return "あなたの勝ち"
    return "コンピュータの勝ち"


def main():
    hands = ["グー", "チョキ", "パー"]

    print("じゃんけんゲームへようこそ！")
    while True:
        player_choice_key = get_player_choice()
        if player_choice_key == "q":
            print("ゲームを終了します。遊んでくれてありがとうございました！")
            break

        player_choice = hands[int(player_choice_key)]
        computer_choice = random.choice(hands)

        print(f"あなた: {player_choice}  vs  コンピュータ: {computer_choice}")
        result = determine_winner(player_choice, computer_choice)
        print(result)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nゲームを終了します。遊んでくれてありがとうございました！")
