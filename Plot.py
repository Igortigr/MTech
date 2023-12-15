import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
def plot(arr1, arr2, hyp=1):
    '''Функция для визуализации данных'''

    name1 = 'Мужчины'
    name2 = 'Женщины'
    if hyp == 2:
        name1 = 'age >= 35'
        name2 = 'age < 35'
    fig = plt.figure(figsize=(20, 10))
    fig.add_subplot(2, 2, 1)
    sns.histplot(arr1)
    plt.title(name1)

    fig.add_subplot(2, 2, 2)
    plt.title(name2)
    sns.histplot(arr2)

    fig.add_subplot(2, 2, 3)
    plt.title('Объединенный график')
    sns.histplot(arr1)
    sns.histplot(arr2)
    st.pyplot(fig)
