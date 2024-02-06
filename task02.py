import turtle

def tree_P(t, i, cur_recursion, max_recursion):
    if cur_recursion > max_recursion:
        return
    else:
        t.forward(i)
        t.left(45)
        tree_P(t, 3/4*i, cur_recursion+1, max_recursion)
        t.right(90)
        tree_P(t, 3/4*i, cur_recursion+1, max_recursion)
        t.left(45)
        t.backward(i)

def draw_koch_curve(recursion_level):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)  
    t.penup()
    t.goto(0, -100)
    t.left(90)
    t.pendown()

    tree_P(t, 100, 0 ,recursion_level)

    t.penup()
   
    window.mainloop()

# Виклик функції
try:
    recursion_level=int(input("Enter recursion level "))
    draw_koch_curve(recursion_level)
except:
    print("Incorrect recursion level")