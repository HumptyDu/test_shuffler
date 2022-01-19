import random

# A list of all categories the user inputs
all_cats = []

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
def init_cat(cat_dict, path):
    f = open(path, "r")

    for line in f:
        if line == "\n": continue
        a = line.split("-")
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
def add_cat(name, path=""):
    temp = {"name": name}
    if path == "": path = input("Enter the full path of the file to process: ")
    init_cat(temp, path)
    all_cats.append(temp) 


'''
Summary: Handles user input for options.
Params : The one-letter string that specifies which function to run bit, the current mode of the languages lang 
Output : Depends on the bit parameter 
'''
def handle_option(bit, lang):
    valid = "avdes"

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
        run_cat("food", lang*-1)

    if bit == "d":
        print(all_cats)
        d = input("Select the name of the category you want to delete: ")
        #iterate through and delete 

    if bit == "e": pass
    
'''
Summary: Shuffles the questions in the categories. 
Params :
Output :
'''
def run_cat(name, lang=1):
    cat = {}
    for cur_cat in all_cats:
        if cur_cat["name"] == name: 
            cat = cur_cat
            break

    if cat == {}: pass #throw an error 

    entry_list = list(cat.keys())
    
    print("Type q to exit or o for more options")
    while True:
        rand =  random.randint(0, len(entry_list)-1)

        if lang == 1:
            q = entry_list[rand]
            ans = cat[q]
        if lang == -1:
            q = cat[entry_list[rand]]
            ans = entry_list[rand]

        x = input(q)
        if x == "q": break
        if x == "o":
            print("a - add a new category")
            print("v - view current categories")
            print("d - delete a category")
            print("e - edit a category")
            print("s - swap qs/as in the current category")
            o = input("Choose an option: ")
            handle_option(o, lang)
        if x != "o": print(ans)

def main():
    path = "./2_food_myLab.txt"
    add_cat("food",path)
    run_cat("food")

main()