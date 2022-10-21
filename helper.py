# import image module
from IPython.display import Image
  

# ------ Display confusion matrix function ------
def matrix():

# get the image
    return Image(url="confusion_matrix.png", width=920, height=474)



# ------ Print standard import functions for quick use ------
def imports():

    print('''
# standardized modules
import seaborn as sns
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import scipy.stats as stats
from sklearn.model_selection import train_test_split

# Decision Tree and Model Evaluation Imports
from sklearn.tree import DecisionTreeClassifier, plot_tree, export_text
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, plot_confusion_matrix

#my modules
import acquire as ac
import prepare as pp)''')