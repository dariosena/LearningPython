import turtle


def main():
    # This line reads a line of input from the user
    filename = input('Please enter drawing filename: ')

    # Create a Turtle Graphics window to draw in.
    t = turtle.Turtle()
    # The screen is used at the end of the program.
    screen = t.getscreen()

    # reading the file
    file = open(filename, 'r')

    # Process each line of the file
    for line in file:

        # The strip method strips off the newline character at the
        # end of the line and any blanks that might be at the beginning
        # or end of the line
        text = line.strip()

        # splits the text variable into its pieces
        commandList = text.split(',')

        # get the drawing command
        command = commandList[0]

        if command == 'goto':
            x = float(commandList[1])
            y = float(commandList[2])

            width = float(commandList[3])
            color = commandList[4].strip()
            t.width(width)
            t.pencolor(color)
            t.goto(x, y)
        elif command == 'circle':
            radius = float(commandList[1])
            width = float(commandList[2])
            color = commandList[3].strip()
            t.width(width)
            t.pencolor(color)
            t.circle(radius)
        elif command == 'beginfill':
            color = commandList[1].strip()
            t.fillcolor(color)
            t.begin_fill()
        elif command == 'endfill':
            t.end_fill()
        elif command == 'penup':
            t.penup()
        elif command == 'pendown':
            t.pendown()
        else:
            print('Unknown command found in file: {}'.format(command))

    # close the file
    file.close()

    # hide the turtle that we used to draw the picture
    t.ht()

    # this causes the program to hold the turtle graphics window open
    # until the mouse is clicked.
    screen.exitonclick()
    print('Program Execution Completed.')


if __name__ == '__main__':
    main()
