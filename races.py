#!/bin/python3

from turtle import *
import random
from time import sleep
import colorsys
import math
import sys

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
	
	
def getTurtleY(turtleCount, position):
	return window_height()/3 - (window_height()/1.55)/turtleCount*(position)

def getLeftBound():
	return -window_width() / 2.4

def getTurtleX(ratio):
	return getLeftBound() + (window_width()*3/4)*ratio

	
darkMode = False
turtleCount = 8
turtleSize = 5
lineCount = 20
	
try:
	index = sys.argv.index("--turtleCount")
	turtleCount = int(sys.argv[index+1])
except:
	print("Defaulting to " + str(turtleCount) + " turtles. To configure, pass --turtleCount num")

	
try:
	index = sys.argv.index("--turtleSize")
	turtleSize = float(sys.argv[index+1])
except:
	print("Defaulting to size " + str(turtleSize) + " turtles. To configure, pass --turtleSize num")

	
try:
	index = sys.argv.index("--darkMode")
	darkMode = True
except:
	print("Defaulting to light mode. Pass --darkMode to use dark mode. ")
	
	
try:
	index = sys.argv.index("--lineCount")
	lineCount = int(sys.argv[index+1])
except:
	print("Defaulting to " + str(lineCount) + " lines. To configure, pass --lineCount num")

	
def drawTrack():
	if darkMode:
		bgcolor("black")
		color("white")
	
	speed(0) #Max Speed.
	
	hideturtle()
	penup()
	
	for counter in range(lineCount + 1):
		goto(getTurtleX(counter/lineCount), getTurtleY(1, 0))
		pendown()
		write(int(counter * 100/lineCount), align="center")
		downward(window_height()/1.5)
		penup()
		
		
	
def raceTurtles():
	
	turtles = []
	for counter in range(turtleCount):
		turtle = Turtle()
		turtle.hideturtle()
		turtle.shape("turtle")
		turtle.shapesize(turtleSize,turtleSize)
		turtle.pensize(turtleSize)
		
		#Programmatically generate colors
		hue = 360 / turtleCount * counter
		lightness = 0.4
		if darkMode: 
			lightness = 0.6
		color = colorsys.hls_to_rgb(hue/360,lightness,1) #colorsys.hls_to_rgb(hue/360,0.5,1)
		turtle.color(color)
		
		turtles.append(turtle)

	for counter in range(len(turtles)):
		turtle = turtles[counter]
		turtle.penup()
		turtle.speed(0)
		turtle.goto(getLeftBound(), getTurtleY(len(turtles), counter + 0.75))
		#TODO: Add numbers for each turtle.
		
		goto(getLeftBound() - window_width()/40, getTurtleY(len(turtles), counter + 0.75))
		write(counter + 1, align="center")
		
		turtle.pendown()
		turtle.showturtle()
		
	
	sleep(0.5)
	
	distances = []
	#Time to race!
	for counter in range(len(turtles)):
		distances.append([])

	
	min = window_width()/1000	
	max = window_width()/100
	
	if turtleCount > 10:
		max = max*((turtleCount/10)**0.5) #Speed up the turtles slightly if there are lots. (Because the program runs slower due to large numbers of turtles)
	
	min = math.ceil(min)
	max = math.ceil(max)
	print(min, max)
	
	end = getTurtleX(1)
	finished = False
	
	#With larger numbers of turtles, we don't want a wave going down as they move. Mix it up.
	moveOrder = []
	for turtleNum in range(len(turtles)):
		moveOrder.append(turtleNum)
	random.shuffle(moveOrder)
	
	while finished == False:
		allfinished = True
		for turtleNum in moveOrder:
			turtle = turtles[turtleNum]
			
			current = turtle.pos()[0]
			
			if current < end:
				move = random.randint(min,max)
				distances[turtleNum].append(move)
				turtle.forward(move)
				allfinished = False
				
		finished = allfinished
	
	topTurtles = []
	leastMoves = 9999999999999999
	for counter in range(len(turtles)):
		moves = distances[counter]
		if len(moves) < leastMoves:
			topTurtles = [counter]
			leastMoves = len(moves)
		elif len(moves) == leastMoves:
			topTurtles.append(counter)

	#TODO: If two turtles tie on moves, check the total distance they went. If those are equal, have a tie.
	
	#Double turtle size, move it forward, and have it spin if it won.
	for turtleNum in topTurtles:
		turtle = turtles[turtleNum]
		turtle.shapesize(turtleSize*2, turtleSize*2)
		turtle.speed(1)
		turtle.forward(window_width()/18)
		turtle.right(1080)
		
	
	#Instant replay
	def replay():
		for turtleNum in range(len(turtles)):
			turtle = turtles[turtleNum]
			turtle.speed(0)
			turtle.penup()
			turtle.clear()
			turtle.goto(getLeftBound(), getTurtleY(len(turtles), turtleNum + 0.75))
			
		sleep(1)	
			
		for turtleNum in topTurtles:
			turtle = turtles[turtleNum]
			turtle.shapesize(turtleSize, turtleSize)
			
		
			
	
	sleep(1)
	replay()
	sleep(5)
	
		

		
drawTrack()
raceTurtles()

sleep(10)
