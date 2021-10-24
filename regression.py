#-*- coding: utf-8 -*-
"""
regresion.py - file develop graphics
Исследование необходимо провести на выборке объектов только класса С. При этом рекомендуется очистить данные в том числе от выбросов.
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from scipy.stats import linregress

#load .xlsx to pd.DataFrame
df = pd.read_excel('output.xlsx',sheet_name='Sheet1', index_col=None)
df = df.iloc[:,1:]
# score corr()
print(df.corr())

#graphic corr()
plt.figure(figsize=(12,10), dpi=80)
sns.heatmap(df.corr(), xticklabels=df.corr().columns, yticklabels=df.corr().columns, cmap='RdYlGn', center=0, annot=True)
plt.show()

