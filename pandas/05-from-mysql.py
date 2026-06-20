import pandas as pd
from sqlalchemy import create_engine

# 1. Создаем подключение (движок)
engine = create_engine('mysql://home:home@localhost:5432/homeco_robot')

# 2. Пишем SQL запрос
query = "SELECT * FROM agent LIMIT 10"

# 3. Получаем DataFrame
df = pd.read_sql(query, engine)

print(df)