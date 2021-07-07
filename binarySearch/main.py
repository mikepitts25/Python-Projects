low = 1
high = 1000
answer = 101

print("Think of a number between {} and {}.".format(low, high))
input("Press ENTER to start.")

guesses = 1
while low != high:
    guess = low + (high - low) // 2
    """high_low = input("My guess is {}. Should I guess (h)igher, (l)ower or was I "
                     "(c)orrect? Enter h, l, or c to continue.".format(guess).casefold())

    
    
    if high_low == 'h':
        low = guess + 1

    elif high_low == 'l':
        high = guess - 1

    elif high_low == 'c':
        print("I got it in {} guesses!".format(guesses))
        break
    else:
        print("Please enter h, l, or c ")
"""
    print("My guess is {}.".format(guess))
    if guess < answer:
        low = guess + 1
    elif guess > answer:
        high = guess -1
    elif guess == answer:
        print("I got it in {} guesses!".format(guesses))
        break
    guesses += 1
else:
    print("Your number was {}".format(low))
    print("I got it in {} guesses!".format(guesses))
