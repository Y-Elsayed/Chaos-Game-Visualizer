import turtle
import random
import math


#Declared leo the turtle
leo = turtle.Turtle()
leo.color("#20C20E")
screen = turtle.Screen()
screen.bgcolor("black")
# leo.shape("cursor")

#Vertices of the triangle(might take them as inputs l8r)
A = [0,0]
B = [250,0]
C = [125,216.5063509]

def take_inp():
    length_side = input("Enter the length of the side: ")
    B[0] = length_side
    C[0] = 0.5 * length_side
    C[1] = math.sqrt((length_side)**2-(0.5 * length_side)**2)


#Draws a triangle
def triangle():
    leo.penup()
    for i in range(3):
        leo.forward(B[0])
        leo.dot()
        leo.left(120)
    leo.left(90)
    
#Generates a random point and draws it if the point is inside the triangle
def chaos_game_point1():
    #First point
    posx = random.uniform(0,B[0])
    posy = random.uniform(0,C[1])
    P = [posx,posy]
    #Repeats if the point is not inside the triangle
    while not is_inside_triangle(P) :
        posx = random.uniform(0,B[0])
        posy = random.uniform(0,C[1])
        P = [posx,posy]
    
    leo.setx(posx)
    leo.sety(posy)
    leo.dot()
    return  P

    #This function should generate the other random points between the distance of the last drawn point and any random vertix
def mid_point(point = []):
    vertices = [A,B,C]
    rand_vertix = vertices[random.randint(0,2)]
    midpoint1 = [ (rand_vertix[0]+point[0])/2 , (rand_vertix[1]+point[1])/2 ]
    leo.setx(midpoint1[0])
    leo.sety(midpoint1[1])
    leo.dot()
    return midpoint1
        
    




#Checks if the point generated is inside the triangle
def is_inside_triangle(P = []):
    w1 = (A[0]*(C[1]-A[1])+(P[1]-A[1])*(C[0]- A[0]) - P[0]*(C[1]-A[1]))/((B[1]-A[1])*(C[0]-A[0])-(B[0]-A[0])*(C[1]-A[1]))
    w2 = (P[1]-A[1]-w1*(B[1]-A[1]))/(C[1]-A[1])

    if(w1 >= 0 and w2 >= 0 and (w1+w2) <=1):
        return True
    else:
        return False

def Chaos_Game():
    counter = 0
    triangle()
    #first point
    p1 = chaos_game_point1()
    #first midpoint
    y = mid_point(p1)
    # loop of midpoints
    while True:
        counter += 1
        z = mid_point(y)
        y = z
        print(counter)

Chaos_Game()

