#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np

# import splitting functions
from sklearn.model_selection import train_test_split


# In[2]:


def prep_iris_df(iris_df):
    iris_df = iris_df.drop(columns='species_id')
    iris_df = iris_df.rename(columns={'species_name': 'species'})
    dummy_iris_df = pd.get_dummies(iris_df.species, drop_first=True)
    iris_df = pd.concat([iris_df, dummy_iris_df], axis=1)
    return iris_df


# In[ ]:


def prep_titanic_df(titanic_df):
    titanic_df = titanic_df.drop(columns=['passenger_id', 'class', 'deck'])
    dummy_df = pd.get_dummies(data=titanic_df['sex'], drop_first=True)
    dummy_df2 = pd.get_dummies(data=titanic_df['embark_town'], drop_first=False)
    titanic_df = pd.concat([titanic_df, dummy_df, dummy_df2], axis=1)
    return titanic_df


# In[ ]:


def prep_telco_churn_df(telco_churn_df):
    telco_churn_df = telco_churn_df.drop(columns=['payment_type_id', 'contract_type_id', 
                                              'internet_service_type_id', 'customer_id'])
    encoded_df = pd.DataFrame()
    encoded_df['male_encoded'] = telco_churn_df.gender.map({'Male': 1, 'Female': 0})
    encoded_df['partner_encoded'] = telco_churn_df.partner.map({'Yes': 1, 'No': 0})
    encoded_df['dependents_encoded'] = telco_churn_df.dependents.map({'Yes': 1, 'No': 0})
    encoded_df['phone_service_encoded'] = telco_churn_df.phone_service.map({'Yes': 1, 'No': 0})
    encoded_df['multiple_lines_encoded'] = telco_churn_df.phone_service.map({'Yes': 1, 'No': 0})
    encoded_df['online_security_encoded'] = telco_churn_df.phone_service.map({'Yes': 1, 'No': 0})
    encoded_df['online_backup_encoded'] = telco_churn_df.phone_service.map({'Yes': 1, 'No': 0})
    encoded_df['device_protection_encoded'] = telco_churn_df.phone_service.map({'Yes': 1, 'No': 0})
    encoded_df['streaming_tv_encoded'] = telco_churn_df.phone_service.map({'Yes': 1, 'No': 0})
    encoded_df['streaming_movies_encoded'] = telco_churn_df.phone_service.map({'Yes': 1, 'No': 0})
    encoded_df['paperless_billing_encoded'] = telco_churn_df.paperless_billing.map({'Yes': 1, 'No': 0})
    encoded_df['churn_encoded'] = telco_churn_df.churn.map({'Yes': 1, 'No': 0})
    encoded_df['tech_support_encoded'] = telco_churn_df.churn.map({'Yes': 1, 'No': 0})
    encoded_cols = encoded_df.columns

    dummy_df = pd.get_dummies(data=telco_churn_df[['internet_service_type', 
                                                   'contract_type', 
                                                   'payment_type'
                                                  ]], drop_first=False)
    
    telco_churn_df = pd.concat([telco_churn_df, encoded_df, dummy_df], axis=1)
    
    drop_cols = ['gender', 'partner', 'dependents', 'phone_service', 'multiple_lines', 
             'online_security', 'online_backup', 'device_protection', 'streaming_tv', 
             'streaming_movies', 'paperless_billing', 'churn', 'internet_service_type', 
             'contract_type', 'payment_type', 'tech_support']
    
    telco_churn_df = telco_churn_df.drop(columns = drop_cols)
    
    return telco_churn_df.T


# In[4]:


def train_val_test_split(df, target):
    train, test = train_test_split(df, test_size=.2, random_state=1992, stratify = df[target])
    train, validate = train_test_split(train, test_size=.25, random_state=1992, stratify = train[target])
    print('_______________________________________________________________')
    print('|                              DF                             |')
    print('|-------------------|-------------------|---------------------|')
    print('|       Train       |       Validate    |          Test       |')
    print('|-------------------|-------------------|-----------|---------|')
    print('| x_train | y_train |   x_val  |  y_val |   x_test  |  y_test |')
    print('|-------------------------------------------------------------|')
    print('')
    print('* 1. tree_1 = DecisionTreeClassifier(max_depth = 5)')
    print('* 2. tree_1.fit(x_train, y_train)')
    print('* 3. predictions = tree_1.predict(x_train)')
    print('* 4. pd.crosstab(y_train, predictions)')
    print('* 5. val_predictions = tree_1.predict(x_val)')
    print('* 6. pd.crosstab(y_val, val_predictions)')
    return train, validate, test


# In[ ]:




