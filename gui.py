from tkinter import *
import os
	
#A simple GUI to start the Turtle Races.
	
window = Tk()
 
window.title("Tucker's Turtle Race Creator")

window.geometry('1200x800')
 

rowNum = 0


title = Label(window, text="Tucker's Turtle Race Creator", font=("Arial Bold", 30))
title.grid(column=0, row=rowNum)


rowNum += 1
title = Label(window, text="Competitors: ", font=("Arial Bold", 22))
title.grid(column=0, row=rowNum)


rowNum += 1
turtleCountText = Label(window, text="Number of Turtles (Default: 8): ", font=("Arial Bold", 15))
turtleCountText.grid(column=0, row=rowNum)
	
turtleCountBox = Entry(window,width=10,font=("Arial Bold", 14))
turtleCountBox.grid(column=1, row=rowNum)
 

	
	
	
rowNum += 1
turtleSizeText = Label(window, text="Size of Turtles (Default: 5): ", font=("Arial Bold", 15))
turtleSizeText.grid(column=0, row=rowNum)
	
turtleSizeBox = Entry(window,width=10,font=("Arial Bold", 14))
turtleSizeBox.grid(column=1, row=rowNum)



rowNum += 1
title = Label(window, text="Track: ", font=("Arial Bold", 22))
title.grid(column=0, row=rowNum)


rowNum += 1
lineCountText = Label(window, text="Line Count (Default: 20): ", font=("Arial Bold", 15))
lineCountText.grid(column=0, row=rowNum)
	
lineCountBox = Entry(window,width=10,font=("Arial Bold", 14))
lineCountBox.grid(column=1, row=rowNum)



rowNum += 1
slowDownText = Label(window, text="Instant Replay Camera Slow Down (Default: 2): ", font=("Arial Bold", 15))
slowDownText.grid(column=0, row=rowNum)
	
slowDownBox = Entry(window,width=10,font=("Arial Bold", 14))
slowDownBox.grid(column=1, row=rowNum)


rowNum += 1
title = Label(window, text="Accessibility & User Preference: ", font=("Arial Bold", 22))
title.grid(column=0, row=rowNum)


rowNum += 1
darkMode = IntVar()
darkModeBox = BooleanVar()
darkModeBox.set(False) #set check state
darkModeBox = Checkbutton(window, text='Dark Mode ', var=darkMode, font=("Arial Bold", 22))
darkModeBox.grid(column=0, row=rowNum)

	
def clicked():
	
	command = "python3 turtles.py "
	
	print(turtleCountBox.get())
	
	if turtleCountBox.get():
		command += "--turtleCount " + turtleCountBox.get() + " "
		
	if turtleSizeBox.get():
		command += "--turtleSize " + turtleSizeBox.get() + " "
		
	if lineCountBox.get():
		command += "--lineCount " + lineCountBox.get() + " "
		
	if slowDownBox.get():
		command += "--replaySlowDown " + slowDownBox.get() + " "
		
	if darkMode.get():
		command += "--darkMode "

	print(command)
	#os.system(python3 turtles.py --turtleCount 11 --turtleSize 5 --darkMode --lineCount 20 --replaySlowDown 2
	os.system(command)
	return


rowNum += 1
btn = Button(window, text="Start Race", command=clicked, font=("Arial Bold", 30))
btn.grid(column=0, row=rowNum)
 
window.mainloop()




