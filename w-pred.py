import pandas as pd
import os

#--------------------------------------------------------Load Sorted Dataset----------------------------------------------------------------#
os.chdir(r"C:/Users/charlesrowe/Downloads/GitHub/powerball_project/dataset")
df = pd.read_csv("powerball.csv")
os.chdir(r"C:\Users\charlesrowe\Downloads\GitHub\powerball_project")

df = df.drop(columns=['Draw Date','Winning Numbers'])
print(df.head())
print(df.dtypes)

#---------------------------------------------------------Fully Random Drawing--------------------------------------------------------#
import numpy as np
import scipy

pop1 = np.arange(1,70)
pop2 = np.arange(1,27)

select1 = np.random.choice(pop1,size=5,replace=False)
select2 = np.random.choice(pop2,size=1,replace=False)

print(select1)
print(select2)

#--------------------------------------------------------Starting Stats---------------------------------------------------------------#
print(df.describe())

max_pball = 26
cond = df['PB'] <= max_pball
df = df[cond]

print(df.describe())

'''
                S1           S2           S3           S4           S5           PB           PP
count  1669.000000  1669.000000  1669.000000  1669.000000  1669.000000  1669.000000  1669.000000
mean     11.410425    22.548832    34.039545    45.323547    56.189335    13.572199     2.589575
std       9.157752    11.686945    12.610266    12.170878    10.139441     7.593721     1.210926
min       1.000000     2.000000     3.000000     7.000000    20.000000     1.000000     1.000000
25%       4.000000    13.000000    24.000000    37.000000    50.000000     7.000000     2.000000
50%       9.000000    21.000000    34.000000    46.000000    58.000000    14.000000     2.000000
75%      16.000000    30.000000    43.000000    54.000000    64.000000    20.000000     3.000000
max      52.000000    61.000000    65.000000    68.000000    69.000000    26.000000    10.000000
'''

print(df.PB.max())

print(df.corr(numeric_only=True))

'''
          S1        S2        S3        S4        S5        PB        PP
S1  1.000000  0.630110  0.456289  0.345128  0.213792 -0.006138  0.046772
S2  0.630110  1.000000  0.712188  0.516004  0.326873  0.008491  0.029482
S3  0.456289  0.712188  1.000000  0.742311  0.494005 -0.033838  0.028586
S4  0.345128  0.516004  0.742311  1.000000  0.675855 -0.020349  0.022724
S5  0.213792  0.326873  0.494005  0.675855  1.000000 -0.010059  0.052378
PB -0.006138  0.008491 -0.033838 -0.020349 -0.010059  1.000000 -0.019562
PP  0.046772  0.029482  0.028586  0.022724  0.052378 -0.019562  1.000000
'''

drawing_list = df.to_numpy().tolist()
print(drawing_list)

def unique_counter(col):
    print(df[col].value_counts())

unique_counter('S1')
unique_counter('S2')
unique_counter('S3')
unique_counter('S4')
unique_counter('S5')
unique_counter('PB')
unique_counter('PP')

#----------------------------------------------Probability------------------------------------------#

import itertools as it

def probability_2col(col1,col2):
    st_dev_dic = {'S1_-1_stdev':1,'S1_med':9,'S1_+1_stdev':18,
                     'S2_-1_stdev':10,'S2_med':21,'S2_+1_stdev':32}
    
    if col1 == 'S1':
        if col2 == 'S2':
            col1vals = np.arange(st_dev_dic['S1_-1_stdev'],st_dev_dic['S1_+1_stdev']+1)
            col2vals = np.arange(st_dev_dic['S2_-1_stdev'],st_dev_dic['S2_+1_stdev']+1)
            cols = df[[col1,col2]]
            cols_list = cols.columns.to_list()
            for combo in it.combinations(cols_list,2):
                print(df[list(combo)].value_counts())
                new_csv = pd.DataFrame(df[list(combo)].value_counts())
                new_csv.to_csv(f'{col1}_{col2}_combos.csv')
            print(col1vals)
            print(col2vals)
        
probability_2col('S1','S2')