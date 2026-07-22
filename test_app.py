import joblib
import numpy as np

# --- Load Model ---
model = joblib.load('cr_predictor_model.pkl')


def round_to_quarter(value):
    """
    Round float to nearest 0.25 to match CR increments.
    """
    return round(value * 4) / 4


def test_model_loads():
    """
    Verify Model is loaded without errors.
    """
    assert model is not None


#
def test_prediction_returns_float():
    """
    Verify the model returns a float value for a standard stat block input.
    """
    features = np.array([[12, 50, 10, 10, 10, 10, 10, 10]])
    prediction = model.predict(features)[0]
    assert isinstance(prediction, float)


def test_prediction_within_cr_range():
    """
    Verify the model prediction falls within the valid CR range of 0 to 30.
    """
    features = np.array([[12, 50, 10, 10, 10, 10, 10, 10]])
    prediction = model.predict(features)[0]
    assert 0 <= prediction <= 30


def test_rounding_to_quarter():
    """
    Verify the rounding function correctly rounds to the nearest 0.25.
    """
    assert round_to_quarter(1.1) == 1.0
    assert round_to_quarter(1.3) == 1.25
    assert round_to_quarter(2.6) == 2.5
    assert round_to_quarter(3.9) == 4.0
