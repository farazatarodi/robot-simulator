"""
explanation:
Pretty much a simple program, mosly hardcoded. It works for this situation but of course isn't really logical to expand.
Tested it with pytest and got 100%.
"""


class Robot:
    def __init__(self):
        pass

    def execute(self, inputString):
        # parse the input string
        xStr, yStr, direction, command = inputString.split(' ')
        x, y = int(xStr), int(yStr)

        # created this list to maintain the order of direction while turning.
        # it is a list because I can use the index to calculate the new direction
        dirList = ['NORTH', "EAST", "SOUTH", "WEST"]
        dirIndex = dirList.index(direction)

        # The command can have 3 different characters: R, L, A
        for char in command:
            if char == 'R':
                # just a simple loop back to beginning of the direction list
                if dirIndex == 3:
                    dirIndex = 1
                else:
                    dirIndex += 1

            elif char == 'L':
                # same here but for the end of the list
                if dirIndex == 0:
                    dirIndex = 3
                else:
                    dirIndex -= 1

            # This blocks adds to or removes from coordinates based on the direction
            elif char == 'A':
                if dirIndex == 0:
                    y += 1
                elif dirIndex == 1:
                    x += 1
                elif dirIndex == 2:
                    y -= 1
                elif dirIndex == 3:
                    x -= 1

        # and the fromatted output string
        return '{} {} {}'.format(x, y, dirList[dirIndex])
