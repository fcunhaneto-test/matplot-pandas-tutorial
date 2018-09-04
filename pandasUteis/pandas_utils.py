import numpy as np
import pandas as pd

def frequency_by_natural_order(dataframe, column):
    """
    Create a dataframe that gives the total by natural order, frequencies,
    accumulated total and frequency per item.
    Dataframe output example:

        tot  freq  tot_ac  freq_ac
    17    9  0.18       9     0.18
    18   22  0.44      31     0.62
    19    7  0.14      38     0.76
    20    4  0.08      42     0.84
    21    3  0.06      45     0.90
    23    2  0.04      47     0.94
    24    1  0.02      48     0.96
    25    2  0.04      50     1.00

    :param dataframe:
    :param column:
    :return: dataframe
    """
    s_ini = dataframe[column]
    s_sum = s_ini.value_counts()
    s_sort = s_sum.sort_index()

    s_tot = s_sort.sum()
    tot_ac = s_sort.cumsum()

    freq = np.array(s_sort) / s_tot
    freq_ac = freq.cumsum()

    df = pd.DataFrame({
        'tot': s_sort,
        'freq': freq,
        'tot_ac': tot_ac,
        'freq_ac': freq_ac,
    })

    return df