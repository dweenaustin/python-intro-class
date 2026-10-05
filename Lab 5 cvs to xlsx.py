#############################################
# Lab 5 Dataset Conversion # Edwina Faustin #
# ----------------------------------------- #
# 10/4/26 efaustin@usf.edu ##################
#############################################

# import libraries
import pandas as pd

# open the .csv         df short for data frame
df = pd.read_csv("Maternal Health Risk Data Set.csv")

# save it as a .xlsx
df.to_excel("Maternal Health Risk Data Set.xlsx", index = False)