

"""
This program implements a program that handles
the general case of drawing olygons of decreasing
sides,recursively.

The picture can be best seen at sides 6 and 7.
while entering input of 8 as side, the output will take
a bit of more time to generate.
"""

import turtle as t
import time
import math
import sys


def init():
    """
    Initialize for drawing.  (-1500, -1500) is in the lower left and
    (1500, 1500) is in the upper right.
    :pre: pos (0,0), heading (east), up
    :post: pos (0,0), heading (east), up
    :return: None
    """
    t.setworldcoordinates(-1500, -1500, 1500, 1500)
    t.speed(0)
    t.tracer(0, 0)
    t.title('Polygons')
    t.bgcolor("yellow")

def DrawPolygon(sides, length):
    """
     Draws polygon based on the sides and lenth.
     :pre: (relative) pos (0,0), heading (east), up
     :post: (relative) pos (0,0), heading (east), up
     :return: None

     It is an helper function to draw a single polygon
     based on no of sides passed.
     """

    for i in range(sides):
        if ((sides - 1) % 2 == 0):
            t.down()
            t.forward(length)
            t.left(360 / sides)
        else:
            t.forward(length)
            t.right(360 / sides)
    t.up()


def DrawPolygon_rec2(sides,states, length):

    """
     Draws polygon recursively based on the sides and lenth.
     :pre: (relative) pos (0,0), heading (east), up
     :post: (relative) pos (0,0), heading (east), up
     :return: sum - length of all sides

     if sides is less than 0, it returns 0 or else proceed
     with drawing of polygon and returning sum.
     """
    sum = 0
    if(sides<=2):
        return 0
    else:
        """
        Checks if state entered is fill,
        if true it will fill the drawn polygon
        else only polygon will be drawn without
        any filling
        
        it calls helper function DrawPolygon
        """
        if(states=='fill'):
            t.begin_fill()
        DrawPolygon(sides, length)
        t.end_fill()

        """
        for no of sides entered, each time,
        the function will perform a set of statements
        and will call itself recursively with
        sides redcued by 1 and length decreased by
        half of its value
        """

        for i in range (sides):
            t.down()

            """
            if sides entered is an even no, then it will draw 
            the polygon above the respective x - axis that also means
            while calling it recursively it will draw the polygon
            insided the previous polygon
            """

            if((sides-1)%2==0):
                t.color("blue","red")
                if (states == 'fill'):
                    t.begin_fill()
                    t.end_fill()
                t.forward(length)
                t.left(360/sides)
                sum=sum+length

            else:

                """
                if the sides is an odd number, it will
                be drawn below the respective x-axis that is also
                outside of the previously drawn polygon.
                """

                t.color("blue","blue")
                if (states == 'fill'):
                    t.begin_fill()
                t.forward(length)
                t.right(360 / (sides))

                """
                Each time a polygon is drawn its length is added in sum 
                each time a side of the same polygon is drawn
                hence in total it stores the combined length
                obtained by adding all sides for that particular
                polygon
                """

                sum = sum + length

            """
            DrawPolygon_rec2 is call recursively and is added to the previous
            value of sum, hence giving the total sum of all the polygons
            till that time
            
            """
            sum= sum + DrawPolygon_rec2((sides-1),states,length/2)
            t.color("violet", "green")
            t.begin_fill()
            t.circle((length / (2 * (math.tan(180 / 4))))/4)
            t.end_fill()
        t.up()
        t.end_fill()
        return sum


def main():
    """
    Initializes the turtle
    Takes sides and states as system parameters
    which is then passed om to the drawploygon_rec
    method along with length

    checks if the user is entering input only in
    between 3 to 8 for sides and fill/unfill for
    states else prints statement for incorrect
    input

     """


    length = 400
    sum=0
    Finsalsum = 0
    sides= int(sys.argv[1])
    states = sys.argv[2]

    t.up()
    #DrawPolygon_rec(,length)
    init()
    if (sides>=3 and sides<=8) and (states=='fill' or states=='unfill'):
        Finalsum= DrawPolygon_rec2(sides,states,length)
        print()
        print()
        print('******************************************')
        print('Sum: '+ str(Finalsum))
        print('******************************************')

    else:
        print()
        print()
        print('******************************************')
        print('Incorrect Input - please pass value between 3 to 8 for sides and fill or unfill for states')
        print('******************************************')

    #t.exitonclick()
    t.update()
    t.mainloop()


if __name__ == '__main__':
    main()