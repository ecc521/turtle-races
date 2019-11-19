#!/bin/python3

from turtle import *
from random import randint
from time import sleep
import colorsys

print("Width: " + str(window_height()))
print("Height: " + str(window_width()))
setup(width=2000,height=2000)
#print("Width: " + str(window_height()))
#print("Height: " + str(window_width()))


title("Tucker's Turtle Races")

def downward(amount): 
	#turtle doesn't have a downward function - so I'm going to make one.
	right(90)
	forward(amount)
	left(90)

def upward(amount):
	#turtle upward function
	downward(-amount)
	
	
	
def drawTrack():
	speed(0) #Max Speed.
	
	penup()
	goto(-window_width() / 3,window_height()/3) #2/3rds of way to top left.
	pendown()
	
	lines = 20		
	
	for counter in range(lines + 1):
		hideturtle()
		pendown()
		write(int(counter * 100/lines), align="center")
		downward(window_height()/2.9)
		upward(window_height()/2.9)
		penup()
		forward(window_width()/lines*2/3)

	global end
	end = pos()[0] #Position to end at.

	
darkmode = True
if darkmode:
	bgcolor("black")
	color("white")

def raceTurtles():
	turtleCount = 12
	turtles = []
	for counter in range(turtleCount):
		turtle = Turtle()
		turtle.hideturtle()
		turtle.shape("turtle")
		turtle.shapesize(1.5,1.5) #Stretch to 1.5x in both dimensions
		
		#Programmatically generate colors
		hue = 360 / turtleCount * counter
		lightness = 0.4
		if darkmode: 
			lightness = 0.6
		color = colorsys.hls_to_rgb(hue/360,lightness,1) #colorsys.hls_to_rgb(hue/360,0.5,1)
		turtle.color(color)
		
		turtles.append(turtle)

	for counter in range(len(turtles)):
		turtle = turtles[counter]
		turtle.penup()
		turtle.speed(0)
		turtle.goto(-window_width()/3, window_height()/3 - (window_height()/3)/turtleCount*(counter+1))
		turtle.showturtle()
		
		
	
	sleep(0.5)
	
	distances = []
	#Time to race!
	for counter in range(len(turtles)):
		distances.append([])

	
	min = -window_width()/500	
	max = window_width()/100
	
	finished = False
	
	while finished == False:
		allfinished = True
		for turtleNum in range(len(turtles)):
			turtle = turtles[turtleNum]
			
			current = turtle.pos()[0]
			print(current)
			print(end)
			
			if current < end:
				move = randint(min,max)
				distances[turtleNum].append(move)
				turtle.forward(move)
				allfinished = False
				
		finished = allfinished





		
drawTrack()
raceTurtles()

sleep(10)
