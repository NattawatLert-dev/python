import random

options = ("rock", "paper", "scissors")
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

number = random.randint(1, 6)
# number = random.random()
option = random.choice(options)
card = random.shuffle(cards)

print(number)