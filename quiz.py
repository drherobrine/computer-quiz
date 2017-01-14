import time

rightAnswers = 0
qnumber = 0

def ask(q, goodAnsN, badAns1N, badAns2N, goodAns, badAns1, badAns2):
    global qnumber
    qnumber += 1
    global rightAnswers
    print(q + "\n\n")
    if goodAnsN == 1:
        print("1." + goodAns)

    if badAns1N == 1:
        print("1." + badAns1)

    if badAns2N == 1:
        print("1." + badAns2)

    if goodAnsN == 2:
        print("2." + goodAns)

    if badAns1N == 2:
        print("2." + badAns1)

    if badAns2N == 2:
        print("2." + badAns2)

    if goodAnsN == 3:
        print("3." + goodAns)

    if badAns1N == 3:
        print("3." + badAns1)

    if badAns2N == 3:
        print("3." + badAns2)

    answer = int(input("Type the number of the answer (without the full stop at the end) you think is correct "))
    if answer == goodAnsN:
        print("Correct!")
        rightAnswers += 1
    else:
        print("Sorry, you're wrong")
    time.sleep(1)
    print("\n" * 45)

ask("How many bytes in a kilobyte?", 2, 1, 3, "1024", "1000", "999")
ask("What do you call one digit of a byte?", 1, 3, 2, "Bit", "1/8 of a byte", "Bytelet")
ask("How do you import a package in Java?", 2, 3, 1, "import <package name>.<class name>; OR package <package name>;", "import <package name>;", "import <package name>.<class name> OR package <package name>")
ask("What are the 3 main OSs?", 3, 1, 2, "Linux, macOS, Windows", "Sierra, El Capitan, Yosemite", "Windows 7, Windows 8, Windows 10")
ask("What are the 2 kinds of loops in Python?", 1, 2, 3, "for, while", "Repeat n times, infinite loop", "Repeat n times, conditional loop")
ask("In which language does the 'char' variable type appear?", 2, 1, 3, "Java", "JavaScript", "Python")


print("Your score: " + str(rightAnswers) + "/" + str(qnumber))

if rightAnswers > qnumber:
    print("You HAX0R! /ban @p For hacking the game")
elif rightAnswers == (qnumber / 2):
    print("Dude, that's so average")
elif rightAnswers == qnumber:
    print("NERD ALARM! NERD ALARM!")
elif rightAnswers > (qnumber / 2) and rightAnswers < qnumber:
    print("That's... more than average.")
elif rightAnswers == 0:
    print("Try again, n00b")
elif rightAnswers > 0 and rightAnswers < (qnumber / 2):
    print("Worse than average.. You should learn more.")
