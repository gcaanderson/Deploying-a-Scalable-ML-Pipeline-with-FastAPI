import pytest
# Add necessary imports
from train_model.py import train, test, model, model_dir, model_path
from main.py import data_processed

# TODO: implement the first test. Change the function name and input as needed
def test_datasets_file_type(train, test):
    """
    # Check if the train and test datasets have the expected file type, which is a CSV.
    """
    assert train.endswith(".csv")
    assert test.endswith(".csv")
    
    pass


# TODO: implement the second test. Change the function name and input as needed
def test_model_encoder_files():
    """
    # Check if the model and encoder have been saved successfully. 
    """
    # Check the existence of the files
    assert os.path.exists("model\encoder.pkl"), f"Encoder pickle file does not exist"
    assert os.path.exists("model\model.pkl"), f"Model pickle file does not exist"

    # Check if the files are empty
    assert os.stat("model\encoder.pkl").st_size > 0, f"Encoder pickle file is empty"
    assert os.stat("model\model.pkl").st_size > 0, f"Model pickle file is empty"

    pass


# TODO: implement the third test. Change the function name and input as needed
def test_process_data():
    """
    # Check if process_data function produces an array for data_processed.
    """
    assert isinstance(data_processed, array) == True
    pass
