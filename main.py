# List
valid_pokemon_types = ['bug', 'dark', 'dragon', 'electric', 'fairy', 'fighting', 'fire', 'flying', 'ghost', 'grass', 'ground', 'ice', 'normal', 'poison', 'psychic', 'rock', 'steel', 'water']

# Functions
def read_file(txt_file):
    pokemon = {} # create a dictionary
    with open(txt_file, 'r') as file: # open file
        for i in file:
            values = i.strip().split(',') # extract data
            name = values[0]
            quantity = int(values[1])
            fee = float(values[2])
            types = values[3:]
            pokemon[name.lower()] = {'quantity': quantity, 'fee': fee, 'types': types} # put data into list
        return pokemon
def dictionary_to_txt(dictionary):
    lines = [] # create a list
    for name, data in dictionary.items(): # turn dictionary into txt in a list
        line = f"{name},{data['quantity']},{data['fee']},{','.join(data['types'])}\n"
        lines.append(line)
    return lines

# Main Program
txt = "pokemon_data.txt"
pokemon = read_file(txt) # read file and create dictionary

while True:
    print("Welcome to the Pokemon Center PC Database 2.0!")
    action = input("(a)dd, (r)emove, r(e)port, (s)earch by name, search by (t)ype, (l)ist or (q)uit: ")
    if action.lower() not in ['a', 'r', 'e', 's', 't', 'l', 'q']: # put actions in list and check if input is a possible action
        print("Unknown command, please try again") # error message
    if action == "q":
        print("See you next time!") # exit message
        quit()

    if action == "s":
        search = input("Name of Pokemon to search for: ")
        found = False  # set a flag
        for name, data in pokemon.items(): # search for key and data
            if name == search.lower():  # if name is found
                found = True  # set flag to true
                print(f"We have {data['quantity']} {name.title()} at the Pokemon Center PC.")
                print(f"It will cost ${data['fee']:.2f} to adopt this Pokemon")
                print(f"{name.title()} has the following types: {', '.join(data['types']).title()}")
        if not found:
            print(f"We do not have any {search.title()} at the Pokemon Center PC.")

    if action == "t":
        search_type = input("Enter Pokemon type: ")
        found = False  # set a flag

        for name, data in pokemon.items():
            if search_type.lower() in [t.lower() for t in data['types']]:
                found = True
                break  # Exit the loop if  a match is found
        if found:
            # Display header if "if" found is True
            print("{:<20} {:>20} {:>20} {:<}".format("Name", "Amount Available", "Adoption Fee", "Type(s)"))
            for name, data in sorted(pokemon.items()):

                if search_type.lower() in [t.lower() for t in data['types']]: #check if type is in dictionary
                    print("{:<20} {:>20} {:>20.2f} {}".format(name.title(), data['quantity'], data['fee'], ', '.join(data['types']).title()))
        else:
            print(f"We have no Pokemon of that type at our Pokemon Center PC.") # if not print error

    if action == "a":
        stop = False  # set a flag
        while True:
            if stop == True:  # if stop is true break
                break
            new_name = input("Enter name of new Pokemon: ")

            # Check for duplicate names
            if new_name.lower() in pokemon.keys():
                print("Duplicate name, add operation cancelled")
            else:
                while True:
                    if stop == True:
                        break
                    else:

                        value = int(input("How many of these Pokemon are you adding? "))
                        if value <= 0:  # check if value greater than 0
                            print("Invalid, please try again")
                        else:
                            while True:
                                if stop == True:
                                    break
                                else:

                                    adoption = int(input("What is the adoption fee for this Pokemon? "))
                                    if adoption <= 0:  # check if value greater than 0
                                        print("Invalid, please try again")
                                    else:
                                        types = [] # create list

                                        print(
                                            "Next you will be prompted to enter the 'types' for this Pokemon.  Pokemon can have multiple types. Type 'help' to view all possible Pokemon types, and type 'end' to stop entering types. You must enter at least one valid 'type'")

                                        while True:

                                            word = input("What type of Pokemon is this? ")

                                            if word == "help":
                                                for i in valid_pokemon_types:
                                                    print(f"* {i}")  # Print each valid type
                                            if word == "end":
                                                # Add new Pokemon to dictionary
                                                pokemon[new_name.lower()] = {'quantity': value, "fee": adoption, "types": types}
                                                # Update file to include new Pokemon
                                                with open(txt, "a") as add_file:
                                                    add_file.write(f"{new_name},{value},{adoption},{','.join(types)}\n")
                                                print("Pokemon Added!")
                                                stop = True  # set stop to true
                                                break
                                            if word.lower() not in valid_pokemon_types:
                                                print("This is not a valid type, please try again")
                                            else:
                                                print(f"Type {word} added")
                                                types.append(word)

    if action == "l":
        # print header
        print("{:<20} {:>20} {:>20} {:<0}".format("Name", "Amount Available", "Adoption Fee", "Type(s)"))
        for name, data in sorted(pokemon.items()):
            # iterate through all lists and print out each value
            print("{:<20} {:>20} {:>20.2f} {}".format(name.title(), data["quantity"], data["fee"], ' '.join(data["types"]).title()))

    if action == "r":
        pokemon_to_remove = input("Enter name of Pokemon to remove: ")

        if pokemon_to_remove.lower() not in pokemon.keys(): # check if pokemon exists
            print("Pokemon not found, cannot remove") # if not print error message
        else:
            del pokemon[pokemon_to_remove] # if it does delete from list
            with open(txt, "w") as del_file: # update text file
                lines = dictionary_to_txt(pokemon)
                del_file.writelines(lines)
                print("Pokemon removed")

    if action == "e":
        # create lists
        total = []
        fees = []
        for data in pokemon.values(): # break up data from dictionary into lists
            fees.append(data["fee"])

        highest_fee = max(fees) # find max
        lowest_fee = min(fees) # find min
        for name, data in pokemon.items():
            if highest_fee == data["fee"]:
                highest_fee_name = name
            if lowest_fee == data["fee"]:
                lowest_fee_name = name
        for data in pokemon.values():
            total_fee = data["fee"] * data["quantity"] # find product of quantity and price
            total.append(total_fee) # add total to list
        adopt_all =sum(total) # add all the totals

        # print data
        print(f"Highest priced Pokemon: {highest_fee_name.title()} @ ${highest_fee:.2f} per Pokemon")
        print(f"Lowest priced Pokemon: {lowest_fee_name.title()} @ ${lowest_fee:.2f} per Pokemon")
        print(f"Total cost to adopt all Pokemon in the Center: ${adopt_all}")


































