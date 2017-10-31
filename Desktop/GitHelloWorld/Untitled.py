Python 3.6.2 (v3.6.2:5fd33b5926, Jul 16 2017, 20:11:06) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.
import turtle
>>> def drawSnake(rad,anglemlen,neckrad):
	for i in range(len):
		turtle.circle(rad,angle)
		turtle.circle(-rad,angle)
	turtle.circle(rad,angle/2)
	turtle.fd(rad)
	turtle.circle(neckrad+1,180)
	turtle.fd(rad*2/3)

	
>>> def main():
	turtle.setup(1300,800,0,0)
	pythonsize = 30
	turtle.pensize(pythonsize)
	turtle.pencolor("blue")
	turtle.seth(-40)
	drawSnake(40,80,5,pythonsize/2)

	
>>> main()
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    main()
  File "<pyshell#17>", line 7, in main
    drawSnake(40,80,5,pythonsize/2)
TypeError: drawSnake() takes 3 positional arguments but 4 were given
>>> main()
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    main()
  File "<pyshell#17>", line 7, in main
    drawSnake(40,80,5,pythonsize/2)
TypeError: drawSnake() takes 3 positional arguments but 4 were given
>>> import turtle
>>> def drawSnake(rad,anglemlen,neckrad):
	for i in range(len):
		turtle.circle(rad,angle)
		turtle.circle(-rad,angle)
	turtle.circle(rad,angle/2)
	turtle.fd(rad)
	turtle.circle(neckrad+1,180)
	turtle.fd(rad*2/3)

	
>>> def main():
	turtle.setup(1300,800,0,0)
	pythonsize = 30
	turtle.pensize(pythonsize)
	turtle.pencolor("blue")
	turtle.seth(-40)
	drawSnake(40,80,5,pythonsize/2)
