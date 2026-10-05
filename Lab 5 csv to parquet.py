#############################################
# Lab 5 Dataset Conversion # Edwina Faustin #
# ----------------------------------------- #
# 10/4/26 efaustin@usf.edu ##################
#############################################

# import libraries
import pandas as pd

# open the .csv         df short for datat frame
df = pd.read_csv("Maternal Health Risk Data Set.csv")

# save it as a .parquet
df.to_parquet("Maternal Health Risk Data Set.parquet", engine="pyarrow", index=False)



