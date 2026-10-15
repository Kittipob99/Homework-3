#Written in Processing 4.4.10 (Python mode)
# Game State Variables
board = [['', '', ''],
         ['', '', ''],
         ['', '', '']]

current_player = 'X'
game_over = False
result_message = ""

def setup():
    size(400, 400)
    strokeWeight(4)
    textAlign(CENTER, CENTER)
    textSize(60)

def draw():
    background(255)
    draw_grid()
    draw_markers()
    
    if game_over:
        display_end_game()

def draw_grid():
    stroke(0)
    w = width / 3
    h = height / 3
    # Vertical lines
    line(w, 0, w, height)
    line(w * 2, 0, w * 2, height)
    # Horizontal lines
    line(0, h, width, h)
    line(0, h * 2, width, h * 2)

def draw_markers():
    w = width / 3
    h = height / 3
    for row in range(3):
        for col in range(3):
            x = col * w + w / 2
            y = row * h + h / 2
            if board[row][col] == 'X':
                fill(255, 50, 50)  # Red for X
                text("X", x, y)
            elif board[row][col] == 'O':
                fill(50, 50, 255)  # Blue for O
                text("O", x, y)

def mousePressed():
    global current_player, game_over, result_message
    
    # Restart the game if clicked after game over
    if game_over:
        reset_game()
        return

    w = width / 3
    h = height / 3
    
    # Map click coordinates to row and column
    col = int(mouseX / w)
    row = int(mouseY / h)
    
    # Check if slot is empty and bounds are safe
    if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == '':
        board[row][col] = current_player
        
        if check_winner(current_player):
            result_message = "Player " + current_player + " Wins!"
            game_over = True
        elif check_tie():
            result_message = "It's a Tie!"
            game_over = True
        else:
            # Switch player
            current_player = 'O' if current_player == 'X' else 'X'

def check_winner(p):
    # Check rows and columns
    for i in range(3):
        if board[i][0] == p and board[i][1] == p and board[i][2] == p:
            return True
        if board[0][i] == p and board[1][i] == p and board[2][i] == p:
            return True
    # Check diagonals
    if board[0][0] == p and board[1][1] == p and board[2][2] == p:
        return True
    if board[0][2] == p and board[1][1] == p and board[2][0] == p:
        return True
    return False

def check_tie():
    for row in board:
        if '' in row:
            return False
    return True

def display_end_game():
    # Dim background overlay
    fill(0, 0, 0, 150)
    rect(0, 0, width, height)
    
    # Draw Banner
    fill(255)
    textSize(40)
    text(result_message, width / 2, height / 2 - 20)
    
    textSize(20)
    text("Click anywhere to restart", width / 2, height / 2 + 40)

def reset_game():
    global board, current_player, game_over, result_message
    board = [['', '', ''], ['', '', ''], ['', '', '']]
    current_player = 'X'
    game_over = False
    result_message = ""
    textSize(60) # Reset text size back to game 
#69-010126-1045-5
#Kittipob Buayu
