import turtle
wn = turtle.Screen()
wn.bgcolor("aliceblue")
 
 
leo = turtle.Turtle()
leo.color("blue")

leo.penup()
leo.goto(-150, -150)
 
leo.pendown()
leo.circle(150)

leo.penup()
leo.goto(-100,-100)

leo.pendown()
leo.circle(15)

leo.penup()
leo.goto(-180,-100)

leo.pendown()
leo.circle(15)

leo.penup()
leo.goto(-140,50)

leo.pendown()
leo.circle(22)

wn.exitonclick()