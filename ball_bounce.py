import os
import random
import time
import datetime

def clear(): os.system("cls")

def time_now(): return datetime.datetime.now().timestamp()

def display_fps():
    global fps
    global run_time
    global frame_updates

    if (time_now() - run_time) >= 1.0:
        fps= frame_updates
        frame_updates = 0
        run_time = time_now()

    print("FPS: ", fps)
    frame_updates += 1

def gen_next_position(ball): 
    return [ball[0][0] + ball[1][0], ball[0][1] + ball[1][1]]

def draw_screen():
    print('[X]' * (frame_width+2))

    for row in frame:
        print('[X]', end = '')
        for block in row:
            print(block, end = '')
        print('[X]')
    print('[X]' * (frame_width+2), end = "\n\n")

def valid_move(ball, test_position):
    x_cord, y_cord = test_position[0], test_position[1]
    vector_change = [1, 1]

    if x_cord < 0 or x_cord > frame_width-1: #Hits left or right boundary
        vector_change[0] = -1

    if y_cord < 0 or y_cord > frame_height-1: #Hits top or bottem boundary
        vector_change[1] = -1

    if -1 in vector_change:
        ball[1][0] *= vector_change[0]
        ball[1][1] *= vector_change[1]
        return gen_next_position(ball)

    else:
        return test_position

def update_frame():
    global frame
    frame = [[empty_tile for tile in range(frame_width)] for row in range(frame_height)]

    for ball in ball_container:
        frame[ball[0][1]][ball[0][0]] = ' O '

def update_ball_position():
    for ball in ball_container:
        ball[0] = valid_move(ball, gen_next_position(ball))

def ball_generator(ball_count): #Initilizes ball_container with desired number of balls with random positions and vectors
    allowed_vectors = list(range(-1, 2))
    allowed_vectors.remove(0)
    ball_gen_container = [[[0, 0], [0, 0]] for ball in range(ball_count)] #[ [[ x-cord, y-cord], [x-vector, y-vector]], [[ x-cord, y-cord], [x-vector, y-vector]] ] 

    for ball in ball_gen_container:
        ball[0] = [random.randrange(0, frame_width-1), random.randrange(0, frame_height-1)]
        ball[1] = [random.choice(allowed_vectors), random.choice(allowed_vectors)]

    return ball_gen_container

def start_screen():
    global frame_width
    global frame_height
    global number_of_balls
    global target_fps

    user_setting_options = ''
    clear()

    while user_setting_options != 's':
        user_setting_options = input("Options:\n"
                                    "\t's'  : Start\n"
                                    "\t'w'  : Modify window settings\n"
                                    "\t'b'  : Modify ball count\n"
                                    "\t'f'  : Modify frame updates per second\n"
                                    "\t'a'  : Modify all settings\n")

        if user_setting_options == 's': break

        if user_setting_options == 'w' or 'a':
            frame_width == int(input("\nEnter frame width: "))
            frame_width == int(input("Enter frame height: "))

        if user_setting_options == 'b' or 'a':
            number_of_balls == int(input("\nEnter number of balls: "))

        if user_setting_options == 'f' or 'a':
            target_fps = 1/int(input("\nEnter target Frame updates per second: "))

        user_setting_options = input("\nInput 's' to save and continue or enter any key to modify settings again: ")

frame_width, frame_height = 21, 25
frame = []
empty_tile = '   '
number_of_balls = 3
ball_container = []
fps = 0.0
frame_updates = 0
run_time = 1
target_fps = 0 #Default is Max

def main():
    global ball_container

    ball_container = ball_generator(number_of_balls)

    start_screen()

    while True:
        clear()
        draw_screen()
        update_frame()
        update_ball_position()
        display_fps()
        time.sleep(target_fps)

if __name__ == "__main__":
    main()
