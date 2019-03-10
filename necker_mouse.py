from psychopy import visual, event

mywin = visual.Window([400, 400], monitor="testMonitor", units="deg",
						color= [1,.58,-1])
mywin.mouseVisible = False
mouse = event.Mouse(win=mywin,newPos=[0,0],visible=False)

black = [-1,-1,-1]

lineWidth = 5 #pixels
squareSize = 3 #edge size (deg)

#create square that stays in middle
square = visual.ShapeStim(win=mywin, units="deg", vertices = [[0-squareSize, 0-squareSize],
											[0-squareSize, 0+squareSize],
											[0+squareSize, 0+squareSize],
											[0+squareSize, 0-squareSize]], 
					fillColor=None,lineColor=black, lineWidth=lineWidth )
square.pos = (0, 0)

#create square that moves in same place
mid_square = visual.ShapeStim(win=mywin, units="deg", vertices = [[0-squareSize, 0-squareSize],
											[0-squareSize, 0+squareSize],
											[0+squareSize, 0+squareSize],
											[0+squareSize, 0-squareSize]], 
						fillColor=None,lineColor=black, lineWidth=lineWidth)
mid_square.pos = square.pos

#lines joining squares
topLeftLine = visual.Line(win=mywin, lineWidth=lineWidth, lineColor=black)
topRightLine = visual.Line(win=mywin, lineWidth=lineWidth, lineColor=black)
botLeftLine = visual.Line(win=mywin, lineWidth=lineWidth, lineColor=black)
botRightLine = visual.Line(win=mywin, lineWidth=lineWidth, lineColor=black)

#one end of the lines stays the same
topLeftLine.end   =  [mid_square.pos[0] - squareSize, mid_square.pos[1] + squareSize]
topRightLine.end   = [mid_square.pos[0] + squareSize, mid_square.pos[1] + squareSize]
botLeftLine.end	  =  [mid_square.pos[0] - squareSize,	mid_square.pos[1] - squareSize]
botRightLine.end   = [mid_square.pos[0] + squareSize, 	mid_square.pos[1] - squareSize]

#draw first frame
square.draw()
mid_square.draw()
mywin.flip()
mywin.getMovieFrame()

while True:
	
	square.pos = mouse.getPos()

	#connecting lines change
	topLeftLine.start =  [square.pos[0] - squareSize,      	square.pos[1] + squareSize]
	topRightLine.start = [square.pos[0] + squareSize, 		square.pos[1] + squareSize]
	botLeftLine.start =  [square.pos[0] - squareSize, 		square.pos[1] - squareSize]
	botRightLine.start = [square.pos[0] + squareSize, 		square.pos[1] - squareSize]

	#Draw it all
	square.draw()
	topLeftLine.draw()
	topRightLine.draw()
	botLeftLine.draw()
	botRightLine.draw()
	mid_square.draw()
	
	#flip, save frame for gif, and wait
	mywin.flip()
	mywin.getMovieFrame()

	keys = event.getKeys()
	if keys:
		if keys[0] == 'q':
			break

#save gif and close
#mywin.saveMovieFrames('necker_move_mouse.gif')
mywin.mouseVisible = True
mywin.close()