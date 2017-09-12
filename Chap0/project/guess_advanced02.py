import random

class NumberGame(object):
    def __init__(self):
        self.A = 0
        self.B = 0

    def generate(self):
        answer = random.sample(range(10),4)
        while (answer[0]==0):
            answer = random.sample(range(10),4)
        return(answer)

    def check(self, guess, answer):
        if guess.isdigit() and len(guess) == 4:# check if the input is an integer and it's of 4 digits
            for i in range(4):
                if int(guess[i]) in answer:  #print(type(guess[i])) # str
                    if int(guess[i]) == answer[i]: # number is right
                        self.A += 1 # digit is right
                    else:
                        self.B += 1
        else:
            print("Wrong input. Please input a 4-digit integer.")


game1 = NumberGame()
answer = game1.generate()
print(answer)

def main():
    for n in range(10): # 10 chances to guess
        game1.A = game1.B = 0
        guess = input("Please input a four-digit number with no repeated digits >")
        game1.check(guess, answer)

        if (game1.A == 4):
            print("Correct number. Good job!")
            exit(0)
        else:
            print(str(game1.A)+'A'+str(game1.B)+'B')
            print(("You have %d chances left") % (9-n))

if __name__ == '__main__':
    main()
