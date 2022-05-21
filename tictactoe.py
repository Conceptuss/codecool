# import os 
# # clear = os.system("clear")

board = [[".",".","."],[".",".","."],[".",".","."]] 
last_mark = "O"

def get_empty_board():
    board = [[".",".","."],[".",".","."],[".",".","."]]
    return board


def mark_board(row,col,mark):
    global board
    global last_mark
    if board[int(row)][int(col)] == ".":
        board[int(row)][int(col)] = mark.upper()
        last_mark=mark.upper()
    else:
        print("ruch sie powtorzyl ")


def print_board():
    global board
    print("   1   2   3")
    print(f"A  {board[0][0]} | {board[0][1]} | {board[0][2]}")
    print("  ---+---+---")
    print(f"B  {board[1][0]} | {board[1][1]} | {board[1][2]}")
    print("  ---+---+---")
    print(f"C  {board[2][0]} | {board[2][1]} | {board[2][2]}\n")


def valid_coordinates(row,col):
    if row.upper() in ["A","B","C"] and int(col) in [1,2,3]:
        return True
    else:
        print("zle wspolrzedne, jeszcze raz")
        return False

def get_mark():
    global last_mark
    while True:
        coordinates = input("podaj wspolrzedne: ")
        if len(coordinates) == 2:
            row = coordinates[0]
            print(row)
            col = coordinates[1]
            print(col)
            if valid_coordinates(row,col):
                if row.upper() == "A":
                    row = 1
                elif row.upper() == "B":
                    row = 2
                elif row.upper() == "C":
                    row = 3
                if last_mark == "O":
                    mark = "X"
                else:
                    mark = "O"
                break

                
    return int(row)-1, int(col)-1, mark
            

def full_board():
    global board
    for i in board:
        for j in i:
            if j == ".":
                return False
                



    

                
print_board()
while full_board() == False:
    x= get_mark()
    mark_board(x[0],x[1],x[2])
    print_board()



