print("Welcome to the Quiz Game!")
print("You have 5 chances to answer the questions correctly.")


choice = input("Do you want to play the game? (yes/no): ").lower()
if choice == "yes":
    print("Let's start the game!")
else:
    print("Goodbye!")
    exit()

questions = {
    "What is the capital city of Turkey": "Ankara",
    "Which team won the FIFA World Cup in 2022": "Argentina",
    "What is the largest planet in our solar system": "Jupiter",
    "What is the chemical symbol for silver": "Ag",
    "Which NBA team has the most championships": "Boston Celtics",
}

score = 0
deneme = 5

#item ile questions dictionary'ını döngüye alıyoruz.
#item ile hem key hem de value'yu alıyoruz. burda key sorular , value cevaplar oluyor.
for question, answer in questions.items():
    print(question)
    while deneme > 0:
        user_answer = input("Your answer: ")
        if user_answer.lower() == answer.lower():
            print("Correct!")
            score += 1
            break
        else:
            deneme -= 1
            print(f"Wrong! You have {deneme} chances left.")
    if deneme == 0:
        print(f"The correct answer is: {answer}")
        break
    print(f"Your current score is: {score}")