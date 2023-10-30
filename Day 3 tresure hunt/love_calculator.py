print("The Love Calculator is calculator is calculating your score....")
def calc():
    name1 = input("What is your name? ")
    name2 = input("What is their name? ")
    name = name1 + name2
    lower_name = name.lower()
    t=lower_name.count("t")
    r=lower_name.count("r")
    u=lower_name.count("u")
    e=lower_name.count("e")
    first = t+r+u+e     
    secound=lower_name.count("l")+lower_name.count("o")+lower_name.count("v")+lower_name.count("e")
    score = int(str(first)+str(secound))
    if score < 10 or score > 90:
        print(f"Your score is {score}, you go together like coke and mentos.")
    elif score > 40 and score < 50:
        print(f"Your score is {score}, you are alright together.")
    else:
        print(f"Your score is {score}.")

if __name__ == "__main__":
    calc()
    check = input("Do you want to calculate again? Type 'y' or 'n': ")
    if(check == "y"):
        calc()
    else:
        print("Good Bye, thanks for using love calculator.")