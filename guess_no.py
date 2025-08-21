import random
print("Guess the no between 1 to 50")
print("You have 7 chances")
low=1
high=50
rand_no=random.randint(low,high)
gc=0
while gc<7:
    gc+=1
    guess=int(input("guess the no:"))
    if guess==rand_no:
        print("Great...You guessed it right!!")
        break
    elif guess>rand_no:
        print(f"Umm too high!!")
    elif guess<rand_no:
        print(f"Umm too low!")
    elif gc>=7 and guess!=rand_no:
        print("Hard luck..Better luck next time!!")