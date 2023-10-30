import random

def toss():
    a=random.randint(0,1)
    if(a==0):
        print("Tails")
    else:
        print("Heads")

if __name__=="__main__":
    toss()
    check = input("Do you want to toss again? Type 'y' or 'n': ")
    if(check == "y"):
        toss()
    else:
        print("Good Bye, thanks for using toss.")