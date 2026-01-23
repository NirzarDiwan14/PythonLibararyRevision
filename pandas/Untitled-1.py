# %%
import pandas as pd

# %%
df = pd.read_csv("raw_data.csv")
df

# %%
#help understanding the data 
df.head(10)
df.tail(11)
df.info()

# %%
df.describe()

# %%
df[['order_amount',"payment_mode"]]

# %%
condition = df[(df['order_amount'] > 20) & (df['payment_mode'] == "Cash")]
len(condition)

# %% [markdown]
# #Part -2 

# %%
#adding data frame 
# way-1 = straight-forward way 
df['new_data'] = [i +  2 for i in range(len(df))]
df

# %%
#way-2 = using insert method

# syntax = df.insert(location,"Column_name",data)
data = [[i + 3] for i in range(len(df))]

df.insert(2,"new_data_2",data)
df



# %%
#Updating the vaalues 
# df.loc(rowIndex,"col_name") = new_value


df.loc[0,"payment_mode"] = "Cash"
df

# %%
#removing 
# syntax = df.drop(columns = ["column_name"],inplace = True/False)
df.drop(columns = ['new_data_2'],inplace = True) # it will modify it in-place
df

# %%
#handling missing data 

#syntax - isnull().sum()

df.isnull().sum()

# %%
# 1. removing missing value 
print(df)
df.dropna(axis = 1, inplace = True)
print(df)

# %%
# 2. filling missing values 

df.fillna(40,inplace = True)
df


# %%
# data interpolation  = adding data using existing values 
# example - linear interpolation ,etc 
# it is used for data intergrity ,for smooth trends ,avoid data loss 

df = pd.read_csv("raw_data.csv")
print(df)
# types = linear , polynomial ,time etc 
df.interpolate(method = "linear",axis  = 0,inplace = True)
df

# %%
#sorting data 

 #single 
#  df.sort_values(by = "order_amount",ascending = True,inplace = True)
df.sort_values(by = ["order_date","order_amount"],ascending = [True,True],inplace = True) #multiple 
df

# %%
#aggreagation of data = it involves calculating statistics regarding the data
print(df['order_amount'].min())
print(df['order_amount'].max())
print(df['order_amount'].mean())
print(df['order_amount'].std())
print(df['order_amount'].sum())
print(df['order_amount'].count())





# %%
#grouping  -- very imp 
df.groupby("payment_mode")['order_amount'].sum()

# %%
#merging and joining 
# how = left =gives data from right only and add Nan into right cols missing data ,right , outer,inner,cross

df = pd.merge(df,df,on = "user_id",how = "right")
df

# %%
# concatination of data 
# 1. vertically , 2. horizontally  
# syntax = pd.concate([df1,df2],axis = 0,ignore_index = True)




