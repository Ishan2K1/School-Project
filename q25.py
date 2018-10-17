import os

import time

WIDTH = 79
j=100

message = "noob!".upper()

printedMessage = [ "","","","","","","" ]

characters = { " " : [ " ",
                       " ",
                       " ",
                       " ",
                       " ",
                       " ",
                       " " ],

               "O" : [ "******",
                       "*    *",
                       "*    *",
                       "*    *",
                       "*    *",
                       "*    *",
                       "******" ],
               
               "N" : [ "*     *",
                       "**    *",
                       "* *   *",
                       "*  *  *",
                       "*   * *",
                       "*    **",
                       "*     *" ], 

               "B" : [ "*****",
                       "*   *",
                       "*   *",
                       "***",
                       "*   *",
                       "*   *",
                       "*****" ],

               "L" : [ "******",
                       "*    *",
                       "*    *",
                       "*    *",
                       "*    *",
                       "*    *",
                       "******" ],

               "!" : [ "  *  ",
                       "  *  ",
                       "  *  ",
                       "  *  ",
                       "  *  ",
                       "     ",
                       "  *  " ]
               
               }

#build up the printed banner. to do this, the 1st row of the
#display is created for each character in the message, followed by
#the second line, etc..
for row in range(7):
    for char in message:
        printedMessage[row] += (str(characters[char][row]) + "  ")

#the offset is how far to the right we want to print the message.
#initially, we want to print the message just off the display.
offset = WIDTH
while j!=0:
    os.system("cls")
    #print each line of the message, including the offset.
    for row in range(7):
        print(" " * offset + printedMessage[row][max(0,offset*-1):WIDTH - offset])
    #move the message a little to the left.
    offset -=1
    #if the entire message has moved 'through' the display then
    #start again from the right hand side.
    if offset <= ((len(message)+2)*6) * -1:
        offset = WIDTH
    #take out or change this line to speed up / slow down the display
    time.sleep(0.05)
    j-=1