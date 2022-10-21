#!/usr/bin/env python
# coding: utf-8

# <div class="alert alert-info">Example text highlighted in blue (<b>info</b>) background.</div>

# <div class="alert alert-success">Example text highlighted in green (<b>success</b>) background.</div>

# <div class="alert alert-warning">Example text highlighted in yellow (<b>warning</b>) background.</div>

# <div class="alert alert-danger">Example text highlighted in red (<b>danger</b>) background.</div>

# # ----------------**TITANIC DATA** ```FROM SQL```----------------

# In[1]:

import pandas as pd
import numpy as np
import os
from pydataset import data

import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.metrics import classification_report
from env import get_db_url


def new_titanic_data():
    '''
    This function reads the titanic data from the Codeup database into a DataFrame.
    '''
    
    # Create SQL query.
    sql_query = 'SELECT * FROM passengers'
    
    # Read in DataFrame from Codeup database.
    df = pd.read_sql(sql_query, get_db_url('titanic_db'))
    
    return df


# In[2]:


def get_titanic_data():
    '''
    This function reads in titanic data from Codeup database, writes data to
    a csv file if a local file does not exist, and returns a DataFrame.
    '''
    
    
    if os.path.isfile('titanic_df.csv'):
        
        # If csv file exists, read in data from csv file.
        df = pd.read_csv('titanic_df.csv', index_col=0)
        
    else:
        
        # Read fresh data from db into a DataFrame.
        df = new_titanic_data()
        
        # Write DataFrame to a csv file.
        df.to_csv('titanic_df.csv')
        
    return df


# # ----------------**IRIS DATA** ```FROM SQL```----------------

# In[3]:


def new_iris_data():
    '''
    This function reads the iris data from the Codeup database into a DataFrame.
    '''
    
   # Create SQL query.
    sql_query = 'SELECT species_id, species_name, sepal_length, sepal_width, petal_length, petal_width FROM measurements JOIN species USING(species_id)'
    
    # Read in DataFrame from Codeup db.
    df = pd.read_sql(sql_query, get_db_url('iris_db'))
    
    return df


# In[ ]:


def get_iris_data():
    '''
    This function reads in iris data from Codeup database, writes data to
    a csv file if a local file does not exist, and returns a DataFrame.
    '''
    
    if os.path.isfile('iris_df.csv'):
        
        # If csv file exists read in data from csv file.
        df = pd.read_csv('iris_df.csv', index_col=0)
        
    else:
        
        # Read fresh data from db into a DataFrame
        df = new_iris_data()
        
        # Cache data
        df.to_csv('iris_df.csv')
        
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

