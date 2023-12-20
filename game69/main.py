import os
import random

def clear_terminal():
    # Clear terminal screen based on the operating system
    os.system('cls' if os.name == 'nt' else 'clear')

def get_player_choice():
    # Function to get the player's choice
    choice = input("Enter your choice (1-4): ").strip()
    return choice

def update():
    #update 
    variables = []

    with open("data.txt", "r") as file:
        for line in file:
            # Remove newline characters and append each line to the list
            variables.append(line.strip())

    # Now, 'variables' contains the data read from the file
    return variables

def DSTF(damage, damage_type):
    #clear_terminal()
    #print("damage storage turn flop")
    list = update()
    if list[1] == '1':
        #print("christmas")
        #player turn
        #deal damage to enemy and change to enemy turn
        if damage_type == "magic":
            print("magic shield: " + list[8])
            #print(list)
            post_shield = (int(list[8]) - damage)
            if post_shield <= 0:
                print("shield broken")
                print("damage: " + str(abs(post_shield)))
                change_variable(8, int(list[7]) - abs(post_shield))
                change_variable(9, 0)
            else:
                print("shield")
                change_variable(9, post_shield)
        else:
            print("physical shield: " + list[9])
            post_shield = (int(list[9]) - damage)
            if post_shield <= 0:
                print("shield broken")
                print("damage: " + str(abs(post_shield)))
                change_variable(8, int(list[7]) - abs(post_shield))
                change_variable(9, 0)
            else:
                print("shield")
                change_variable(9, post_shield)
        change_variable(2, 0)
        input("Press Enter to continue...")
        clear_terminal()
        basic_loop(int(list[16]))
    else:
        #print("evil christmas")
        #enemy turn 
        #deal damage to enemy and change to player turn
        if damage_type == "magic":
            print("magic shield: " + list[10])
            #print(list)
            post_shield = (int(list[10]) - damage)
            if post_shield <= 0:
                print("shield broken")
                print("damage: " + str(abs(post_shield)))
                change_variable(4, int(list[3]) - abs(post_shield))
                change_variable(11, 0)
            else:
                print("shield")
                change_variable(9, post_shield)
        else:
            print("physical shield: " + list[11])
            post_shield = (int(list[11]) - damage)
            if post_shield <= 0:
                print("shield broken")
                print("damage: " + str(abs(post_shield)))
                change_variable(4, int(list[3]) - abs(post_shield))
                change_variable(12, 0)
            else:
                print("shield")
                change_variable(12, post_shield)
        change_variable(2, 1)
        input("Press Enter to continue...")
        clear_terminal()
        basic_loop(int(list[16]))

def get_random_element(*args):
    if not args:
        return None  # Return None if no arguments are provided

    return random.choice(args)

def change_variable(line_number, new_value):
    # Read all lines from the file
    with open("data.txt", "r") as file:
        lines = file.readlines()

    # Update the specified line with the new value
    lines[line_number - 1] = str(new_value) + "\n"

    # Write the modified lines back to the file
    with open("data.txt", "w") as file:
        file.writelines(lines)

def basicAttack():
    list = update()
    damage = (int(list[2]) * 2) + 5
    #attach tailsman
    if int(list[4]) > 0: 
        print("sigil attached")
        change_variable(5, (int(list[4]) - 1))
        change_variable(18, (int(list[17]) + 1))
    else:
        print("no sigils")
    DSTF(damage, "physical")

def skill(ecode):
    list = update()
    print(list[5])
    #print(list[16])
    skill = input("Enter skill code: ")
    #skill list
    if (skill == '101') and (skill in list[5]):
        if (int(list[17]) > 0):
            print("shock")
            change_variable(18, (int(list[17]) - 1))
            DSTF(10, "magic")
        else:
            print("no sigil attached")
            basic_loop(ecode)
    elif (skill == '102') and (skill in list[5]):
        clear_terminal()
        print(get_random_element("luck of the draw", "shuffle!", "exhilarating gamble"))
        input("")
        clear_terminal()
        change_variable(5, (get_random_element(1, 2, 3)))
        #switch turn without DSTF
        change_variable(2, 0)
        basic_loop(ecode)     
    else:
        #no skill selected
        basic_loop(ecode)

def enemy(ecode):
    if ecode == 301:
        #301 sets stats 
        print("Ose")
        change_variable(8, 40)
        change_variable(13, 10)
        change_variable(14, 100)
        change_variable(15, 1)
        change_variable(16, 0)
        change_variable(17, 302)
        print("the fictional being begins its offensive")
        if get_random_element("desperate flail", "discharge") == "desperate flail":
            #desperate flail
            print("it swings its claws around disorderly")
            DSTF(5, "physical")
        else:
            #discharge
            print("electricity collects around it")
            DSTF(5, "magic")
    elif ecode == 302:
        #302 is in fight
        print("Relentless!")
        if get_random_element("desperate flail", "discharge") == "desperate flail":
            #desperate flail
            print("it swings its claws around disorderly")
            DSTF(5, "physical")
        else:
            #discharge
            print("electricity collects around it")
            DSTF(5, "magic")
    else:
        print("erm")

def basic_loop(ecode):
    list = update()
    if list[1] == '1':
        #player turn
        #display health and tailsman
        print("sigils:", end='')
        for i in range(int(list[4])):
            print('[T] ', end='')
        print()
        print("hp: " + list[3])
        print("1. Skills")
        print("2. Basic attack")
        print("3. Talk")
        print("4. leave")
        choice = get_player_choice()
        if choice == '1':
            skill(ecode)
            #logic

        elif choice == '2':
            basicAttack()
            # Implement defend logic here

        elif choice == '3':
            print("You chose to use an item!")
            # Implement use item logic here

        elif choice == '4':
            print("Exiting the game. Goodbye!")

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
            basic_loop(ecode)
        #input("Press Enter to continue...")
    else:
        print("enemy action")
        #enemy turn
        enemy(ecode)
        #enemy function with enemy code


def main():
#main story text
    paragraphs = [
        "As the protaganist of this game let me introduce myself as a man whos first name is Kaiki",

        """other than that i suppose your primary intrest might be my motivation in being a protaganist
        which i can answer honestly by saying that my main goal is money""", 

        "so lets make this an enjoyable expierance for the both of us"
    ]
#begins the game, game ends when all paragraphs have been read
    for paragraph in paragraphs:
        print(paragraph)
        #print(update())
        input("Press Enter to continue...")
        #increase stage variable 
        clear_terminal()

    current = update()
    #print(current)
    if int(current[0]) == 0:
        print("its time")
        change_variable(1, 1)
        current = update()
    else:
        change_variable(2, 1)
        change_variable(17, 301)
        basic_loop(301)
        
        


if __name__ == "__main__":
    main()
