import pandas as pd
import os

#--------------------------------------------------------Load Dataset----------------------------------------------------------------#
os.chdir(r"C:\Users\hsgam\OneDrive\Documents\GitHub\powerball_project\dataset")
df = pd.read_csv("powerball.csv")
os.chdir(r"C:\Users\hsgam\OneDrive\Documents\GitHub\powerball_project")

df = df.drop(columns='Winning Numbers')
print(df.head())
print(df.dtypes)

#---------------------------------------------------------Fully Random Drawing--------------------------------------------------------#
import numpy as np
import scipy

pop1 = np.arange(1,65)
pop2 = np.arange(1,25)

select1 = np.random.choice(pop1,size=5,replace=False)
select2 = np.random.choice(pop2,size=1,replace=False)

print(select1)
print(select2)