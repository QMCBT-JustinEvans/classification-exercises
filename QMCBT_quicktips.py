#!/usr/bin/env python
# coding: utf-8

# <div class="alert alert-info">Example text highlighted in blue (<b>info</b>) background.</div>

# <div class="alert alert-success">Example text highlighted in green (<b>success</b>) background.</div>

# <div class="alert alert-warning">Example text highlighted in yellow (<b>warning</b>) background.</div>

# <div class="alert alert-danger">Example text highlighted in red (<b>danger</b>) background.</div>

# **POSITIVE (+)** = insert Positive statement here  
# **NEGATIVE (-)** = insert Negative statement here  
# 
# **RECALL**  
# TP / (TP + FN)  
# Use for less **Type II** errors when **FN** is worst outcome  
# Maximize for **RECALL** if Cost of **FN** > Cost of **FP**  
# 
# **PRECISION**  
# TP / (TP + FP)  
# Use for less **Type I** errors when **FP** is worst outcome  
# Maximize for **PRECISION** if Cost of **FP** > Cost of **FN**  
# 
# **ACCURACY**  
# (TP + TN)/(FP+FN+TP+TN)  
# total # prediction TRUE / total  
# Maximize for **ACCURACY** if neither **RECALL** or **PRECISION** outweigh eachother  
# 
# * **Classification Confusion Matrix** (actual_col, prediction_row)(Positive_first, Negative_second)
# |                     | actual Positive (+) | actual Negative(-) |
# |---------------------|---------------------|--------------------|
# |  pred Positive (+)  |     TP              |     FP (Type I)    |
# |  pred Negative (-)  |     FN (Type II)    |     TN             |  
# 
# * <b>sklearn Confusion Matrix</b> (prediction_col, actual_row)(Negative_first, Positive_second)
# |                     | pred Negative(-) | pred Positive (+) |
# |---------------------|------------------|-------------------|
# | actual Negative (-) |        TN        |    FP (Type I)    |
# | actual Positive (+) |   FN (Type II)   |         TP        |  
# 
# **FP**: We **predicted** it was a **POSITIVE** when it was **actually** a **NEGATIVE**  
# *    FP = We **FALSE**LY predicted it was **POSITIVE**  
# * False = Our prediction was False, it was actually the opposite of our prediction  
# * Oops... **TYPE I** error!  
# 
# **FN**: We **predicted** it was a **NEGATIVE** when it was **actually** a **POSITIVE**  
# *    FN = We **FALSE**LY predicted it was **NEGATIVE**  
# * False = Our prediction was False, it was actually the opposite of our prediction  
# * Oops... **TYPE II** error!  
# 
# **TP**: We **predicted** it was a **POSITIVE** and it was **actually** a **POSITIVE**  
# *   TP = We **TRUE**LY predicted it was **POSITIVE**  
# * True = Our prediction was True, it was actually the same as our prediction  
# 
# **TN**: We **predicted** it was a **NEGATIVE** and it was **actually** a **NEGATIVE**  
# *   TN = We **TRUE**LY predicted it was **NEGATIVE**  
# * True = Our prediction was True, it was actually the same as our prediction  

# **A. Set Hypothesis**  
# 
# * One Tail (```<= | >```) or Two Tails (```== | !=```)?\
#  **two_tail (gender, been_manager)**  
# 
# 
# * One Sample or Two Samples?\
#  **two_sample (gender, been_manager)**  
# 
# 
# * Continuous or Discreat?\
#  **Discreat (gender) vs Discreat (been_manager) = $Chi^2$**  
#      * T-Test = ```Discreat``` vs ```Continuous```
#      * Pearson’s = ```Continuous``` vs ```Continuous``` (linear)
#      * $Chi^2$ = ```Discreat``` vs ```Discreat```
# 
# 
# * $𝐻_0$: The opposite of what I am trying to prove\  
#  **$H_{0}$: The employee gender is **NOT** ```dependent``` on whether the employee has been a manager**\
#  ```employees.gender ``` != ```employees.been_manager```  
# 
# 
# * $𝐻_𝑎$: What am I trying to prove\  
#  **$H_{a}$: The employee gender is ```dependent``` on whether the employee has been a manager**\  
#  ```employees.gender ``` == ```employees.been_manager```

# ```
# _______________________________________________________________
# |                              DF                             |
# |-------------------|-------------------|---------------------|
# |       Train       |       Validate    |          Test       |
# |-------------------|-------------------|-----------|---------|
# | x_train | y_train |   x_val  |  y_val |   x_test  |  y_test |
# |-------------------------------------------------------------|
# ```
# * 1. tree_1 = DecisionTreeClassifier(max_depth = 5)
# * 2. tree_1.fit(x_train, y_train)
# * 3. predictions = tree_1.predict(x_train)
# * 4. pd.crosstab(y_train, predictions)
# * 5. val_predictions = tree_1.predict(x_val)
# * 6. pd.crosstab(y_val, val_predictions)

# In[ ]:


# dir(acquire)


# ['__builtins__',
#  '__cached__',
#  '__doc__',
#  '__file__',
#  '__loader__',
#  '__name__',
#  '__package__',
#  '__spec__',
#  'data',
#  'get_db_url',
#  'get_iris_sns_df',
#  'get_iris_sql_df',
#  'get_telco_churn_df',
#  'get_titanic_df',
#  'new_iris_sns_df',
#  'new_iris_sql_df',
#  'new_telco_churn_df',
#  'new_titanic_df',
#  'np',
#  'os',
#  'pd',
#  'sns']
