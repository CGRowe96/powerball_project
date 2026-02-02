import pandas as pd
import os

#---------------Load Datasets-----------------#

os.chdir(r"C:\Users\charlesrowe\Downloads\GitHub\powerball_project\daily wv\datasets")
df1 = pd.read_csv('Daily 3_Winning_Numbers_File_Past Year_2026-02-02.csv')
df2 = pd.read_csv('Daily 4_Winning_Numbers_File_Past Year_2026-02-02.csv')
os.chdir(r"C:\Users\charlesrowe\Downloads\GitHub\powerball_project\daily wv")

#---------------Confirmation of Load---------------------#
print(df1.head())
print(df2.head())

#---------------Summary-----------------#
print(df1.describe())
print(df2.describe())

'''
         Number 1    Number 2    Number 3
count  312.000000  312.000000  312.000000
mean     4.403846    4.400641    4.115385
std      2.846059    2.875174    2.843080
min      0.000000    0.000000    0.000000
25%      2.000000    2.000000    2.000000
50%      4.000000    4.000000    4.000000
75%      7.000000    7.000000    7.000000
max      9.000000    9.000000    9.000000
'''

'''
         Number 1    Number 2    Number 3    Number 4
count  312.000000  312.000000  312.000000  312.000000
mean     4.189103    4.538462    4.564103    4.737179
std      2.843079    2.789241    2.864978    2.828682
min      0.000000    0.000000    0.000000    0.000000
25%      2.000000    2.000000    2.000000    2.000000
50%      4.000000    4.500000    5.000000    5.000000
75%      7.000000    7.000000    7.000000    7.000000
max      9.000000    9.000000    9.000000    9.000000
'''

#---------------Drop "Date"--------------#
df1 = df1.drop(columns='Date')
df2 = df2.drop(columns='Date')

#-----------------Correlation------------------#
print(df1.corr())
print(df2.corr())

'''
          Number 1  Number 2  Number 3
Number 1  1.000000 -0.021408  0.035550
Number 2 -0.021408  1.000000  0.010848
Number 3  0.035550  0.010848  1.000000
'''

'''
          Number 1  Number 2  Number 3  Number 4
Number 1  1.000000 -0.027073  0.026732 -0.054173
Number 2 -0.027073  1.000000  0.056828 -0.003198
Number 3  0.026732  0.056828  1.000000  0.069933
Number 4 -0.054173 -0.003198  0.069933  1.000000
'''

#-------------Value Counts---------------#
def unique_counter1(col):
    print(df1[col].value_counts())

def unique_counter2(col):
    print(df2[col].value_counts())

unique_counter1('Number 1')
unique_counter1('Number 2')
unique_counter1('Number 3')

unique_counter2('Number 1')
unique_counter2('Number 2')
unique_counter2('Number 3')
unique_counter2('Number 4')

#---------------Probability-----------------#

import numpy as np
import itertools as it

def probability_2col1(col1,col2):
    st_dev_dic = {'S1_-1_stdev':1,'S1_med':4,'S1_+1_stdev':7,
                     'S2_-1_stdev':1,'S2_med':4,'S2_+1_stdev':7,
                     'S3_-1_stdev':1,'S3_med':4,'S3_+1_stdev':7}
    
    if col1 == 'Number 1':
        if col2 == 'Number 2':
            col1vals = np.arange(st_dev_dic['S1_-1_stdev'],st_dev_dic['S1_+1_stdev']+1)
            col2vals = np.arange(st_dev_dic['S2_-1_stdev'],st_dev_dic['S2_+1_stdev']+1)
            cols = df1[[col1,col2]]
            cols_list = cols.columns.to_list()
            for combo in it.combinations(cols_list,2):
                print(df1[list(combo)].value_counts())
                new_csv = pd.DataFrame(df1[list(combo)].value_counts())
                new_csv.to_csv(f'{col1}_{col2}_combos1.csv')
            print(col1vals)
            print(col2vals)
    
    if col1 == 'Number 1':
        if col2 == 'Number 3':
            col1vals = np.arange(st_dev_dic['S1_-1_stdev'],st_dev_dic['S1_+1_stdev']+1)
            col2vals = np.arange(st_dev_dic['S3_-1_stdev'],st_dev_dic['S3_+1_stdev']+1)
            cols = df1[[col1,col2]]
            cols_list = cols.columns.to_list()
            for combo in it.combinations(cols_list,2):
                print(df1[list(combo)].value_counts())
                new_csv = pd.DataFrame(df1[list(combo)].value_counts())
                new_csv.to_csv(f'{col1}_{col2}_combos1.csv')
            print(col1vals)
            print(col2vals)

    if col1 == 'Number 2':
        if col2 == 'Number 3':
            col1vals = np.arange(st_dev_dic['S2_-1_stdev'],st_dev_dic['S2_+1_stdev']+1)
            col2vals = np.arange(st_dev_dic['S3_-1_stdev'],st_dev_dic['S3_+1_stdev']+1)
            cols = df1[[col1,col2]]
            cols_list = cols.columns.to_list()
            for combo in it.combinations(cols_list,2):
                print(df1[list(combo)].value_counts())
                new_csv = pd.DataFrame(df1[list(combo)].value_counts())
                new_csv.to_csv(f'{col1}_{col2}_combos1.csv')
            print(col1vals)
            print(col2vals)
    
    if col1 == 'Number 2':
        if col2 == 'Number 1':
            raise SyntaxError('Reverse order of columns')
            
    if col1 == 'Number 3':
        if col2 == 'Number 2':
            raise SyntaxError('Reverse order of columns')
        
    if col1 == 'Number 3':
        if col2 == 'Number 1':
            raise SyntaxError('Reverse order of columns')
        
probability_2col1('Number 1','Number 2')
probability_2col1('Number 1','Number 3')
probability_2col1('Number 2','Number 3')

def probability_2col2(col1,col2):
    st_dev_dic = {'S1_-1_stdev':1,'S1_med':4,'S1_+1_stdev':7,
                     'S2_-1_stdev':1,'S2_med':4,'S2_+1_stdev':7,
                     'S3_-1_stdev':1,'S3_med':4,'S3_+1_stdev':7,
                     'S4_-1_stdev':1,'S4_med':4,'S4_+1_stdev':7}
    
    if col1 == 'Number 1':
        if col2 == 'Number 2':
            col1vals = np.arange(st_dev_dic['S1_-1_stdev'],st_dev_dic['S1_+1_stdev']+1)
            col2vals = np.arange(st_dev_dic['S2_-1_stdev'],st_dev_dic['S2_+1_stdev']+1)
            cols = df2[[col1,col2]]
            cols_list = cols.columns.to_list()
            for combo in it.combinations(cols_list,2):
                print(df2[list(combo)].value_counts())
                new_csv = pd.DataFrame(df2[list(combo)].value_counts())
                new_csv.to_csv(f'{col1}_{col2}_combos2.csv')
            print(col1vals)
            print(col2vals)
    
    if col1 == 'Number 1':
        if col2 == 'Number 3':
            col1vals = np.arange(st_dev_dic['S1_-1_stdev'],st_dev_dic['S1_+1_stdev']+1)
            col2vals = np.arange(st_dev_dic['S3_-1_stdev'],st_dev_dic['S3_+1_stdev']+1)
            cols = df2[[col1,col2]]
            cols_list = cols.columns.to_list()
            for combo in it.combinations(cols_list,2):
                print(df2[list(combo)].value_counts())
                new_csv = pd.DataFrame(df2[list(combo)].value_counts())
                new_csv.to_csv(f'{col1}_{col2}_combos2.csv')
            print(col1vals)
            print(col2vals)

    if col1 == 'Number 1':
        if col2 == 'Number 4':
            col1vals = np.arange(st_dev_dic['S1_-1_stdev'],st_dev_dic['S1_+1_stdev']+1)
            col2vals = np.arange(st_dev_dic['S4_-1_stdev'],st_dev_dic['S4_+1_stdev']+1)
            cols = df2[[col1,col2]]
            cols_list = cols.columns.to_list()
            for combo in it.combinations(cols_list,2):
                print(df2[list(combo)].value_counts())
                new_csv = pd.DataFrame(df2[list(combo)].value_counts())
                new_csv.to_csv(f'{col1}_{col2}_combos2.csv')
            print(col1vals)
            print(col2vals)

    if col1 == 'Number 2':
        if col2 == 'Number 3':
            col1vals = np.arange(st_dev_dic['S2_-1_stdev'],st_dev_dic['S2_+1_stdev']+1)
            col2vals = np.arange(st_dev_dic['S3_-1_stdev'],st_dev_dic['S3_+1_stdev']+1)
            cols = df2[[col1,col2]]
            cols_list = cols.columns.to_list()
            for combo in it.combinations(cols_list,2):
                print(df2[list(combo)].value_counts())
                new_csv = pd.DataFrame(df2[list(combo)].value_counts())
                new_csv.to_csv(f'{col1}_{col2}_combos2.csv')
            print(col1vals)
            print(col2vals)

    if col1 == 'Number 2':
        if col2 == 'Number 4':
            col1vals = np.arange(st_dev_dic['S2_-1_stdev'],st_dev_dic['S2_+1_stdev']+1)
            col2vals = np.arange(st_dev_dic['S4_-1_stdev'],st_dev_dic['S4_+1_stdev']+1)
            cols = df2[[col1,col2]]
            cols_list = cols.columns.to_list()
            for combo in it.combinations(cols_list,2):
                print(df2[list(combo)].value_counts())
                new_csv = pd.DataFrame(df2[list(combo)].value_counts())
                new_csv.to_csv(f'{col1}_{col2}_combos2.csv')
            print(col1vals)
            print(col2vals)

    if col1 == 'Number 3':
        if col2 == 'Number 4':
            col1vals = np.arange(st_dev_dic['S3_-1_stdev'],st_dev_dic['S3_+1_stdev']+1)
            col2vals = np.arange(st_dev_dic['S4_-1_stdev'],st_dev_dic['S4_+1_stdev']+1)
            cols = df2[[col1,col2]]
            cols_list = cols.columns.to_list()
            for combo in it.combinations(cols_list,2):
                print(df2[list(combo)].value_counts())
                new_csv = pd.DataFrame(df2[list(combo)].value_counts())
                new_csv.to_csv(f'{col1}_{col2}_combos2.csv')
            print(col1vals)
            print(col2vals)
    
    if col1 == 'Number 2':
        if col2 == 'Number 1':
            raise SyntaxError('Reverse order of columns')
        
    if col1 == 'Number 3':
        if col2 == 'Number 1':
            raise SyntaxError('Reverse order of columns')  
  
    if col1 == 'Number 4':
        if col2 == 'Number 1':
            raise SyntaxError('Reverse order of columns')
            
    if col1 == 'Number 3':
        if col2 == 'Number 2':
            raise SyntaxError('Reverse order of columns')
    
    if col1 == 'Number 4':
        if col2 == 'Number 2':
            raise SyntaxError('Reverse order of columns')
    
    if col1 == 'Number 4':
        if col2 == 'Number 3':
            raise SyntaxError('Reverse order of columns')
        
probability_2col2('Number 1','Number 2')
probability_2col2('Number 1','Number 3')
probability_2col2('Number 1','Number 4')
probability_2col2('Number 2','Number 3')
probability_2col2('Number 2','Number 4')
probability_2col2('Number 3','Number 4')

def probability_3col1(col1,col2,col3):
    st_dev_dic = {'S1_-1_stdev':1,'S1_med':4,'S1_+1_stdev':7,
                     'S2_-1_stdev':1,'S2_med':4,'S2_+1_stdev':7,
                     'S3_-1_stdev':1,'S3_med':4,'S3_+1_stdev':7}
    
    if col1 == 'Number 1':
        if col2 == 'Number 1':
            raise SyntaxError('Columns cannot be the same')
        if col2 == 'Number 2':
            if col3 == 'Number 1':
                raise SyntaxError('Columns cannot be the same')
            if col3 == 'Number 2':
                raise SyntaxError('Columns cannot be the same')
            if col3 == 'Number 3':
                col1vals = np.arange(st_dev_dic['S1_-1_stdev'],st_dev_dic['S1_+1_stdev']+1)
                col2vals = np.arange(st_dev_dic['S2_-1_stdev'],st_dev_dic['S2_+1_stdev']+1)
                col3vals = np.arange(st_dev_dic['S3_-1_stdev'],st_dev_dic['S3_+1_stdev']+1)
                cols = df1[[col1,col2,col3]]
                cols_list = cols.columns.to_list()
                for combo in it.combinations(cols_list,3):
                    print(df1[list(combo)].value_counts())
                    new_csv = pd.DataFrame(df1[list(combo)].value_counts())
                    new_csv.to_csv(f'{col1}_{col2}_{col3}_combos1.csv')
                print(col1vals)
                print(col2vals)
                print(col3vals)

probability_3col1('Number 1','Number 2','Number 3')

def probability_3col2(col1,col2,col3):
    st_dev_dic = {'S1_-1_stdev':1,'S1_med':4,'S1_+1_stdev':7,
                     'S2_-1_stdev':1,'S2_med':4,'S2_+1_stdev':7,
                     'S3_-1_stdev':1,'S3_med':4,'S3_+1_stdev':7,
                     'S4_-1_stdev':1,'S4_med':4,'S4_+1_stdev':7}
    
    if col1 == 'Number 1':
        if col2 == 'Number 1':
            raise SyntaxError('Columns cannot be the same')
        if col2 == 'Number 2':
            if col3 == 'Number 1':
                raise SyntaxError('Columns cannot be the same')
            if col3 == 'Number 2':
                raise SyntaxError('Columns cannot be the same')
            if col3 == 'Number 3':
                col1vals = np.arange(st_dev_dic['S1_-1_stdev'],st_dev_dic['S1_+1_stdev']+1)
                col2vals = np.arange(st_dev_dic['S2_-1_stdev'],st_dev_dic['S2_+1_stdev']+1)
                col3vals = np.arange(st_dev_dic['S3_-1_stdev'],st_dev_dic['S3_+1_stdev']+1)
                cols = df2[[col1,col2,col3]]
                cols_list = cols.columns.to_list()
                for combo in it.combinations(cols_list,3):
                    print(df2[list(combo)].value_counts())
                    new_csv = pd.DataFrame(df2[list(combo)].value_counts())
                    new_csv.to_csv(f'{col1}_{col2}_{col3}_combos2.csv')
                print(col1vals)
                print(col2vals)
                print(col3vals)
            if col3 == 'Number 4':
                col1vals = np.arange(st_dev_dic['S1_-1_stdev'],st_dev_dic['S1_+1_stdev']+1)
                col2vals = np.arange(st_dev_dic['S2_-1_stdev'],st_dev_dic['S2_+1_stdev']+1)
                col3vals = np.arange(st_dev_dic['S4_-1_stdev'],st_dev_dic['S4_+1_stdev']+1)
                cols = df2[[col1,col2,col3]]
                cols_list = cols.columns.to_list()
                for combo in it.combinations(cols_list,3):
                    print(df2[list(combo)].value_counts())
                    new_csv = pd.DataFrame(df2[list(combo)].value_counts())
                    new_csv.to_csv(f'{col1}_{col2}_{col3}_combos2.csv')
                print(col1vals)
                print(col2vals)
                print(col3vals)
    if col1 == 'Number 2':
        if col2 == 'Number 1':
            raise SyntaxError('Please put columns in order')
        if col2 == 'Number 2':
            raise SyntaxError('Columns cannot be the same')
        if col2 == 'Number 3':
            if col3 == 'Number 1':
                raise SyntaxError('Please put columns in order')
            if col3 == 'Number 2':
                raise SyntaxError('Columns cannot be the same')
            if col3 == 'Number 3':
                raise SyntaxError('Columns cannot be the same')
            if col3 == 'Number 4':
                col1vals = np.arange(st_dev_dic['S2_-1_stdev'],st_dev_dic['S2_+1_stdev']+1)
                col2vals = np.arange(st_dev_dic['S3_-1_stdev'],st_dev_dic['S3_+1_stdev']+1)
                col3vals = np.arange(st_dev_dic['S4_-1_stdev'],st_dev_dic['S4_+1_stdev']+1)
                cols = df2[[col1,col2,col3]]
                cols_list = cols.columns.to_list()
                for combo in it.combinations(cols_list,3):
                    print(df2[list(combo)].value_counts())
                    new_csv = pd.DataFrame(df2[list(combo)].value_counts())
                    new_csv.to_csv(f'{col1}_{col2}_{col3}_combos2.csv')
                print(col1vals)
                print(col2vals)
                print(col3vals)

probability_3col2('Number 1','Number 2','Number 3')
probability_3col2('Number 1','Number 2','Number 4')
probability_3col2('Number 2','Number 3','Number 4')

def probability_4col(col1,col2,col3,col4):

    st_dev_dic = {'S1_-1_stdev':1,'S1_med':4,'S1_+1_stdev':7,
                     'S2_-1_stdev':1,'S2_med':4,'S2_+1_stdev':7,
                     'S3_-1_stdev':1,'S3_med':4,'S3_+1_stdev':7,
                     'S4_-1_stdev':1,'S4_med':4,'S4_+1_stdev':7}
    
    if col1 == 'Number 1':
        if col2 == 'Number 1':
            raise SyntaxError('Columns cannot be the same')
        if col2 == 'Number 2':
            if col3 == 'Number 1':
                raise SyntaxError('Columns cannot be the same')
            if col3 == 'Number 2':
                raise SyntaxError('Columns cannot be the same')
            if col3 == 'Number 3':
                if col4 == 'Number 4':
                    col1vals = np.arange(st_dev_dic['S1_-1_stdev'],st_dev_dic['S1_+1_stdev']+1)
                    col2vals = np.arange(st_dev_dic['S2_-1_stdev'],st_dev_dic['S2_+1_stdev']+1)
                    col3vals = np.arange(st_dev_dic['S3_-1_stdev'],st_dev_dic['S3_+1_stdev']+1)
                    col4vals = np.arange(st_dev_dic['S4_-1_stdev'],st_dev_dic['S4_+1_stdev']+1)
                    cols = df2[[col1,col2,col3,col4]]
                    cols_list = cols.columns.to_list()
                    for combo in it.combinations(cols_list,4):
                        print(df2[list(combo)].value_counts())
                        new_csv = pd.DataFrame(df2[list(combo)].value_counts())
                        new_csv.to_csv(f'{col1}_{col2}_{col3}_{col4}_combos2.csv')
                    print(col1vals)
                    print(col2vals)
                    print(col3vals)
                    print(col4vals)

probability_4col('Number 1','Number 2','Number 3','Number 4')