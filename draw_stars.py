# Use turtle module
# Draw picture of stars in the night sky
# The main portion of the lab is to use stars.txt file
# (got to open() and put into 'r')
# first three fields is x y z coordinates given as
# a real number in range [-1, 1]
# fourth field is the star identifier number (not necessary)
# fifth field is the magnitude (brightness) o the star
# sixth filed is the another star identifier (not necessary)
# seventh field is a name identifier for the stars
# need for sure is the x a nd y coordinates and the magnitude
# calculate size of stars in pixels: round(10/(magnitude + 2))
import turtle

screen = turtle.Screen()


def main():
    xion = turtle.Turtle()
    turtle.bgcolor('black')
    turtle.screensize(500, 500)
    turtle.speed(0)
    turtle.tracer(1, 0)

    with open('stars.txt', 'r') as starsFile:
        lines = starsFile.readlines()

    for line in lines:
        lineSplit = line.split()
        x = 250 * float(lineSplit[0])
        y = 250 * float(lineSplit[1])
        starMag = float(lineSplit[4])
        starSize = round(10/(starMag + 2))
        if starSize > 10:
            starSize = 10
        elif starSize < 1:
            starSize = 1
        move(xion, x, y)
        drawWhiteSquare(xion, starSize)


def move(t, x, y):
    t.pu()
    t.goto(x, y)
    t.pd()


def drawWhiteSquare(t, starSize):
    t.color('white')
    t.fillcolor('white')
    t.begin_fill()
    t.fd(starSize)
    t.right(90)
    t.fd(starSize)
    t.right(90)
    t.fd(starSize)
    t.right(90)
    t.fd(starSize)
    t.end_fill()


main()

turtle.Screen().exitonclick()

if __name__ == '__main__':
    main()
