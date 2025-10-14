'''
my_value_count = weather_data["snowfall"].value_counts()
my_value_count.loc['0.0']
output: 
0.0     12683
my_value_count.loc[my_value_count.index.isin(['0.0','0.2','0.1'])]
output: 
0.0     12683
0.2     32
0.1     31
my_value_count.loc[my_value_count.index < 0.4]
output:
0.0     12683
0.2     32
0.1     31
0.3     18

df = pd.DataFrame({'mycolumn': [1,2,2,2,3,3,4]})
for val, cnt in df.mycolumn.value_counts().items():
    print('value', val, 'was found', cnt, 'times')

value 2 was found 3 times
value 3 was found 2 times
value 4 was found 1 times
value 1 was found 1 times
'''