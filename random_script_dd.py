import random
import os
ingredient_range = random.randrange(2, 10)
PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
PROJECT_UI = os.path.join(PROJECT_PATH, "newproject")

with open("IBA.txt", encoding="utf8") as f:
    iba_cocktails = f.readlines()
iba_cocktails = [x.strip() for x in iba_cocktails]
iba_cocktails = list(dict.fromkeys(iba_cocktails))

with open("simple.txt", encoding="utf8") as f:
    ingredient = f.readlines()
ingredient = [x.strip() for x in ingredient]
ingredient = list(dict.fromkeys(ingredient))
ingredient_title = []
for item in ingredient:
    ingredient_title.append(item.lower())


def cocktail_generate(n):
    counter_of_ingredients = 0
    global ingredient_title

    counter = 1
    for j in range(n):
        x = 10
        part_a = ("-------------------------------" + "\n" + "Random Cocktail" + " #" + str(counter))
        part_b = ""

        print("Random Cocktail" + " #" + str(counter))
        counter_of_ingredients = 0
        for i in range(ingredient_range):
            sizing = random.randrange(1, x-1)
            random_ingredient = random.choice(ingredient_title)
            print(str(sizing) + " part " + str(random_ingredient))
            part_b += str(sizing) + " part " + str(random_ingredient) + "\n"
            if random_ingredient in ingredient:
                ingredient.remove(random_ingredient)
            counter_of_ingredients += 1
        print("-------------------")
        part_c = "-------------------------------"
        counter += 1

    return str(part_a) + "\n" + str(part_b) + "\n" + str(part_c)


def cocktail_generate_print_to_window():
    return str(cocktail_generate(1))


def random_iba_cocktail(n):
    for i in range(n):
        return random.choice(iba_cocktails)


def iba_cocktail_generate_print_to_window():
    return str(random_iba_cocktail(1))



