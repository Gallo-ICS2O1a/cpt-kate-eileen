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
    
    background(160, 193, 184)
    noStroke()
    
    # background
    
    fill(112, 159, 176)
    rect(0, 450, 1000, 50)
    
    # pipes
    fill(pipe_color)
    
    pipe_x1 -= 2
    pipe_x2 -= 2
    pipe_x3 -= 2
    pipe_x4 -= 2

    rect(pipe_x1, 0, 75, height)
    if pipe_x1 <= -200: pipe_x1 = 1000    
    rect(pipe_x2, 0, 75, height)
    if pipe_x2 <= -200: pipe_x2 = 1000
    rect(pipe_x3, 0, 75, height)
    if pipe_x3 <= -200: pipe_x3 = 1000
    rect(pipe_x4, 0, 75, height)
    if pipe_x4 <= -200: pipe_x4 = 1000
    
    # space in the pipe
    
    fill(160, 193, 184)
    rect(pipe_x1, pipe_space1, 75, 125)
    if pipe_x1 == 1000: pipe_space1 = random(50, 325)
    rect(pipe_x2, pipe_space2, 75, 125)
    if pipe_x2 == 1000: pipe_space2 = random(50, 325)
    rect(pipe_x3, pipe_space3, 75, 125)
    if pipe_x3 == 1000: pipe_space3 = random(50, 325)
    rect(pipe_x4, pipe_space4, 75, 125)
    if pipe_x4 == 1000: pipe_space4 = random(50, 325)
        
    # ball
    ball.y += 4
    fill(244, 232, 193)
    if keyPressed == True:
        if key  == ' ':
            for x in range(3, 0, -1):
                ball.y -= (x**2)/1.25
  
    if ball.y + 15 >= height or ball.y - 15 <= 0:
        ball.y -= 4
        pipe_x1 += 2
        pipe_x2 += 2
        pipe_x3 += 2
        pipe_x4 += 2
    
    if pipe_x1 - 15 <= 200 and pipe_x1 + 75 >= 200:
        if ball.y - 15 <= pipe_space1 or ball.y + 15 >= pipe_space1 + 125:
            ball.y -= 4
            pipe_x1 += 2
            pipe_x2 += 2
            pipe_x3 += 2
            pipe_x4 += 2

    if pipe_x2 - 15 <= 200 and pipe_x2 + 75 >= 200:
        if ball.y - 15 <= pipe_space2 or ball.y + 15 >= pipe_space2 + 125:
            ball.y -= 4
            pipe_x1 += 2
            pipe_x2 += 2
            pipe_x3 += 2
            pipe_x4 += 2
            
    if pipe_x3 - 15 <= 200 and pipe_x3 + 75 >= 200:
        if ball.y - 15 <= pipe_space3 or ball.y + 15 >= pipe_space3 + 125:
            ball.y -= 4
            pipe_x1 += 2
            pipe_x2 += 2
            pipe_x3 += 2
            pipe_x4 += 2
            
    if pipe_x4 - 15 <= 200 and pipe_x4 + 75 >= 200:
        if ball.y - 15 <= pipe_space4 or ball.y + 15 >= pipe_space4 + 125:
            ball.y -= 4
            pipe_x1 += 2
            pipe_x2 += 2
            pipe_x3 += 2
            pipe_x4 += 2
    
    ellipse(ball.x, ball.y, 30, 30)
    
    
