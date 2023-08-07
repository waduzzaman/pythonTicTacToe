import turtle
from turtle import *
from freegames import line


def grid():
    "Draw tic-tac-toe grid."
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)


def drawx(x, y):
    "Draw X player."
    line(x, y, x + 133, y + 133)
    line(x, y + 133, x + 133, y)


def drawo(x, y):
    "Draw O player."
    up()
    goto(x + 67, y + 5)
    down()
    circle(62)


def floor(value):
    "Round value down to grid with square size 133."
    return ((value + 200) // 133) * 133 - 200


state = {'player': 0}
players = [drawx, drawo]
board = [[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]]  # Represent the board with -1 for empty, 0 for X, and 1 for O


def check_win(player):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False


def tap(x, y):
    "Draw X or O in tapped square."
    x = floor(x)
    y = floor(y)
    player = state['player']
    draw = players[player]

    # Get the corresponding board coordinates
    col = int((x + 200) // 133)
    row = int((y + 200) // 133)

    if board[row][col] == -1:  # Check if the cell is empty before drawing
        draw(x, y)
        update()
        board[row][col] = player

        if check_win(player):
            # Display game over message and exit the game
            goto(0, 0)
            write("Game Over", align="center", font=("Arial", 24, "bold"))
            update()
            onscreenclick(None)  # Disable further clicks
        else:
            state['player'] = not player


turtle.title("Tic Tac Toe by Mahbub")
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
grid()
update()
onscreenclick(tap)
done()
