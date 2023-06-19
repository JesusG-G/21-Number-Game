import random

def lose_message():
     print ("YOU LOSE !")
     print("Better luck next time !")
     exit(0)

def check_order(numbers_entered):
    i = 1
    while i < len(numbers_entered):
        if (numbers_entered[i] - numbers_entered[i-1])!=1:
            print ("You did not input consecutive integers.")
            return True
        i = i + 1
    return False

def insert_number(amount_of_numbers_to_enter,numbers_entered):
    for _ in range(amount_of_numbers_to_enter):
        number = int(input(">"))
        numbers_entered.append(number)

def start_game_two_or_more_players(first_player, second_player,numbers_entered):
    print(f"{first_player} is the first to play")
    while numbers_entered[-1] != 21:
        amount_of_numbers_to_enter = int(input("How much numbers do you want to enter?>"))
        insert_number(amount_of_numbers_to_enter,numbers_entered)
        checked_list = check_order(numbers_entered)
        if checked_list == True:
            lose_message()
        print(numbers_entered)
        print(f"Turn of {second_player}")

if __name__ == "__main__":
    answer = False
    numbers_entered = []
    while answer != True:
        players = input("How many players want to play? >")
        if not players.isnumeric():
            print("Please enter a number.")
        elif int(players) == 0:
            print("The number of playes need to be more than zero")
        elif int(players) > 2:
            print("Please the maximun of players are 2")
        else:
            number_of_players = int(players) 
            answer = True

    if number_of_players == 1:
        print("vs Computer")
    else:
        print("Two or more playes")
        name_player_1 = input("Please player one enter your name: ")
        name_player_2 = input("Please player two enter your name: ")
        turns = 1# random.randrange(1,number_of_players+1)
        if turns == 1:
            start_game_two_or_more_players(name_player_1,name_player_2,numbers_entered)
                                 
        else:
            start_game_two_or_more_players(name_player_2,name_player_1,numbers_entered)
        
        


