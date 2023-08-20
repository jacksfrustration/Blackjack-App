import random
logo='''
888     888                888       d8b                888      
888     888                888       Y8P                888      
888     888                888                          888      
88888b. 888 8888b.  .d8888b888  888 8888 8888b.  .d8888b888  888 
888 "88b888    "88bd88P"   888 .88P "888    "88bd88P"   888 .88P 
888  888888.d888888888     888888K   888.d888888888     888888K  
888 d88P888888  888Y88b.   888 "88b  888888  888Y88b.   888 "88b 
88888P" 888"Y888888 "Y8888P888  888  888"Y888888 "Y8888P888  888 
                                     888                         
                                    d88P                         
                                  888P"                          
'''
cards=[1,2,3,4,5,6,7,8,9,10,10,10,10,11]
def check_ace(user):
    '''checks if sum of user cards is over
    or equal to 21 and if there is an 11 inside in
    order to change the ace to a value of 1'''
    return 11 in user and sum(user)>=21
profit=0
user_cards=[]
comp_cards=[]
playing=True
play = input("Do you want to play?\n")

while playing:
    #generate the two user and computer cards
    for x in range(0, 2):
        user_cards.append(random.choice(cards))
        comp_cards.append(random.choice(cards))
    print(logo)
    #check if player wants to keep playing
    if play=="y" or play=="ye" or play=="yes":
        keep_going=True
        #choose how much you would like to bet
        bet=float(input(f"How much would you like to bet?\n£"))
        print(f"User Cards: {user_cards}\n"
              f"Computer Cards: -,-\n")
    elif play=="n" or play=="no":
        #stops the loop
        playing=False
    else:
        #if the answer is not yes or no break out of the while loop in order to restart the program
        print(f"{play} is not an option.\nRestarting program!!")
        break
    while keep_going:
        if check_ace(user_cards):
            user_cards.remove(11)
            user_cards.append(1)
        if sum(user_cards)>21:
            #check to see if sum of user cards is a bust
            print(f"You had a total score of {sum(user_cards)}"
                      f"\nYou bust!!\nYou lose £{bet}!!\n")
            profit-=bet
            #empty lists
            user_cards=[]
            comp_cards=[]
            break
        if sum(comp_cards)>21:
            #check to see if computer is a bust
            profit+=bet
            print(f"Computer busts\n. You win!!"
                      f"Your bet of {bet} is matched.\n"
                      f"You have made £{profit}\n")
            #empty lists
            user_cards = []
            comp_cards = []
            break
        hit = input("Would you like another card?\nType 'yes' or 'no'\n"
                    "Program will keep dealing until 'no' is pressed").lower()
        #check to see if player wants more cards and keeps looping until the input is no or n
        while hit!="no":
            user_cards.append(random.choice(cards))
            print(f"User Cards {user_cards[0:2]}")
            hit = input("Would you like another card?\nType 'yes' or 'no'\n"
                        "Program will keep dealing until 'no' is pressed").lower()

        if sum(user_cards)>sum(comp_cards) and sum(user_cards)<=21:
            #checks to see if user won. If yes profit is added according the the bet amount and empties lists
            profit+=bet
            print(f"You win\n"
                f"You had a total of {sum(user_cards)}\n"
                f"Computer had {sum(comp_cards)}\n"
                f"You won!!")
            user_cards = []
            comp_cards = []

        elif sum(comp_cards)>sum(user_cards) and sum(comp_cards)<=21:
            #check to see if computer won. Subtracts bet from profit and empties lists
            profit-=bet
            print(f"You lost.\n"
                f"You had a total of {sum(user_cards)}\n"
                f"Computer had {sum(comp_cards)}\n")

            user_cards = []
            comp_cards = []

        elif sum(user_cards)==sum(comp_cards):
            #check to see if result is push and empties lists
            print(f"You and computer both had {sum(user_cards)}\n"
                              f"It is a push\n")
            user_cards = []
            comp_cards = []

        elif sum(user_cards)>21:
            profit-=bet
            print(f"You bust!!\n"
                  f"You had a total of {sum(user_cards)}\n"
                  f"You lose!!")
            user_cards=[]
            comp_cards=[]




        if profit<0:
            #if profit is less than 0 it assignes the amount to an 'owe' variable and loops until debt is paid
            owe=round(profit,2)
            while owe<0:
                payment=float(input(f"You owe {owe*-1}0.\n"
                                          f"How much would you like to pay?\n£"))
                payment=round(payment,2)
                owe += payment
                if owe==0:
                    profit=0
                elif owe>0:
                    profit = owe


        stop = input(f"You have made a profit of £{profit}0 today.\n "
                             f"Would you like to keep playing?\n").lower()

        if stop=="y"  or stop=="ye" or stop=="yes":
            break
        elif stop=="n" or stop=='no':
            playing=False
            if profit>0:
                print(f"You have made £{profit}0!!\nHave a good day!!")
            break
        else:
            print("Not valid response.\nThe game will keep going until further notice")
            break
