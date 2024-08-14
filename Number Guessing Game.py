import art,random
def guess_again(user, computer):
    response = ""
    if user > computer:
        response = "Too high"
        return response
    elif user < computer:
        response = "Too low"
        return response

def easy_mode():
    computer_num = random.choice(range(1,101))
    guesses = 10
    while guesses > 0:
        print(f"You have {guesses} left")
        user_guess = int(input("Guess a number: \n"))
        if user_guess == computer_num:
            return "You win!"
        else:
            print(guess_again(user_guess, computer_num))
            guesses -= 1
    if guesses == 0:
        print("You lose!")
        
def hard_mode():
    computer_num = random.choice(range(1,101))
    guesses = 5
    while guesses > 0:
        print(f"You have {guesses} left")
        user_guess = int(input("Guess a number: \n"))
        if user_guess == computer_num:
            return "You win!"
        else:
            print(guess_again(user_guess, computer_num))
            guesses -= 1
    if guesses == 0:
        print("You lose!")

#ask user for if hard mode or easy mode
print(art.logo1)
print("Welcome to the number guessing game!")
print("You will guess a number from 1 to 100")
selected_difficulty = input("Type 'easy' or 'hard' mode:\n").lower()
# adjust game for selected difficulty
if selected_difficulty == 'easy':
    easy_mode()
elif selected_difficulty == 'hard':
    hard_mode()
