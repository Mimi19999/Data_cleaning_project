# Import library
import numpy as np
import pandas as pd

# Load data
df_foodchoice = pd.read_csv('/Users/mimi/Downloads/archive/food_coded.csv')
print(df_foodchoice.head(10))
print(df_foodchoice.tail(10))
print(df_foodchoice.columns)

# Change into same decimal numbers in columns with float values
df_foodchoice['GPA'] = pd.to_numeric(df_foodchoice['GPA'], errors='coerce')
print(df_foodchoice['GPA'])
def round_df_columns(df, columns, decimals):
    rounded_df = df.copy()    
    rounded_df[columns] = rounded_df[columns].round(decimals)
    return rounded_df
float_cols = df_foodchoice.select_dtypes(include=np.float64).columns
rounded_df_foodchoice = round_df_columns(df_foodchoice, float_cols, 2)
print(rounded_df_foodchoice)

# Count missing values
def missing_values(df):
    # Get missing values in each column
    missing = df.isnull().sum()
    # Get the percentage of missing values in each column
    percent_missing = (missing/len(df)) * 100
    # Combine these result into dataframe
    missing_results = pd.DataFrame({
        'Sum_missing': missing,
        'Percent_missing': percent_missing
    })
    return missing_results
missing_results = missing_values(rounded_df_foodchoice)
print(missing_results)
print(rounded_df_foodchoice.describe())

# Dealing columns has NA values > 9 NA values
row_with_missing = missing_results.loc[missing_results['Sum_missing'] > 8]
print(row_with_missing)

print(rounded_df_foodchoice['calories_day'].value_counts())
rounded_df_foodchoice['calories_day'].fillna(1, inplace=True)

print(rounded_df_foodchoice['comfort_food_reasons_coded'].value_counts())
rounded_df_foodchoice['comfort_food_reasons_coded'].fillna(9, inplace=True)

print(rounded_df_foodchoice['cuisine'].value_counts())
rounded_df_foodchoice['cuisine'].fillna(6, inplace=True)

print(rounded_df_foodchoice['employment'].value_counts())
rounded_df_foodchoice['employment'].fillna(4, inplace=True)

print(rounded_df_foodchoice['exercise'].value_counts())
rounded_df_foodchoice['exercise'].fillna(5, inplace=True)

print(rounded_df_foodchoice['type_sports'].value_counts())
rounded_df_foodchoice['type_sports'].fillna('none', inplace=True)





