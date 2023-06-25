import tkinter as tk
import turtle

def draw_logo():
    turtle.clear()

    initials=entry.get()

    #set up turtle graphics
    turtle.speed(2)
    turtle.pensize(5)

    turtle.bgcolor("#C8E6C9")

    #set the initial position
    turtle.penup()
    turtle.goto(0,0)
    turtle.setheading(0)
    turtle.pendown()

    #draw outer line of circle
    turtle.color("black")
    turtle.circle(100)

    #fill tthe circle with color
    turtle.color("blue")
    turtle.begin_fill()
    turtle.circle(95)
    turtle.end_fill()


    #write initial inside the circle
    turtle.penup()
    turtle.goto(0,60)
    turtle.pendown()
    turtle.color("white")
    turtle.write(initials, align='center',font=('Monotype Corsiva',40,"bold"))

    turtle.hideturtle()

window=tk.Tk()
window.title("Initial Logo Maker")
window.configure(bg="#D1C4E9")

label=tk.Label(window,text="Enter two initials : ",font=("Roboto",20,"italic","bold"))
label.pack()

entry=tk.Entry(window)
entry.pack()

button=tk.Button(window,text="Generate Logo",font=("Arial Black",10),command=draw_logo)
button.pack()

canvas=turtle.ScrolledCanvas(window)
canvas.pack()

screen=turtle.TurtleScreen(canvas)
turtle.RawTurtle(screen)

window.mainloop()