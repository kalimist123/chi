import matplotlib.pyplot as plt
import numpy as np
import math
import seaborn as sns
import pandas as pd


cols = ['age', 'workclass', 'fnlwg', 'education', 'education-num',
        'marital-status','occupation','relationship', 'race','sex',
        'capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'income']
data = pd.read_csv('census.csv', names=cols)
print(data)


def process_hours(df):
    cut_points = [0,9,19,29,39,49,1000]
    label_names = ["0-9","10-19","20-29","30-39","40-49","50+"]
    df["hours_per_week_categories"] = pd.cut(df["hours-per-week"],
                                             cut_points,labels=label_names)
    return df

data = process_hours(data)

workhour_by_sex = data[['sex', 'hours_per_week_categories']]
print(workhour_by_sex.head())


print(workhour_by_sex['sex'].value_counts())

print(workhour_by_sex['hours_per_week_categories'].value_counts())


contingency_table = pd.crosstab(
    workhour_by_sex['sex'],
    workhour_by_sex['hours_per_week_categories'],
    margins = True
)

print(contingency_table)