date = input("Enter today's date: ")
mood = input("How do you rate your mood today from 1to 10? ")
thoughts = input("Let your thoughts flow : \n")

with open(f"files/{date}.txt", "w") as file:
    file.write("mood = " + mood + "\n")
    file.write(thoughts)
