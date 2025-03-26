# Importing libraries
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
dataset = pd.read_csv('diabetes_prediction_dataset.csv')

import pandas as pd

# Load the dataset
dataset = pd.read_csv('diabetes_prediction_dataset.csv')

# Drop all rows with any NaN or missing values
dataset = dataset.dropna()

# Save the cleaned dataset to a new CSV file
dataset.to_csv('preprocessed.csv', index=False)

print("Rows with missing values removed and saved to 'preprocessed.csv'.")


# Load the dataset
data = pd.read_csv("preprocessed.csv")  # Replace with the path to your dataset

# Perform one-hot encoding for both 'gender' and 'smoking_history' columns
data_encoded = pd.get_dummies(data, columns=['gender', 'smoking_history'], prefix=['gender', 'smoking_history'])

# Reorder columns to place 'diabetes' as the last column
columns = [col for col in data_encoded.columns if col != 'diabetes']  # Get all columns except 'diabetes'
columns.append('diabetes')  # Add 'diabetes' column at the end

# Apply the new column order
data_encoded = data_encoded[columns]

# Save the updated dataset to a new CSV file
data_encoded.to_csv("encoded_dataset.csv", index=False)

print("One-hot encoding completed. Updated dataset saved as 'encoded_dataset.csv'.")

