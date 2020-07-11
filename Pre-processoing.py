## Pre-processing of data ##

# IMPORT THE LIBRARY
import pandas as pd               # GIVE ANY ALYAS NAME 

# IMPORT THE DATASET
data=pd.read_csv('Data.csv')     # GIVE THE REQUIRED DATASET NAME WITH EXTENSION AS .CSV (COMMA SEPRATED VALUES)

# CREATING THE X,Y ARRAY
x=data.iloc[:,:-1].values        # HERE  :  MEANS ALL THE ROWS :-1 ACCEPT LAST COLUMN (according to used dataset)
y=data.iloc[:,-1].values         # HERE  :  MAENS ALL THE ROWS -1 FROM LAST COLUMN

 
# CLEANING THE DATA SET (FIXING THE MISSING DATA IN SET)
from sklearn.preprocessing import Imputer
 
