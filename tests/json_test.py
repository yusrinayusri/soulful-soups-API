import json


# soup_id = "soup4"
# with open('../data/soups_recipe.json', 'r') as f:
#     soup_data = json.load(f)
#
# soup_location = int(soup_id.replace("soup", ""))
# print(soup_location)
# del(soup_data[soup_location-1])
# print(soup_data)


soup_id = 'soup3'
with open('./data/soups_recipe.json', 'r') as fi:
    one_soup = json.load(fi)

    for soup in one_soup:
        if soup_id in soup:
            print(soup[soup_id])
        #elif soup_id not in soup:
            #print("Not found")
        #else:
            #print("The soup you are looking for does not exist")

