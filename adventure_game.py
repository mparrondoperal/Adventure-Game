import time
import random
import sys
items = []
monsters = ['Pirate', 'Troll', 'Vampire', 'Wolf']
bad_people = random.choice(monsters)


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


def valid_input(prompt, option1, option2):
    while True:
        response = input(prompt).lower()
        if option1 in response:
            break
        elif option2 in response:
            break
        else:
            print_pause("Sorry, I don't understand.")
    return response


def play_game():
    global bad_people, items

    items = []
    bad_people = random.choice(monsters)

    intro()
    field(items)


def play_again():
    response = valid_input("Would you like to play again? (y/n).\n", "y", "n")
    if "n" in response:
        print_pause("Come back soon!")
        sys.exit()
    elif "y" in response:
        print_pause("Excellent! Restarting the game ...")
        play_game()


def intro():
    print_pause("You find yourself standing in an open field,"
                "filled with grass and yellow wildflowers..")
    print_pause("Rumor has it that "+(bad_people)+" is somewhere around here,"
                "and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty (but not very effective) "
                "dagger.")


def field(items):
    print_pause("Enter 1 to knock on the door of the house.\n"
                "Enter 2 to peer into the cave.\n"
                "What would you like to do?")
    number = input("(Please enter 1 or 2.)\n")
    if number == '1':
        house(items)
    elif number == '2':
        cave(items)
    else:
        field(items)


def house(items):
    if "sword" in items:
        print_pause("You approach the door of the house.")
        print_pause("You are about to knock when the door opens"
                    "and out steps a "+(bad_people)+".")
        print_pause("Eep! This is the "+(bad_people)+" house!")
        print_pause("The "+(bad_people)+" attacks you!")
        next_move()
    else:
        print_pause("You approach the door of the house.")
        print_pause("You are about to knock when the door opens"
                    "and out steps a "+(bad_people)+".")
        print_pause("Eep! This is the "+(bad_people)+" house!")
        print_pause("The "+(bad_people)+" attacks you!")
        print_pause("You feel a bit under-prepared for this,"
                    "what with only having a tiny dagger.")
        next_move()


def cave(items):
    if "sword" in items:
        print_pause("You peer cautiously into the cave."
                    "You've been here before, and gotten all the good stuff.\n"
                    "It's just an empty cave now.\n"
                    "You walk back out to the field.")
    else:
        print_pause("You peer cautiously into the cave.")
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical Sword of Ogoroth!")
        print_pause("You discard your silly old dagger"
                    "and take the sword with you.")
        print_pause("You walk back out to the field.")
        items.append("sword")
    field(items)


def next_move():
    move = input("Would you like to (1) fight or (2) run away?")
    if move == '1':
        fight(items)
    elif move == '2':
        run_away()
    else:
        next_move()


def fight(items):
    if "sword" in items:
        print_pause("As the "+(bad_people)+" moves to attack,"
                    "you unsheath your new sword.")
        print_pause("The Sword of Ogoroth shines brightly in your hand"
                    "as you brace yourself for the attack.")
        print_pause("But the "+(bad_people)+" takes one look at your"
                    "shiny new toy and runs away!")
        print_pause("You have rid the town of the "+(bad_people)+"."
                    "You are victorious!")
        print_pause("GAME OVER!")
        play_again()
    else:
        print_pause("You do your best...")
        print_pause("but your dagger is no match for the "+(bad_people)+".")
        print_pause("You have been defeated!")
        play_again()


def run_away():
    print_pause("You run back into the field."
                "Luckily, you don't seem to have been followed.")
    field(items)


play_game()
