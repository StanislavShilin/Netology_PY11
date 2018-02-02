def get_cook_book():
    with open('cook_book.txt') as fd:
        cook_book = {}
        for line in fd:
            name_of_dish = line.strip().lower()
            quantity_of_ingrdients = int(fd.readline())
            contains_of_dish = []
            ingridient = {}
            i = 0
            while i < quantity_of_ingrdients:
                data_for_ingridient = fd.readline().split(' |')
                ingridient['ingridient_name'] = data_for_ingridient[0]
                ingridient['quantity'] = int(data_for_ingridient[1])
                ingridient['measure'] = data_for_ingridient[2].strip()
                contains_of_dish.append(ingridient.copy())
                i += 1

            cook_book[name_of_dish] = contains_of_dish
            fd.readline()

    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    cook_book = get_cook_book()
    for dish in dishes:
        for ingridient in cook_book[dish]:
            new_shop_list_item = dict(ingridient)

            new_shop_list_item['quantity'] *= person_count
            if new_shop_list_item['ingridient_name'] not in shop_list:
                shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
            else:
                shop_list[new_shop_list_item['ingridient_name']]['quantity'] += new_shop_list_item['quantity']
    return shop_list


def print_shop_list(shop_list):
    for shop_list_item in shop_list.values():
        print('{} {} {}'.format(shop_list_item['ingridient_name'], shop_list_item['quantity'],
                                shop_list_item['measure']))


def create_shop_list():
    person_count = int(input('Введите количество человек: '))
    dishes = input('Введите блюда в расчете на одного человека (через запятую): ') \
        .lower().split(', ')
    shop_list = get_shop_list_by_dishes(dishes, person_count)
    print_shop_list(shop_list)

create_shop_list()