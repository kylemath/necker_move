from psychopy import visual, core, event
import random 

mywin = visual.Window([1280, 800], monitor="testMonitor", units="deg",
						fullscr=True, color= [1,.58,-1])

green = [-1,1,-1]
red = [1,-1,-1]
blue = [-1,-1,1]
black = [-1,-1,-1]

lineWidth = 5 #pixels
squareSize = 3 #edge size (deg)
increment = 1e-2 #movement per frame (deg)
distance = 200 #number of frames out and back

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

#each frame of animation
for i in range(distance):
	
	#out and back
	if i <= distance/2:
		square.pos = (square.pos[0] - increment, 
					  square.pos[1] + increment)
	else:
		square.pos = (square.pos[0] + increment, 
					  square.pos[1] - increment)	

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


#wait for space, save gif and close
#event.waitKeys(keyList="space")
#mywin.saveMovieFrames('necker_move.gif')
mywin.close()