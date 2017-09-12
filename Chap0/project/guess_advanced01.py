import random

A = B = 0

# Generate a four-digit random number with no repeated digits
def generate_number():
    answer = random.sample(range(10),4)
    while (answer[0]==0):
        print(answer)
        answer = random.sample(range(10),4)
    return(answer)

def check_number(guess, answer):
    global A, B
    if guess.isdigit() and len(guess) == 4:# check if the input is an integer and it's of 4 digits
        for i in range(4):
            if int(guess[i]) in answer:  #print(type(guess[i])) # str
                if int(guess[i]) == answer[i]: # number is right
                    A += 1 # digit is right
                else:
                    B += 1
    else:
        print("Wrong input. Please input a 4-digit integer.")

def main():
    answer = generate_number()

    global A, B

    for n in range(10): # 10 chances to guess
        A = B = 0
        guess = input("Please input a four-digit number with no repeated digits >")
        check_number(guess, answer)

        if (A == 4):
            print("Correct number. Good job!")
            exit(0)
        else:
            print(str(A)+'A'+str(B)+'B')
            print(("You have %d chances left") % (9-n))

if __name__ == '__main__':
    main()
