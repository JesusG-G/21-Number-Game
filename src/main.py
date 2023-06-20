import random

def lose_message(name_player):
     print (f"YOU LOSE {name_player.upper()}!")
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

def start_game_two_or_more_players(first_player, second_player,numbers_list):
    last_number = 0
    checked_list = False
    turn = 1
    print(f"{first_player} is the first to play")
    while True:
        if turn == 1:
            if checked_list == True:
                lose_message(first_player)
            elif last_number == 20:
                lose_message(first_player)
            print(f"Turn of {first_player}")
            turn = 2
        else:
            if checked_list == True:
                lose_message(second_player)
            elif last_number == 20:
                lose_message(second_player)
            print(f"Turn of {second_player}")
            turn = 1
        amount_of_numbers_to_enter = int(input("How much numbers do you want to enter?>"))
        insert_number(amount_of_numbers_to_enter,numbers_list)
        checked_list = check_order(numbers_list)
        last_number = numbers_list[-1]
        print(numbers_entered)
        

if __name__ == "__main__":
    finish_loop = False
    numbers_entered = []
    while finish_loop != True:
        print("Enter 'C' if you want to play versus the computer")
        print("Enter 'P' if you want to play versus another person")
        selectd_option = input("Select a option>").upper()
        match selectd_option:
            case 'C':
                print("versus computer")
                finish_loop = True
            case 'P':
                print("versus another player")
                print("Two playes")
                name_player_1 = input("Please player one enter your name: ")
                name_player_2 = input("Please player two enter your name: ")
                turns = random.randrange(1,3)
                if turns == 1:
                    start_game_two_or_more_players(name_player_1,name_player_2,numbers_entered)                 
                else:
                    start_game_two_or_more_players(name_player_2,name_player_1,numbers_entered)
                finish_loop = True
            case _:
                print("Please enter one of the valid option")

        
        
        


