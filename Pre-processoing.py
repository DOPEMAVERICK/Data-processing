## Pre-processing of data ##

# IMPORT THE LIBRARY

import pandas as pd               # GIVE ANY ALYAS NAME 

# IMPORT THE DATASET

data=pd.read_csv('DATA.csv')     # GIVE THE REQUIRED DATASET NAME WITH EXTENSION AS .CSV (COMMA SEPRATED VALUES)

# CREATING THE X,Y ARRAY
x=data.iloc[:,:-1].values        # HERE  :  MEANS ALL THE ROWS ACCEPT LAST COLUMN (according to my dataset)
y=data.iloc[:,-1].values         



 
