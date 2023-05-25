from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import pandas as pd

# Assuming your data is in a CSV file and the target variable is 'group'
data = pd.read_csv('your_data_file.csv')

# Assume that the last column is the target and the rest are features
X = data.iloc[:, :-1]  # Features
y = data.iloc[:, -1]  # Target variable

# Split the dataset into a training set and a test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1) 

# Create a Decision Tree Classifier object
clf = DecisionTreeClassifier()

# Train the model using the training sets
clf.fit(X_train, y_train)

# Predict the response for the test dataset
y_pred = clf.predict(X_test)

# You can print out the accuracy and the classification report as follows:
from sklearn import metrics

print("Accuracy:", metrics.accuracy_score(y_test, y_pred))
print(metrics.classification_report(y_test, y_pred))
