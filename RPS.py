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


def who_wins(user_moves,n1,n2):
    u1 = user_moves[0]
    u2 = user_moves[1]
    if u2 == loser[u1]:
        return(n2)
    elif u1 == loser[u2]:
        return(n1)
    else: 
        return("nobody")
    
def get_move(n1,n2):
    user1 = input(n1 + " enter your move: ")
    user2 = input(n2 + " enter your move: ")
    user_moves = [user1,user2]
    return(user_moves)

name1 = input("user1 , enter your name: ")
name2 = input("user2 , enter your name: ")
def game(name1,name2):
    champion = who_wins(get_move(name1,name2),name1,name2)
    print(champion + " wins")
    cont = input("do you want to continue? y/n: ")
    if cont == "y":
        game(name1,name2)

game(name1,name2)

