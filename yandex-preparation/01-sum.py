# Input:  the array of integers and the target number
# Output: the list of pairs of indices which give you the sum equal to the target number
#         if nothing found then return some extra message, e.g. "nothing found" or "-1"

import random
import pprint
import sys

def find_pairs(target: int, numbers: list) -> list:
    #print(f"initial: target: {type(target)} {target}, list: {numbers}")
    out = list()

    for i, number in enumerate(numbers):
        for j, element in enumerate(numbers[i+1:]):
            sum_pair = number + element
            is_success = ''
            
            if sum_pair == target:
                out.append([target, number, element, sum_pair])
                is_success = 'BINGO'
                pprint.pprint(out)                
                #if len(out) > 2:
                    #sys.exit()

            
            print(f"{i}, {j}: {number:>3}: {number:>3} + {element:>3} = {sum_pair:>3} {is_success:>10}")

    return out

def test_positive():
    target = 2
    numbers = [-1, 3]
    assert find_pairs(target, numbers) == [ [target, numbers[0], numbers[1], target] ]

"""
def test_add_negative():
    # Проверяем сложение отрицательных чисел
    assert add(-1, -1) == -2

def test_add_fail():
    # Специально падающий тест для демонстрации
    assert add(2, 2) == 5    
"""

a = -20
b =  21

target  = random.randint(a, b)
numbers = random.choices(range(a, b), k=113)

res = find_pairs(target, numbers)
pprint.pprint(res)
print(f"Found {len(res)} pairs")
#find_pairs(target, numbers)