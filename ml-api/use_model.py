import sys
import joblib
import numpy as np

def main(model_path):
    # Load the model
    model = joblib.load(model_path)
    
    # Example: Perform some predictions
    # Use the actual feature names of the Iris dataset for clarity
    example_data = np.array([[5.1, 3.5, 1.4, 0.2],  # Setosa
                             [6.7, 3.1, 4.7, 1.5],  # Versicolor
                             [7.2, 3.6, 6.1, 2.5]])  # Virginica

    predictions = model.predict(example_data)
    
    # Mapping of target labels to species names
    target_names = ['Setosa', 'Versicolor', 'Virginica']
    
    # Print the predictions with corresponding species names
    for i, pred in enumerate(predictions):
        print(f"Example data {i + 1}: {example_data[i]}, Prediction: {target_names[pred]}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python use_model.py <model_path>")
        sys.exit(1)
    
    model_path = sys.argv[1]
    main(model_path)
