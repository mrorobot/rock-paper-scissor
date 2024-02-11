import random
choice=input("enter '1' for Rock, '2' for Paper, '3' for Scissors")
rock= ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
paper=("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
scissor=("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

print("you choose")
if choice=="1":
    print(rock)
elif choice=="2":
    print(paper)
elif choice=="3":
    print(scissor)
else:
    print("enter valid choise")
print("computer choose")
mylist=[rock,paper,scissor]
print(random.choice(mylist))


