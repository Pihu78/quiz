questions = \
{
    "Who developed python programming language": {
        "A": "Wick van Rossum",
        "B": "Rasmus Lerdorf",
        "C": "Guido van Rossum",
        "D": "Niene Stom",
        },
    "Which type of Programming does Python support?": {
        "A": "object-oriented programming",
        "B": "structured programming",
        "C": "functional programming",
        "D": "all of the mentioned",
    },
    "Which of the following is the correct extension of the Python file?": {
        "A":  ".python",
        "B": ".pl",
        "C": ".py",
        "D": ".p",
    },
    "Which of the following is used to define a block of code in Python language? ": {
        "A": "Indentation",
        "B": " Key",
        "C": "Brackets",
        "D": "All of the mentioned",
    },
    "Which keyword is used for function in Python language?":{
        "A": "Function",
        "B": "def",
        "C": "Fun",
        "D": "Define"

    }
}
print("\nwelcome to the python programming quiz")
prompt = ">>> "
correct_options = ['D', 'C', 'D', 'B', 'A']
score_count = 0

for question, options in questions.items():
    print("\n", question, "\n")
    for option, answer in options.items():
        print(option, ":", answer)
    print("\nWhat's your answer?")
    choice = str(input(prompt))
    for correct_option in correct_options:
        if choice.upper() == correct_option:
            score_count += 1
            print("your score=",score_count)
            if score_count>=3:
                print("congrats")
            else:
                print("fail")


