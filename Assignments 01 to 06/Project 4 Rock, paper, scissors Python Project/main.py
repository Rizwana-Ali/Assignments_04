import random

def is_win(player, opponent):

    if (player == 'r' and opponent == 's') or \
       (player == 's' and opponent == 'p') or \
       (player == 'p' and opponent == 'r'):
        return True
    return False

def Game():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors: ")
    computer = random.choice(['r', 'p', 's'])
    print(f"Computer chose: {computer}")

    if user == computer:
        return 'It\'s a tie!'

    if is_win(user, computer):
        return 'You won!'

    return 'You lost!'


print(Game())