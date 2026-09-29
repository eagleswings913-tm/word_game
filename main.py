import re

answer = 'title'

guess = 'trite'

answer_list = []
answer_letter_list = []
guess_letter_list = []
for letter in answer:
    indices = [m.start() for m in re.finditer(letter, answer)]
    if letter not in answer_letter_list:
        answer_letter_list.append(letter)
        answer_list.append([letter, indices])

for index, letter in enumerate(guess):
    if letter in answer_letter_list:
        for row in answer_list:
            if row[0] == letter:
                for idx in row[1]:
                    if idx ==index:
                        guess_letter_list.append("\033[42m" + letter + "\033[0m")
                        break
                else:
                    guess_letter_list.append("\033[43m" + letter + "\033[0m")
    else:
        guess_letter_list.append(letter)
print(*guess_letter_list, end=" ",sep='')