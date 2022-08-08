print('''**********************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')

print("Welcome To Treasure Island! Try to find the treasure. Good luck!!!!!")
print("As soon as you start looking for treasure, a fork in the road appears!")

direction = input("Which way should you go? Left or right?  ")

if direction.lower() == "left":
    print("You come across a stream while following the path!")
    stream = input("Do you want to wait or swim across? w or s? ")
    if stream.lower() == "w":
        print("Finally! A boat comes. You climbed aboard and you ended up at two different doors.")
        place = input("Which door do you pick? door one or door two?  ")
        if place.lower() == "door one":
            print("You did it! You found the treasure!")
        else:
            print("The door led you to a place full of lions. Game over!")
    else:
        print("You drowned wile swimming across. Game over!")
else:
    print("You fell into a ditch. Game over!")
