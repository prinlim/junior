import play #loading the play library 
import random #loading random library

#determine a constant Court's width and height/global variable for horizontal and vertical size 
w=300
h=500
#determine a constant for the middle Court's w&h/global variable for half w&h
half_Width= w/2
half_Height=h/2
#determine the beginning score/global variable
score=0
#determine the speed of ball/global variable
speed=3
@play.when_program_starts
#declare a function/creates keyframe to start game
def do():
  #defining or intializing the function DO
  play.set_backdrop("crimson") #sets bg color
  
  #define the playing court
court= play.new_box( #declaring variable that will be the play field (play) calls the library(.)query for a prebuild function (new_box) creates rectangles, parenthesis hold the parameters 
  color="white", #intializing the parameter for the color 
  x=0, #intializing x, horizontal coor. value 
  y=0, #intializing y, vertical coor. value  
  width=w, #intializing width to preset value 'w'
  height=h, #intializing height to preset value 'h'
) # close parameters


ball= play.new_circle ( #declares the variable that will be the ball/ as a circle 
  radius=10, #initializing parameter radius 
  x=0, #intializing x, horizontal coor. value 
  y=half_Height - 30, #intializing y with global variable haldHeight - 30 to have a fixed starting point, vertical coor. value  
  color="gold", #intializing parameter for color 
  angle= random.randint(210,330) #intializing angle of ball bounce
)

paddle = play.new_box( #declares variable that will be tha paddle/as a rectangle 
  color="forestgreen", #intializing parameter color
  x=0,
  # x of paddle equals MouseX, intializing x, horizontal coor. value 
  y=-half_Height + 10,   # fixed starting point for y for the paddle with global variable halfHeight + 10
  width=25, #intializes parameter width
  height=5, #intializes parameter height 
)

scoretext = play.new_text(
  # declares the varible for the score as text 
  color="lightyellow", #intializes parameter color 
  words="SCORE: " + str(score), #intializes parameter for text and the string score 
  x=0, # intializes horizontal coordinate
  y=half_Height+15, # intializes vertical coordinate, with global variable halfHeight + 15
  font= None,  #intializes font style 
)
@play.repeat_forever #keyfram to do the following as long as game is playing 
#declare the paddle movement
def do(): # redefine DO func. 
    global score #calling for global variable score
    paddle.x = play.mouse.x #Dot notation to call the x parameter of paddle to reassign value to match mouse x coor. 
  
  #to ensure the paddle isn't off the court 
    if(play.mouse.x < -half_Width + paddle.width/2): #left side
        paddle.x = -half_Width+paddle.width/2
    if(play.mouse.x > half_Width - paddle.width/2):#right side
        paddle.x=half_Width - paddle.width/2
    ball.move(speed)
#top wall
    if(ball.y + ball.radius > half_Height):
        ball.angle= 360-ball.angle
#bottom wall
    if(ball.y - ball.radius < -half_Height):
        ball.angle= 360-ball.angle
        score -= 1 # score = score-1
#bounce off left/right :180-angle 

#right wall
    if(ball.x + ball.radius > half_Width):
        ball.angle = 180 - ball.angle
#left wall
    if(ball.x - ball.radius < -half_Width):
        ball.angle=180-ball.angle
  #make it bounce as if it hit the bottom, and give it a little change of trajectory
    if(ball.is_touching(paddle)):
        ball.angle=360-ball.angle + random.randint(-30,30)
        ball.angle %= 360 #ensure angle is valid 
    #make sure ball goes up after hitting paddle 
        if(ball.angle < 20):
            ball.angle = 20 
        elif(ball.angle>160):
            ball.angle = 160
        score +=1
        if(score==5):
            paddle.width-= 5
    ball.angle %=360 #ensure angle is valid
    scoretext.words= " SCORE: " + str(score)

play.start_program()





