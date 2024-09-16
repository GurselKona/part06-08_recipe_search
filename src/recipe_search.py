def search_by_name(filename: str, word: str) -> list:
    lines = []
    with open(filename) as f:
        for line in f:
            lines.append(line.strip())
    recipe = []
    recipes = []
    for line in lines:
        if line == "":
            recipes.append(recipe)
            recipe =[]
            continue
        recipe.append(line)
    recipes.append(recipe)
    recipe_dict = {}
    for recipe in recipes:
        recipe_dict[recipe[0]] = recipe[1:]
    found_recipes = []
    for key in recipe_dict:
        if word in key.lower():
            found_recipes.append(key)
    return found_recipes
                    
def search_by_time(filename: str, prep_time: int) -> list:
    lines = []
    with open(filename) as f:
        for line in f:
            lines.append(line.strip())
    recipe = []
    recipes = []
    for line in lines:
        if line == "":
            recipes.append(recipe)
            recipe =[]
            continue
        recipe.append(line)
    recipes.append(recipe)
    recipe_dict = {}
    for recipe in recipes:
        recipe_dict[recipe[0]] = recipe[1:]
    found_recipes = []
    for k,v in recipe_dict.items():
        if int(v[0]) <= prep_time:
            found_recipes.append(k+", preparation time "+v[0]+" min")
    return found_recipes

def search_by_ingredient(filename: str, ingredient: str) -> list:
    lines = []
    with open(filename) as f:
        for line in f:
            lines.append(line.strip())
    recipe = []
    recipes = []
    for line in lines:
        if line == "":
            recipes.append(recipe)
            recipe =[]
            continue
        recipe.append(line)
    recipes.append(recipe)
    recipe_dict = {}
    for recipe in recipes:
        recipe_dict[recipe[0]] = recipe[1:]
    found_recipes = []
    for k,v in recipe_dict.items():
        if ingredient in v:
            found_recipes.append(k+", preparation time "+v[0]+" min")
    return found_recipes          
              
              
              
if __name__ == "__main__":
    found_recipes = search_by_ingredient("recipes1.txt", "eggs")

    for recipe in found_recipes:
        print(recipe)
