#1 installed.......

#2

for i in range(1, 100+1):
    print(i)


#3
def print_1_x(x = 10): 
    for i in range(1, x+1):
        print(i)


print_1_x(18)


#4
import random
lucky = random.randint(1, 100)
guess_count = 0
while True:
    guess_count += 1
    cur_guess = int(input('guess the number: '))
    if cur_guess == lucky:
        print('Bingo!')
        print(f'it took you {guess_count} guesses')
        break
    elif cur_guess > lucky:
        print('guess lower...')
    elif cur_guess < lucky:
        print('guess higher...')


#5
import random

for i in range(3):
    lucky = random.randint(1, 100)
    guess_count = 0
    while True:
        guess_count += 1
        cur_guess = int(input('guess the number: '))
        if cur_guess == lucky:
            print('Bingo!')
            print(f'it took you {guess_count} guesses')
            break
        elif cur_guess > lucky:
            print('guess lower...')
        elif cur_guess < lucky:
            print('guess higher...')