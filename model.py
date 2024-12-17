from sklearn.linear_model import LogisticRegression
import seaborn as sns
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay 
from imblearn.over_sampling import SMOTE
from sklearn.ensemble import RandomForestClassifier

df=pd.read_csv('C:\Users\ADMIN\Desktop\CK\Chronic_Kidney_Dsease_data.csv',index_col='PatientID')