users = {
  "Jonathan": {
    "twitter": "jonnyt",
    "lottery_numbers": [6, 12, 49, 33, 45, 20],
    "home_town": "Stirling",
    "pets": [
    {
      "name": "fluffy",
      "species": "cat"
    },
    {
      "name": "fido",
      "species": "dog"
    },
    {
      "name": "spike",
      "species": "dog"
    }
  ]
  },
  "Erik": {
    "twitter": "eriksf",
    "lottery_numbers": [18, 34, 8, 11, 24],
    "home_town": "Linlithgow",
    "pets": [
    {
      "name": "nemo",
      "species": "fish"
    },
    {
      "name": "kevin",
      "species": "fish"
    },
    {
      "name": "spike",
      "species": "dog"
    },
    {
      "name": "rupert",
      "species": "parrot"
    }
  ]
  },
  "Avril": {
    "twitter": "bridgpally",
    "lottery_numbers": [12, 14, 33, 38, 9, 25],
    "home_town": "Dunbar",
    "pets": [
      {
        "name": "monty",
        "species": "snake"
      }
    ]
  }
}

# 1. Get Jonathan's Twitter handle (i.e. the string `"jonnyt"`)

Jonathans_twitter = users["Jonathan"]["twitter"]
print(Jonathans_twitter)

# 2. Get Erik's hometown

Eriks_hometown = users["Erik"]["home_town"]
print(Eriks_hometown)

# 3. Get the list of Erik's lottery numbers

Eriks_lottery_numbers = users["Erik"]["lottery_numbers"]
print(Eriks_lottery_numbers)

# 4. Get the species of Avril's pet Monty

for species in users["Avril"]["pets"]:
    print(species)

# 5. Get the smallest of Erik's lottery numbers

smallest_lottery_number = min(users["Erik"]["lottery_numbers"])
print(smallest_lottery_number)

# 6. Return an list of Avril's lottery numbers that are even

even_numbers = []
for even in users["Avril"]["lottery_numbers"]:
    if (even %2 == 0):
        even_numbers.append(even)

print(even_numbers)

# 7. Erik is one lottery number short! Add the number `7` to be included in his lottery numbers

users["Erik"]["lottery_numbers"].append("7")

print(users["Erik"]["lottery_numbers"])

# 8. Change Erik's hometown to Edinburgh

users["Erik"]["home_town"] = ["Edinburgh"]

print(users["Erik"]["home_town"])

# 9. Add a pet dog to Erik called "fluffy"

users["Erik"]["pets"].append({"name": "fluffy",
         "species": "dog"})

print(users["Erik"]["pets"])

# 10. Add another person to the users dictionary

users["Ewelina"] = "Ewelina"
print(users)


# Extensions

# For the following list of numbers:

numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]



# 1. Print out a list of the even integers:

even_integers = []
for even in numbers:
    if (even %2 == 0):
        even_integers.append(even)

print(even_integers)


# 2. Print the difference between the largest and smallest value:

def difference_max_min(numbers):
    smallest = min(numbers)
    largest = max(numbers)

    diff = largest - smallest

    return diff

print(difference_max_min(numbers))