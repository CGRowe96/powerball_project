#----------------------------------------------New Dataset--------------------------------------------------#
import numpy as np
import pandas as pd
import random

random.seed(1111)

def dataset_creation(points):
    list1 = []
    list2 = []
    pop1 = np.arange(1,70)
    pop2 = np.arange(1,27)
    i = 1
    while i <= points:
        select1 = np.random.choice(pop1,size=5,replace=False)
        select2 = np.random.choice(pop2,size=1,replace=False)
        list1.append(select1)
        list2.append(select2)
        i += 1
    choice_list = pd.DataFrame(list1, columns=['choice1','choice2','choice3','choice4','choice5'])
    pb_list = pd.DataFrame(list2, columns=['pb_choice'])
    new_df = pd.concat([choice_list, pb_list],axis=1)
    new_df.to_csv('new_data.csv')

dataset_creation(2000)