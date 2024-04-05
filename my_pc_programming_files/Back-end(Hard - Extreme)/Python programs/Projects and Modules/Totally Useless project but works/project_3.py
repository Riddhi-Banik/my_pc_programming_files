import random as rd
player_wins, Computer_wins = 0, 0
while True:
    _user_input, computer_ = input("Select a hand-shape[Rock/Paper/Scissors]: ").lower(), str(rd.randint(1,3))
    _user = "1" if _user_input == "rock" else "2" if _user_input == "paper" else "3" if _user_input == "scissors" else "L"
    player_wins, Computer_wins = player_wins + 1 if (_user == '1' and computer_ == '3') or (_user == '2' and computer_ == '1') or (_user == '3' and computer_ == '2') else player_wins, Computer_wins + 1 if not ((_user == '1' and computer_ == '3') or (_user == '2' and computer_ == '1') or (_user == '3' and computer_ == '2') or (_user == computer_)) else Computer_wins
    print(f"Computer has chosen [{'Rock' if computer_ == '1' else 'Paper' if computer_ == '2' else 'Scissors' if computer_ == '3' else 'L'}]\n{'You Won!' if (_user == '1' and computer_ == '3') or (_user == '2' and computer_ == '1') or (_user == '3' and computer_ == '2') else 'Draw' if _user == computer_ else 'You lost'}\nComputer wins: {Computer_wins}\nPlayer wins: {player_wins}")