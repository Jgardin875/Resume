#!/usr/bin/env python
# coding: utf-8

# # Modeling

# - Last observed value
# - Simple average
# - Moving average
# - Holt's Linear Trend
# - Previous cycle

# In[1]:


# for presentation purposes
import warnings
warnings.filterwarnings("ignore")

import numpy as np
import pandas as pd

# visualize 
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
# wrangle
#import acquire
import prepare

# working with dates
from datetime import datetime

# to evaluated performance using rmse
from sklearn.metrics import mean_squared_error
from math import sqrt 

# for tsa 
import statsmodels.api as sm

# holt's linear trend model. 
from statsmodels.tsa.api import Holt

# facebook prophet model
#from prophet import Prophet


# # Wrangle

# ### Let's plot our data, viewing where the data is split into train and test.

# # Evaluation Functions

# In[2]:


def evaluate(target_var, val, yhat):
    '''
    This function will take the actual values of the target_var from validate, 
    and the predicted values stored in yhat_df, 
    and compute the rmse, rounding to 0 decimal places. 
    it will return the rmse. 
    '''
    rmse = round(sqrt(mean_squared_error(val[target_var], yhat[target_var])), 0)
    return rmse


# In[7]:


def plot_and_eval(target_var, train, val, yhat):
    '''
    This function takes in the target var name (string), and returns a plot
    of the values of train for that variable, validate, and the predicted values from yhat_df. 
    it will als lable the rmse. 
    '''
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=train.index, y=train.views,
                        mode='lines',
                        name='train', marker = dict(color = '#D7B1FA')))
    fig.add_trace(go.Scatter(x=val.index, y=val.views,
                        mode='lines',
                        name='validate', marker = dict(color = '#6975AB')))
    fig.add_trace(go.Scatter(x=yhat.index, y=yhat.views,
                        mode='lines',
                        name='prediction', marker = dict(color = '#E80F88')))


    fig.update_layout(paper_bgcolor="#202020", plot_bgcolor='#202020', font_color='#f3e2fe', font_size = 16)

    fig.show()
    rmse = evaluate(target_var, val, yhat)
    print(target_var, '-- RMSE: {:.0f}'.format(rmse))


# In[ ]:





# Write `append_eval_df(model_type)` to append evaluation metrics for each model type, target variable, and metric type, along with the metric value into our `eval_df` data frame object. Which we will create an empty `eval_df` dataframe object to start.

# In[4]:


# create an empty dataframe
eval_df = pd.DataFrame(columns=['model_type', 'target_var', 'rmse'])
eval_df


# In[5]:


# function to store the rmse so that we can compare
def append_eval_df(val, yhat, model_type, target_var):
    '''
    this function takes in as arguments the type of model run, and the name of the target variable. 
    It returns the eval_df with the rmse appended to it for that model and target_var. 
    '''
    rmse = evaluate(target_var, val, yhat)
    d = {'model_type': [model_type], 'target_var': [target_var],
        'rmse': [rmse]}
    d = pd.DataFrame(d)
    return eval_df.append(d, ignore_index = True)


# In[6]:


def make_predictions(val, views=None, likes=None):
    yhat_df = pd.DataFrame({'views': [views],
                           'likes': [likes]},
                          index=val.index)
    return yhat_df


# # Forecasting

# In[ ]:




