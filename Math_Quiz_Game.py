import random
# Function to generate a math 
def generate_question(choice):
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    
    if choice == "addition":
        correct_answer = num1 + num2
        print(f"What is {num1} + {num2}?")
    elif choice == "subtraction":
        correct_answer = num1 - num2
        print(f"What is {num1} - {num2}?")
    elif choice == "multiplication":
        correct_answer = num1 * num2
        print(f"What is {num1} x {num2}?")
    elif choice == "division":
        correct_answer = num1 // num2
        print(f"What is {num1} ÷ {num2}")  

    return correct_answer

# Function for the quiz round
def quiz_round():
    while True:
        choice = input("Choose a type of question (addition/subtraction/multiplication/division): ")
        if choice in ["addition", "subtraction", "multiplication", "division"]:
            break
        else:
            print("Invalid choice, please enter either addition, subtraction, multiplication, division.")

    correct_answer = generate_question(choice)

    attempts = 0
    max_attempts = 2
    while attempts < max_attempts:
        try:
            user_answer = int(input("Your answer: "))
            if user_answer == correct_answer:
                print("Correct!")
                return True
            else:
                attempts += 1
                if attempts < max_attempts:
                    print("Incorrect, try again.")
                else:
                    print(f"Sorry, the correct answer was {correct_answer}.")
                    return False
        except ValueError:
            print("Please enter a valid number.")

# Main game loop
def math_quiz():
    score = 0
    rounds = 3

    print("Welcome to the Math Quiz Game!")

    for i in range(rounds):
        print(f"\nRound {i + 1}")
        if quiz_round():
            score += 1

    print(f"\nGame Over! Your final score is: {score}/{rounds}, Thanks for playing this game!")

# Run the game
math_quiz()