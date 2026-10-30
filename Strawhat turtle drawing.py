import turtle
wn = turtle.Screen()
wn.bgcolor("white")

top_skull = turtle.Turtle()
bottom_skull = turtle.Turtle()
straw_hat = turtle.Turtle()
cross_bones = turtle.Turtle()

def draw_filled_circle(t, x, y, radius):
    t.up()
    t.goto(x, y)
    t.down()
    t.begin_fill()
    t.circle(radius)
    t.end_fill()
    t.up()

def draw_jaw(t, x, y, angle, turn):
    t.up()
    t.goto(x, y)
    t.down()
    t.setheading(angle)

    for i in range(18):
        t.forward(8)
        t.setheading(t.heading() + turn)

def draw_teeth_horizontal(t, x, y, angle, turn):
    t.up()
    t.goto(x, y)
    t.down()
    t.setheading(angle)
    for i in range(18):
        t.forward(8)
        t.setheading(t.heading() + turn)

def draw_teeth_vertical(t, x, y, angle, f):
    t.up()
    t.goto(x,y)
    t.down()
    t.setheading(angle)
    t.forward(f)

def draw_strawhat_brim(t, x, y, angle):
    t.up()
    t.goto(x,y,)
    t.down()
    t.setheading(angle)
    for i in range(2):
        t.begin_fill()
        t.forward(240)
        t.circle(8,180)
        t.end_fill()

def draw_crossbones(t, x, y, angle, f, radius, degrees):
    t.up()
    t.goto(x, y)
    t.down()
    t.setheading(angle)
    t.forward(f)
    t.right(90)
    t.circle(radius,degrees)

 
# Main skull outline
top_skull.pensize(5)
top_skull.circle(100)

# Eyes and nose
top_skull.fillcolor("black")
draw_filled_circle(top_skull, 40, 50, 30)
draw_filled_circle(top_skull, -40, 50, 30)
draw_filled_circle(top_skull, 0, 30, 10)

# Jaw
bottom_skull.pensize(5)
draw_jaw(bottom_skull, -70, 25, -100, 5)
draw_jaw(bottom_skull, 70, 25, -80, -5)
draw_teeth_horizontal(bottom_skull, -65, -20, -30, 3.7)
draw_teeth_horizontal(bottom_skull, -70, 0, -30, 3.7)
draw_teeth_vertical(bottom_skull, 0, 0, -90, 40)
draw_teeth_vertical(bottom_skull, 40, 10, -80, 40)
draw_teeth_vertical(bottom_skull, -40, 10, -100, 40)

# Strawhat
#brim
straw_hat.pensize(5)
straw_hat.fillcolor("yellow")
draw_strawhat_brim(straw_hat, -120, 120, 0)
#cap
straw_hat.up()
straw_hat.goto(95,135)
straw_hat.down()
straw_hat.begin_fill()
straw_hat.left(90)
straw_hat.circle(95,180)
straw_hat.end_fill()
#red band
straw_hat.fillcolor("red")
straw_hat.up()
straw_hat.goto(-95, 135)
straw_hat.down()
straw_hat.setheading(0)
straw_hat.begin_fill()
straw_hat.forward(190)
straw_hat.goto(86, 170)
straw_hat.goto(-86, 170)
straw_hat.goto(-95, 135)
straw_hat.end_fill()

#crossbones
cross_bones.pensize(5)
#top
draw_crossbones(cross_bones, 100, 140, 45, 70, 20, 222)
draw_crossbones(cross_bones, 85, 170, 45, 60, 20, -222)
draw_crossbones(cross_bones, -100, 140, 135, 70, 20, -222)
draw_crossbones(cross_bones, -85, 170, 135, 60, 20, 222)
#bottom
draw_crossbones(cross_bones, 70, -30, -45, 70, 20, -222)
draw_crossbones(cross_bones, 55, -60, -45, 60, 20, 222)
draw_crossbones(cross_bones, -70, -30, -135, 70, 20, 222)
draw_crossbones(cross_bones, -55, -60, -135, 60, 20, -222)


wn.exitonclick()