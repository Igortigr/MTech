import streamlit as st
import pandas as pd
import numpy as np
import scipy.stats as sts
from F_test import f_test
from Plot import plot
from testng_hypotheses import testing_hypotheses_1, testing_hypotheses_2
st.title('Data analysis')
data = st.file_uploader('Загрузите файл с данными')


def load_data(data):
    '''Функция приведения в нормальный вид данные'''

    df = pd.read_csv(data, encoding='Windows-1251')
    df[['Количество больничных дней', 'Возраст', 'Пол']] \
        = df['Количество больничных дней,"Возраст","Пол"'].str.split(',', expand=True)
    df.drop('Количество больничных дней,"Возраст","Пол"', axis=1, inplace=True)
    df['Количество больничных дней'] = df['Количество больничных дней'].astype(np.int32)
    df['Возраст'] = df['Возраст'].astype(np.int32)
    return df



if data is not None:
    df = load_data(data)
    st.dataframe(df.head())

hypotheses = st.sidebar.radio('Выберите гипотезу', ['Гипотеза 1', 'Гипотеза 2'])
if hypotheses == 'Гипотеза 1' and data is not None:
    work_days = st.number_input('work_days', value=2, min_value=0, max_value=6)
    df[f'Количество больничных дней от {work_days} дней'] = (df['Количество больничных дней'] > work_days).map(int)
    hyp_1_M = df.loc[
        (df['Пол'] == '"М"'), f'Количество больничных дней от {work_days} дней']
    hyp_1_F = df.loc[
        (df['Пол'] == '"Ж"'), f'Количество больничных дней от {work_days} дней']
    plot(hyp_1_M, hyp_1_F)

    f, p = f_test(hyp_1_M, hyp_1_F)
    st.write(f'Результаты F-теста: ***p={p}***')
    if p >= 0.05:
        st.write('По результатам *F-теста* мы получили значение *p_value* выше чем уровень значимости *a=0.05*.'
                 'Это означает, что у нас есть достаточно доказательств, чтобы сказать, что две дисперсии равны. '
                 'Следовательно, соблюдены все условия для применения статистического критерия Стьюдента')
        t, p_value = sts.ttest_ind(hyp_1_F, hyp_1_M)
        st.write(f'Результаты статистического критерия Стьюдента *t={t}, **p_value={p_value}***')
        testing_hypotheses_1(p_value)
    else:
        st.write('По результатам *F-теста* мы получили значение *p_value* ниже чем уровень значимости *a=0.05*. '
                 'Это означает, что у нас нет достаточных доказательств, чтобы сказать, что две дисперсии равны. '
                 'Следовательно, мы не можем примененить статистический критерий Стьюдента. В этот случае применим '
                 'непараметрический статистический критерий Манна-Уитни')

        # результаты статистического критерия Манна-Уитни
        U, p_value = sts.mannwhitneyu(hyp_1_F, hyp_1_M)
        st.write(f'Результаты статистического критерия Манна-Уитни *U={U}, **p_value={p_value}***')
        testing_hypotheses_1(p_value)

elif hypotheses == 'Гипотеза 2' and data is not None:
    age = st.number_input('age', min_value=0, value=35)
    work_days = st.number_input('work_days', value=2, min_value=0, max_value=6)
    df[f'Количество больничных дней от {work_days} дней'] = (df['Количество больничных дней'] > work_days).map(int)
    hyp_2_1 = df.loc[
        (df['Возраст'] >= age), f'Количество больничных дней от {work_days} дней']
    hyp_2_2 = df.loc[
        (df['Возраст'] < age), f'Количество больничных дней от {work_days} дней']
    plot(hyp_2_1, hyp_2_2)
    f, p = f_test(hyp_2_2, hyp_2_2)
    st.write(f'Результаты F-теста: ***p={p}***')
    if p >= 0.05:
        st.write('По результатам *F - теста* мы получили значение *p_value* выше чем уровень значимости *a=0.05*.'
                 'Это означает, что у нас есть достаточно доказательств, чтобы сказать, что две дисперсии равны. '
                 'Следовательно, соблюдены все условия для применения статистического критерия Стьюдента')
        t, p_value = sts.ttest_ind(hyp_2_1, hyp_2_2)
        st.write(f'Результаты статистического критерия Стьюдента *t={t}, **p_value={p_value}***')
        testing_hypotheses_2(p_value)
    else:
        st.write('По результатам *F-теста* мы получили значение *p_value* ниже чем уровень значимости *a=0.05*. '
                 'Это означает, что у нас нет достаточных доказательств, чтобы сказать, что две дисперсии равны. '
                 'Следовательно, мы не можем примененить статистический критерий Стьюдента. В этот случае применим '
                 'непараметрический статистический критерий Манна-Уитни')
        U, p_value = sts.mannwhitneyu(hyp_2_1, hyp_2_2)
        st.write(f'Результаты статистического критерия Манна-Уитни *U={U}, **p_value={p_value}***')
        testing_hypotheses_2(p_value)
