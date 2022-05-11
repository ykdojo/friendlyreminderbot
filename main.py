# Task: Open reminders.txt, which contains a list of reminders, and print a random one out.
import random
lines = open('reminders.txt').readlines()

# Select a random line from the reminders file.
line = lines[random.randint(0, len(lines) - 1)]
print(line.strip())