ball = PVector(30, 250)
pipes = random(30, 470)
pipe_x1 = 1500
pipe_x2 = 1200
pipe_x3 = 900
pipe_x4 = 600
pipe_space1 = random(50, 350)
pipe_space2 = random(50, 350)
pipe_space3 = random(50, 350)
pipe_space4 = random(50, 350)
pipe_color = color(200)


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
    
    background(255)
    noStroke()
    
    # pipes
    fill(200)
    
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
    
    fill(255)
    rect(pipe_x1, pipe_space1, 75, 100)
    if pipe_x1 == 1000: pipe_space1 = random(50, 350)
    rect(pipe_x2, pipe_space2, 75, 100)
    if pipe_x2 == 1000: pipe_space2 = random(50, 350)
    rect(pipe_x3, pipe_space3, 75, 100)
    if pipe_x3 == 1000: pipe_space3 = random(50, 350)
    rect(pipe_x4, pipe_space4, 75, 100)
    if pipe_x4 == 1000: pipe_space4 = random(50, 350)
        
    # ball
    ball.y += 4
    fill(0)
    if keyPressed == True:
        if key  == ' ':
            ball.y -= 10
            
    if ball.y >= height:
        ball.y = 250
        pipe_x1 = 1500
        pipe_x2 = 1200
        pipe_x3 = 900
        pipe_x4 = 600
    
    ball_space_color = get(ball.x + 16, ball.y + 16)
    if ball_space_color == pipe_color:
        ball.y = 250
        pipe_x1 = 1500
        pipe_x2 = 1200
        pipe_x3 = 900
        pipe_x4 = 600
        
    ellipse(ball.x, ball.y, 30, 30)
    
