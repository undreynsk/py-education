import pandas as pd

#df = pd.DataFrame( {
	#'number' : [ i for i in range( 10 ) ]
	#, 'char' : [ 'a' + str(i) for i in range( 10 ) ]
#} )

wage = pd.read_csv( 'C:\\prj\\py\\2023-10-22-task-1\\wage-1-ee13a6b1-605e-44fe-83a6-85d3d7a0b3ae-2873619c-9efe-44e2-932a-f6fed7be056b.csv' )

print(wage.head())

wage.gender = wage.gender.apply(
	lambda x: 
		'F' if x == 0 else 
		'M' if x == 1 else 
		x )
#df_wage['gender'] = df_wage['gender'].apply(lambda x: 'M' if x == 1 else 'F')

print(wage.head())

print(wage.groupby('gender').aggregate({'wage' : 'mean'}))
#df_wage.groupby('gender')['wage'].mean()\n",
#Так же можно вывести через метод describe. 
# Он выведет количество, среднее, стандартное отклонение, мин, макс и квантили \n",
#df_wage.describe()"
wage.describe()

#print(wage.groupby('gender')['wage'].mean())

#print(wage[(wage['gender']=='F') & (wage['wage']>40000)]);

#"5. Теперь взглянем внимательнее на данные и обнаружим, 
# что некоторые люди попали в выборку несколько раз. \n",
#"    1. Найдите таких людей. Подсказка: `value_counts()`\n",

df_wage.value_counts()[0:10] 

# Видим, что есть клиенты с двумя записями  

#res = (wage['person_id'].value_counts() > 1) == True
#print( wage['person_id'].value_counts())
#print( wage[wage.person_id == 15] )
print( wage.value_counts( subset = ['person_id','wage'] ).head() )
print( wage.value_counts( subset = ['person_id','wage'] ).nunique() )
#print( wage.groupby(['person_id','wage']).head() )
#print( wage.value_counts( subset = ['person_id'] ).head(12) )

#print( wage.groupby('person_id')['person_id'].count() )




#"    0. Убедитесь, что записи по ним с одинаковым `wage`. 
# Возможно, тут вам пригодится функция агрегации `nunique()`, 
# отображающая количество разных значений\n",

#print(wage['person_id'].nunique())
df_wage.loc[((df_wage['person_id'] > 11) & (df_wage['person_id' ] < 18))]

#"    0. Избавьтесь от повторяющихся значений. Подсказка: `drop_duplicates()`"

df_wage = df_wage.drop_duplicates()
#print(df.loc[df.char=="a6"])

# Проверяем, что убрали дубли\n",
df_wage.value_counts()

#6. Теперь посмотрим внимательнее на зарплаты\n",
#    1. Охарактеризуйте имеющиеся данные по зарплатам. Подсказка: `describe`\n",
#    1. Избавьтесь от бессмысленных значений"
df_wage.describe()

# Видим, что есть отридцательные зарплаты. Давайте посмотрим внимательнее, построив гистаграмму \n",
df_wage['wage'].plot(kind='hist')

#    "# Таких зарплат не много. Это явно ошибка. Выбросим такие значения\n",
df_wage = df_wage.loc[df_wage['wage'] > 0]
df_wage = df_wage.dropna(subset=['wage']) # ещё на всякий случай удалим с пустыми значениями

# Проверим, что теперь все хорошо\n",
df_wage['wage'].plot(kind='hist')

#7. Давайте теперь посмотрим на зарплату с учетом бонуса. 
#Для этого нам понадобится таблица `bonus.csv`. 
#Считайте ее в переменную `bonus`. Заметьте, что она сохранена 
#немного в другом формате, и вам понадобится уточнить параметр `sep` - 
#разделитель записей. Сравните текущий файл с предыдущим и попробуйте решить проблему"
df_bonus = pd.read_csv('bonus-1-c177edc7-6e8e-4e53-8f5d-098bd95cc4de.csv', sep=';')

#8. Чтобы посчитать итоговую зарплату, нам нужно по каждому человеку знать и оклад, и премию. 
#Для этого надо будет соединить (сджойнить) таблицы по `person_id`. 
#Используйте для этого функцию `pd.merge`. Помните, что параметр `how` должен быть `'outer'`,
# чтобы сохранить те записи, что есть только в одной таблице. Результат запишите в новый dataframe `df`"
df_full = df_wage.merge(df_bonus, how = 'outer', on = 'person_id')

#    "9. Наконец, давайте посчитаем итоговую зарплату\n",
#    "    1. Замените отсутствующие записи в колонке `bonus` нулями\n",
#    "    1. Уберите людей без `wage` - это те \"плохие\" записи, от которых мы избавлялись на предыдущих шагах\n",
#    "    1. Сделайте новую колонку `total`, которая будет равна 12 окладам и премии\n",
#    "    1. Посчитайте среднюю и медианную итоговую зарплату в разрезе по полу. 
#Подсказка: вместо функции агрегации можно написать `.agg()` и перечислить внутри нужные агрегаты"

df_full = df_full.fillna(0)
df_full.head(5)

df_full['total'] = 12 * df_full['wage'] + df_full['bonus']
df_full.head(5)
#       "                total               \n",
#       "                 mean         median\n",
#       "gender                              \n",
#       "0       142936.832502  142936.832502\n",
#       "F       570746.139432  347622.913892\n",
#       "M       657142.490282  437499.824868"

df_full.groupby('gender').agg({'total':['mean','median']})

#    "10. Сохраните `df` в файл, используя метод `to_csv()`. Не записывайте индексы"
df_full.to_csv('total_wage.csv', index = False)
