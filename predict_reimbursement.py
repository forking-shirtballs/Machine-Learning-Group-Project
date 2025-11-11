import sys
import pickle
import numpy as np
from typing import Tuple


def validate_inputs(trip_duration_days: float, miles_traveled: float, 
                    total_receipts_amount: float) -> Tuple[bool, str]:
    """
    Validate input parameters.
    
    Args:
        trip_duration_days: Number of days spent traveling
        miles_traveled: Total miles traveled
        total_receipts_amount: Total dollar amount of receipts
    
    Returns:
        Tuple of (is_valid, error_message)
    """
    try:
        # Convert to float and check if valid numbers
        trip_days = float(trip_duration_days)
        miles = float(miles_traveled)
        receipts = float(total_receipts_amount)
        
        # Check for negative values
        if trip_days < 0:
            return False, "Trip duration cannot be negative"
        if miles < 0:
            return False, "Miles traveled cannot be negative"
        if receipts < 0:
            return False, "Receipt amount cannot be negative"
        
        return True, ""
    
    except (ValueError, TypeError) as e:
        return False, f"Invalid input type: {str(e)}"


def preprocess_features(trip_duration_days: float, miles_traveled: float,
                       total_receipts_amount: float) -> np.ndarray:
    """
    Preprocess input features into model-ready format.
    
    This should match the feature engineering from the EDA phase.
    
    Args:
        trip_duration_days: Number of days spent traveling
        miles_traveled: Total miles traveled  
        total_receipts_amount: Total dollar amount of receipts
    
    Returns:
        Numpy array of features ready for prediction
    """
    # Basic features
    features = [
        trip_duration_days,
        miles_traveled,
        total_receipts_amount
    ]
    
    # TODO: Add derived features that improve model performance
    # Examples from project requirements:
    # - cost_per_mile = total_receipts_amount / miles_traveled (if miles > 0)
    # - cost_per_day = total_receipts_amount / trip_duration_days (if days > 0)
    # - Interaction terms
    # - Polynomial features
    
    return np.array(features).reshape(1, -1)


def load_models():
    """
    Load trained models from pickle files.
    
    Returns:
        Dictionary of loaded models
    """
    models = {}
    
    try:
        # TODO: Load your trained models
        # Example:
        # with open('models/linear_regression.pkl', 'rb') as f:
        #     models['linear'] = pickle.load(f)
        # with open('models/decision_tree.pkl', 'rb') as f:
        #     models['tree'] = pickle.load(f)
        # with open('models/neural_network.pkl', 'rb') as f:
        #     models['nn'] = pickle.load(f)
        
        pass
    
    except FileNotFoundError as e:
        print(f"Error: Model file not found - {str(e)}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error loading models: {str(e)}", file=sys.stderr)
        sys.exit(1)
    
    return models


def ensemble_predict(models: dict, features: np.ndarray) -> float:
    """
    Make prediction using ensemble of models.
    
    Args:
        models: Dictionary of trained models
        features: Preprocessed feature array
    
    Returns:
        Final prediction as float
    """
    predictions = []
    
    # TODO: Implement ensemble logic
    # Options:
    # 1. Simple averaging
    # 2. Weighted averaging (based on model performance)
    # 3. Stacking
    # 4. Voting
    # 5. Model selection based on input characteristics
    
    # Example simple ensemble:
    # if 'linear' in models:
    #     predictions.append(models['linear'].predict(features)[0])
    # if 'tree' in models:
    #     predictions.append(models['tree'].predict(features)[0])
    # if 'nn' in models:
    #     predictions.append(models['nn'].predict(features)[0])
    
    # if predictions:
    #     final_prediction = np.mean(predictions)
    # else:
    #     # Fallback prediction logic
    #     final_prediction = 0.0
    
    # TODO: Replace this placeholder with actual ensemble logic
    final_prediction = 0.0
    
    return final_prediction


def predict_reimbursement(trip_duration_days: float, miles_traveled: float,
                         total_receipts_amount: float) -> float:
    """
    Main prediction function.
    
    Args:
        trip_duration_days: Number of days spent traveling (integer)
        miles_traveled: Total miles traveled (integer)
        total_receipts_amount: Total dollar amount of receipts (float)
    
    Returns:
        Predicted reimbursement amount rounded to 2 decimal places
    """
    # Validate inputs
    is_valid, error_msg = validate_inputs(trip_duration_days, miles_traveled, 
                                         total_receipts_amount)
    if not is_valid:
        print(f"Error: {error_msg}", file=sys.stderr)
        sys.exit(1)
    
    # Preprocess features
    features = preprocess_features(trip_duration_days, miles_traveled, 
                                  total_receipts_amount)
    
    # Load models (in production, this would be done once at startup)
    models = load_models()
    
    # Make prediction
    prediction = ensemble_predict(models, features)
    
    # Round to 2 decimal places as required
    return round(prediction, 2)


def main():
    """
    Main entry point for command-line usage.
    
    Usage:
        python predict_reimbursement.py <trip_duration_days> <miles_traveled> <total_receipts_amount>
    
    Example:
        python predict_reimbursement.py 5 250 450.50
    """
    if len(sys.argv) != 4:
        print("Usage: python predict_reimbursement.py <trip_duration_days> <miles_traveled> <total_receipts_amount>")
        print("\nExample:")
        print("  python predict_reimbursement.py 5 250 450.50")
        sys.exit(1)
    
    try:
        trip_duration_days = float(sys.argv[1])
        miles_traveled = float(sys.argv[2])
        total_receipts_amount = float(sys.argv[3])
        
        result = predict_reimbursement(trip_duration_days, miles_traveled, 
                                      total_receipts_amount)
        
        # Output only the single number as required
        print(result)
        
    except ValueError as e:
        print(f"Error: Invalid input format - {str(e)}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
