# regression.py
import numpy as np
from sklearn.linear_model import LinearRegression

def predict_value(x):
    # Generate some sample data
    X = np.array([[1], [2], [3], [4], [5]])
    y = np.array([2, 4, 6, 8, 10])

    # Create a linear regression model
    model = LinearRegression()

    # Fit the model to the data
    model.fit(X, y)

    # Predict using the trained model
    y_pred = model.predict(x)

    return y_pred

# Example usage
x_new = np.array([[6]])
predicted_value = predict_value(x_new)
print(f"Predicted value for x={x_new[0][0]}: {predicted_value[0]}")
