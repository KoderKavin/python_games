import random 

def get_move():
    user_check = int(input("play : "))
    if user_check in range(1,7):
        user = user_check
        choices = [1,2,3,4,5,6]
        comp = random.choice(choices)
        print("computer plays : " + str(comp))
        moves = [user,comp]
        return(moves)
    else : 
        print("invalid move")

def score(moves,b,total):
    user = moves[0]
    comp = moves[1]
    move_dict = {
        "comp": comp,
        "user": user,
    }
    total = total + move_dict[b]
    print("score is " + str(total))
    return(total)

def toss():
    user_ht = input("call: heads/tails: ")
    tosses = ["heads", "tails"]
    toss_r = random.choice(tosses)
    print("toss resulted in : "+ toss_r)
    if user_ht == toss_r:
        user_choice = input("what do you choose: bat/chase : ")
        choice1 = {
            "bat": "user",
            "chase": "comp"
        }
        batsman = choice1[user_choice]
    else: 
        batsman = "comp"
    print(batsman + " is batting")
    return(batsman)

batsman = toss()

def switch_batting(batsman):
    switch = {
        "user": "comp",
        "comp": "user"
    }
    return (switch[batsman])

def inning2(next_batsman,total):
    moves = get_move()
    user = moves[0]
    comp = moves[1]
    new_total = 0
    while user != comp and new_total <= total : 
        new_total = score(moves,next_batsman,new_total)
        if new_total>total: 
            break
        moves = get_move()
        user = moves[0]
        comp = moves[1]
    if new_total>total: 
        winner = next_batsman
    elif new_total== total: 
        winner = "nobody"
        print(next_batsman + " is out")
    elif user == comp: 
        print(next_batsman + " is out")
        winner = batsman
    print(next_batsman + " has scored: "+ str(new_total))
    print(winner + " wins")

def inning1(batsman):
    moves = get_move()
    user = moves[0]
    comp = moves[1]
    total = 0
    while user != comp: 
        if user == comp: 
            break
        total = score(moves,batsman,total)
        moves = get_move()
        user = moves[0]
        comp = moves[1]
        
    print(batsman+ " is out")
    print(batsman + " has scored " + str(total))
    next_batsman = switch_batting(batsman)
    inning2(next_batsman,total)

inning1(batsman)

