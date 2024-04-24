import pytest
# Add necessary imports
from train_model.py import train, test, model, model_dir, model_path

# TODO: implement the first test. Change the function name and input as needed
def test_datasets_file_type(train, test):
    """
    # Check if the train and test datasets have the expected file type, which is a CSV.
    """
    assert train.endswith(".csv")
    assert test.endswith(".csv")
    pass


# TODO: implement the second test. Change the function name and input as needed
def test_two():
    """
    # Check if the model and encoder have been saved successfully. 
    """
    # Your code here
    pass


# TODO: implement the third test. Change the function name and input as needed
def test_process_data():
    """
    # Check if process_data function produces an array for data_processed.
    """
    assert isinstance(data_processed, array) == True
    pass
