
# Turtle Graphics & keyboard Version 1.1

```python
import keyboard
import turtle

t = turtle.Turtle()
t.shape("turtle")

n = 1
t.pensize(n)
t.speed(0)

t.penup()
t.goto(-400, -400)
t.pendown()
t.goto(400, -400)
t.goto(400, 400)
t.goto(-400, 400)
t.goto(-400, -400)
t.penup()
t.home()
t.pendown()

while True:
    
    if keyboard.is_pressed("w"):
        t.setheading(90)
        t.forward(1)
    
    if keyboard.is_pressed("a"):
        t.setheading(180)
        t.forward(1)
        
    if keyboard.is_pressed("s"):
        t.setheading(270)
        t.forward(1)
        
    if keyboard.is_pressed("d"):
        t.setheading(0)
        t.forward(1)

    if keyboard.is_pressed("+"):
        n += 1
        t.pensize(n)

    if keyboard.is_pressed("-"):
        n -= 1
        if n < 0:
            n += 1
        t.pensize(n)

    if keyboard.is_pressed("c"):
        t.circle(10)

    if t.xcor() > 400:
        t.setheading(180)
        t.forward(1)

    if t.xcor() < -400:
        t.setheading(0)
        t.forward(1)

    if t.ycor() > 400:
        t.setheading(270)
        t.forward(1)

    if t.ycor() < -400:
        t.setheading(90)
        t.forward(1)

```
# Turtle Graphics & keyboard Version 1.0

```python
import keyboard
import turtle

t = turtle.Turtle()
t.shape("turtle")

n = 1
t.pensize(n)
t.speed(0)

while True:
    
    if keyboard.is_pressed("w"):
        t.setheading(90)
        t.forward(1)
    
    if keyboard.is_pressed("a"):
        t.setheading(180)
        t.forward(1)
        
    if keyboard.is_pressed("s"):
        t.setheading(270)
        t.forward(1)
        
    if keyboard.is_pressed("d"):
        t.setheading(0)
        t.forward(1)
```
