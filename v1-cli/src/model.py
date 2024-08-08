# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LogisticRegression
# from sklearn.metrics import classification_report
#
# def train_model(X, y):
#     """to train the ML model"""
#     X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
#     model = LogisticRegression()
#     model.fit(X_train, y_train)
#     y_pred = model.predict(X_test)
#     print(classification_report(y_test, y_pred))
#     return model
#
# # my aim is to implement machine learning models to predict risk factors.

# let me update totally:
import os
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import joblib

def train_model(X, y):
    """to train the ml model now"""
    # encoding categorical features in X
    for col in X.select_dtypes(include=['object']).columns:
        le = LabelEncoder()
        X[col] = le.fit_transform(X[col])

    # encoding target variable if necessary
    if y.dtype == 'object':
        le = LabelEncoder()
        y = le.fit_transform(y)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LogisticRegression()
    model.fit(X_train, y_train)

    # help me create the 'models' directory if it does not exist
    model_dir = 'models'
    if not os.path.exists(model_dir):
        os.makedirs(model_dir)

    # to save the trained model
    model_path = os.path.join(model_dir, 'logistic_regression_model.pkl')
    joblib.dump(model, model_path)
    # joblib.dump(model, 'models/logistic_regression_model.pkl')
    return model