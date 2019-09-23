
'''

Convert text-input (i.e. "Hello World!") 
into coordinates for drawing

'''

import turtle

'''
(1) start @ [0,0]
(2) execute 'A' instruction
(2) shift all x-coords rightwards by charSpace*numCharsDrawn
'''

def generateCoordinates(inputText):

	minimumAngle = 70
	maximumAngle = 110
	effectiveRange = maximumAngle - minimumAngle

	# LUT
	charLUT = {
		'spiral': [[80,80], [85,80],[85,100]],
		' ': [[0,0]], #space
		'A': [[0,0], 'P1', [0,10], [10,10], [10,5], [0,5], [10,5], [10,0], 'P0'],					# P0 :: turn off laser
		'B': [[0,0], 'P1', [0,10], [10,10], [10,5], [0,5], [10,5], [10,0], [0,0], 'P0'],			# P1 :: turn ON laser
		'C': [[0,0], 'P1', [0,10], [10,10], [0,10], [0,0], [10,0], 'P0'],
		'D': [[0,0], 'P1', [0,10], [10,10], [10,0], [0,0], 'P0'],
		'E': [[0,0], 'P1', [0,10], [10,10], [0,10], [0,5], [10,5], [0,5], [0,0], [10,0], 'P0'],
		'H': [[0,0], 'P1', [0,10], [0,5], [10,5], [10,10], [10,0], 'P0'],
		'K': [[0,0], 'P1', [0,10], [0,5], [10,10], [0,5], [10,0], 'P0'],
		'M': [[0,0], 'P1', [0,10], [5,10],[5,5],[5,10],[10,10],[10,0], 'P0'],
		'S': [[0,0], 'P1', [10,0], [10,5], [0,5], [0,10], [10,10], 'P0'],
		'T': [[5,0], 'P1', [5,10], [0,10], [10,10], 'P0'],
		'R': [[0,0], 'P1' , [0,10],[10,10],[10,5], [0,5], [10,5], [10,0], 'P0'],
		'N': [[0,0], 'P1', [0,10], [10,0], [10,10], 'P0']
	}


	# return coordinates for drawing inputText
	drawingSequence = []		# append coordinate-data here
	incrementPerChar = 10+4		# space between char-origins
	numCharsDrawn = 0			# counter
	for char in inputText:
		for coord in charLUT[char.upper()]:
			if coord in ['P0','P1']:	# element is a lift/drop flag
				drawingSequence.append(coord)
				continue
			else: # element is coord
				xMax = 10 + len(inputText)*12
				x = (coord[0] + numCharsDrawn*incrementPerChar)/xMax * effectiveRange + minimumAngle
				y = (coord[1]/xMax)*effectiveRange  + minimumAngle
				drawingSequence.append([x,y])
		numCharsDrawn += 1

	return drawingSequence


# Test Generated Coordinates
def turtleTest(coordSequence):

	# create drawing tools
	window = turtle.Screen()
	pencil = turtle.Turtle()
	pencil.penup()

	for coord in coordSequence:
		if coord == 'P1': pencil.pendown()	# put pen on canvas @ start of char
		elif coord == 'P0': pencil.penup()	# lift pen off canvas @ end of char
		else:
			pencil.goto(coord[0]*5-400, coord[1]*5-400)
	window.exitonclick()


# Generate file for serial-transmission to Microcontroller
def writeCoordsToFile(coordSequence):
	# angle = 70 -> 110
	# write coords + newline
	f = open('code.txt', 'w+')
	for coord in coordSequence:
		command = coord
		if coord not in ['P0', 'P1']: 
			command = 'X'+str(coord[0]) + ' Y'+str(coord[1])
		f.write(command+'\n')

	# append 'D' to ensure file is deleted off uC
	f.write('\n')
	f.close()

stairs = [[80,80],'P1', [85,80], [85,85], [90,85],[90,90],[95,90],[95,95], [100,95], [100,100]]
spiral = [[80,80],'P1',[80,100], [100,100], [100,80], [82,80], [82,98], [98,98], [98, 82], [84,82], [84,96], [96,96], [96,84], [86,84], [86,94],[94,94],[94,86],[88,86], [88,92], [92,92], [92,88], [90,88], [90,90]]

hack = generateCoordinates('hack the ndrth')
writeCoordsToFile(hack)
turtleTest(hack)
