import turtle

t = turtle.Turtle()
t.hideturtle()
t.pensize(4)
t.right(90)
t.speed(0)
t.pendown()
j = 3

xMin = 0
xMax = 0

yMin = 0
yMax = 0

sz = 10

alist = []
blist = []

iterations = 15


for i in range(iterations):

  while j <= i:




    if i % 2 == 0:
      t.right(90)
     
  
    else:
      t.left(90)
     

    if j == 1:

      t.pendown()

      if t.heading() == 0:
        t.forward(sz)
        xMax += sz
        alist.append(sz)
        

      if t.heading() == 90:
        t.forward(sz)
        yMax += sz
        alist.append(sz)

      if t.heading() == 180:
        t.forward(sz)
        xMin -= sz
        alist.append(sz)
        

      if t.heading() == 270:
        t.forward(sz)
        yMin -= sz
        alist.append(sz)
      

    if j > 1:


  

      

      if t.heading() == 0:
        alist.append(int(t.distance(xMax + sz, t.ycor())))
        t.goto(xMax + sz, t.ycor())
        xMax = t.xcor()
        

        

      if t.heading() == 90:
        alist.append(int(t.distance(t.xcor(), yMax + sz)))
        t.goto(t.xcor(), yMax + sz)
        yMax = t.ycor()
        

      if t.heading() == 180:
        alist.append(int(t.distance(xMin - sz, t.ycor())))
        t.goto(xMin - sz, t.ycor())
        xMin = t.xcor()
        

      if t.heading() == 270:
        alist.append(int(t.distance(t.xcor(), yMin - sz)))
        t.goto(t.xcor(), yMin - sz)
        yMin = t.ycor()
        
      


    j += 1


  total = sum(alist)/sz
  blist.append(total)
  total = 0
  del alist[:]

  j = 1

del blist[0]
print(blist)
