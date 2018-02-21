#This is the logistic regression algorithm. Here we impose a penalty of 10 for misclassifying a 0, and a penalty of 1 for misclassifying a 1. This is compensate for the fact that we are looking at an unbalanced data set. 

# Importing necessary packages
import pandas as pd
from sklearn.model_selection import cross_val_predict, KFold
from sklearn.linear_model import LogisticRegression

# Reading in the cleaned data
loans = pd.read_csv('clean_data.csv')


penalty = {0:10, 1:1} #The penalty dictionary


lr = LogisticRegression(class_weight=penalty)

kf = KFold(features.shape[0], random_state=1)

predictions = cross_val_predict(lr, features,target, cv=kf)

predictions = pd.Series(predictions)

# False positives.
fp_filter = (predictions == 1) & (loans["loan_status"] == 0)
fp = len(predictions[fp_filter])

# True positives.
tp_filter = (predictions == 1) & (loans["loan_status"] == 1)
tp = len(predictions[tp_filter])

# False negatives.
fn_filter = (predictions == 0) & (loans["loan_status"] == 1)
fn = len(predictions[fn_filter])

# True negatives
tn_filter = (predictions == 0) & (loans["loan_status"] == 0)
tn = len(predictions[tn_filter])

# Rates
tpr = float(tp) / float(tp + fn)  # true positive rate
fpr = float(fp) / float(fp + tn)  # false positive rate 

print(tpr)
print(fpr)
