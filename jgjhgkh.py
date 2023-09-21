import turtle as t

t.bgcolor("white")
t.fillcolor("red")
t.pensize(2)
t.speed(1)

# Dibuja la parte superior del corazón
t.begin_fill()
t.left(140)
t.forward(224)
for _ in range(200):
    t.right(1)
    t.forward(2)
t.left(120)
for _ in range(200):
    t.right(1)
    t.forward(2)
t.forward(224)
t.end_fill()

# Dibuja la parte inferior del corazón
t.fillcolor("red")
t.begin_fill()
t.left(140)
t.forward(224)
for _ in range(100):
    t.right(1)
    t.forward(2)
t.left(120)
for _ in range(100):
    t.right(1)
    t.forward(2)
t.forward(224)
t.end_fill()

# Oculta la pluma y muestra el corazón completo
t.hideturtle()

# Cierra la ventana al hacer clic en ella
t.exitonclick()