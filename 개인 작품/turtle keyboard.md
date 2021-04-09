
# Turtle Graphics & keyboard

```python
import keyboard
import turtle

t = turtle.Turtle()
t.shape("turtle")

t.pensize(1)
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
