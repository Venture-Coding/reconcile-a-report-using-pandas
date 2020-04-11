# --------------

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Code starts here
df=pd.read_csv(path)
df['state']=df['state'].apply(lambda x:x.lower())
 
df['total']=df['Jan']+df['Feb']+df['Mar']
sum_row=df[['Jan','Feb','Mar','total']].sum()



df_final=pd.DataFrame()
df_final=df.append(sum_row,ignore_index=True)
 


# Code ends here


# --------------
import requests

# Code starts here
url="https://en.wikipedia.org/wiki/List_of_U.S._state_abbreviations"
response=requests.get(url)
df1=pd.read_html(response.content)[0]
 
df1=df1.iloc[11:,:]
df1.columns=df1.iloc[0]
df1=df1.iloc[1:,:]
print(df1.head())
df1['United States of America']=df1['United States of America'].apply(lambda s:s.replace(" ", ""))




# Code ends here


# --------------
df1['United States of America'] = df1['United States of America'].astype(str).apply(lambda x: x.lower())
df1['US'] = df1['US'].astype(str)

# Code starts here
mapping = df1.set_index('United States of America')['US'].to_dict()
print(mapping)
 
df_final['abbr'] = df_final['state'].map(mapping)


# Code ends here


# --------------
# Code stars here
print(df_final[(df_final['abbr'].isnull()) & (df_final['state']=='mississippi')])
 
df_final.loc[(df_final['abbr'].isnull()) & (df_final['state']=='mississipi'), 'abbr'] = 'MS'
df_final.loc[(df_final['abbr'].isnull()) & (df_final['state']=='tenessee'), 'abbr'] = 'TN'



# Code ends here


# --------------
# Code starts here

df_sub = df_final.groupby('abbr')[['Jan','Feb' ,'Mar']].sum().reset_index()
print(df_sub.head())

formatted_df = df_sub.applymap(lambda x: '$'+ str(x) )

print(formatted_df)




# Code ends here


# --------------
# Code starts here
sum_row=df[['Jan','Feb','Mar']].sum()
 
df_sub_sum=pd.DataFrame(data=sum_row).T
 
df_sub_sum=df_sub_sum.applymap(lambda x: '$'+ str(x) )
 
final_table=formatted_df.append(df_sub_sum)

print(final_table.head())
final_table.rename(index = {0: "Total"}) 


# Code ends here


# --------------
# Code starts here
df_sub['total']=df['Jan']+df['Feb']+df['Mar']
 
df_sub.plot.pie(y='total', figsize=(5, 5))

# Code ends here


