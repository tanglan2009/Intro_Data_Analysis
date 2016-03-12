import pandas as pd

# Adding using +
if False:
    s = pd.Series([1, 2, 3, 4])
    df = pd.DataFrame({
        0: [10, 20, 30, 40],
        1: [50, 60, 70, 80],
        2: [90, 100, 110, 120],
        3: [130, 140, 150, 160]
    })
    
    print df
    print '' # Create a blank line between outputs
    print df + s
    
# Adding with axis='index'
if False:
    s = pd.Series([1, 2, 3, 4])
    df = pd.DataFrame({
        0: [10, 20, 30, 40],
        1: [50, 60, 70, 80],
        2: [90, 100, 110, 120],
        3: [130, 140, 150, 160]
    })
    
    print df
    print '' # Create a blank line between outputs
    print df.add(s, axis='index')
    # The functions sub(), mul(), and div() work similarly to add()
    
# Adding with axis='columns'
if True:
    s = pd.Series([1, 2, 3, 4])
    df = pd.DataFrame({
        0: [10, 20, 30, 40],
        1: [50, 60, 70, 80],
        2: [90, 100, 110, 120],
        3: [130, 140, 150, 160]
    })
    print df
    print '' # Create a blank line between outputs
    print df.add(s, axis='columns')
    # The functions sub(), mul(), and div() work similarly to add()
    
grades_df = pd.DataFrame(
    data={'exam1': [43, 81, 78, 75, 89, 70, 91, 65, 98, 87],
          'exam2': [24, 63, 56, 56, 67, 51, 79, 46, 72, 60]},
    index=['Andre', 'Barry', 'Chris', 'Dan', 'Emilio', 
           'Fred', 'Greta', 'Humbert', 'Ivan', 'James']
)
print grades_df

def standardize(df):
    '''
    Fill in this function to standardize each column of the given
    DataFrame. To standardize a variable, convert each value to the
    number of standard deviations it is above or below the mean.

    This time, try to use vectorized operations instead of apply().
    You should get the same results as you did before.
    '''
    # print df.sum(axis='index')
    # print grades_df.count(axis='index')
    mean = df.sum(axis='index')/df.count(axis='index')
    # print (grades_df - mean_grades)/grades_df.std()
    return (df - mean)/df.std(ddof=0)
print standardize(grades_df)

def standardize_rows(df):
    '''
    Optional: Fill in this function to standardize each row of the given
    DataFrame. Again, try not to use apply().

    This one is more challenging than standardizing each column!
    '''
    # mean_along_row = df.sum(axis="columns")/df.count(axis="columns")
    # print mean_along_row
    # print df.sub(mean_along_row, axis='index')
    # print df.sub(mean_along_row, axis='index')/df.std(ddof=0)
    # print (df-mean_along_row)/df.std(axis="index")
    # print mean_along_row/df.std(axis="columns")
    mean_diffs = df.sub(df.mean(axis= "columns"), axis="index")
    return mean_diffs.div(df.std(axis = "columns"),axis="index")
print standardize_rows(grades_df)
df = pd.DataFrame(
    {0: [95, 85, 75, 65, 55], 1: [94, 84, 74, 64, 54]},
    index=[0, 1, 2, 3, 4]
)
print standardize_rows(df)