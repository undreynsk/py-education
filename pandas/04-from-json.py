import pandas as pd
import json

with open('C:\\prj\\py\\pandas\\page1_0438.json', 'r', encoding='utf-8') as f:
    data = json.load(f)  # загружает данные в память

#j = pd.read_json( 'C:\\prj\\py\\pandas\\page1_0438.json' )

#df = pd.DataFrame(data=scores, index=['Ivan', 'Maria', 'Oleg'], columns=['Math', 'Physics'])
print(data)
