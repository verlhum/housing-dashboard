import statsmodels.api as sm
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from data_cleaning import *
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.ensemble import GradientBoostingRegressor

df = pd.read_csv(r"~/housing/combined_data.csv", low_memory=False)
df.drop(columns=['APN', 'Add Rec', 'Situs', 'PriorPID', 'Addl Owner', 'City', 'LegalDesc','Mailing1', 'Mailing2', 'Owner1', 'Owner1', 'PriorOwner', 'RecDoc', 'State', 'Zip', 'Subdivision'],
        inplace=True)

building_types = ['Townhse Ins', 'Townhse End', 'Sgl Fam Res ', 'MH Real Prop']

df = df[df['BldgType'].isin(building_types)]

# Update the date parsing with automatic format detection
df['Sales Date'] = pd.to_datetime(df['Sales Date'], errors='coerce')

# Include the quarter of sale in the data
df['Sales Quarter'] = df['Sales Date'].dt.strftime('%Y-Q') + df['Sales Date'].dt.quarter.astype(str)

y = np.log(df['Sale Price'])

# gather the X values that will be used in the regression
X = df[inclusion_test(df.drop(columns=['Sales Date']), target_column='Sale Price')]

# Normalize the numerical values of X
X = normalize_non_normal_columns(X)

# Encode the categorical data
X = preprocessing_categorical_data(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=2008)

print('after split')
# Dimentionality reduction on X
pca = PCA(n_components=35)
X_train_pca = pca.fit_transform(X_train)
X_test_pca = pca.transform(X_test)

# Fit the OLS model on the transformed training data
model = GradientBoostingRegressor()
result = model.fit(X_train_pca, y_train)

r2_model = model.score(X_train_pca, y_train)

r2_test = model.score(X_test_pca, y_test)

print(f'The R2 fom the model is {r2_model} and from the test data is {r2_test}')