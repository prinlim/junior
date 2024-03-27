import play 
w=300
h=300
@play.when_program_starts
def do():
  play.screen.width = w
  play.screen.height = h

box = play.new_box(
  color="LavenderBlush",
  x=300,
  y=60,
  width=w,
  height=h,
)
# text bubble
play.set_backdrop((50,99,34))
# ------------------
# the face and body
pl_leg = play.new_circle(
  color = "gold",
  radius= 20,
  x=30,
  y=-230,
)
pr_leg = play.new_circle(
  color = "gold",
  radius= 20,
  x=110,
  y=-230,
)
pr_arm = play.new_circle(
  color = "lightyellow",
  radius= 20,
  x=10,
  y=-140,
  border_width=5,
  border_color="gold",
)
pl_arm = play.new_circle(
  color = "lightyellow",
  radius= 20,
  x=135,
  y=-140,
  border_width=5,
  border_color="gold",
)
body_p = play.new_circle(
color = "moccasin",
  x=70,
  y=-180,
  radius= 60,  
  border_width=10,
  border_color="gold",
)
p_ear = play.new_circle(
  color= "moccasin",
  x=30,
  y=20,
  radius=40,
  border_width=10,
  border_color="gold",
)
pl_ear = play.new_circle(
  color= "moccasin",
  x=130,
  y=20,
  radius=40,
  border_width=10,
  border_color="gold",
)

p_head = play.new_circle(
  color = "gold",
  x=80,
  y=-50,
  radius=90,
)
p_nose = play.new_circle(
  color = "moccasin",
  x=110,
  y=-75,
  radius=7,
)
eye_P = play.new_circle(
    color="forestgreen",
    x=90,
    y=-50,
    radius=10,
  border_color= "aliceblue",
  border_width=5,
  
)
eye_p = play.new_circle(
    color="forestgreen",
    x=120,
    y=-50,
    radius=10,
   border_color= "white",
  border_width=5,
)
pr_eyebrow = play.new_circle(
  color="lightyellow",
  x=90,
  y=-30,
  radius=8,
)
pl_eyebrow = play.new_circle(
  color="lightyellow",
  x=120,
  y=-30,
  radius=8,
)
pri_mouth = play.new_box(
  border_color="salmon",
  border_width=1,
  color="white",
  x=110,
  y=-105,
  width=50,
  height=10,
)

# Ears: x +/- 50 from head, both
# Brows:x - left- 10, right - 40
# Eyes: x - left - 10, right - 40
# Nose:x - 30
# Mouth:x - 20
# Body:x - 10 
# Arms:x - right - 70, left - 55
# Legs: right - 40, left - 50
# ------------------
text= play.new_text(
    color="rosybrown",
    words= "Honey?",
    x=290, 
    y=55,
    font_size=20, 
  )
@play.repeat_forever
async def speak_slowly():
    await play.timer(seconds=5)
    text.words=" Yes please, with a side of bees!"
# the text appears after 3 seconds
mouse_text = play.new_text(
 color="rosybrown",
    words= "blank",
    x=290, 
    y=55,
    font_size=20, 
)
@play.repeat_forever
def mouse_coords():
  mouse_text.go_to(play.mouse)
  mouse_text.words= str(int(play.mouse.x)) +","+str(int(play.mouse.y))
# helps find x and y coordinates
play.start_program()
