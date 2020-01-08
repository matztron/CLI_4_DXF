import ezdxf

doc = ezdxf.new('R2010')  # create a new DXF R2010 drawing, official DXF version name: 'AC1024'

#Specify units
#see https://ezdxf.readthedocs.io/en/master/howto.html for the other options
doc.header['$MEASUREMENT'] = 1 # 1 = metric
doc.header['$AUNITS'] = 0 #  0 = Decimal degrees (for angles)
doc.header['$INSUNITS'] = 4 # 4 = Millimeters

msp = doc.modelspace()  # add new entities to the modelspace
msp.add_line((0, 0), (10, 0))  # add a LINE entity

defaultSavename = "unnamed"

def greetUser():
    print("-----------------------------")
    print("Simple DXF")
    print("Create simple dxf files in command line")
    print("COMMANDS:")
    print("LINE x1 y1 x2 y2")
    print("    x1: x-axis pos of first point")
    print("    y1: y-axis pos of first point")
    print("    x2: x-axis pos of second point")
    print("    y2: y-axis pos of second point")

    print("CIRCLE x1 y1 r")
    print("x1&x2: pos of circle middle")
    print("    r: radiua of circle")

    print("RECTANGLE x1 y1 x2 y2")
    print("            +---+ <- (x2,y2)")
    print("            |   |")
    print(" (x1,y1) -> +---+")

    print("SAVE optional(name)")
    print("    default savename is 'unnamed'")
    print("EXIT")
    print("-----------------------------")

def plotWork(factor, unit):
    print("one * represents " + str(factor) + " " + unit)
    #here is where the plotting happens

def saveWork(name):
    # Save DXF document.
    doc.saveas(name + ".dxf")

def drawLine(x1,y1, x2,y2):
    msp.add_line((x1, y1), (x2, y2))  # add a LINE entity

cmd = ""
while cmd != "EXIT":
    #get next command
    cmd = input("€:")

    #get first word in string
    words = cmd.split(' ')
    if words[0] == "EXIT":
        print("bye!")

    elif words[0] == "SAVE":  
        if len(words)  == 2:
            if words[1] is not None:
                saveWork(words[1])
        else:
            saveWork(defaultSavename)

    elif words[0] == "HELP":
        greetUser()

    elif words[0] == "LINE":  
        if len(words) == 5:
            drawLine(int(words[1]), int(words[2]), int(words[3]), int(words[4]))

            plotWork(1,"mm")
        else:
            print("Error: You provided " + str(len(words)) + " words. But 5 words are expected. Insert HELP for more.")

    elif words[0] == "RECTANGLE":  
        if len(words) == 5:
            #          2.
            # (x1,y2)+---+(x2,y2)
            #    3.  |   |  4.
            # (x1,y1)+---+(x2,y1)
            #          1.

            #1.
            drawLine(int(words[1]), int(words[2]), int(words[3]), int(words[2]))
            #2.
            drawLine(int(words[1]), int(words[4]), int(words[3]), int(words[4]))
            #3.
            drawLine(int(words[1]), int(words[2]), int(words[1]), int(words[4]))
            #4.
            drawLine(int(words[3]), int(words[2]), int(words[3]), int(words[4]))

            plotWork(1,"mm")
        else:
            print("Error: You provided " + str(len(words)) + " words. But 5 words are expected. Insert HELP for more.")

    elif words[0] == "CIRCLE":  
        if len(words) == 4:
            msp.add_circle((int(words[1]), int(words[2])), int(words[3]))

            plotWork(1,"mm")
        else:
            print("Error: You provided " + str(len(words)) + " words. But 5 words are expected. Insert HELP for more.")
