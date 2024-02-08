import random
from collections import defaultdict


def main():
    nums = 2000000
    counts = defaultdict(int)

    for _ in range(nums):
        dice_01 = random.randint(1, 6)
        dice_02 = random.randint(1, 6)
        dice = dice_01 + dice_02
        counts[dice] += 1

    probabilities = {key: count / nums for key, count in counts.items()}
    myKeys = list(probabilities.keys())
    myKeys.sort()
    prob_sort = {i: probabilities[i] for i in myKeys}

    print('| Сума | Імовірність ')
    print('|------|-------------')
    for dice, prob in prob_sort.items():
        print(f'|{dice:<5} | {prob:.2%}')

if __name__ == '__main__':
    main()    