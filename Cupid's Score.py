# This program tests the compatibility between two people based on your names
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name = name1.lower() + name2.lower()
true_count = name.count("t") + name.count("r") + name.count("u") + name.count("e") 
love_count =  name.count("l") + name.count("o") + name.count("v") + name.count("e") 
final_count = int(str(true_count) + str(love_count))

if final_count < 10 or final_count > 90:
    print(f"Your score is {final_count}, you go together like coke and  mentos.")
elif final_count >= 40 and final_count <= 50:
    print(f"Your score is {final_count}, you are alright together.")
else:
    print(f"Your score is {final_count}.")


