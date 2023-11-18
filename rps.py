import random
user = input("Enter your choice: ")
computer = random.choice(['rock','paper','scissors'])
print(f'Your choice is {user} and computer choice is {computer}')
if((user == 'rock' and computer == 'scissors') or (user == 'paper' and computer == 'rock') or (user == 'scissors' and computer == 'rock')):
    print("You won")
elif(user == computer):
    print("It's a Tie")
else:
    print("computer won")