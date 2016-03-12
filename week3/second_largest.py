import numpy as np
import pandas as pd

df = pd.DataFrame({
    'a': [4, 5, 3, 1, 2],
    'b': [20, 10, 40, 50, 30],
    'c': [25, 20, 5, 15, 10]
})
print df
# Change False to True for this block of code to see what it does

# DataFrame apply() - use case 2
if False:
    print df.apply(np.mean)
    print df.apply(np.max)
#
def second_largest(column):
    largest = max(column)
    second_largest = None
    for value in column:
        if value > second_largest and value < largest:
            second_largest = value

    return second_largest
print second_largest(df["c"])

def second_largest2(column):
    sorted_column = column.sort_values(ascending=False)
    return sorted_column.iloc[1]

print second_largest2(df["c"])


def second_largest(df):
    '''
    Fill in this function to return the second-largest value of each
    column of the input DataFrame.
    '''
    return df.apply(second_largest2)

print second_largest(df)