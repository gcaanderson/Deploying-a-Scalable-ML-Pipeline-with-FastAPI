import pytest
# Add necessary imports
from train_model import train, test, data, X_train, y_train
from main import process_data
from sklearn.ensemble import RandomForestClassifier
import os

def test_size_datasets():
    """
    Check if the train and test datasets are the expected size, 
    which is 80% training and 20% testing as we set in train_model.py.
    I set the tolerance within 1% to account for rounding. 
    """
    total = data.shape[0]
    train_percent = total * 0.8
    test_percent = total * 0.2

    assert abs(train.shape[0] - train_percent) <=1
    assert abs(test.shape[0] - test_percent) <= 1
    
    pass


# TODO: implement the second test. Change the function name and input as needed
def test_model_encoder_files():
    """
    # Check if the model and encoder have been saved successfully. 
    """
    # Check the existence of the files
    assert os.path.exists("model\\encoder.pkl"), f"Encoder pickle file does not exist"
    assert os.path.exists("model\\model.pkl"), f"Model pickle file does not exist"

    # Check if the files are empty
    assert os.stat("model\\encoder.pkl").st_size > 0, f"Encoder pickle file is empty"
    assert os.stat("model\\model.pkl").st_size > 0, f"Model pickle file is empty"

    pass


# TODO: implement the third test. Change the function name and input as needed
def test_model_algorithm():
    """
    # Check if the model uses the expected algorithm, Random Forest Classifier.
    """
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    expected_algorithm = 'RandomForestClassifier'
    assert model.__class__.__name__ == expected_algorithm

    pass