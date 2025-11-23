import csv
import random


def main():
    print("Hello from learn-a-language!")
    while True:
        print("choose language: ")
        language = input("g: German, s: Spanish: ")
        if language == "g":
            words = readwords("german")
            language = "German"
        elif language == "s":
            words = readwords("spanish")
            language = "Spanish"
        else:
            print("Invalid language selected.")
            continue

        print("Choose mode: ")
        print("1: Revision Mode")
        print("2: Test English")
        print(f"3: Test {language}")
        print("q: Quit")
        mode = input("Enter your selection: ")
        if mode == "1":
            revisionmode(words, language)
        elif mode == "2":
            testegnlish(words, language)
        elif mode == "3":
            testgerman(words, language)
        elif mode == "q":
            break
        else:
            print("Invalid mode selected.")


def readwords(language):
    words = []
    with open(f"languages/{language}.csv", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            words.append(row)
    return words


def revisionmode(words, language):
    while True:
        index = random.randint(0, len(words) - 1)
        word = words[index]
        print(f"{language}: '{word[0]}'")
        print(f"English: '{word[1]}'")
        quit = input("Press Enter to continue... or type 'q' to quit: ")
        if quit == "q":
            break


def testegnlish(words, language):
    while True:
        index = random.randint(0, len(words) - 1)
        word = words[index]
        print(f"{language}: '{word[0]}'")
        guesse = input("type english ... or type 'q' to quit: ")
        if guesse == "q":
            break
        english = word[1]
        if guesse == english:
            print("Correct")
        else:
            print(f"Wrong, the correct answer is '{english}'")


def testgerman(words, language):
    while True:
        index = random.randint(0, len(words) - 1)
        word = words[index]
        print(f"english: '{word[1]}'")
        guessg = input(f"type {language} ... or type 'q' to quit: ")
        if guessg == "q":
            break
        german = word[0]
        if guessg == german:
            print("Correct")
        else:
            print(f"Wrong, the correct answer is '{german}'")


if __name__ == "__main__":
    main()