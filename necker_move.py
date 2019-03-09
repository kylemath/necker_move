from psychopy import visual, core, event

mywin = visual.Window([1280, 800], monitor="testMonitor", units="deg",
						fullscr=True, color= [1,.58,-1])

lineWidth = 5
squareSize = 5
square = visual.Rect(win=mywin, width=squareSize, height=squareSize, 
					fillColor=None,lineColor=[1,-1,-1], lineWidth=lineWidth )
square.pos = (0, 0)
mid_square = visual.Rect(win=mywin, width=squareSize, height=squareSize,
						fillColor=None,lineColor=[-1,-1,1], lineWidth=lineWidth)
mid_square.pow = square.pos

square.draw()
mid_square.draw()
mywin.flip()

increment = 1e-3
for i in range(65):
	offset = i*increment
	square.pos = (square.pos[0] - offset, 
				  square.pos[1] + offset)

	topLeftLine = visual.Line(win=mywin, lineWidth=lineWidth, lineColor=[-1,1,-1])
	topLeftLine.start = [square.pos[0] - squareSize,     square.pos[1] + squareSize]
	topLeftLine.end   = [mid_square.pos[0] - squareSize, mid_square.pos[1] + squareSize]


	square.draw()
	mid_square.draw()
	topLeftLine.draw()

	mywin.flip()
	core.wait(.01)



mywin.flip()


event.waitKeys(keyList="space")
mywin.close()