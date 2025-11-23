import csv
import random


def main():
    words = readwords()
    print("Hello from learn-a-language!")
    while True:
        print("Choose mode: ")
        print("1: Revision Mode")
        print("2: Test English")
        print("3: Test German")
        print("q: Quit")
        mode = input("Enter your selection: ")
        if mode == "1":
            revisionmode(words)
        elif mode == "2":
            testegnlish(words)
        elif mode == "3":
            testgerman(words)
        elif mode == "q":
            break
        else:
            print("Invalid mode selected.")


def readwords():
    words = []
    with open("languages/german.csv") as f:
        reader = csv.reader(f)
        for row in reader:
            words.append(row)
    return words


def revisionmode(words):
    while True:
        index = random.randint(0, len(words) - 1)
        word = words[index]
        print(f"German: '{word[0]}'")
        print(f"English: '{word[1]}'")
        quit = input("Press Enter to continue... or type 'q' to quit: ")
        if quit == "q":
            break


def testegnlish(words):
    while True:
        index = random.randint(0, len(words) - 1)
        word = words[index]
        print(f"German: '{word[0]}'")
        guesse = input("type english ... or type 'q' to quit: ")
        if guesse == "q":
            break
        english = word[1]
        if guesse == english:
            print("Correct")
        else:
            print(f"Wrong, the correct answer is '{english}'")


def testgerman(words):
    while True:
        index = random.randint(0, len(words) - 1)
        word = words[index]
        print(f"english: '{word[1]}'")
        guessg = input("type german ... or type 'q' to quit: ")
        if guessg == "q":
            break
        german = word[0]
        if guessg == german:
            print("Correct")
        else:
            print(f"Wrong, the correct answer is '{german}'")


if __name__ == "__main__":
    main()
