import re

print(
    "Ener the 2 length of rectangle edges:\n -they must be integers-\n -separate them with comma-\n -example: 12,10 -")
usersEdgesLength = input()
isCorrectUsersEdgesLength = re.match("[1-9][0-9]*,[1-9][0-9]*", usersEdgesLength)

print("Rectangle filled inside:\n -Enter True or False-")
usersFillAnswear = input()
isCorrectUsersFillAnswear = re.match("True|False", usersFillAnswear)


def reToBoolConverter(match_1, match_2):
    if ((match_1 is None) | (match_2 is None)):
        return False
    else:
        return True


def isRectangleFilledChecker(userAnswear):
    if (userAnswear == "True"):
        return True
    else:
        return False


def drawRectangle(edgesTab, isFill):
    edge_a = int(edgesTab[0])
    edge_b = int(edgesTab[1])

    if (isFill == False):
        for index_y in range(edge_b):
            if ((index_y == 0) | (index_y == edge_b - 1)):
                for index_x in range(edge_a):
                    if (index_x == edge_a - 1):
                        print("#")
                    else:
                        print("#", end='')
            else:
                for index_x in range(edge_a):
                    if (index_x == 0):
                        print("#", end='')
                    if ((index_x > 0) & (index_x < edge_a - 1)):
                        print(" ", end='')
                    if (index_x == edge_a - 1):
                        print("#")
    else:
        for index_y in range(edge_b):
            for index_x in range(edge_a):
                if (index_x == edge_a - 1):
                    print("#")
                else:
                    print("#", end='')


if (reToBoolConverter(isCorrectUsersEdgesLength, isCorrectUsersFillAnswear)):
    edgesLengthTab = usersEdgesLength.split(',')
    usersAnswearCheckisFill = isRectangleFilledChecker(usersFillAnswear)
    drawRectangle(edgesLengthTab, usersAnswearCheckisFill)
else:
    print("Datas enterd incorrectly!")
