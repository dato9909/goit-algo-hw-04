
def total_salary(path):
    sum_salary = 0
    count_salary = 0

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    name, salary_str = line.strip().split(',', 1)
                    salary = int(salary_str)
                    sum_salary += salary
                    count_salary += 1
                except ValueError:
                    print(f'Ошибка в строке: {line.strip()}')
                    continue

        if count_salary > 0:
            average_salary = sum_salary / count_salary
        else:
            average_salary = 0

        result = (sum_salary, round(average_salary))
        print(f'Загальна сума заробітної плати: {sum_salary}, Середня заробітна плата: {average_salary}')
        return result

    except FileNotFoundError as err:
        print(f'Файл не найден: {err}')
        return None

total_salary("/Users/david/Desktop/GOIT/goit-algo-hw-04/hw_1.txt")
