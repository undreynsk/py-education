import pandas as pd

data = {
    'Product': 'Apple Banana Cherry'.split() #['Apple', 'Banana', 'Cherry'],
    , 'Price': [100, 80, 250]
    , 'In_Stock': [True, True, False]
}

df = pd.DataFrame(data)
print(df.shape)
print(df.dtypes)
print(df)

data = [
    {'id': 1, 'login': 'user1', 'active': True}
    , {'id': 2, 'login': 'user2'}
    , {'id': 3, 'login': 'user3', 'active': False}
]

df = pd.DataFrame(data)
print(df.shape)
print(df.dtypes)
print(df)

scores = [
    [4, 5],
    [3, 4],
    [5, 5]
]
df = pd.DataFrame(data=scores, index=['Ivan', 'Maria', 'Oleg'], columns=['Math', 'Physics'])
print(df)
