import turtle

screen = turtle.Screen()
screen.bgcolor("white")

t = turtle.Turtle()
t.speed(0)
t.left(90)  
t.penup()
t.backward(100)
t.pendown()

def draw_tree(branch_len, t):
    if branch_len > 5:
        t.forward(branch_len)
        t.right(20)
        draw_tree(branch_len - 15, t)
        t.left(40)
        draw_tree(branch_len - 15, t)
        t.right(20)
        t.backward(branch_len)

t.color("green")
draw_tree(75, t)

screen.mainloop()
