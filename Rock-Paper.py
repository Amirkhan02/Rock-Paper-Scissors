import random



loop = True
while loop == True:
    user_shot = input("Enter Jajssssdh")
    counter_shot = random.choice(["r", "p", "s"])
    print("Computer shot:" + user_shot)
    if user_shot not in ["r", "p", "s"]:
        print("Invalid input")
        continue
    else:
        if user_shot == computer_shot:
            print("it's a tie")
            continue
        elif (user_shot == "r" and computer_shot =="p") or (user_shot == "p" and computer_shot == "s") or (user_shot == "s" and computer_shot == "r"):
            print("user wins")
        else:
            print("computer wins")
        breaks