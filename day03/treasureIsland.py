print('''
*******************************************************************************
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
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

left_right = input(
    "You're at a cross road. Which way do you want to go? Type 'left' or 'right' ").lower()
if left_right == "left":
    swim_wait = input(
        "You've come across a river but notice an ominous creature lurking in the depths. Do you swim across or wait? Type 'swim' or 'wait' ").lower()
    if swim_wait == "wait":
        door = input(
            "You reach an ominous forgotten temple. There are two colored doors. Type 'blue',  'red', or 'yellow' to choose a door. ").lower()
        if door == "yellow":
            print("You found the lost treasure of Shang Ri La! You win!")
        elif door == "red":
            print("You step inside. The door slams shut behind you. Suddenly the room is set ablaze. Your burned by fire. Game Over.")
        elif door == "blue":
            print('''
                         /(  /(
                        /   \/   \\\\
          |\___/|      //||\//|| \\\\
         (,\  /,)\__  // ||// || \\\\ \\
         /     /   /_//  |//  ||  \\\\ \\
        (@_^_@)/    /_   //   ||   \\\\  \\
         W//W_/      /_ //    ||    \\\\   \\
       (//) |         ///     ||     \\\\    \\
     (/ /) _|_ /   )  //      ||      \\\\   __\\
   (// /) '/,_ _ _/  ( ; -.   ||    _ _\\\\.-~        .-~~~^-.
 (( // )) ,-{        _      `-||.-~-.           .~         `.
(( /// ))  '/\      /                 ~-. _ .-~      .-~^-.  \\
(( ///))      `.   {            }                   /      \  \\
 ((/ ))     .----~-.\        \-'                 .~         \  `. \^-.
           ///.----..>    (   \             _ -~             `.  ^-`   ^-_
             ///-._ _ _ _ _ _ _}^ - - - - ~                    ~--_.   .-~
                                                                   /.-~
            ''')
            print("You find yourself trapped inside a room with an enormous blue dragon. You are swiftly swallowed! Game Over.")
        else:
            print("Wrong door. You don't want to know what happened to you. Game Over.")
    else:
        print('''

                 |
                 |
                ,|.
               ,\|/.
             ,' .V. `.
            / .     . \\
           /_`       '_\\
          ,' .:     ;, `.
          |@)|  . .  |(@|
     ,-._ `._';  .  :`_,' _,-.
    '--  `-\ /,-===-.\ /-'  --`
   (----  _|  ||___||  |_  ----)
    `._,-'  \  `-.-'  /  `-._,'
             `-.___,-' 
        
        ''')
        print("You were attacked by a giant man-eating trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")
