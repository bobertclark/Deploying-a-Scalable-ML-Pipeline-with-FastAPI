# TODO: add necessary import
import numpy as np
import math
# Runs train_model.py file
import train_model


# TODO: implement the first test. Change the function name and input as needed
def test_dataset_size():
    """
    Tests if the training and test datasets have the expected size.
    """

    # Your code here
    assert (train_model.train.shape[0] == math.floor(train_model.data.shape[0]*0.8) and
            train_model.test.shape[0] == math.ceil(train_model.data.shape[0]*0.2))


# TODO: implement the second test. Change the function name and input as needed
def test_preds():
    """
    Tests if the predictions output is the right type
    """
    # Your code here
    assert isinstance(train_model.preds, (np.ndarray))


# TODO: implement the third test. Change the function name and input as needed
def test_computing_metrics():
    """
    Tests if the computing metrics functions return the expected value.
    """
    # Your code here
    assert 0 <= train_model.p <= 1 and 0 <= train_model.r <= 1 and 0 <= train_model.fb <= 1
