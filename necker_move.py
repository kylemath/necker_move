from psychopy import visual, core, event
import random 

mywin = visual.Window([1280, 800], monitor="testMonitor", units="deg",
						fullscr=True, color= [1,.58,-1])

green = [-1,1,-1]
red = [1,-1,-1]
blue = [-1,-1,1]
black = [-1,-1,-1]

lineWidth = 5
squareSize = 3
square = visual.ShapeStim(win=mywin, units="deg", vertices = [[0-squareSize, 0-squareSize],
											[0-squareSize, 0+squareSize],
											[0+squareSize, 0+squareSize],
											[0+squareSize, 0-squareSize]], 
					fillColor=None,lineColor=black, lineWidth=lineWidth )
square.pos = (0, 0)
mid_square = visual.ShapeStim(win=mywin, units="deg", vertices = [[0-squareSize, 0-squareSize],
											[0-squareSize, 0+squareSize],
											[0+squareSize, 0+squareSize],
											[0+squareSize, 0-squareSize]], 
						fillColor=None,lineColor=black, lineWidth=lineWidth)
mid_square.pos = square.pos

topLeftLine = visual.Line(win=mywin, lineWidth=lineWidth, lineColor=black)
topRightLine = visual.Line(win=mywin, lineWidth=lineWidth, lineColor=black)
botLeftLine = visual.Line(win=mywin, lineWidth=lineWidth, lineColor=black)
botRightLine = visual.Line(win=mywin, lineWidth=lineWidth, lineColor=black)

topLeftLine.end   =  [mid_square.pos[0] - squareSize, mid_square.pos[1] + squareSize]
topRightLine.end   = [mid_square.pos[0] + squareSize, mid_square.pos[1] + squareSize]
botLeftLine.end	  =  [mid_square.pos[0] - squareSize,	mid_square.pos[1] - squareSize]
botRightLine.end   = [mid_square.pos[0] + squareSize, 	mid_square.pos[1] - squareSize]


square.draw()
mid_square.draw()
mywin.flip()
mywin.getMovieFrame()

increment = 1e-3
delay = 1e-3
distance = 70


for j in range(2):

	square.pos = (0, 0)
	mid_square.pos = (0, 0)

	for i in range(distance):

		offset = i*increment

		square.pos = (square.pos[0] - offset, 
					  square.pos[1] + offset)

		topLeftLine.start =  [square.pos[0] - squareSize,      	square.pos[1] + squareSize]
		topRightLine.start = [square.pos[0] + squareSize, 		square.pos[1] + squareSize]
		botLeftLine.start =  [square.pos[0] - squareSize, 		square.pos[1] - squareSize]
		botRightLine.start = [square.pos[0] + squareSize, 		square.pos[1] - squareSize]

		square.draw()
		topLeftLine.draw()
		topRightLine.draw()
		botLeftLine.draw()
		botRightLine.draw()
		mid_square.draw()

		mywin.flip()
		mywin.getMovieFrame()

		core.wait(delay)

	for i in range(distance):

		offset = i*increment

		square.pos = (square.pos[0] + offset, 
					  square.pos[1] - offset)


		topLeftLine.start =  [square.pos[0] - squareSize,      	square.pos[1] + squareSize]
		topRightLine.start = [square.pos[0] + squareSize, 		square.pos[1] + squareSize]
		botLeftLine.start =  [square.pos[0] - squareSize, 		square.pos[1] - squareSize]
		botRightLine.start = [square.pos[0] + squareSize, 		square.pos[1] - squareSize]

		square.draw()
		topLeftLine.draw()
		topRightLine.draw()
		botLeftLine.draw()
		botRightLine.draw()
		mid_square.draw()

		mywin.flip()
		mywin.getMovieFrame()
		core.wait(delay)

event.waitKeys(keyList="space")
mywin.saveMovieFrames('necker_move.gif')
mywin.close()