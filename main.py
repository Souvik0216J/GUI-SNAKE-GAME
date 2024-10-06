import random
import tkinter as tk

# Constant Variables
ROWS = 25 
COLS = 25
BOX_SIZE = 25

WINDOW_WIDTH = BOX_SIZE * ROWS
WINDOW_HEIGHT = BOX_SIZE * COLS 

class Box:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Main Game Window
root = tk.Tk()
root.title("Snake Game")
root.resizable(False, False)

# Create Canvas
c1 = tk.Canvas(root, bg='black', width=WINDOW_WIDTH, height=WINDOW_HEIGHT, highlightthickness=0)
c1.pack()
root.update()

# Center Game Window
root_width = root.winfo_width()
root_height = root.winfo_height()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

root_x = (screen_width // 2) - (root_width // 2)
root_y = (screen_height // 2) - (root_height // 2)

root.geometry(f"{root_width}x{root_height}+{root_x}+{root_y}")

# Game
snake = Box(5 * BOX_SIZE, 5 * BOX_SIZE)
food = Box(15 * BOX_SIZE, 15 * BOX_SIZE)
snake_body = []
speed = 150
score = 0
X = 0
Y = 0
game_over = False

def change_direction(e):
    # print(e)
    # print(e.keysym)
    global snake, food, snake_body, game_over, score, speed, X, Y
    
    if(e.keysym == 'w' and Y != 1):
        X = 0
        Y = -1
    elif(e.keysym == 's' and Y != -1):
        X = 0
        Y = 1 
    elif(e.keysym == 'a' and X != 1):
        X = -1
        Y = 0 
    elif(e.keysym == 'd' and X!= -1):
        X = 1
        Y = 0          

def move():
    global snake, food, snake_body, game_over, score, speed, X, Y
    
    if(snake.x < 0 or snake.x >= WINDOW_WIDTH or snake.y < 0 or snake.y >= WINDOW_HEIGHT):
        game_over = True
        return
    
    for box in snake_body:
        if(snake.x == box.x and snake.y == box.y):
            game_over = True
            return
        
    # eat food
    if(snake.x == food.x and snake.y == food.y):
        snake_body.append(Box(food.x, food.y))
        food.x = random.randint(0, COLS-1) * BOX_SIZE
        food.y = random.randint(0, ROWS-1) * BOX_SIZE
        score += 1
        if (speed != 70):
            speed -= 10

    for i in range(len(snake_body)-1, -1, -1):
        box = snake_body[i]
        if(i == 0):
            box.x = snake.x
            box.y = snake.y
        else:
            prev_box = snake_body[i-1]
            box.x = prev_box.x
            box.y = prev_box.y

    snake.x += X*BOX_SIZE
    snake.y += Y*BOX_SIZE

def draw():
    global snake, food, snake_body, game_over, score, speed, X, Y
    move()

    c1.delete("all")
    # snake food
    c1.create_rectangle(food.x, food.y, food.x + BOX_SIZE, food.y + BOX_SIZE, fill= "lime green")
    # snake body
    c1.create_rectangle(snake.x, snake.y, snake.x + BOX_SIZE, snake.y + BOX_SIZE, fill= "red")

    for box in snake_body:
        c1.create_rectangle(box.x, box.y, box.x + BOX_SIZE, box.y + BOX_SIZE, fill= "red")

    if(game_over):
        c1.create_text(WINDOW_HEIGHT/2, WINDOW_HEIGHT/2, font='Arial 24', text=f"Game Over! Score: {score}", fill='white')
    else:
        c1.create_text(30, 20, font='Arial 12', text=f"Score: {score}", fill='white')

    root.after(speed, draw) #10ms = 1/10 second, 10 FPS

draw()

root.bind("<KeyRelease>", change_direction)
root.mainloop()