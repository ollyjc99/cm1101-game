import os, sys, time
from items import *
from player import *
from gameparser import *
from map import rooms

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

def list_of_items(items):

    s = ""
    for i in range(len(items)):
        s = s + items[i]["name"] + ", "
        print(s)
    return s[:-2]
    print(s)
    if s == 0:
        return None

def print_room_items(room):
	if room["items"] != []:
		print("~ There is " + list_of_items(room["items"]) + " here")

def print_inventory_items(inventory):
    if inventory != []:
        print("~ You have " + list_of_items(inventory),"\n")
        print("Current weight =",current_weight,"\n")

def print_room(room):
    clear()
    print("\n"+room["name"].upper()+"\n")
    print(room["description"]+"\n")

def exit_leads_to(exits, direction):

    return rooms[exits[direction]]["name"]

def print_exit(direction, leads_to):

    print("GO "+ direction.upper()+" to "+ leads_to + ".")

def print_take_items(room):
    for item in current_room["items"]:
        print ("<> "+item["id"])
    print()
    return

def print_drop_items(inventory):
    for item in inventory:
        print("<> "+item["id"])
    print()
    return

def print_menu(exits, room_items, inv_items):
    print_room_items(current_room)
    print_inventory_items(inventory)

    print("You can:")
    for direction in exits:
        print_exit(direction, exit_leads_to(exits, direction))
    print()
    if current_room["items"] != []:
        print("TAKE an item")
    if inv_items != []:
        print("DROP an item")

    print("What do you want to do?")

def is_valid_exit(exits, chosen_exit):
    choice = False
    for exit in exits:
        if exit == chosen_exit:
            choice = True
    return choice

def execute_go(direction):
	global current_room
	if is_valid_exit(current_room["exits"], direction) == True:
		current_room = rooms[current_room["exits"][direction]]
	else:
		print("You cannot go there")

def execute_take(item_id):
    take_item = False
    for i in range(len(current_room["items"])):
        if current_room["items"][i]["id"] == item_id:
            take_item = True
            inventory.append(current_room["items"][i])
            current_room["items"].remove(current_room["items"][i])
            print(item_id, " added to inventory")
            return

    if take_item == False:
        print("You cannot take that.")
        return False

def execute_drop(item_id):
    drop_item = False
    for i in range(len(inventory)):
        if item_id == inventory[i]["id"]:
            drop_item = True
            current_room["items"].append(inventory[i])
            inventory.remove(inventory[i])
            print(item_id + " dropped")
            return True

    if drop_item == False:
        print("You cannot drop that")
        return False

def execute_command(command):
    if 0 == len(command):
        print("")
    if command[0] == "go":

        if len(command) > 1:
            execute_go(command[1])
        else:
            print("Go where?")

    elif command[0] == "take":

        if current_room["items"] != []:
            if len(command) > 1:
                execute_take(command[1])
            else:
                print("\nWhich item would you like to take?\n")
                print_take_items(current_room["items"])
                take_command = menu(current_room["exits"], current_room["items"], inventory)
                execute_take(take_command[0])

        else:
            print("Cannot take that.")

    elif command[0] == "drop":

            if inventory != []:
                if len(command) > 1:
                    execute_drop(command[1])
                else:
                    print("\nWhich item would you like to drop?\n")
                    print_drop_items(inventory)
                    drop_command = menu(current_room["exits"], current_room["items"], inventory)
                    execute_drop(drop_command[0])

            else:
                print("Cannot drop that.")

def menu(exits, room_items, inv_items):

    user_input = input("> ")

    normalised_user_input = normalise_input(user_input)
    return normalised_user_input

def move(exits, direction):

    return rooms[exits[direction]]

def main(gameWon):

    while gameWon == False:
        time.sleep(1.25)
        print_room(current_room)
        print_menu(current_room["exits"], current_room["items"], inventory)
        command = menu(current_room["exits"], current_room["items"], inventory)
        execute_command(command)

if __name__ == "__main__":
    gameWon = False
    main(gameWon)
