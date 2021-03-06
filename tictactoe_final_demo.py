from os_clear import os_clear_function
from time_function import time_sleep
from writings import starting, made_by, thanking, restart_screen, writing_draw, player_x_winning, player_o_winning, congratulations
from table_printing import table_example, print_table
from variables import tic_tac_toe_table, list_of_player_inputs, possible_player_inputs, possible_player_inputs_for_restart


def user_manual():
    print("\n\n\n\n\n\n\n")
    print("-" * 142)
    print(" " * 65 + "USER MANUAL:\n")
    print(" " * 50 + "1.You will play this game on a 3x3 board.\n")
    print(" " * 27 + "2.You have to choose the numbers between 1 and 9 to be able to enter a correct input.\n")
    print(" " * 15 + "3.The first player who enters his/her name will play with 'X' and the second player is going to play with 'O'.\n")
    print(" " * 63 + "Don\'t cheat! ;)\n")
    print(" " * 58 + "Good luck and have fun! :)")
    print("-" * 142)
    time_sleep(15)
    os_clear_function()
    print(" " * 54 + "This is how the game works.")
    print(" " * 48 + "The sectioning of the numbers look like this.")
    print("\n\n\n\n")
    table_example()
    time_sleep(7)
    os_clear_function()


def user_inputs():   
    list_of_names = []
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    starting_input_1 = str(input("Please, the first player enter his/her name: "))
    list_of_names.append(starting_input_1)
    os_clear_function() 
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    starting_input_2 = str(input("Please, the second player enter his/her name: "))
    list_of_names.append(starting_input_2)
    os_clear_function()
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n")   
    print(" " * 60 + "-" * len(list_of_names[0] + "-" * len(list_of_names[1] + "-" * 14)))
    print(" " * 60 + "{} = X and {} = O.".format(list_of_names[0], list_of_names[1]))
    print(" " * 60 + "-" * len(list_of_names[0] + "-" * len(list_of_names[1] + "-" * 14)))
    time_sleep(4)
    os_clear_function()


def wining_conditions():
    if tic_tac_toe_table[0] == tic_tac_toe_table[1] and tic_tac_toe_table[0] == tic_tac_toe_table[2] and not "_" or\
    tic_tac_toe_table[3] == tic_tac_toe_table[4] and tic_tac_toe_table[3] == tic_tac_toe_table[5] and not "_" or\
    tic_tac_toe_table[6] == tic_tac_toe_table[7] and tic_tac_toe_table[6] == tic_tac_toe_table[8] and not "_" or\
    tic_tac_toe_table[0] == tic_tac_toe_table[5] and tic_tac_toe_table[0] == tic_tac_toe_table[8] and not "_" or\
    tic_tac_toe_table[2] == tic_tac_toe_table[5] and tic_tac_toe_table[2] == tic_tac_toe_table[6] and not "_":
        return True


def player_input_function():
    x_or_o_variable = None
    if len(list_of_player_inputs) % 2 == 0:
        x_or_o_variable = "X"
    elif len(list_of_player_inputs) % 2 != 0:
        x_or_o_variable = "O"
    os_clear_function()
    print_table()
    player_input = input("Please enter your number: ")
    while player_input not in possible_player_inputs:
        os_clear_function()
        print("Invalid input!")
        player_input = input("Please enter your number: ") 
    try:
        tic_tac_toe_table.pop(int(player_input) - 1)
        tic_tac_toe_table.insert(int(player_input) - 1, x_or_o_variable)
        list_of_player_inputs.append(player_input)
    except ValueError:
        print("Invalid input!")     
   

def draw_game_restart_or_exit():
    if len(list_of_player_inputs) == 9:
        time_sleep(2)
        os_clear_function()
        return True


def draw_check():
    writing_draw()
    draw_restart = input("y / n: ")
    while draw_restart not in possible_player_inputs_for_restart:
        draw_restart = input("y / n: ")
        if draw_restart == "y":
            clear_game_for_restart() 
            print_table()
        elif draw_restart == "n":
            break 


def restart_game():
    os_clear_function()
    restart_screen()
    print("\n\n\n\n\n\n\n\n\n")
    restart = input(" " * 67 + "y / n:")
    while restart not in possible_player_inputs_for_restart:
        print("Invalid input. Please enter y or n (case sensitive).")
        restart = input("y / n: ")
        os_clear_function()
        if "y" in possible_player_inputs_for_restart:
            clear_game_for_restart()
            print_table()
            game()
        elif "n" in possible_player_inputs_for_restart:
            thanking()
            time_sleep(3)
            break


def clear_game_for_restart():
    list_of_player_inputs.clear()
    global tic_tac_toe_table
    tic_tac_toe_table = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]


def game():  
    for repetition in range(9): 
        player_input_function()
        if draw_game_restart_or_exit() == True:
            time_sleep(2)
            draw_check()
            break


def main():
    #starting()
    #made_by()
    #user_manual()
    user_inputs()
    game()
    #thanking()


if __name__ == '__main__':
    main()
