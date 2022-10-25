#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
import seaborn as sns
import os
from pydataset import data
from env import get_db_url
import warnings 
warnings.filterwarnings("ignore")


# # ----------------**TITANIC DATA** ```FROM SQL```----------------

# In[1]:


def new_titanic_df():
    '''
    This function reads the titanic data from the Codeup database into a DataFrame.
    '''
   
    # Create SQL query.
    sql_query = 'SELECT * FROM passengers'
    
    # Read in DataFrame from Codeup database.
    df = pd.read_sql(sql_query, get_db_url('titanic_db'))
    
    return df


# In[2]:


def get_titanic_df():
    '''
    This function reads in titanic data from Codeup database, writes data to
    a csv file if a local file does not exist, and returns a DataFrame.
    '''
    
    if os.path.isfile('titanic_df.csv'):
        
        # If csv file exists, read in data from csv file.
        df = pd.read_csv('titanic_df.csv', index_col=0)
        
    else:
        
        # Read fresh data from db into a DataFrame.
        df = new_titanic_df()
        
        # Write DataFrame to a csv file.
        df.to_csv('titanic_df.csv')
        
    return df


# # ----------------**IRIS DATA** ```FROM SQL```----------------

# In[3]:


def new_iris_sql_df():
    '''
    This function reads the iris data from the Codeup database into a DataFrame.
    '''
    
    # Create SQL query.
    sql_query = 'SELECT species_id, species_name, sepal_length, sepal_width, petal_length, petal_width FROM measurements JOIN species USING(species_id)'
    
    # Read in DataFrame from Codeup db.
    df = pd.read_sql(sql_query, get_db_url('iris_db'))
    
    return df


# In[ ]:


def get_iris_sql_df():
    '''
    This function reads in iris data from Codeup database, writes data to
    a csv file if a local file does not exist, and returns a DataFrame.
    '''

    if os.path.isfile('iris_sql_df.csv'):
        
        # If csv file exists read in data from csv file.
        df = pd.read_csv('iris_sql_df.csv', index_col=0)
        
    else:
        
        # Read fresh data from db into a DataFrame
        df = new_iris_sql_df()
        
        # Cache data
        df.to_csv('iris_sql_df.csv')
        
    return df


# # ----------------**IRIS DATA** ```from seaborn```----------------

# In[4]:


def new_iris_sns_df():
    '''
    This function reads the iris data from the seaborn database into a DataFrame.
    '''
    
    # Read in DataFrame from pydata db.
    df = sns.load_dataset('iris')
    
    return df


# In[ ]:


def get_iris_sns_df():
    '''
    This function reads in iris data from seaborn database, writes data to
    a csv file if a local file does not exist, and returns a DataFrame.
    '''
  
    if os.path.isfile('iris_sns_df.csv'):
        
        # If csv file exists read in data from csv file.
        df = pd.read_csv('iris_sns_df.csv', index_col=0)
        
    else:
        
        # Read fresh data from db into a DataFrame
        df = new_iris_sns_df()
        
        # Cache data
        df.to_csv('iris_sns_df.csv')
        
    return df


# # ----------------**Telco_Churn DATA** ```FROM SQL```----------------

# In[ ]:


def new_telco_churn_df():
    '''
    This function reads the telco_churn (NOT telco_normalized) data from the Codeup database into a DataFrame.
    '''
    # Create SQL query.
    sql_query = 'SELECT * FROM customers LEFT JOIN internet_service_types USING (internet_service_type_id) LEFT JOIN contract_types USING (contract_type_id) LEFT JOIN payment_types USING (payment_type_id);'
    
    # Read in DataFrame from Codeup db.
    df = pd.read_sql(sql_query, get_db_url('telco_churn'))
    
    return df


# In[ ]:


def get_telco_churn_df():
    '''
    This function reads in telco_churn (NOT telco_normalized) data from Codeup database, writes data to
    a csv file if a local file does not exist, and returns a DataFrame.
    '''
    if os.path.isfile('telco_churn_df.csv'):
        
        # If csv file exists read in data from csv file.
        df = pd.read_csv('telco_churn_df.csv', index_col=0)
        
    else:
        
        # Read fresh data from telco db into a DataFrame
        df = new_telco_churn_df()
        
        # Cache data
        df.to_csv('telco_churn_df.csv')
        
    return df

