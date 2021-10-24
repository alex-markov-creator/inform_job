#-*- coding: utf-8 -*-
"""
selection.py - Data sampling file from source file of format .xlsx
Задание состоит в изучении статистической выборки по ценам на офисную недвижимость и построении многофакторной регрессии. А именно зависимости удельной стоимости недвижимости (удельная стоимость, руб./кв.м = цена предложения, руб./общая площадь, кв.м) от конкретных ценообразующих факторов – общей площади и расстояния до центра города.

Исследование необходимо провести на выборке объектов только класса С. При этом рекомендуется очистить данные в том числе от выбросов.
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats


#load .xlsx to pd.DataFrame
df_edit = pd.read_excel('Офисы Продажа 2021г.xlsx',sheet_name='Sheet0')
#selection columns
df = df_edit[['id','Класс','Общая площадь','Цена', 'Расстояние до центра, м.']]
df = df.loc[df['Класс']=='C']
#save to file for tests
df.to_excel('df_tests.xlsx')
df_tests = pd.read_excel('df_tests.xlsx')
# apply dropna()
df = df.dropna()
df = df.reset_index(drop=True)

def test_function():
    """
    tests function after dropna()
    """
    assert round(float(df.loc[df['id'] == 2562125]['Общая площадь']),2) == round(1058.900024, 2)
    assert round(float(df.loc[df['id'] == 2562125]['Цена']),2) == round(25000000, 2)
    assert round(float(df.loc[df['id'] == 2562125]['Расстояние до центра, м.']),2) == round(7358.726948,2)
    #assert df.loc[df['id'] == 2562125]['Класс'] == 'C'

    assert round(float(df.loc[df['id'] == 2362259]['Общая площадь']),2) == round(151.000000,2)
    assert round(float(df.loc[df['id'] == 2362259]['Цена']),2) == round(4000000,2)
    assert round(float(df.loc[df['id'] == 2362259]['Расстояние до центра, м.']),2) == round(6348.352448,2)

    assert round(float(df.loc[df['id'] == 2359419]['Общая площадь']),2) == round(50.200001, 2)
    assert round(float(df.loc[df['id'] == 2359419]['Цена']), 2) == round(1400000, 2)
    assert round(float(df.loc[df['id'] == 2359419]['Расстояние до центра, м.']), 2) == round(12991.190962, 2)

test_function()

# add column 'Удельная стоимость'
df['Удельная стоимость'] = df['Цена']/df['Общая площадь']

df_calc = df[['Общая площадь', 'Расстояние до центра, м.', 'Удельная стоимость']]
sns.boxplot(data=df_calc)
plt.show()

# selection results
df_super=df_calc[(np.abs(stats.zscore(df_calc)) < 0.3).all(axis=1)]
sns.boxplot(data=df_super)
plt.show()

#save results to file
df_super.to_excel('output.xlsx')

if __name__ == '__main__':
    print(df_calc.describe())
    print(df_super.describe())



