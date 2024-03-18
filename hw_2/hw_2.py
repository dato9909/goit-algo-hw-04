from pathlib import Path

def get_cats_info(path):
    
    path = Path("hw_2/hw_2.txt")

    list_of_dicts = []

    try:
        with open(path, 'r', encoding='utf-8') as file:
        
            for line in file:
                id , name, age = line.strip().split(',')
                my_dict = {'id':id, 'name': name, 'age':age}
                list_of_dicts.append(my_dict)

            print(list_of_dicts)

    except FileNotFoundError as err:
        print('Ошибка')

get_cats_info("/hw_2/hw_2.txt")