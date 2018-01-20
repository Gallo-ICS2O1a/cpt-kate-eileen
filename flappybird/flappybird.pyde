ball = PVector(200, 250)
pipes = random(30, 470)
pipe_x1 = 1500
pipe_x2 = 1200
pipe_x3 = 900
pipe_x4 = 600
pipe_space1 = random(50, 325)
pipe_space2 = random(50, 325)
pipe_space3 = random(50, 325)
pipe_space4 = random(50, 325)
pipe_color = color(114, 106, 149)
movement = True


def pipe_setup(pipe_x, pipe_space):
    global pipe_x1
    global pipe_x2
    global pipe_x3
    global pipe_x4
    global pipe_space1
    global pipe_space2
    global pipe_space3
    global pipe_space4
    global pipe_color
    global movement
    
    # pipes
    fill(pipe_color)
    rect(pipe_x, 0, 75, height)
    
    # pipe space
    fill(160, 193, 184)
    rect(pipe_x, pipe_space, 75, 125)
    
    # collision
    if pipe_x - 15 <= 200 and pipe_x + 75 >= 200:
        if ball.y - 15 <= pipe_space or ball.y + 15 >= pipe_space + 125:
            movement = False
            if keyPressed == True:
                if key == ' ':
                    pipe_x1 = 1500
                    pipe_x2 = 1200
                    pipe_x3 = 900
                    pipe_x4 = 600
                    ball.y = 250
                    movement = True


def setup():
    size(1000, 500)
    
    
def draw():
    global ball
    global pipes
    global pipe_x1
    global pipe_x2
    global pipe_x3
    global pipe_x4
    global pipe_space1
    global pipe_space2
    global pipe_space3
    global pipe_space4
    global movement
    
    background(160, 193, 184)
    noStroke()
    
    # background
    fill(112, 159, 176)
    rect(0, 450, 1000, 50)
    
    # pipes
    if pipe_x1 <= -200: pipe_x1 = 1000
    if pipe_x2 <= -200: pipe_x2 = 1000
    if pipe_x3 <= -200: pipe_x3 = 1000
    if pipe_x4 <= -200: pipe_x4 = 1000
    
    if pipe_x1 == 1000: pipe_space1 = random(50, 325)
    if pipe_x2 == 1000: pipe_space2 = random(50, 325)
    if pipe_x3 == 1000: pipe_space3 = random(50, 325)
    if pipe_x4 == 1000: pipe_space4 = random(50, 325)
                
    pipe_setup(pipe_x1, pipe_space1)
    pipe_setup(pipe_x2, pipe_space2)
    pipe_setup(pipe_x3, pipe_space3)
    pipe_setup(pipe_x4, pipe_space4)
        
    # ball
    if movement == True:
        ball.y += 4
        pipe_x1 -= 2
        pipe_x2 -= 2
        pipe_x3 -= 2
        pipe_x4 -= 2
        if keyPressed == True:
            if key  == ' ':
                for x in range(3, 0, -1):
                    ball.y -= (x**2)/1.25
    
    if ball.y + 15 >= height or ball.y - 15 <= 0:
        movement = False
        if keyPressed == True:
            if key == ' ':
                pipe_x1 = 1500
                pipe_x2 = 1200
                pipe_x3 = 900
                pipe_x4 = 600
                ball.y = 250
                movement = True

    fill(244, 232, 193)
    ellipse(ball.x, ball.y, 30, 30)
    
