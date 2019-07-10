#import libraries
import random
import time

#set up global variables
board = ['Go', 'Mediterranean Avenue', 'Baltic Avenue', 'Reading Railroad','Oriental Avenue', 'Jail']
property_info = {'Mediterranean Avenue':{'cost':100,'rent':50,'ownerID':0},'Baltic Avenue':{'cost':150,'rent':60,'ownerID':0}, 'Reading Railroad':{'cost':175,'rent':50,'ownerID':0},'Oriental Avenue':{'cost':200,'rent':75,'ownerID':0}}
player = {'position':0,'money':600,'playerID': 1}
computer = {'position':0,'money':600,'playerID': 2}
game_over = False

#handle players turn
def player_move(player):
    global game_over
    spaces = random.randint(1,6)
    player['position'] = (player['position']+spaces)%len(board)
    print("You landed on {}".format(board[player['position']]))
    if board[player['position']] in property_info:
        if property_info[board[player['position']]]['ownerID'] == 0:
            answer = input("Would you like to buy {}? (y or n)  ".format(board[player['position']]))
            if answer == "y":
                property_info[board[player['position']]]['ownerID'] = player['playerID']
                player['money'] -= property_info[board[player['position']]]['cost']
                print("You bought {}. You now have ${}.".format(board[player['position']], player['money']))
            else:
                print("You passed up a great opportunity :(")
        elif property_info[board[player['position']]]['ownerID'] != player['playerID']:
            player['money'] -= property_info[board[player['position']]]['rent']
            if player['money'] < 0:
                game_over = True
                print("You went bankrupt. The computer wins.")
                return
            print("Rent is ${}. You now have ${}.".format(property_info[board[player['position']]]['rent'], player['money']))
    elif board[player['position']] == 'Go':
        player['money']+= 200
        print("You collected $200. You now have ${}.".format(player['money']))
    elif board[player['position']] == 'Jail':
        print("You're just visiting though.")
    print()

#handle computer's turn
def ai_move(computer):
    global game_over
    spaces = random.randint(1,6)
    computer['position'] = (computer['position']+spaces)%len(board)
    print("The computer landed on {}.".format(board[computer['position']]))
    if board[computer['position']] in property_info:
        if property_info[board[computer['position']]]['ownerID'] == 0:
            if computer['money'] > property_info[board[computer['position']]]['cost']:
                computer['money'] -= property_info[board[computer['position']]]['cost']
                property_info[board[computer['position']]]['ownerID'] = computer['playerID']
                print("The computer bought {}".format(board[computer['position']]))
        elif property_info[board[computer['position']]]['ownerID'] != computer['playerID']:
            player['money'] += property_info[board[computer['position']]]['rent']
            computer['money'] -= property_info[board[computer['position']]]['rent']
            if computer['money'] < 0:
                game_over = True
                print("The computer went bankrupt. You win!");
                return
            print("The computer payed you ${} in rent money and now has ${}. You now have ${}.".format(property_info[board[computer['position']]]['rent'], computer['money'], player['money']))
    elif board[computer['position']] == "Go":
        computer['money']+= 200
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

