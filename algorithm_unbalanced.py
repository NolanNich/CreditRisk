#This is the logistic regression algorithm. The data is unbalanced, and have much more loans that are paid off than are defaulted on. This results in a large false positive rate. 

# Importing necessary packages
import pandas as pd
from sklearn.model_selection import cross_val_predict, KFold
from sklearn.linear_model import LogisticRegression

# Reading in the cleaned data
loans = pd.read_csv('clean_data.csv')

features = loans.drop("loan_status", axis=1)

target = loans["loan_status"]

lr = LogisticRegression()
kf = KFold(features.shape[0], random_state=1)


predictions = cross_val_predict(lr, features,target,cv=kf)
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

# True positive and false positive rates
tpr = tp / (tp + fn)
fpr = fp / (fp + tn)

print(tpr)
print(fpr)
