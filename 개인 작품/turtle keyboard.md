# Turtle Graphics & keyboard Version 1.9

```python
import keyboard
import turtle as t
import time as tt

def sq(a, b, z):
    t.setheading(0)
    t.forward(z)
    t.setheading(90)
    t.forward(z)
    t.setheading(180)
    t.forward(z)
    t.setheading(270)
    t.forward(z)
    t.setheading(0)

def tr(a, b, x):
    t.setheading(0)
    t.forward(x)
    t.setheading(120)
    t.forward(x)
    t.setheading(240)
    t.forward(x)
    t.setheading(0)

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

print('wasd로 거북이를 이동합니다')
print('v(거북이), b(화살표), n(삼각형), m(원)으로 모양을 바꿀 수 있습니다.')
print('1~0 숫자키로 색을 변경할 수 있습니다. (빨주노초파남보흰검회)')
print('k를 누르면 거북이의 속도가 느려지고 l을 누르면 빨라집니다.')
print('+와 -로 펜의 굵기를 조절할 수 있습니다.')
print('u를 누르면 penup, i를 누르면 pendown을 할 수 있습니다.')
print('c를 누르면 원을 그릴 수 있습니다.')
print('< 을 누르면 원의 반지름이 작아지고 > 을 누르면 반대로 커집니다.')
print('z 버튼을 누르면 정사각형을 그릴 수 있습니다. [와 ]로 크기 조절이 가능합니다.')
print('x 버튼을 누르면 정삼각형을 그릴 수 있습니다. g와 h로 크기 조절이 가능합니다.')
print('; 버튼을 누르면 채우기 현재 위치가 채우기 시작점으로 설정되고, \'를 누르면 채워집니다.')

r = 0

k = 1

z = 1

x = 1

while True:
    
    if keyboard.is_pressed("w"):
        t.setheading(90)
        t.forward(k)
    
    if keyboard.is_pressed("a"):
        t.setheading(180)
        t.forward(k)
        
    if keyboard.is_pressed("s"):
        t.setheading(270)
        t.forward(k)
        
    if keyboard.is_pressed("d"):
        t.setheading(0)
        t.forward(k)

    if keyboard.is_pressed("u"):
        t.penup()

    if keyboard.is_pressed("i"):
        t.pendown()

    if keyboard.is_pressed("v"):
        t.shape("turtle")

    if keyboard.is_pressed("b"):
        t.shape("classic")

    if keyboard.is_pressed("n"):
        t.shape("triangle")

    if keyboard.is_pressed("m"):
        t.shape("circle")

    if keyboard.is_pressed("+"):
        n += 1
        tt.sleep(0.1)
        print('n =', n)
        t.pensize(n)

    if keyboard.is_pressed("-"):
        n -= 1
        print('n =', n)
        if n < 0:
            n += 1
        t.pensize(n)
        tt.sleep(0.1)

    if keyboard.is_pressed("]"):
        z += 1
        tt.sleep(0.1)
        print('z =', z)

    if keyboard.is_pressed("["):
        z -= 1
        print('z =', z)
        if z < 0:
            z += 1
        tt.sleep(0.1)

    if keyboard.is_pressed("h"):
        x += 1
        tt.sleep(0.1)
        print('x =', x)

    if keyboard.is_pressed("g"):
        x -= 1
        print('x =', x)
        if x < 0:
            x += 1
        tt.sleep(0.1)

    if keyboard.is_pressed(","):
        r -= 0.5
        print('r =', r)
        if r < 0:
            r += 1
        tt.sleep(0.1)

    if keyboard.is_pressed("."):
        r += 0.5
        print('r =', r)
        tt.sleep(0.1)

    if keyboard.is_pressed("c"):
        t.circle(r)

    if keyboard.is_pressed("l"):
        k += 0.1
        print('k =', k)
        tt.sleep(0.1)

    if keyboard.is_pressed("k"):
        k -= 0.1
        print('k =', k)
        if k < 0:
            k += 0.1
        tt.sleep(0.1)

    if keyboard.is_pressed("1"):
        t.color("red")

    if keyboard.is_pressed("2"):
        t.color("orange")

    if keyboard.is_pressed("3"):
        t.color("yellow")

    if keyboard.is_pressed("4"):
        t.color("green")

    if keyboard.is_pressed("5"):
        t.color("blue")

    if keyboard.is_pressed("6"):
        t.color("navy")

    if keyboard.is_pressed("7"):
        t.color("purple")

    if keyboard.is_pressed("8"):
        t.color("white")

    if keyboard.is_pressed("9"):
        t.color("black")

    if keyboard.is_pressed("0"):
        t.color("gray")

    if keyboard.is_pressed(";"):
        t.begin_fill()

    if keyboard.is_pressed("'"):
        t.end_fill()

    if keyboard.is_pressed("z"):
        sq(t.xcor, t.ycor, z)
        tt.sleep(0.2)
        
    if keyboard.is_pressed("x"):
        tr(t.xcor, t.ycor, x)
        tt.sleep(0.2)

    if t.xcor() > 400:
        t.setheading(180)
        t.forward(k)

    if t.xcor() < -400:
        t.setheading(0)
        t.forward(k)

    if t.ycor() > 400:
        t.setheading(270)
        t.forward(k)

    if t.ycor() < -400:
        t.setheading(90)
        t.forward(k)
```

# Turtle Graphics & keyboard Version 1.8

```python
import keyboard
import turtle as t
import time as tt

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

print('wasd로 거북이를 이동합니다')
print('v(거북이), b(화살표), n(삼각형), m(원)으로 모양을 바꿀 수 있습니다.')
print('1~0 숫자키로 색을 변경할 수 있습니다. (빨주노초파남보흰검회)')
print('k를 누르면 거북이의 속도가 느려지고 l을 누르면 빨라집니다.')
print('+와 -로 펜의 굵기를 조절할 수 있습니다.')
print('u를 누르면 penup, i를 누르면 pendown을 할 수 있습니다.')
print('c를 누르면 원을 그릴 수 있습니다.')
print('< 을 누르면 원의 반지름이 작아지고 > 을 누르면 반대로 커집니다.')

r = 0

k = 1

while True:
    
    if keyboard.is_pressed("w"):
        t.setheading(90)
        t.forward(k)
    
    if keyboard.is_pressed("a"):
        t.setheading(180)
        t.forward(k)
        
    if keyboard.is_pressed("s"):
        t.setheading(270)
        t.forward(k)
        
    if keyboard.is_pressed("d"):
        t.setheading(0)
        t.forward(k)

    if keyboard.is_pressed("u"):
        t.penup()

    if keyboard.is_pressed("i"):
        t.pendown()

    if keyboard.is_pressed("v"):
        t.shape("turtle")

    if keyboard.is_pressed("b"):
        t.shape("classic")

    if keyboard.is_pressed("n"):
        t.shape("triangle")

    if keyboard.is_pressed("m"):
        t.shape("circle")

    if keyboard.is_pressed("+"):
        n += 1
        tt.sleep(0.1)
        print('n =', n)
        t.pensize(n)

    if keyboard.is_pressed("-"):
        n -= 1
        print('n =', n)
        if n < 0:
            n += 1
        t.pensize(n)
        tt.sleep(0.1)

    if keyboard.is_pressed(","):
        r -= 0.5
        print('r =', r)
        if r < 0:
            r += 1
        tt.sleep(0.1)

    if keyboard.is_pressed("."):
        r += 0.5
        print('r =', r)
        tt.sleep(0.1)

    if keyboard.is_pressed("c"):
        t.circle(r)

    if keyboard.is_pressed("l"):
        k += 0.1
        print('k =', k)
        tt.sleep(0.1)

    if keyboard.is_pressed("k"):
        k -= 0.1
        print('k =', k)
        if k < 0:
            k += 0.1
        tt.sleep(0.1)

    if keyboard.is_pressed("1"):
        t.color("red")

    if keyboard.is_pressed("2"):
        t.color("orange")

    if keyboard.is_pressed("3"):
        t.color("yellow")

    if keyboard.is_pressed("4"):
        t.color("green")

    if keyboard.is_pressed("5"):
        t.color("blue")

    if keyboard.is_pressed("6"):
        t.color("navy")

    if keyboard.is_pressed("7"):
        t.color("purple")

    if keyboard.is_pressed("8"):
        t.color("white")

    if keyboard.is_pressed("9"):
        t.color("black")

    if keyboard.is_pressed("0"):
        t.color("gray")

    if t.xcor() > 400:
        t.setheading(180)
        t.forward(k)

    if t.xcor() < -400:
        t.setheading(0)
        t.forward(k)

    if t.ycor() > 400:
        t.setheading(270)
        t.forward(k)

    if t.ycor() < -400:
        t.setheading(90)
        t.forward(k)
```

# Turtle Graphics & keyboard Version 1.7

```python
import keyboard
import turtle as t
import time as tt

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

print('wasd로 거북이를 이동합니다')
print('1~0 숫자키로 색을 변경할 수 있습니다. (빨주노초파남보흰검회)')
print('k를 누르면 거북이의 속도가 느려지고 l을 누르면 빨라집니다.')
print('키패드 부분의 +와 -로 펜의 굵기를 조절할 수 있습니다.')
print('u를 누르면 penup, i를 누르면 pendown을 할 수 있습니다.')
print('c를 누르면 원을 그릴 수 있습니다.')
print('< 을 누르면 원의 반지름이 작아지고 > 을 누르면 반대로 커집니다.')

r = 0

k = 1

while True:
    
    if keyboard.is_pressed("w"):
        t.setheading(90)
        t.forward(k)
    
    if keyboard.is_pressed("a"):
        t.setheading(180)
        t.forward(k)
        
    if keyboard.is_pressed("s"):
        t.setheading(270)
        t.forward(k)
        
    if keyboard.is_pressed("d"):
        t.setheading(0)
        t.forward(k)

    if keyboard.is_pressed("u"):
        t.penup()

    if keyboard.is_pressed("i"):
        t.pendown()

    if keyboard.is_pressed("+"):
        n += 1
        tt.sleep(0.1)
        print('n =', n)
        t.pensize(n)

    if keyboard.is_pressed("-"):
        n -= 1
        print('n =', n)
        if n < 0:
            n += 1
        t.pensize(n)
        tt.sleep(0.1)

    if keyboard.is_pressed(","):
        r -= 0.5
        print('r =', r)
        if r < 0:
            r += 1
        tt.sleep(0.1)

    if keyboard.is_pressed("."):
        r += 0.5
        print('r =', r)
        tt.sleep(0.1)

    if keyboard.is_pressed("c"):
        t.circle(r)

    if keyboard.is_pressed("l"):
        k += 0.1
        print('k =', k)
        tt.sleep(0.1)

    if keyboard.is_pressed("k"):
        k -= 0.1
        print('k =', k)
        if k < 0:
            k += 0.1
        tt.sleep(0.1)

    if keyboard.is_pressed("1"):
        t.color("red")

    if keyboard.is_pressed("2"):
        t.color("orange")

    if keyboard.is_pressed("3"):
        t.color("yellow")

    if keyboard.is_pressed("4"):
        t.color("green")

    if keyboard.is_pressed("5"):
        t.color("blue")

    if keyboard.is_pressed("6"):
        t.color("navy")

    if keyboard.is_pressed("7"):
        t.color("purple")

    if keyboard.is_pressed("8"):
        t.color("white")

    if keyboard.is_pressed("9"):
        t.color("black")

    if keyboard.is_pressed("0"):
        t.color("gray")

    if t.xcor() > 400:
        t.setheading(180)
        t.forward(k)

    if t.xcor() < -400:
        t.setheading(0)
        t.forward(k)

    if t.ycor() > 400:
        t.setheading(270)
        t.forward(k)

    if t.ycor() < -400:
        t.setheading(90)
        t.forward(k)
```

# Turtle Graphics & keyboard Version 1.6

```python
mport keyboard
import turtle as t
import time as tt

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

k = 1

while True:
    
    if keyboard.is_pressed("w"):
        t.setheading(90)
        t.forward(k)
    
    if keyboard.is_pressed("a"):
        t.setheading(180)
        t.forward(k)
        
    if keyboard.is_pressed("s"):
        t.setheading(270)
        t.forward(k)
        
    if keyboard.is_pressed("d"):
        t.setheading(0)
        t.forward(k)

    if keyboard.is_pressed("u"):
        t.penup()

    if keyboard.is_pressed("i"):
        t.pendown()

    if keyboard.is_pressed("+"):
        n += 1
        tt.sleep(0.1)
        print('n =', n)
        t.pensize(n)

    if keyboard.is_pressed("-"):
        n -= 1
        print('n =', n)
        if n < 0:
            n += 1
        t.pensize(n)
        tt.sleep(0.1)

    if keyboard.is_pressed(","):
        r -= 0.5
        print('r =', r)
        if r < 0:
            r += 1
        tt.sleep(0.1)

    if keyboard.is_pressed("."):
        r += 0.5
        print('r =', r)
        tt.sleep(0.1)

    if keyboard.is_pressed("c"):
        t.circle(r)

    if keyboard.is_pressed("l"):
        k += 0.1
        print('k =', k)
        tt.sleep(0.1)

    if keyboard.is_pressed("k"):
        k -= 0.1
        print('k =', k)
        if k < 0:
            k += 0.1
        tt.sleep(0.1)

    if keyboard.is_pressed("1"):
        t.color("red")

    if keyboard.is_pressed("2"):
        t.color("orange")

    if keyboard.is_pressed("3"):
        t.color("yellow")

    if keyboard.is_pressed("4"):
        t.color("green")

    if keyboard.is_pressed("5"):
        t.color("blue")

    if keyboard.is_pressed("6"):
        t.color("navy")

    if keyboard.is_pressed("7"):
        t.color("purple")

    if keyboard.is_pressed("8"):
        t.color("white")

    if keyboard.is_pressed("9"):
        t.color("black")

    if keyboard.is_pressed("0"):
        t.color("gray")

    if t.xcor() > 400:
        t.setheading(180)
        t.forward(k)

    if t.xcor() < -400:
        t.setheading(0)
        t.forward(k)

    if t.ycor() > 400:
        t.setheading(270)
        t.forward(k)

    if t.ycor() < -400:
        t.setheading(90)
        t.forward(k)

```

# Turtle Graphics & keyboard Version 1.5

```python
import keyboard
import turtle as t
import time as tt
mport keyboard
import turtle as t
import time as tt

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

k = 0

while True:
    
    if keyboard.is_pressed("w"):
        t.setheading(90)
        t.forward(k)
    
    if keyboard.is_pressed("a"):
        t.setheading(180)
        t.forward(k)
        
    if keyboard.is_pressed("s"):
        t.setheading(270)
        t.forward(k)
        
    if keyboard.is_pressed("d"):
        t.setheading(0)
        t.forward(k)

    if keyboard.is_pressed("u"):
        t.penup()

    if keyboard.is_pressed("i"):
        t.pendown()

    if keyboard.is_pressed("+"):
        n += 1
        tt.sleep(0.1)
        print('n =', n)
        t.pensize(n)

    if keyboard.is_pressed("-"):
        n -= 1
        print('n =', n)
        if n < 0:
            n += 1
        t.pensize(n)
        tt.sleep(0.1)

    if keyboard.is_pressed(","):
        r -= 0.5
        print('r =', r)
        if r < 0:
            r += 1
        tt.sleep(0.1)

    if keyboard.is_pressed("."):
        r += 0.5
        print('r =', r)
        tt.sleep(0.1)

    if keyboard.is_pressed("c"):
        t.circle(r)

    if keyboard.is_pressed("l"):
        k += 0.1
        print('k =', k)
        tt.sleep(0.1)

    if keyboard.is_pressed("k"):
        k -= 0.1
        print('k =', k)
        if k < 0:
            k += 0.1
        tt.sleep(0.1)

    if t.xcor() > 400:
        t.setheading(180)
        t.forward(k)

    if t.xcor() < -400:
        t.setheading(0)
        t.forward(k)

    if t.ycor() > 400:
        t.setheading(270)
        t.forward(k)

    if t.ycor() < -400:
        t.setheading(90)
        t.forward(k)
```

# Turtle Graphics & keyboard Version 1.4

```python
import keyboard
import turtle as t
import time as tt

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

k = 0

while True:
    
    if keyboard.is_pressed("w"):
        t.setheading(90)
        t.forward(k)
    
    if keyboard.is_pressed("a"):
        t.setheading(180)
        t.forward(k)
        
    if keyboard.is_pressed("s"):
        t.setheading(270)
        t.forward(k)
        
    if keyboard.is_pressed("d"):
        t.setheading(0)
        t.forward(k)

    if keyboard.is_pressed("+"):
        n += 1
        tt.sleep(0.1)
        print('n =', n)
        t.pensize(n)

    if keyboard.is_pressed("-"):
        n -= 1
        print('n =', n)
        if n < 0:
            n += 1
        t.pensize(n)
        tt.sleep(0.1)

    if keyboard.is_pressed(","):
        r -= 0.5
        print('r =', r)
        if r < 0:
            r += 1
        tt.sleep(0.1)

    if keyboard.is_pressed("."):
        r += 0.5
        print('r =', r)
        tt.sleep(0.1)

    if keyboard.is_pressed("c"):
        t.circle(r)

    if keyboard.is_pressed("l"):
        k += 0.1
        print('k =', k)
        tt.sleep(0.1)

    if keyboard.is_pressed("k"):
        k -= 0.1
        print('k =', k)
        if k < 0:
            k += 0.1
        tt.sleep(0.1)

    if t.xcor() > 400:
        t.setheading(180)
        t.forward(k)

    if t.xcor() < -400:
        t.setheading(0)
        t.forward(k)

    if t.ycor() > 400:
        t.setheading(270)
        t.forward(k)

    if t.ycor() < -400:
        t.setheading(90)
        t.forward(k)
```

# Turrle Graphics & keyboard Version 1.3

```python
import keyboard
import turtle as t
import time as tt

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
        tt.sleep(0.1)

    if keyboard.is_pressed(","):
        r -= 0.5
        print('r =', r)
        if r < 0:
            r += 1
        tt.sleep(0.1)

    if keyboard.is_pressed("."):
        r += 0.5
        print('r =', r)
        tt.sleep(0.1)

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
