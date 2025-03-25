import os
import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense, Dropout, Bidirectional
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# Load dataset
def load_data(file_path):
    data = pd.read_csv(file_path)
    return data['comment'], data['label']

# Preprocess text
def preprocess_text(comments, max_words=10000, max_len=100):
    tokenizer = Tokenizer(num_words=max_words, oov_token="<OOV>")
    tokenizer.fit_on_texts(comments)
    sequences = tokenizer.texts_to_sequences(comments)
    padded_sequences = pad_sequences(sequences, maxlen=max_len, padding='post', truncating='post')
    return padded_sequences, tokenizer

# Build model
def build_model(vocab_size, embedding_dim=128, max_len=100):
    model = Sequential([
        Embedding(vocab_size, embedding_dim, input_length=max_len),
        Bidirectional(LSTM(64, return_sequences=True)),
        Dropout(0.5),
        Bidirectional(LSTM(32)),
        Dense(64, activation='relu'),
        Dropout(0.5),
        Dense(1, activation='sigmoid')
    ])
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model

# Main function
if __name__ == "__main__":
    # Load and preprocess data
    comments, labels = load_data('vietnamese_comments.csv')  # Replace with your dataset path
    padded_sequences, tokenizer = preprocess_text(comments)
    vocab_size = len(tokenizer.word_index) + 1

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(padded_sequences, labels, test_size=0.2, random_state=42)

    # Build and train model
    model = build_model(vocab_size)
    model.summary()
    model.fit(X_train, y_train, epochs=5, batch_size=32, validation_split=0.2)

    # Evaluate model
    y_pred = (model.predict(X_test) > 0.5).astype("int32")
    print(classification_report(y_test, y_pred))