ball = PVector(30, 250)
pipes = random(30, 470)
pipe_x_loc = 1500

def setup():
    size(1000, 500)
    
    
def draw():
    global ball
    global pipes
    global pipe_x_loc
    
    background(255)
    noStroke()
    
    # pipes
    fill(200)
    for x in range(1000, 0, -200):
        rect(x, 0, 75, height)
    
    # ball
    fill(0)
    ellipse(ball.x, ball.y, 30, 30)
    

    
    
    
