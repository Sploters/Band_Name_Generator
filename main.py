from msvcrt import getch
# A prompt for user
print("Welcome to the Band Generator.")
city = input("What's name of the city you grew up in?\n")
pet_name = input("What's your pet's name?\n")

print("Your band name could be " + city + " " + pet_name)
getch()
