#!/usr/bin/env python
# coding: utf-8

# In[34]:


print("**CUSTOM EXPLORATION FUNCTIONS")
print("nunique_column_all(df): PRINT NUNIQUE OF ALL COLUMNS")
print("nunique_column_objects(df): PRINT NUNIQUE OF COLUMNS THAT ARE OBJECTS")
print("nunique_column_qty(df): PRINT NUNIQUE OF COLUMNS THAT ARE *NOT* OBJECTS")
print("numeric_range(df): COMPUTE RANGE FOR ALL NUMERIC VARIABLES")
print("")
print("**USEFUL EXPLORATORY CODE**")
print ("DFNAME.head()")
print ("DFNAME.shape")
print ("DFNAME.shape[0] #read row count")
print ("DFNAME.describe().T")
print ("DFNAME.columns.to_list()")
print("DFNAME.COLUMNNAME.value_counts(dropna=False)")
print ("DFNAME.dtypes")
print("DFNAME.select_dtypes(include='object').columns")
print("DFNAME.select_dtypes(include='float').columns")
print("pd.crosstab(DFNAME.COLUMN-1, DFNAME.COLUMN-2)")


# In[ ]:


# PRINT NUNIQUE OF ALL COLUMNS

def nunique_column_all(df):
    for col in df.columns:
        print(df[col].value_counts())
        print()


# In[4]:


# PRINT NUNIQUE OF COLUMNS THAT ARE OBJECTS

def nunique_column_objects(df): 
    for col in df.columns:
        if df[col].dtypes == 'object':
            print(f'{col} has {df[col].nunique()} unique values.')


# In[5]:


# PRINT NUNIQUE OF COLUMNS THAT ARE *NOT* OBJECTS

def nunique_column_qty(df): 
    for col in df.columns:
        if df[col].dtypes != 'object':
            print(f'{col} has {df[col].nunique()} unique values.')


# In[ ]:


# **COMPUTE RANGE FOR ALL NUMERIC VARIABLES**

def numeric_range(df):
    numeric_list = df.select_dtypes(include = 'float').columns.tolist()
    numeric_range = df[numeric_list].describe().T
    numeric_range['range'] = numeric_range['max'] - numeric_range['min']
    return numeric_range


# In[ ]:


# 

