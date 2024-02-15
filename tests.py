# tests.py
import numpy as np
from regression import predict_value

def test_regression():
    # Test the regression prediction
    x_new = np.array([[6]])
    predicted_value = predict_value(x_new)
    expected_value = 15.0

    assert np.isclose(predicted_value[0], expected_value), "Prediction error"
