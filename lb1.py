import play
def emoji():
	pl_leg = play.new_circle(
	  color = "gold",
	  radius= 20,
	  x=-160,
	  y=-230,
	)
	pr_leg = play.new_circle(
	  color = "gold",
	  radius= 20,
	  x=-70,
	  y=-230,
	)
	pr_arm = play.new_circle(
	  color = "lightyellow",
	  radius= 20,
	  x=-180,
	  y=-140,
	  border_width=5,
	  border_color="gold",
	)
	pl_arm = play.new_circle(
	  color = "lightyellow",
	  radius= 20,
	  x=-55,
	  y=-140,
	  border_width=5,
	  border_color="gold",
	)
	body_p = play.new_circle(
	color = "moccasin",
	  x=-120,
	  y=-180,
	  radius= 60,  
	  border_width=10,
	  border_color="gold",
	)
	p_ear = play.new_circle(
	  color= "moccasin",
	  x=-160,
	  y=20,
	  radius=40,
	  border_width=10,
	  border_color="gold",
	)
	pl_ear = play.new_circle(
	  color= "moccasin",
	  x=-60,
	  y=20,
	  radius=40,
	  border_width=10,
	  border_color="gold",
	)
	
	p_head = play.new_circle(
	  color = "gold",
	  x=-110,
	  y=-50,
	  radius=90,
	)
	p_nose = play.new_circle(
	  color = "moccasin",
	  x=-80,
	  y=-75,
	  radius=7,
	)
	eye_P = play.new_circle(
	    color="forestgreen",
	    x=-100,
	    y=-50,
	    radius=10,
	  border_color= "aliceblue",
	  border_width=5,
	  
	)
	eye_p = play.new_circle(
	    color="forestgreen",
	    x=-70,
	    y=-50,
	    radius=10,
	   border_color= "white",
	  border_width=5,
	)
	pr_eyebrow = play.new_circle(
	  color="lightyellow",
	  x=-100,
	  y=-30,
	  radius=8,
	)
	pl_eyebrow = play.new_circle(
	  color="lightyellow",
	  x=-70,
	  y=-30,
	  radius=8,
	)
	pri_mouth = play.new_box(
	  border_color="salmon",
	  border_width=1,
	  color="white",
	  x=-90,
	  y=-105,
	  width=50,
	  height=10,
	)
