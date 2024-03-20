import random
loser = {
        "rock": "paper",
        "paper": "scissor",
        "scissor": "rock"
    }
winner = {
        "paper": "rock",
        "rock" : "scissor",
        "scissor" : "paper"
    }


def who_wins(user_moves):
    u1 = user_moves[0]
    u2 = user_moves[1]
    if u2 == loser[u1]:
        return("computer")
    elif u1 == loser[u2]:
        return("user")
    else: 
        return("nobody")
    
def get_move():
    user1 = input("enter your move: ")
    choices = ["rock","paper","scissor"]
    user2 = random.choice(choices)
    print("computer plays: " + user2)
    user_moves = [user1,user2]
    return(user_moves)
def game():
    champion = who_wins(get_move())
    print(champion + " wins")
    cont = input("do you want to continue? y/n: ")
    if cont == "y":
        game()

game()

