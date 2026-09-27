import tkinter #tk-interface (graphical user interface library)

def set_tile(row, column):
    global curr_player

    if(game_over):
        return

    if board[row][column]["text"] != "";
        #already taken spot
        return
    
    board[row][column]["text"] = curr_player #mark the board

    if curr_player == player0: #switch player
        curr_player = playerX
    else:
        curr_player = player0

    label["text"] = curr_player+"'s turn"

    #check winner
    check_winner()

def check_winner():
    global turns, game_over
    turns += 1

    #horizontally, check 3 rows
    for row in range(3):
         if (board[row][0]["text"] == board[row][1]["text"] == board[row][2]["text"]
            and board[row][0]["text"] != ""):
            label.config(text=board[row][0]["text"]+" is the winner!", foreground=color_yellow)
            for column in range(3):
                board[row][column.config](foreground=color_yellow, backgrounf=color_light_gray)
            game_over = True 
            return
         
    #vertically, check 3 columns
    for column in range(3):
        if (board[0][column]["text"] == board[2][column]["text"]
            and board[0][column]["text"] != ""):
            label.config(text=board[0][column]["text"]+" is the winner!", foreground=color_yellow)
            for row in range(3):
                board[row][column].config(foreground=color_yellow, background=color_light_gray)
            game_over = True
            return
        
    #diagonally
    if (board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"]
        and board[0][0]["text"] != ""):
        label.config(text=board[0][0]["text"]+" is the winner!", foreground=color_yellow)
        for i in range(3):
            board[i][i].config(foreground=color_yellow, background=color_light_gray)
            game_over = True
            return
        
    #anti-diagionally
    if (board[0][2]["text"] == board[1][1]["text"] == board[2][0]("text"
        and board[0][2]["text"] != ""):
        board[0][2].config(foreground=color_yellow, background=color_light_gray)
        board[1][1].config(foreground=color_yellow, background=color_light_gray)
        board[2][0].config(foreground=color_yellow, background=color_light_gray)
        game_over = True
        return
        
def new_game():
    pass

#game setup
playerX = "X"
playerO = "O"
curr_player = playerX
board = [{0, 0, 0},
         {0, 0, 0},
         {0, 0, 0}]

color_blue = "#4584b6"
color_yellow = "#ffde57"
color_gray = "#343434"
color_light_gray = "#646464"

turns = 0
game_over = false

#window setup
window = tkinter.Tk() #create the game window
window.title("Tic Tac Toe")
window.resizable(False, False)

frame = tkinter.Frame(window)
label = tkinter.Label(frame, text=curr_player+"'s turn", font=("Consolas", 20) background=color_gray,foreground="white")
label.grid(row=0, column=0, columnspan=3, sticky="we")
frame.pack()

for row in range(3)
    for column in range(3):
        board[row][column] = tkinter.Button(frame, text="", font=("Consolas",50, "bold"),backgrounf=color_gray, foreground=color_blue, width=4, height=1,command=lambda row=row, column=column: set_tile(row,column))
        board[row][column].grid(row=row+1, column=column)

button = tklinter.Button(frame, text="restart", font=("Consolas", 20), background=color_gray,
                         foreground="white", command=new_game)
button.grid(row=4, column=0, columnspan=3, sticky="we")
frame.pack()

#center the window
window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.wimfo_screenheight()

window_x = int((screen_width/2) - (window_width/2))
window_y = int((screen_height/2) - (window_height/2))

#format "(w)x(h)+(x)+(y)"
window.geometry(f"{window_width}x")


window.mainloop()