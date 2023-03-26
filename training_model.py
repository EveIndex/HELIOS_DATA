# Import libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load CSV file into dataframe
df = pd.read_csv("HELIOS_DATA_1.csv")

# Split dataframe into features and labels
X = df["question"] # questions that correspond to answers
y = df["answer"] # numerical values that are the answers

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Choose and train a question answering model
model = LogisticRegression()
model.fit(X_train, y_train)

# Test and evaluate the model
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))

# Answer new questions using the model
new_question = "What is eve scout rescue?" # example question
new_answer = model.predict([new_question]) # get the label that matches the question
print("Answer:", new_answer[0]) # print the answer value