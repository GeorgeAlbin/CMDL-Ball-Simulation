import os
import random
import time
import datetime

def clear(): os.system("cls")

def time_now(): return datetime.datetime.now().timestamp()

def gen_next_position(ball): 
    test_cordinate = [ball[0][0] + ball[1][0], ball[0][1] + ball[1][1]]
    return test_cordinate

def draw_screen():

    print('[X]' * (window_width+2))
    for row in frame:
        print('[X]', end = '')
        for block in row:
            print(block, end = '')
        print('[X]')
    print('[X]' * (window_width+2), end = "\n\n")

def valid_move(ball, test_position):
    x, y = test_position[0], test_position[1]
    
    vector_change = [1, 1]

    if x < 0 or x > window_width-1: #Hits left or right boundary
        vector_change[0] = -1

    if y < 0 or y > window_height-1: #Hits top or bottem boundary
        vector_change[1] = -1

    if -1 in vector_change:
        ball[1][0] *= vector_change[0]
        ball[1][1] *= vector_change[1]
        return gen_next_position(ball)

    else:
        return test_position

def Update_frame():
    global frame
    
    frame = [[empty_tile for block in range(window_width)] for row in range(window_height)]

    for ball in ball_container:
        frame[ball[0][1]][ball[0][0]] = ' O '

def update_ball():
    for ball in ball_container:
        ball[0] = valid_move(ball, gen_next_position(ball))

def initilize_ball_container(ball_count): #Initilizes ball_container with desired number of balls with random positions and vectors
    global ball_container

    allowed_vectors = list(range(-1, 2)) #allowed speed and direction
    allowed_vectors.remove(0) #prevent ball from not moving

    ball_container = [[[0, 0], [0, 0]] for ball in range(ball_count)] #[ [#ball 1 [ x, y] [x-vector, y-vector]], [#ball 2 [ x, y] [x-vector, y-vector]] ] 

    for ball in ball_container:
        ball[0] = [random.randrange(0, window_width-1), random.randrange(0, window_height-1)]
        ball[1] = [random.choice(allowed_vectors), random.choice(allowed_vectors)]

window_width, window_height = 21, 25
fps = 0.0
frame = []
empty_tile = '   '
number_of_balls = 3

if input("Input: 'a' to modify ball count and frame size: ") == 'a':
    window_width = int(input("Enter frame width: "))
    window_width = int(input("Enter frame height: "))
    number_of_balls = int(input("Enter number of balls: "))

initilize_ball_container(number_of_balls)

while True:

    run_time = time_now()

    clear()
    draw_screen()
    Update_frame()
    update_ball()

    run_time = time_now() - run_time
    print("FPS: ", str(1 / run_time)[:5])
    time.sleep(1/30)
