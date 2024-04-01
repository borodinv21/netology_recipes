import os

file_path = os.path.join(os.getcwd(), 'recipes.txt')
recepts_l = []

with open(file_path, 'r+') as file:
    current_line = ' '
    el = []

    while current_line != '':
        current_line = file.readline()

        if current_line != '\n' and current_line != '':
            el.append(current_line.strip())
        else:
            recepts_l.append(el)
            el = []
    else:
        recepts_l.append(el)

recepts_l.pop()
cook_book = {}

for i in recepts_l:
    cook_book[i[0]] = []
    for j in i[2:]:
        ingredient_name, quantity, measure = j.split('|')
        cook_book[i[0]].append({'ingredient_name': ingredient_name.strip(), 'quantity': int(quantity.strip()), 'measure': measure.strip()})

def get_shop_list_by_dishes(dishes, person_count):
    result_dict = {}
    for i in dishes:
        for j in cook_book[i]:
            if result_dict.get(j['ingredient_name']):
                result_dict[j['ingredient_name']]['quantity'] += j['quantity'] * person_count
            else:
                result_dict[j['ingredient_name']] = {'measure': j['measure'], 'quantity': j['quantity'] * person_count}

    return result_dict

print(get_shop_list_by_dishes(['Омлет', 'Фахитос'], 3))