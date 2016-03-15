import numpy as np
import pandas as pd

values = np.array([1, 3, 2, 4, 1, 6, 4])
example_df = pd.DataFrame({
    'value': values,
    'even': values % 2 == 0,
    'above_three': values > 3
}, index=['a', 'b', 'c', 'd', 'e', 'f', 'g'])
print example_df
# Change False to True for each block of code to see what it does

# Standardize each group
if True:
    def standardize(xs):
        return (xs - xs.mean()) / xs.std()
    grouped_data = example_df.groupby('even')
    print grouped_data['value'].apply(standardize)

# Find second largest value in each group
if True:
    def second_largest(xs):
        sorted_xs = xs.sort(inplace = False, ascending=False)
        return sorted_xs.iloc[1]
    grouped_data = example_df.groupby('even')
    print grouped_data['value'].apply(second_largest)

ridership_df = pd.DataFrame({
    'UNIT': ['R051', 'R079', 'R051', 'R079', 'R051', 'R079', 'R051', 'R079', 'R051'],
    'TIMEn': ['00:00:00', '02:00:00', '04:00:00', '06:00:00', '08:00:00', '10:00:00', '12:00:00', '14:00:00', '16:00:00'],
    'ENTRIESn': [3144312, 8936644, 3144335, 8936658, 3144353, 8936687, 3144424, 8936819, 3144594],
    'EXITSn': [1088151, 13755385,  1088159, 13755393,  1088177, 13755598, 1088231, 13756191,  1088275]
})
print ridership_df
def get_hourly_entries_and_exits_perSet(entries_and_exits):

    hourly_entries_and_exits = entries_and_exits- entries_and_exits.shift(1)
    return hourly_entries_and_exits


def get_hourly_entries_and_exits(entries_and_exits):
    '''
    Fill in this function to take a DataFrame with cumulative entries
    and exits and return a DataFrame with hourly entries and exits.
    The hourly entries and exits should be calculated separately for
    each station (the 'UNIT' column).
    '''
    grouped_subway_data = entries_and_exits.groupby("UNIT")
    return grouped_subway_data[["ENTRIESn","EXITSn"]].apply(get_hourly_entries_and_exits_perSet)
print get_hourly_entries_and_exits( ridership_df)