# Simple quiz Game

name =  input("Please enter your name: ")
print(f"Hey {name}! Welcome to the quiz")

while True:

    questions = [
        "What is 2 + 2?",
        "What is the capital of France?",
        "What year was Liverpool football club founded?",
    ]

    options = [
        ["A) 1", "B) 7", "C) 4"],
        ["A) London", "B) Paris", "C) Sydney"],
        ["A) 1895", "B) 1892", "C) 1905"]
    ]

    answers = ["C", "B", "B"]

    score = 0
    total = len(questions)

    for i in range(total):
        print(f"\nQuestion {i+1}: {questions[i]}")
        for opt in options[i]:
            print(opt)
        while True:
            user_answer = input("Please enter either 'A', 'B' or 'C': ").upper()
            if user_answer in ["A", "B", "C"]:
                break
            print("Invalid input. Please enter 'A', 'B' or 'C'")
        if user_answer == answers[i]:
                score += 1
                print("Congratulations! That is correct")
        else:
            print(f"Incorrect. The correct answer was: {answers[i]}")

    percent = score / total * 100
    print(f"\n{name}, Your score was {score}/{total}, ({score/total*100:.1f}%)")
    if percent == 100:
        print("Congrats! You got a perfect score")
    elif percent >= 70:
        print("Great job! That's a solid performance")
    else:
        print("Better luck next time..")
        
    replay = input("\nWould you like to play again? Enter 'Y' or 'N': ").upper()
    if replay != 'Y':
        print(f"Goodbye {name}!")
        break








