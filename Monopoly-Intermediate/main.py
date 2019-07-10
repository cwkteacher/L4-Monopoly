#import libraries
import random
import time
from monopoly_classes import *

#set up global variables
board = [Space('Go'), Property('Mediterranean Avenue', 100,50), Property('Baltic Avenue',150,60), Property('Reading Railroad',175,50),Property('Oriental Avenue',200,75), Space('Jail')]
player = Player('player')
computer = Player('computer')
game_over = False

#handle players turn
def player_move(player):
    global game_over
    spaces = random.randint(1,6)
    player.position = (player.position+spaces)%len(board)
    print("You rolled a {} and landed on {}".format(spaces,board[player.position].name))
    if type(board[player.position]) is Property:
        if board[player.position].owner == 'none':
            answer = input("You have ${}. Would you like to buy {} for ${}? (y or n)  ".format(player.money,board[player.position].name,board[player.position].cost))
            if answer == "y":
                board[player.position].owner = player.name
                player.money -= board[player.position].cost
                print("You bought {}. You now have ${}.".format(board[player.position].name, player.money))
            else:
                print("You passed up a great opportunity :(")
        elif board[player.position].owner != player.name:
            player.money -= board[player.position].rent
            computer.money += board[player.position].rent
            if player.money < 0:
                game_over = True
                print("You went bankrupt. The computer wins.")
                return
            print("Rent is ${}. You now have ${}.".format(board[player.position].rent, player.money))
    elif board[player.position].name == 'Go':
        player.money+= 200
        print("You collected $200. You now have ${}.".format(player.money))
    elif board[player.position].name == 'Jail':
        print("You're just visiting though.")
    print()

#handle computer's turn
def ai_move(computer):
    global game_over
    spaces = random.randint(1,6)
    computer.position = (computer.position+spaces)%len(board)
    print("The computer rolled a {} landed on {}.".format(spaces, board[computer.position].name))
    if type(board[computer.position]) is Property:
        if board[computer.position].owner == 'none':
            if computer.money > board[computer.position].cost:
                computer.money -= board[computer.position].cost
                board[computer.position].owner = computer.name
                print("The computer bought {} for ${} and now has ${}.".format(board[computer.position].name, board[computer.position].cost, computer.money))
        elif board[computer.position].owner != computer.name:
            player.money += board[computer.position].rent
            computer.money -= board[computer.position].rent
            if computer.money < 0:
                game_over = True
                print("The computer went bankrupt. You win!");
                return
            print("The computer payed you ${} in rent money and now has ${}. You now have ${}.".format(board[computer.position].rent, computer.money, player.money))
    elif board[computer.position].name == "Go":
        computer.money+= 200
    print()
    
#main method, alternates between player and computer turns
def main():
    print("Welcome to Monopoly\n")
    while not game_over:
        input("press enter to continue:")
        print()
        player_move(player)
        if game_over:
            break
        time.sleep(.5)
        ai_move(computer)
        time.sleep(.5)

if __name__ == '__main__':
    main()
