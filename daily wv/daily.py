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