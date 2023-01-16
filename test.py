import pandas as pd

df = pd.read_csv("cas_QC.csv", sep=",")

#print(df.columns)

time_lines =  ['4.25', '4.26', '4.27', '4.28', '4.29', '4.30', '5.01',
                '5.02', '5.03', '5.04', '5.05', '5.06', '5.07', '5.08']

df1 = pd.melt(df,id_vars=['regions'],
    value_vars= time_lines,
    var_name='day',value_name='n_cas', ignore_index=False)

df1.sort_values(["day","regions"], inplace=True)

print(df1)

