score = 0

print('Guess the animal!')

guess1 = input('What animal live in the North Pole? ')


def check_guess(guess, answer):
    global score
    attempt = 0
    still_guessing = True
    while still_guessing and attempt < 3:
        if guess.lower() == answer.lower():
            print('Correct answer')
            score = score + 1
            still_guessing = False
        else:
            if attempt < 2:
                guess = input('Sorry wrong answer. Try again. ')
            attempt = attempt + 1

    if attempt == 3:
        print('The correct answer is ' + answer)


check_guess(guess1, 'polar bear')

guess2 = input('Which is the fastest land animal? ')

check_guess(guess2, 'cheetah')

guess3 = input('Which is the largest animal? ')

check_guess(guess3, 'blue whale')

print('Your score is ' + str(score))
