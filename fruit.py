screen = input("Welcome!")
print(screen)

# create set
fruits_cost = {"apples": 1.79, "cherries": 3.74, "blackberries": 2.15, "oranges": 4.74, "grapes": 5.78}
print(fruits_cost)

#prompt user for input
pick = input("Please pick a fruit from the available options:")
print(pick)

# Check if the selection is in the set
while pick not in fruits_cost:
    print("Invalid selection. Please try again.")
    pick = input("Please pick a fruit from the available options: ")

# If the selection is valid, continue with your code
print("You selected:", pick)

def choice(pick):
    return f"Please place your {pick} in the bag"
result = choice(pick)
print(result)

cost = fruits_cost[pick]
print("The cost of your", pick, "is $", cost, "." )
