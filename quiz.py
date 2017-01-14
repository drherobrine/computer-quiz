import time

rightAnswers = 0
qnumber = 0 # I call it 'cucumber'

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

print("Welcome to the programming quiz! You will be asked 10 questions.")
time.sleep(1)
print("Try to get as many of them correct!")
time.sleep(1)
print("\n" * 45)

ask("How many bytes in a kilobyte?", 2, 1, 3, "1024", "1000", "999")
ask("What do you call one digit of a byte?", 1, 3, 2, "Bit", "1/8 of a byte", "Bytelet")
ask("How do you import a package in Java?", 2, 3, 1, "import <package name>.<class name>; OR package <package name>;", "import <package name>;", "import <package name>.<class name> OR package <package name>")
ask("What are the 3 main OSs?", 3, 1, 2, "Linux, macOS, Windows", "Sierra, El Capitan, Yosemite", "Windows 7, Windows 8, Windows 10")
ask("What are the 2 kinds of loops in Python?", 1, 2, 3, "for, while", "Repeat n times, infinite loop", "Repeat n times, conditional loop")
ask("In which language does the 'char' variable type appear?", 2, 1, 3, "Java", "JavaScript", "Python")
ask("What is the max value you can display using an 8-bit byte?", 3, 2, 1, "255", "256", "11111111 (decimal)")
ask("What is the max number of values you can display using an 8-bit byte?", 2, 3, 1, "256", "255", "8")
ask("What did I nickname the variable for the number of questions?", 3, 1, 2, "Cucumber", "NoQ", "Questionio")
ask("What is the secret message for hackers?", 2, 3, 1, "U HAX0R! /ban @p For hacking the game", "U HAX0R! Y U NO GO AWAY!", "You Hacker! /ban @p For hacking the game")


print("Your score: " + str(rightAnswers) + "/" + str(qnumber))

if rightAnswers > qnumber:
    print("U HAX0R! /ban @p For hacking the game") #Secret easter egg for nerds :P
elif rightAnswers == (qnumber / 2):
    print("Dude, that's so average")
elif rightAnswers == qnumber:
    print("NERD ALARM! NERD ALARM!")
elif rightAnswers > (qnumber / 2) and rightAnswers < (qnumber - 1):
    print("That's... more than average.")
elif rightAnswers == 0:
    print("Try again, n00b")
elif rightAnswers > 0 and rightAnswers < (qnumber / 2):
    print("Worse than average.. You should learn more.")
elif rightAnswers == (qnumber - 1):
    print("Close enough, although...")
    time.sleep(1)
    print("You're under programming arrest for making a mistake!")
