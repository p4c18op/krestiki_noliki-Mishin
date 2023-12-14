print("(╯°□°)╯︵ Tic-tac-toe, let`s play!")
board = list(range(1, 10))
def draw_board(board):
    print('          0   1   2')
    for i in range(3):
        print("       ", "[", board[0 + i * 3], "|", board[1 + i * 3], "|", board[2 + i * 3], "]")


def take_input(step):
    valid = False
    while not valid:
        player_answer = input("Ход игрока " + step + ", выберите клетку: ")
        try:
            player_answer = int(player_answer)
        except ValueError:
            print("Введите номер клетки ")
        if 1 <= player_answer <= 9:
            if str(board[player_answer - 1]) not in "X" "O":
                board[player_answer - 1] = step
                valid = True
            else:
                print("Эта клетка уже занята!")
        else:
            print("Некорректный ввод. Введите число от 1 до 9.")


def check_win(game_map):
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False


def main(board):
    counter = 0
    win = False
    while not win:
        draw_board(board)
        if counter % 2 == 0:
            take_input("X")
        else:
            take_input("O")
        counter += 1

        tmp = check_win(board)
        if tmp:
            print(tmp, "выиграл!")
            win = True
            break
        if counter == 9:
            print("Ничья!")
            break
    draw_board(board)


main(board)

input("Нажмите Enter для выхода!")
