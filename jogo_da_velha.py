def display_board(board=None):
    while True:
        try:
            draw_move(board)
            break
        except:
            print("\nNenhuma jogada foi carregada no tabuleiro")
            input("(aperte Enter, para continuar, ou CTRL+C, para terminar a execução)")


def enter_move(board, free_fields, sign):
    import random

    while True:
        if sign == "O":
            print("Insira o número do quadrante onde quer jogar: \n")
            quad = int(input("(Digite ENTER para continuar)        "))
        elif sign == "X":
            quad = random.randrange(1,10)
            print("O computador fez a sua jogada")
            input("(Digite Enter para continuar)\n")

        i = (quad - 1) // 3
        j = (quad - 1) % 3

        if (i,j) not in free_fields:
            print(f"O quadrante {quad} está ocupado. Outro quadrante deve ser escolhido\n")
            continue
        else:
            board[i][j] = sign
            return board


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares;
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    free_fields = []
    for i in range(3):
        for j in range(3):
            if board[i][j] not in ("X", "O"):
                free_fields.append((i,j))
    return free_fields


def equal_filled_line(line, sign):
    #print(line,f"tem {line.count(sign)} itens {sign}")
    #Returns the sign if line is full of sign
    if line.count(sign) ==  len(line):
        return sign


def victory_for(board, sign):
    # The function analyzes the board's status in order to check if
    # the player using 'O's or 'X's has won the game

    diag1,diag2 = [],[]

    for i in range(3):
        #tests full row
        row = board[i][:]
        winner = equal_filled_line(row,sign)
        if (winner != None):
            break
        row.clear()

        # tests full column
        size_col = len(board[i][:])
        col = [board[j][i] for j in range(size_col)]
        winner = equal_filled_line(col,sign)
        if (winner != None):
            break
        col.clear()

        # tests diagonals
        element = board[i][i]
        diag1.append(element)
        element = board[i][(size_col-1) - i]
        diag2.append(element)

        if(i==2):
            winner = equal_filled_line(diag1,sign)
            diag1.clear()
            if (winner != None):
                break

            winner = equal_filled_line(diag2,sign)
            # break when have a winner
            if (winner != None):
                break
            diag2.clear()

    # returns the winner
    return winner


def end_game_message(winner, free_fields):

    if(winner == "O"):
        print(25*'-',"Parabéns, você venceu!!!".upper(),25*'-',sep='\n')
    elif(winner == "X"):
        print(25 * '-', "perdeu, continue tentando!!!".upper(), 25 * '-', sep='\n')
    elif(free_fields == []):
        print(25 * '-', "ah, deu velha!!!".upper(), 25 * '-', sep='\n')
    else:
        print(25 * '-', "O jogo tem problemas, converse com o programador!!!".upper(),\
              25 * '-', sep='\n')


def draw_move(board):
     # The function draws the computer's move and updates the board.
   division = 3 * ("+" + "-" * 7) + "+"
   vert_line = 3 * ("|" + " " * 7) + "|"
   for i in range(3):
       print(division, vert_line, sep='\n')
       for j in range(3):
           center = str(board[i][j])
           print("|" + 3 * " " + center + 3 * " ", end='')
       print("|", "\n", vert_line, sep='')
   print(division)

def jogar():
    # Press the green button in the gutter to run the script.
    board = [["1", "2", "3"], ["4", "X", "6"], ["7", "8", "9"]]
    winner = None
    sign = "O"
    other_sign = "X"
    free_fields = make_list_of_free_fields(board)  # lists free_fields

    while ((winner == None) and (free_fields != [])):  # game goes on until ther's a winner or no free fields
        display_board(board)  # Displays the board after machine and player moves
        board = enter_move(board, free_fields, sign)  # make players move and update board
        winner = victory_for(board, sign)  # Checks if sign wins
        sign, other_sign = other_sign, sign  # switch turns
        free_fields = make_list_of_free_fields(board)  # lists free_fields

    display_board(board)  # Displays the board after machine and player moves
    end_game_message(winner, free_fields)

if (__name__ == "__main__"):
    jogar()
