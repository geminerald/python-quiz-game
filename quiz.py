def show_menu():
    print("\n \nQUIZ GAME \n")
    print("1. Play the quiz")
    print("2. Add New Questions")
    print("3. End Game\n")

    option = input("Enter Option: ")
    return option

def add_question():
    print("")
    question = input("Enter a question: \n> ")
    print ("")
    print("Tell me the answer")
    answer = input("{0}\n> ".format(question))

    file = open("questions.txt" , "a")
    file.write(question + "\n")
    file.write(answer + "\n")
    file.close()

def ask_questions():
    questions = []
    answers = []

    with open("questions.txt", "r") as file:
        lines = file.read().splitlines()
    
    for i, text in enumerate(lines):
        if i % 2 == 0:
            questions.append(text)
        else:
            answers.append(text)
        
    number_of_questions = len(questions)
    questions_and_answers = zip(questions, answers)

    score = 0

    for question, answer in questions_and_answers:
        guess = input(question + "> ")
        if guess == answer:
            score += 1
            print("Correct - your score is {0}".format(score))
        else:
            print("Incorrect")
        
    print("Game Over - You got {0} correct out of {1}".format(score,number_of_questions))

    

def game_loop():
    while True:
        option = show_menu()
        if option == "1":
            ask_questions()
        elif option == "2":
            add_question()
        elif option == "3":
            break
        else:
            print("you have selected an invalid optoin")
        print("")

game_loop()