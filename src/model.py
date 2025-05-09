import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

class SentimentAnalysisModel:
    ##
    """
    A class for Vietnamese comment sentiment analysis using machine learning.
    """
    def __init__(self):
        # Initialize the pipeline with TF-IDF and Logistic Regression
        self.model = Pipeline([
            ('tfidf', TfidfVectorizer(max_features=5000)),
            ('classifier', LogisticRegression())
        ])
    
    def train(self, X_train, y_train):
        """
        Train the sentiment analysis model.
        Args:
            X_train (list of str): The training data (comments).
            y_train (list of int): The training labels (0 for negative, 1 for positive).
        """
        self.model.fit(X_train, y_train)
    
    def predict(self, X_test):
        """
        Predict sentiment for the given data.
        
        Args:
            X_test (list of str): The test data (comments).
        
        Returns:
            list of int: Predicted sentiment labels (0 or 1).
        """
        return self.model.predict(X_test)
    
    def save_model(self, filepath):
        """
        Save the trained model to a file.
        
        Args:
            filepath (str): The path to save the model.
        """
        with open(filepath, 'wb') as file:
            pickle.dump(self.model, file)
    
    def load_model(self, filepath):
        """
        Load a trained model from a file.
        
        Args:
            filepath (str): The path to load the model from.
        """
        with open(filepath, 'rb') as file:
            self.model = pickle.load(file)

    def evaluate(self, X_test, y_test):
        """
        Evaluate the model's performance.
        
        Args:
            X_test (list of str): The test data (comments).
            y_test (list of int): The true labels.
            
        Returns:
            dict: Dictionary containing accuracy, precision, recall and f1-score.
        """
        y_pred = self.predict(X_test)
        return {
            'accuracy': accuracy_score(y_test, y_pred),
            'precision': precision_score(y_test, y_pred),
            'recall': recall_score(y_test, y_pred),
            'f1': f1_score(y_test, y_pred)
        }

    
            