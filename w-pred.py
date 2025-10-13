import pandas as pd
import os

#--------------------------------------------------------Load Dataset----------------------------------------------------------------#
os.chdir(r"C:/Users/charlesrowe/Downloads/GitHub/powerball_project/dataset")
df = pd.read_csv("powerball.csv")
os.chdir(r"C:\Users\charlesrowe\Downloads\GitHub\powerball_project")

df = df.drop(columns=['Draw Date','Winning Numbers'])
print(df.head())
print(df.dtypes)

#---------------------------------------------------------Fully Random Drawing--------------------------------------------------------#
import numpy as np
import scipy

pop1 = np.arange(1,65)
pop2 = np.arange(1,26)

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
print(df.PB.max())

print(df.corr(numeric_only=True))

drawing_list = df.to_numpy().tolist()
print(drawing_list)