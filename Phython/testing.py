oblig = 5

a = 4
b = 2
c = (a+b)/b
print(c**2)

numbers = []
for x in range(5):
    numbers.append(x)
print(numbers)

animals_in_zoo = {"honey badger": 2, "ape": 15, "zebra": 6, "giraffe": 4}

for animal in animals_in_zoo:
    if animals_in_zoo[animal] < 5:
        print(animal.title())

numbers = [5, 2, 3, 2, 4, 1]

sum_of_numbers = 0
for number in numbers:
    if number <= 2:
        sum_of_numbers += number
    else:
        sum_of_numbers += 1

print(sum_of_numbers)

animals = ["honey badger","giraffe", "ape", "zebra"]

animals[1] = "elephant"

animals.sort()

animals = animals[:2]

for animal in animals:
    print(animals)

animals = ["Elephant","Dog", "Cat", "Gorilla", "Dodo"]
animals = animals[1:3]
animals[0] = "Alligator"
animals.sort(reverse=True)
print(animals)

print("Her kommer neste oppgave")

shopping_list = {}

def add_item(item_name, quantity=1):
    if item_name in shopping_list.keys():
        shopping_list[item_name] += quantity
    else:
        shopping_list[item_name] = quantity

add_item("Bread", 2)
add_item("Milk")
add_item("Milk", 2)
add_item("Bread", 2)
add_item("Eggs")
print(shopping_list)

print("Her kommer neste oppgave")

x = 0
for i in range(0, 5, 2):
    x += i
print(x)

x = 0
for i in range(0, 5):
    x += i
print(x)

print("Her kommer neste oppgave")

a = 5
b = 2
c = 0

c += a**b
print(c)

c = a % b
print(c)

c += a - b * 2
print(c)

c //= b
print(c)

print("Her kommer neste oppgave")

class Game:
    def __init__(self, name, genre, age_rating=18):
        self.name = name
        self.genre = genre
        self.age_rating = age_rating

    def description(self):
        return f"The game {self.name} is of the genre {self.genre} and has an age rating of {self.age_rating}"

game1 = Game("Hades", "Rogue-lite", 12)
game2 = Game("God og War", "Action")
print(game1.age_rating)
print(game2.description())

print()
print("Her kommer neste oppgave")
print()

randomList = [1, "a", 2, "b", 3]
result = 0

for entry in randomList:
    try:
        result += int(entry)
    except ValueError:
        print("A ValueError occurred")

print(f"The sum is: {result}")