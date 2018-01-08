ball = PVector(30, 250)
pipes = random(30, 470)
pipe_x_loc = 1000

def setup():
    size(1000, 500)
    
    
def draw():
    global ball
    global pipes
    global pipe_x_loc
    
    background(255)
    noStroke()
    
    # ball
    fill(0)
    ellipse(ball.x, ball.y, 30, 30)
    
    # pipes
    fill(200)
    rect(pipe_x_loc, 0, 75, height)
    rect(pipe_x_loc - 200, 0, 75, height)
    rect(pipe_x_loc - 400, 0, 75, height)
