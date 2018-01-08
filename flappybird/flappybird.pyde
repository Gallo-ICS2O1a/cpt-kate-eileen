ball = PVector(30, 250)
pipes = random(30, 470)
pipe_x_loc = width

def setup():
    size(1000, 500)
    
    
def draw():
    global ball
    global pipes
    
    background(255)
    noStroke()
    
    # ball
    fill(0)
    ellipse(ball.x, ball.y, 30, 30)
    
    # pipes
    fill(200)
    rect(pipe_x_loc, 0, 75, height)
    
    
    
    
