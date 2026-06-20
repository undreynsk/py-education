import pandas as pd
import numpy as np
import time

def note_time(func):
    def wrap(l):
        start = time.time()
        func(l)
        print(round(time.time() - start, 4))
    return wrap

currencies = {
    'USD': 92.5,
    'EUR': 99.1,
    'CNY': 12.8
}

# Pandas автоматически поймет, что ключи — это индексы
s_curr = pd.Series(currencies)

s = pd.Series([10, 20, 30], name='Temperature', index="a b c".split())

print(s)
print(s.iloc[0])

data = ['Anna', 'Bob', 'Charlie']

user_ids = [101, 102, 103] 

out = pd.Series(data, index=user_ids)
print(out)