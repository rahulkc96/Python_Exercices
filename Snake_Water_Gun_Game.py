import random
a = ["Snake","Water","Gun"]
i = 1
user = 0
system = 0
while(i <= 10):
        b = random.choice(a)
        #print(b)
        #user = 0
        #system = 0

        user_input = input("Enter G for Gun, W for Water and S for Snake : ")
        if user_input == 'G' and b == "Snake":
            print("You Won")
            i = i + 1
            user += 1
        elif user_input == 'G' and b == "Gun":
            print("Tied")
            i = i+1
        elif user_input == 'G' and b == "Water":
            print("You Lost")
            i = i + 1
            system += 1
        elif user_input == 'W' and b == "Snake":
            print("You Lost")
            i = i + 1
            system += 1
        elif user_input == 'W' and b == "Water":
            print("Tied")
            i = i + 1
        elif user_input == 'W' and b == "Gun":
            print("You Won")
            i = i + 1
            user += 1
        elif user_input == 'S' and b == "Snake":
            print("Tied")
            i = i + 1
        elif user_input == 'S' and b == "Water":
            print("You Won")
            i = i + 1
            user += 1
        elif user_input == 'S' and b == "Gun":
            print("You Lost")
            i = i + 1
            system += 1
        else:
            print("Invalid Input")
print("\n")
print("Game Completed")
print ("Total Score")
print(f"You won {user} times and Computer won {system} times")


