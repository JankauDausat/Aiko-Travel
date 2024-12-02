import turtle
import random


def draw_petal():
    turtle.circle(100, 60)  
    turtle.left(120)        
    turtle.circle(100, 60)  
    turtle.left(120)         

def draw_flower():
    for _ in range(6):  
        draw_petal()
        turtle.left(60)  


def draw_stem():
    turtle.right(90)     
    turtle.forward(200)  


def main():
    turtle.speed(10)  
    turtle.bgcolor("White")  

    
    turtle.penup()  
    turtle.goto(0, -100)  
    turtle.pendown()  
    turtle.color(random.choice(["red", "Red", "pink", "purple", "orange"]))
    draw_flower()

    
    turtle.color("Black")
    draw_stem()

    
    turtle.hideturtle()  

    
    turtle.done()        

if __name__ == "__main__":
    main()