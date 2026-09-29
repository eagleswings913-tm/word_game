import re

answer = 'frame'
correct = False
number_of_guesses = 0
message = ""
while not correct:
    while True:
        guess = input("Guess a 5 letter word: ")
        if len(guess) == 5:
            number_of_guesses += 1
            break
        else:
            print("Please enter a 5 letter word")

    answer_list = []
    answer_letter_list = []
    guess_letter_list = []
    for letter in answer:
        indices = [m.start() for m in re.finditer(letter, answer)]
        if letter not in answer_letter_list:
            answer_letter_list.append(letter)
            answer_list.append([letter, indices])
    number_correct = 0
    for index, letter in enumerate(guess):
        if letter in answer_letter_list:
            for row in answer_list:
                if row[0] == letter:
                    for idx in row[1]:
                        if idx ==index:
                            guess_letter_list.append("\033[42m" + letter + "\033[0m")
                            number_correct += 1
                            break
                    else:
                        guess_letter_list.append("\033[43m" + letter + "\033[0m")
        else:
            guess_letter_list.append(letter)
    # print(f'{number_correct} letters guessed correctly.')
    if number_correct == 5:
        message = "Correct!"
        correct = True
    elif number_of_guesses == 6:
        message = "You used up your 6 tries! Better luck next time!"
        correct = True
    print(*guess_letter_list, end="\n",sep='')
print(f'{message}')