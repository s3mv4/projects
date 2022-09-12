from random import randint

try:
    def start():
        global number
        while True:
            limit = input("How high do you want your number to be able to be generated? [>= 10]\n> ")
            if limit.isdigit() == False:
                    continue
            if int(limit) >= 10:
                number = randint(1, int(limit))
                main()
            else:
                continue
            
            
    def main():
        global guess
        guess = input("Take a guess:\n> ")
        if guess.isdigit() == False:
            main()
        guess = int(guess)
        while True:
            if guess == number:
                play_again()
            if guess < number:
                msg = "Too low! Take a guess:\n> "
                take_guess(msg)
            if guess > number:
                msg = "Too high! Take a guess:\n> "
                take_guess(msg)

    def take_guess(msg):
        global guess
        guess = input(msg)
        if guess.isdigit() == False:
            take_guess(msg)
        guess = int(guess)

    def play_again():
        while True:
            play_again = input("Correct! Do you want to play again? [Y/n]\n> ")
            if play_again == "y" or play_again == "Y":
                start()
            elif play_again == "n" or play_again == "N":
                exit()
            else:
                continue

    start()
except KeyboardInterrupt:
    print("")
    exit()