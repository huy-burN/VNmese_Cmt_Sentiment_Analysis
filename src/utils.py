import re
import unicodedata

def preprocess_text(text):
    """
    Preprocess Vietnamese text for sentiment analysis.
    
    Args:
        text (str): The input text to preprocess.
    
    Returns:
        str: The cleaned and normalized text.
    """
    # Convert text to lowercase
    text = text.lower()
    
    # Normalize Unicode characters (e.g., remove accents)
    text = unicodedata.normalize('NFC', text)
    
    # Remove punctuation and special characters
    text = re.sub(r'[^\w\s]', '', text)
    
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text