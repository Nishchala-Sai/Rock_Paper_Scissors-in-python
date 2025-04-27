import random

print("Player needs 3 points to Win the game.")
player_score, computer_score=0,0
opponent_choices= ["rock", "paper", "scissors"]
i=1

while(player_score !=3 and computer_score!=3):
    chosen= random.choice(opponent_choices)
    user_choice= input("Enter choice: ")
    beaten={"rock":"scissors","paper":"rock","scissors":"paper"}
    if(beaten[user_choice.lower()]==chosen):
        print(f"Player WON this Round{i}")
        player_score+=1
    elif(user_choice.lower()==chosen):
        print(f"Round{i}- DRAW")
    else:
        print(f"Computer Wins Round{i}")
        computer_score+=1
    i+=1
else:
    if(player_score==3):
        print("Player WINS!!!")
    else:
        print("Try again next time...")








