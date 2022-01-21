import random
from sys import exit

# A list of all categories the user inputs
all_cats = []
cur_cat = ""

'''
Summary: Iniliazes a user-inputted category by formatting the given text file in a python dictionairy with the following format: 
         category = {
             name: name_of_category,
             key: value,
             key: value,
             ...
         }
Params : An empty dictionairy cat_dict, the RELATIVE path of the text file to be extracted path. 
Output : A dictionairy with the formal described in the summary. 
'''
def init_cat(cat_dict, path, splitter="-"):
    f = open(path, "r")

    for line in f:
        if line == "\n": continue
        a = line.split(splitter)
        a[1] = a[1].strip("\n")
        a[1] = a[1][1:]+a[1][0]
        cat_dict[a[0]] = a[1]

    return cat_dict


'''
Summary: Adds the user category to the all_cats list, ensuring that the path is provided
         NOTE: This function does not check the validity of the path - that is on my list of features to add 
Params : The name of the category to add name, the path of the text file to process path
Output : None - this is essentially a helper function 
'''
def add_cat(name, path="", splitter="-"):
    temp = {"name": name}
    if path == "": path = input("Enter the full path of the file to process: ")
    init_cat(temp, path, splitter)
    all_cats.append(temp) 


'''
Summary: Either deletes, adds
Params : The option the user selects bit
Output : The desired editing of the desired category 
'''
def handle_cat_edit(bit, cat):
    #find category
    #a bunch of if statements to check what you can do
    #add logic later
    return True


'''
Summary: Handles user input for options.
Params : The one-letter string that specifies which function to run bit, the current mode of the languages lang 
Output : Depends on the bit parameter 
'''
def handle_option(bit, lang=1):
    valid = "avdesr"

    if bit not in valid:
        print("ERROR: You did not provide a valid option")
        return False

    if bit == "a":
        name = input("What is the name of the category you want to add? ")
        add_cat(name)

    if bit == "v":
        print("Here are all the current categories: ")
        for cat in all_cats:
            print(cat["name"])

    if bit == "s":
        print("Inversed order of languages.")
        run_cat(cur_cat, lang*-1)

    if bit == "d":
        if len(all_cats) == 1:
            print("ERROR: There is only one category - you can not delete it.")
            return False
        
        #Prints all categories to delete
        handle_option("v")

        d = input("Select the name of the category you want to delete: ")
        for i in range(len(all_cats)):
            if(all_cats[i]["name"] == d): 
                all_cats.pop(i)
                print("Successfully removed " + d)

                #runs a new category (in case user deletes current category)
                print("Current categories: ")
                handle_option("v")
                r = input("Which category would you like to run now? ")
                run_cat(r)
        print("Could not find the category")
        return False
        
    if bit == "e": 
        #which category to edit?
        print("Current categories: ")
        handle_option("v")
        c = input("Which category would you like to edit? ")
        print("What would you like to do? ")
        print("r - rename")
        print("c - change a word")
        print("a - add a word")
        print("r - remove a word")
        o = input("What would you like to do? ")
        handle_cat_edit(o, c)

    if bit == "r":
        print("Current categories: ")
        handle_option("v")
        r = input("Which category would you like to run now? ")
        run_cat(r)

    
'''
Summary: Shuffles the questions in the categories. 
Params : The name of the category to run
Output : Printing of questions and their respective solutions
'''
def run_cat(name, lang=1):
    cat = {}
    for c in all_cats:
        if c["name"] == name: 
            cat = c
            break

    if cat == {}: pass #throw an error, category not found

    cur_cat = cat["name"]
    entry_list = list(cat.keys())
    
    print("Type q to exit or o for more options")
    while True:
        rand =  random.randint(1, len(entry_list)-1)

        if lang == 1:
            q = entry_list[rand]
            ans = cat[q]
        if lang == -1:
            q = cat[entry_list[rand]]
            ans = entry_list[rand]

        x = input(q)
        if x == "q": exit()
        if x == "o":
            print("a - add a new category")
            print("v - view current categories")
            print("d - delete a category")
            print("e - edit a category")
            print("s - swap qs/as in the current category")
            print("r - run a new category")
            o = input("Choose an option: ")
            handle_option(o, lang)
        if x != "o": print(ans)


#Driver code
def main():
    path = "./2_food_myLab.txt"
    add_cat("food",path)
    add_cat("rand","./r1.txt", "=")
    run_cat("food")

main()