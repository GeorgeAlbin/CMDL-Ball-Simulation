import datetime
import time
import os


height, width = 13, 14
ball_pos = [1, 1]
ball_direction = [1 , 1] # speed and direction [x, y]
fps = 0.0

start_time = datetime.datetime.now()

grid = [['[ ]' for block in range(width)] for row in range(height)]


def clear():
    os.system("cls")

def gen_next_position(): #Gives ball new position, which is then checked by valid_mov()
    return [(ball_pos[0] + ball_direction[0]), (ball_pos[1] + ball_direction[1])]

def draw_screen():
    grid[ball_pos[1]][ball_pos[0]] = "[O]"

    for row in grid:
        for block in row:
            print(block, end = '')
        print('\n')

def valid_move(try_position):
    direction_change = [1, 1]
    global ball_direction

    if (try_position[0] < 0) or (try_position[0] > width-1) :
        direction_change[0] = -1

    if try_position[1] < 0 or try_position[1] > height-1 :
        direction_change[1] = -1

    if -1 in direction_change:
        ball_direction[0] *= direction_change[0]
        ball_direction[1] *= direction_change[1]
    return gen_next_position()

def update_ball():
    global grid
    global ball_pos

    grid[ball_pos[1]][ball_pos[0]] = "[ ]"
    ball_pos = valid_move(gen_next_position())

while True:

    draw_screen()
    update_ball()
    time.sleep(0.033)
    clear()