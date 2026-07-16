import random

def guessing_logic(attempts, limit, best_score):

    actual_attempts = attempts 
    number = random.randint(0,limit)
    while(1):
        try:
            guess = int(input(f"Enter your guess. You have {attempts} attempts left: "))
        except Exception as e:
            print(f"Problem: {e}")
            continue

        if attempts <= 0:
            print("Better Luck next time")
            break
        elif guess == number:
            attempts -= 1
            print(f"Guessed Correctly in {actual_attempts - attempts} attempts")
            if (actual_attempts - attempts) < best_score:
                best_score = (actual_attempts - attempts)
                return best_score
            break
        elif guess > number: 
            print(f"Number is smaller than {guess}")
            attempts -= 1
            
        elif guess < number: 
            print(f"Number is larger than {guess}" )
            attempts -= 1


while(1):
    print("Do you want to play...")
    print("This is a number guessing game where you will have to guess the number. \nYou will be provided 3 Levels. \nLevel 1 will have 10 attempts and range of 0-100. \nLevel 2 will have 10 attempts and range of 0-250. \nLevel 3 will have 10 attempts and range of 0-500. \nLevel 4 will have 15 attempts and range of 0-1000")

    best_score = 20

    try:
        level = int(input("Select a level (type a numper): "))
    except Exception as e:
        print(f"Problem: {e}")

    if level == 1:
        best_score = guessing_logic(10, 100, best_score)
    elif level == 2:
        best_score = guessing_logic(10, 250, best_score)
    elif level == 3:
        best_score = guessing_logic(10, 500, best_score)
    elif level == 4:
        best_score = guessing_logic(15, 1000, best_score)
    
    print(f"Your Best Score is {best_score}")

    permission = input("Do you want to continue playing?\n").strip().lower()
    if permission == "yes":
        continue
    else:
        break
