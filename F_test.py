import numpy as np
import scipy.stats as sts
def f_test(x, y):
    '''Функция, рассчитывающая статистику F-теста и соответсвующее значение p_value'''

    f = np.var(x, ddof=1) / np.var(y, ddof=1)
    dfn = x.size - 1
    dfd = y.size - 1
    p = 1 - sts.f.cdf(f, dfn, dfd)
    return f, p