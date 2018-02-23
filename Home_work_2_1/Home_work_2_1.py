def get_cook_book():
    with open('cook_book.txt') as fd:
        cook_book = {}
        for line in fd:
            name_of_dish = line.strip().lower()
            quantity_of_ingredients = int(fd.readline())
            contains_of_dish = []

            for i in range(quantity_of_ingredients):
                data_for_ingredient = fd.readline().split(' |')
                ingredient = {'ingredient_name': data_for_ingredient[0], 'quantity': int(data_for_ingredient[1]),
                              'measure': data_for_ingredient[2].strip()}
                contains_of_dish.append(ingredient)

            cook_book[name_of_dish] = contains_of_dish
            fd.readline()

    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    cook_book = get_cook_book()
    for dish in dishes:
        for ingredient in cook_book[dish]:
            new_shop_list_item = dict(ingredient)

            new_shop_list_item['quantity'] *= person_count
            if new_shop_list_item['ingredient_name'] not in shop_list:
                shop_list[new_shop_list_item['ingredient_name']] = new_shop_list_item
            else:
                shop_list[new_shop_list_item['ingredient_name']]['quantity'] += new_shop_list_item['quantity']
    return shop_list


def print_shop_list(shop_list):
    for shop_list_item in shop_list.values():
        print('{} {} {}'.format(shop_list_item['ingredient_name'], shop_list_item['quantity'],
                                shop_list_item['measure']))


def create_shop_list():
    person_count = int(input('Введите количество человек: '))
    dishes = input('Введите блюда в расчете на одного человека (через запятую): ') \
        .lower().split(', ')
    shop_list = get_shop_list_by_dishes(dishes, person_count)
    print_shop_list(shop_list)

create_shop_list()

#XML - для разметки документов, текстов, где доля разнотипных символьных данных велика, а доля разметки мала
#JSON - как и XML используется для сериализации объектов, но является более лаконичным
#YAML - используется как формат для файлов конфигурации