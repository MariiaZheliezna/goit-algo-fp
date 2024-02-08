import copy


def greedy_algorithm(items: dict, budget: float):
    # Форматуємо дані в більш зручну структуру
    for name, parameters_ in items.items():
        parameters_['ratio'] = round(parameters_['calories'] / parameters_['cost'], 2)
        parameters_['name'] = name
    foodlist = list(items.values())
    foodlist.sort(key=lambda x: x['ratio'], reverse=True) # відсортовуємо продукти за рейтингом

    print('Повні дані про їжу:')
    for f in foodlist:
        print(f)

    budget_remain = budget
    colected_food = list()
    colected_value = 0
    colected_cal = 0

    for f in foodlist:
        if f['cost'] <= budget_remain:
            colected_food.append(f)
            budget_remain -= f['cost']
            colected_value += f['cost']
            colected_cal += f['calories']
    
    return colected_value, colected_cal, colected_food





def dynamic_programming(items: dict, budget: float):
    # Форматуємо дані в більш зручну структуру
    for name, parameters_ in items.items():
        parameters_['name'] = name
    foodlist = list(items.values())

    # print(foodlist)

    # створюємо таблицю K для зберігання оптимальних значень підзадач
    n = len(foodlist)
    K = [[[0,[]] for w in range(budget + 1)] for i in range(n + 1)]

    # будуємо таблицю K знизу вгору
    for i in range(n + 1):
        for b in range(budget + 1):
            if i == 0 or b == 0:
                K[i][b] = [0,[]]
            elif foodlist[i - 1]['cost'] <= b:
                if foodlist[i - 1]['calories'] + K[i - 1][b - foodlist[i - 1]['cost']][0] > K[i - 1][b][0]:
                    K[i][b][0] = foodlist[i - 1]['calories'] + K[i - 1][b - foodlist[i - 1]['cost']][0]
                    K[i][b][1] = copy.deepcopy(K[i-1][b- foodlist[i - 1]['cost']][1])
                    K[i][b][1].append(foodlist[i - 1])
                else:
                    K[i][b] = K[i - 1][b]
            else:
                K[i][b] = K[i - 1][b]
    return K[n][budget]

def main():
    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350}
    }

    # задаємо бюджет на продукти
    budget = 95

    colected_value, colected_cal, colected_food = greedy_algorithm(items, budget)
    print('Жадібний алгоритм (максимізація співвідношення калорій до вартості):')
    print(f'Розмір бюджету: {budget}, вартість страв: {colected_value}, калорійність страв: {colected_cal}')
    print('Відібрані страви:')
    for food in colected_food:
        print(food)

    result = dynamic_programming(items, budget)
    colected_cal = result[0]
    colected_food = result[1]
    colected_value = 0
    for food in colected_food:
        colected_value += food['cost']
    print('Алгоритм динамічного програмування (оптимальний набір страв для максимізації калорійності):')
    print(f'Розмір бюджету: {budget}, вартість страв: {colected_value}, калорійність страв: {colected_cal}')
    print('Відібрані страви:')
    for food in colected_food:
        print(food)

if __name__ == '__main__':
    main()