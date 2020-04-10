import random

print("Who is involved? List all people in a txt file, add a linebreak after each person.")
path = input("Path to your txt: ")
print()
with open(path) as f:
    people = f.read().splitlines()

size = int(input("What's your preferred group size? "))

random.shuffle(people)
groups = []
current = 0
while len(people) > 0:
    current = len(groups)
    groups += [[]]
    while len(people) > 0 and len(groups[current])<size:
        groups[current] += [people.pop(0)]
    if len(people) < size:
        while len(people) > 0:
            current = 0
            groups[current] += [people.pop(0)]
            current += 1
            if current >= len(groups):
                current = 0

print()
print("How about this?")
for group in groups:
    print(" - " + ", ".join(group))
print()