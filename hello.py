#hello.py
#A set of test programs I wrote while following "Automate the Boring Stuff with Python"

#Every beginner writes one of these, right?

import random
randomnumber = random.randint(0,100)

#non recursive
def GuessTheNumber(number):
    while True:
        print('Guess the number')
        guess = int(input())
        if guess == number:
            print('You guessed the number. Congrats.')
            break
        elif guess < number:
            print('Try guessing higher')
        else: #guess > number
            print('Try guessing lower')
        

#recursive

def GuessRecursively(guess,number):
    if guess != number:
        if guess < number:
            print('Guess higher')
        else:
            print('Guess Lower')
        new_guess = int(input())
        GuessRecursively(new_guess,number)
    else:
        print('You Guessed correctly! Well done.')

#Collatz Sequence - tail recursively - not very Pythonic?

def collatz(number):
    if number == 1:
        return
    elif number % 2 == 0:
        newnumber = number //2
        print(newnumber)
        return collatz(newnumber)
    else:
        newnumber = 3*number+1
        print(newnumber)
        return collatz(newnumber)


def collatzPythonic(number): # More Pythonic way of doing it perhaps
    while number != 1:
        if number % 2 == 0:
            number = number // 2
            print(number)
        else:
            number = 3 * number + 1
            print(number)

def collatzLists(number): #Storing in lists non recursive
    mylist = []
    while number != 1:
        if number % 2 == 0:
            number = number // 2
            mylist.append(number)
        else:
            number = 3 * number + 1
            mylist.append(number)
    return mylist

