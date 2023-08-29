# write a program that user need to guess a secret number. first ask the user to guess the number. guess can be maximum be three times. if
# guess is correct within three guess time, user win otherwise failed.
secret_number = 9
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess = int(input("enter your guess: "))
    guess_count +=1
    if guess == secret_number:
        print("You win!")
        break

else:
    print("Sorry, You Failed!")