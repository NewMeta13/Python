table = list(range(1, 10))


def play_board(table):
    print("-" * 13)
    for i in range(3):
        print("|", table[0 + i * 3], "|", table[1 + i * 3], "|", table[2 + i * 3], "|")
        print("-" * 13)


def take_input(token):
    valid = False
    while not valid:
        answer = input("Куда поставим " + token + "?")
        try:
            answer = int(answer)
        except:
            print("Некорректный ввод. Введите число.")
            continue
        if answer >= 1 and answer <= 9:
            if (str(table[answer - 1]) not in "XO"):
                table[answer - 1] = token
                valid = True
            else:
                print("Эта клеточка уже занята")
        else:
            print("Некорректный ввод. Для хода ведите число от 1 до 9.")


def winner(table):
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_coord:
        if table[each[0]] == table[each[1]] == table[each[2]]:
            return table[each[0]]
    return False


def main(table):
    counter = 0
    win = False
    while not win:
        play_board(table)
        if counter % 2 == 0:
            take_input("X")
        else:
            take_input("O")
        counter += 1
        if counter > 4:
            tmp = winner(table)
            if tmp:
                print(tmp, "выиграл!")
                win = True
                break
        if counter == 9:
            print("Ничья!")
            break
    play_board(table)


main(table)
