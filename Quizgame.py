questions=("What is the capital city of Telangana?",
           "What is the capital city of TamilNadu?",
           "What is the capital city of Tripura?",
           "What is the capital city of Nagaland?",
           "What is the capital city of Sikkim?",
           "What is the capital city of Arunachal Pradesh?")

options=(("A. Hyderabad","B. Secunderabad","C. Adilabad","D. Nizamabad"),
         ("A. Chennai","B. Rameswaram","C. Udagamandalam","D. Tiruvananthapuram"),
         ("A. Agartala","B. Gangtok","C. Kohima","D. Itanagar"),
         ("A. Agartala","B. Gangtok","C. Kohima","D. Itanagar"),
         ("A. Agartala","B. Gangtok","C. Kohima","D. Itanagar"),
         ("A. Agartala","B. Gangtok","C. Kohima","D. Itanagar"))
answers=("A","A","A","C","B","D")
guesses = []


def game():
    score = 0
    question_num = 0
    for question in questions:
        print("--------------------------------------------------")
        print(question)
        for option in options[question_num]:
             print(option)
    
        guess = input("Enter (A, B, C, D): ").upper()
        guesses.append(guess)
        if guess == answers[question_num]:
            score += 1
            print("CORRECT")
        else:
            print("INCORRECT!!")
            print(f"{answers[question_num]} is the correct answer")
        question_num += 1
    print("--------------------------------------------------")
    print("            Results                ")
    score = int(score / len(questions) * 100)
    print(f"Your score is: {score}%")

    
game()
print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()


print("Do you want to Play Again?")
ans=int(input("1.Yes  2.No"))


if ans == 1:
    game();
else:
    print("Quiz Ended!!");
