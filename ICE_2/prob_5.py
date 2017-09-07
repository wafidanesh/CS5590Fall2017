heightinp = int(input("Enter the height of the board: "))
widthinp= int(input("Enter the width of the board: "))

dashes = " --- "
bars = " |  |"

def board_draw(heightinp,widthinp):
    for i in list(range(heightinp)):
        print(dashes*heightinp)
        print(bars*widthinp)

board_draw(heightinp,widthinp)