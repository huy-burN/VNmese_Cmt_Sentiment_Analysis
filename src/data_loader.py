import pandas as pd

def load_data(filepath, text_column, label_column):
    """
    Load and preprocess data from a CSV file for sentiment analysis.
    
    Args:
        filepath (str): Path to the CSV file.
        text_column (str): Name of the column containing text data.
        label_column (str): Name of the column containing labels (0 or 1).
    
    Returns:
        tuple: A tuple containing two elements:
            - X (list of str): The text data.
            - y (list of int): The corresponding labels.
    """
    # Load the CSV file into a DataFrame
    data = pd.read_csv(filepath)
    
    # Extract the text and labels
    X = data[text_column].astype(str).tolist()
    y = data[label_column].astype(int).tolist()
    
    return X, y

