import pickle
import json
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
import os


class ModelTrainer:
    """Train and evaluate multiple models for ensemble."""
    
    def __init__(self, data_path: str = 'public_cases.csv', test_size: float = 0.25, 
                 random_state: int = 42):
        """
        Initialize the model trainer.
        
        Args:
            data_path: Path to the training data
            test_size: Proportion of data to use for testing
            random_state: Random seed for reproducibility
        """
        self.data_path = data_path
        self.test_size = test_size
        self.random_state = random_state
        self.models = {}
        self.scalers = {}
        self.feature_names = None
        
    def load_and_prepare_data(self):
        """Load and prepare the data with feature engineering."""
        print("Loading data...")
        df = pd.read_csv(self.data_path)
        
        # Extract basic features
        X = df[['input/trip_duration_days', 'input/miles_traveled', 
                'input/total_receipts_amount']].copy()
        y = df['expected_output']
        
        # Rename columns for easier handling
        X.columns = ['trip_duration_days', 'miles_traveled', 'total_receipts_amount']
        
        # Feature engineering - add derived features
        print("Engineering features...")
        X['cost_per_day'] = X['total_receipts_amount'] / (X['trip_duration_days'] + 0.01)
        X['cost_per_mile'] = X['total_receipts_amount'] / (X['miles_traveled'] + 0.01)
        X['miles_per_day'] = X['miles_traveled'] / (X['trip_duration_days'] + 0.01)
        
        # TODO: Add more engineered features based on EDA insights
        # Examples:
        # X['duration_miles_interaction'] = X['trip_duration_days'] * X['miles_traveled']
        # X['receipts_squared'] = X['total_receipts_amount'] ** 2
        
        self.feature_names = X.columns.tolist()
        
        # Split data
        print(f"Splitting data (test_size={self.test_size})...")
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=self.test_size, random_state=self.random_state
        )
        
        print(f"Training set: {X_train.shape[0]} samples")
        print(f"Test set: {X_test.shape[0]} samples")
        
        return X_train, X_test, y_train, y_test
    
    def train_linear_models(self, X_train, X_test, y_train, y_test):
        """Train linear regression variants."""
        print("\n" + "="*60)
        print("Training Linear Models")
        print("="*60)
        
        # Simple Linear Regression
        print("\n1. Linear Regression...")
        lr = LinearRegression()
        lr.fit(X_train, y_train)
        self.models['linear_regression'] = lr
        self._evaluate_model(lr, X_train, X_test, y_train, y_test, 'Linear Regression')
        
        # Ridge Regression
        print("\n2. Ridge Regression...")
        ridge = Ridge(alpha=1.0)
        ridge.fit(X_train, y_train)
        self.models['ridge'] = ridge
        self._evaluate_model(ridge, X_train, X_test, y_train, y_test, 'Ridge')
        
        # Lasso Regression
        print("\n3. Lasso Regression...")
        lasso = Lasso(alpha=1.0)
        lasso.fit(X_train, y_train)
        self.models['lasso'] = lasso
        self._evaluate_model(lasso, X_train, X_test, y_train, y_test, 'Lasso')
        
        # TODO: Add Polynomial Regression
        # poly_features = PolynomialFeatures(degree=2)
        # X_train_poly = poly_features.fit_transform(X_train)
        # X_test_poly = poly_features.transform(X_test)
        # lr_poly = LinearRegression()
        # lr_poly.fit(X_train_poly, y_train)
        # self.models['polynomial'] = {'model': lr_poly, 'transformer': poly_features}
    
    def train_tree_models(self, X_train, X_test, y_train, y_test):
        """Train tree-based models."""
        print("\n" + "="*60)
        print("Training Tree-Based Models")
        print("="*60)
        
        # Decision Tree
        print("\n1. Decision Tree...")
        dt = DecisionTreeRegressor(random_state=self.random_state, max_depth=10)
        dt.fit(X_train, y_train)
        self.models['decision_tree'] = dt
        self._evaluate_model(dt, X_train, X_test, y_train, y_test, 'Decision Tree')
        
        # Random Forest
        print("\n2. Random Forest...")
        rf = RandomForestRegressor(n_estimators=100, random_state=self.random_state, 
                                   max_depth=15, n_jobs=-1)
        rf.fit(X_train, y_train)
        self.models['random_forest'] = rf
        self._evaluate_model(rf, X_train, X_test, y_train, y_test, 'Random Forest')
        
        # Gradient Boosting
        print("\n3. Gradient Boosting...")
        gb = GradientBoostingRegressor(n_estimators=100, random_state=self.random_state,
                                      max_depth=5, learning_rate=0.1)
        gb.fit(X_train, y_train)
        self.models['gradient_boosting'] = gb
        self._evaluate_model(gb, X_train, X_test, y_train, y_test, 'Gradient Boosting')
        
        # Feature importance for tree-based models
        print("\n--- Feature Importance (Random Forest) ---")
        for name, importance in zip(self.feature_names, rf.feature_importances_):
            print(f"{name:30s}: {importance:.4f}")
    
    def train_neural_network(self, X_train, X_test, y_train, y_test):
        """Train neural network model."""
        print("\n" + "="*60)
        print("Training Neural Network")
        print("="*60)
        
        # Scale features for neural network
        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)
        self.scalers['nn_scaler'] = scaler
        
        # Multi-layer Perceptron
        print("\nMLP Regressor...")
        mlp = MLPRegressor(
            hidden_layer_sizes=(100, 50, 25),
            activation='relu',
            solver='adam',
            learning_rate='adaptive',
            max_iter=1000,
            random_state=self.random_state,
            early_stopping=True,
            validation_fraction=0.1
        )
        mlp.fit(X_train_scaled, y_train)
        self.models['neural_network'] = mlp
        
        # Evaluate with scaled data
        y_train_pred = mlp.predict(X_train_scaled)
        y_test_pred = mlp.predict(X_test_scaled)
        
        print(f"Train R²: {r2_score(y_train, y_train_pred):.4f}")
        print(f"Test R²: {r2_score(y_test, y_test_pred):.4f}")
        print(f"Test MAE: ${mean_absolute_error(y_test, y_test_pred):.2f}")
        print(f"Test RMSE: ${np.sqrt(mean_squared_error(y_test, y_test_pred)):.2f}")
    
    def _evaluate_model(self, model, X_train, X_test, y_train, y_test, model_name):
        """Evaluate a single model."""
        y_train_pred = model.predict(X_train)
        y_test_pred = model.predict(X_test)
        
        train_r2 = r2_score(y_train, y_train_pred)
        test_r2 = r2_score(y_test, y_test_pred)
        test_mae = mean_absolute_error(y_test, y_test_pred)
        test_rmse = np.sqrt(mean_squared_error(y_test, y_test_pred))
        
        # Calculate exact and close matches
        exact_matches = np.sum(np.abs(y_test_pred - y_test) <= 0.01)
        close_matches = np.sum(np.abs(y_test_pred - y_test) <= 1.00)
        
        exact_pct = exact_matches / len(y_test) * 100
        close_pct = close_matches / len(y_test) * 100
        
        print(f"Train R²: {train_r2:.4f}")
        print(f"Test R²: {test_r2:.4f}")
        print(f"Test MAE: ${test_mae:.2f}")
        print(f"Test RMSE: ${test_rmse:.2f}")
        print(f"Exact matches (±$0.01): {exact_pct:.1f}%")
        print(f"Close matches (±$1.00): {close_pct:.1f}%")
        
        # Check for overfitting
        if train_r2 - test_r2 > 0.1:
            print(f"⚠️  Warning: Possible overfitting (train R² - test R² = {train_r2 - test_r2:.3f})")
    
    def create_ensemble(self, X_train, X_test, y_train, y_test):
        """Create an ensemble of the best models."""
        print("\n" + "="*60)
        print("Creating Ensemble Model")
        print("="*60)
        
        # TODO: Implement ensemble logic
        # Options:
        # 1. Simple averaging
        # 2. Weighted averaging based on performance
        # 3. Stacking
        
        # Example: Weighted average ensemble
        predictions = {}
        weights = {}
        
        for name, model in self.models.items():
            if name == 'neural_network':
                scaler = self.scalers.get('nn_scaler')
                X_test_scaled = scaler.transform(X_test)
                pred = model.predict(X_test_scaled)
            else:
                pred = model.predict(X_test)
            
            predictions[name] = pred
            r2 = r2_score(y_test, pred)
            weights[name] = max(0, r2)  # Use R² as weight (ignore negative)
        
        # Normalize weights
        total_weight = sum(weights.values())
        weights = {k: v/total_weight for k, v in weights.items()}
        
        print("\nEnsemble weights:")
        for name, weight in sorted(weights.items(), key=lambda x: x[1], reverse=True):
            print(f"  {name:20s}: {weight:.3f}")
        
        # Calculate ensemble prediction
        ensemble_pred = np.zeros(len(y_test))
        for name, pred in predictions.items():
            ensemble_pred += pred * weights[name]
        
        # Evaluate ensemble
        print("\nEnsemble Performance:")
        print(f"Test R²: {r2_score(y_test, ensemble_pred):.4f}")
        print(f"Test MAE: ${mean_absolute_error(y_test, ensemble_pred):.2f}")
        print(f"Test RMSE: ${np.sqrt(mean_squared_error(y_test, ensemble_pred)):.2f}")
        
        exact_matches = np.sum(np.abs(ensemble_pred - y_test) <= 0.01)
        close_matches = np.sum(np.abs(ensemble_pred - y_test) <= 1.00)
        print(f"Exact matches (±$0.01): {exact_matches / len(y_test) * 100:.1f}%")
        print(f"Close matches (±$1.00): {close_matches / len(y_test) * 100:.1f}%")
        
        # Save ensemble weights
        self.models['ensemble_weights'] = weights
    
    def save_models(self, output_dir: str = 'models'):
        """Save all trained models to disk."""
        print(f"\nSaving models to {output_dir}/...")
        
        os.makedirs(output_dir, exist_ok=True)
        
        for name, model in self.models.items():
            if name == 'ensemble_weights':
                # Save weights as JSON
                with open(f'{output_dir}/{name}.json', 'w') as f:
                    json.dump(model, f, indent=2)
            else:
                # Save model as pickle
                with open(f'{output_dir}/{name}.pkl', 'wb') as f:
                    pickle.dump(model, f)
                print(f"  ✓ Saved {name}")
        
        # Save scalers
        for name, scaler in self.scalers.items():
            with open(f'{output_dir}/{name}.pkl', 'wb') as f:
                pickle.dump(scaler, f)
            print(f"  ✓ Saved {name}")
        
        # Save feature names
        with open(f'{output_dir}/feature_names.json', 'w') as f:
            json.dump(self.feature_names, f, indent=2)
        print(f"  ✓ Saved feature_names.json")
        
        print(f"\n✅ All models saved successfully!")
    
    def train_all(self):
        """Train all models and save them."""
        # Load and prepare data
        X_train, X_test, y_train, y_test = self.load_and_prepare_data()
        
        # Train different model types
        self.train_linear_models(X_train, X_test, y_train, y_test)
        self.train_tree_models(X_train, X_test, y_train, y_test)
        self.train_neural_network(X_train, X_test, y_train, y_test)
        
        # Create ensemble
        self.create_ensemble(X_train, X_test, y_train, y_test)
        
        # Save all models
        self.save_models()
        
        print("\n" + "="*60)
        print("Training Complete!")
        print("="*60)
        print(f"Total models trained: {len(self.models)}")
        print("Models are ready for production deployment.")


def main():
    """Main function to run model training."""
    # Initialize trainer
    trainer = ModelTrainer(
        data_path='public_cases.csv',
        test_size=0.25,
        random_state=42
    )
    
    # Train all models
    trainer.train_all()


if __name__ == '__main__':
    main()
