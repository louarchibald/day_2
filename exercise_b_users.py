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

jonathan_twit_handle = users["Jonathan"]["twitter"]
#print(jonathan_twit_handle)

# 2. Get Erik's hometown

erik_hometown = users["Erik"]["home_town"]
#print(erik_hometown)

# 3. Get the list of Erik's lottery numbers

erik_lotto_nums = users ["Erik"]["lottery_numbers"]
#print(erik_lotto_nums)

# 4. Get the species of Avril's pet Monty

monty_species = users["Avril"]["pets"][0]["species"]
#print(monty_species)

# 5. Get the smallest of Erik's lottery numbers

smallest_lotto = users["Erik"]["lottery_numbers"][2]
#print(smallest_lotto)

# 6. Return an list of Avril's lottery numbers that are even

even_numbers = users["Avril"]["lottery_numbers"]
for number in even_numbers:
    if number % 2 == 0:
        #print(number)

# 7. Erik is one lottery number short! Add the number `7` to be included in his lottery numbers



# 8. Change Erik's hometown to Edinburgh



# 9. Add a pet dog to Erik called "fluffy"



# 10. Add another person to the users dictionary
