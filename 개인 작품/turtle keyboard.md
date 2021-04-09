# Turrle Graphics & keyboard Version 1.3

```python
import keyboard
import turtle as t
import time as T

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

r = 0

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
        T.sleep(0.1)
        print('n =', n)
        t.pensize(n)

    if keyboard.is_pressed("-"):
        n -= 1
        print('n =', n)
        if n < 0:
            n += 1
        t.pensize(n)
        T.sleep(0.1)

    if keyboard.is_pressed(","):
        r -= 0.5
        print('r =', r)
        if r < 0:
            r += 1
        T.sleep(0.1)

    if keyboard.is_pressed("."):
        r += 0.5
        print('r =', r)
        T.sleep(0.1)

    if keyboard.is_pressed("c"):
        t.circle(r)

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

# Turrle Graphics & keyboard Version 1.3

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

r = 0

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

    if keyboard.is_pressed(","):
        r -= 0.1
        if r < 0:
            r += 1

    if keyboard.is_pressed("."):
        r += 0.1

    if keyboard.is_pressed("c"):
        t.circle(r)

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

# Turrle Graphics & keyboard Version 1.2

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

    if keyboard.is_pressed("1"):
        r = 1

    if keyboard.is_pressed("2"):
        r = 2

    if keyboard.is_pressed("3"):
        r = 3

    if keyboard.is_pressed("4"):
        r = 4

    if keyboard.is_pressed("5"):
        r = 5

    if keyboard.is_pressed("6"):
        r = 6

    if keyboard.is_pressed("7"):
        r = 7

    if keyboard.is_pressed("8"):
        r = 8

    if keyboard.is_pressed("9"):
        r = 9   

    if keyboard.is_pressed("c"):
        t.circle(r)

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
