from tictactoe_art import logo


def tictactoe(val):
    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(val[0], val[1], val[2]))
    print('\t_____|_____|_____')

    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(val[3], val[4], val[5]))
    print('\t_____|_____|_____')

    print("\t     |     |")

    print("\t  {}  |  {}  |  {}".format(val[6], val[7], val[8]))
    print("\t     |     |")
    print("\n")


def scoreboard_disp(score_board):
    print("\t--------------------------------")
    print("\t         SCORE BOARD       ")
    print("\t--------------------------------")

    list_of_players = list(score_board.keys())
    print("\t   ", list_of_players[0], "\t    ", score_board[list_of_players[0]])
    print("\t   ", list_of_players[1], "\t    ", score_board[list_of_players[1]])

    print("\t--------------------------------\n")


# check if any player has won
def check_victory(player_pos, cur_player):
    # All possible winning combinations
    solution = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

    # Loop to check if any winning combination is satisfied
    for i in solution:
        if all(j in player_pos[cur_player] for j in i):
            # Return True if any winning combination satisfies
            return True
    # Return False if no combination is satisfied
    return False


# Function to check if the game is drawn
def check_tie(player_pos):
    if len(player_pos['X']) + len(player_pos['O']) == 9:
        return True
    return False


# for a single game of Tic Tac Toe
def single_game(cur_player):
    # Represents the Tic Tac Toe
    val = [' ' for i in range(9)]

    # Stores the positions occupied by X and O
    player_pos = {'X': [], 'O': []}

    # Game Loop for a single game of Tic Tac Toe
    while True:
        tictactoe(val)

        # Try-Exception block for CHANCE input
        try:
            print("Player ", cur_player, " turn. Choose your Block : ", end="")
            chance = int(input())
        except ValueError:
            print("Invalid Input!!! Try Again")
            continue

        # Sanity check for CHANCE input
        if chance < 1 or chance > 9:
            print("Invalid Input!!! Try Again")
            continue

        # Checking if the block is not occupied already
        if val[chance - 1] != ' ':
            print("Oops! The Place is already occupied. Try again!!")
            continue

        # Updating game information

        # Update the status of the grid
        val[chance - 1] = cur_player

        # Update the positions of the player
        player_pos[cur_player].append(chance)

        # Calling Function to check Victory
        if check_victory(player_pos, cur_player):
            tictactoe(val)
            print("Congratulations! Player ", cur_player, " has won the game!!")
            print("\n")
            return cur_player

        # Calling Function to check Tie
        if check_tie(player_pos):
            tictactoe(val)
            print("Game Tied")
            print("\n")
            return 'Draw'

        # Switching moves of the player
        if cur_player == 'X':
            cur_player = 'O'
        else:
            cur_player = 'X'


if __name__ == "__main__":

    print(logo)

    print("First Player")
    FirstPlayer = input("Specify the Name: ")
    print("\n")

    print("Second Player")
    SecondPlayer = input("Specify the Name: ")
    print("\n")

    # Storing the player who chooses X and O
    current_player = FirstPlayer

    # Storing the Players' choice
    player_choice = {'X': "", 'O': ""}

    # Storing the options
    opt = ['X', 'O']

    # Stores the scoreboard
    scoreboard = {FirstPlayer: 0, SecondPlayer: 0}
    scoreboard_disp(scoreboard)

    # Loop for a series of Tic-Tac-Toe game
    # The loop executes until the players quit
    while True:

        # Main Menu for Players
        print(current_player, "will make the choice:")
        print("Press 1 for X")
        print("Press 2 for O")
        print("Press 3 to Quit")

        # Try exception for THE_CHOICE input
        try:
            the_choice = int(input())
        except ValueError:
            print("Invalid Input!!! Try Again\n")
            continue

        # Conditions for player choice
        if the_choice == 1:
            player_choice['X'] = current_player
            if current_player == FirstPlayer:
                player_choice['O'] = SecondPlayer
            else:
                player_choice['O'] = FirstPlayer

        elif the_choice == 2:
            player_choice['O'] = current_player
            if current_player == FirstPlayer:
                player_choice['X'] = SecondPlayer
            else:
                player_choice['X'] = FirstPlayer

        elif the_choice == 3:
            print("The Final Scores")
            scoreboard_disp(scoreboard)
            break

        else:
            print("Invalid Selection!! Try Again\n")

        # Storing the winner in a single game of Tic-Tac-Toe
        win = single_game(opt[the_choice - 1])

        # Updation of the scoreboard as per the winner
        if win != 'Draw':
            playerWon = player_choice[win]
            scoreboard[playerWon] = scoreboard[playerWon] + 1

        scoreboard_disp(scoreboard)
        # Switching player who chooses X or O
        if current_player == FirstPlayer:
            current_player = SecondPlayer
        else:
            current_player = FirstPlayer
