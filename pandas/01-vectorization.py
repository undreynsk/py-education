import pandas as pd
import numpy as np
import time

def note_time(func):
    def wrap(l):
        start = time.time()
        func(l)
        print(round(time.time() - start, 4))
    return wrap

numbers = list(range(10000000))

@note_time
def ordinary_list(l):
    new_numbers = []
    for n in l:
        new_numbers.append(n + 1)
    return new_numbers

@note_time
def pandas_list(l):
    series = pd.Series(l)
    new_series = series + 1
    return new_series

@note_time
def numpy_list(l):
    arr = np.array(l)
    new_arr = arr + 1
    return new_arr

print(pd.__version__)

print("pandas_list ")
pandas_list(numbers) # 1.9728

print("numpy_list ")
numpy_list(numbers) # 0.5361

print("ordinary_list ")
ordinary_list(numbers) # 0.8407

