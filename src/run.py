import argparse
from src.data_loader import load_data
from src.model import SentimentAnalysisModel
from src.utils import preprocess_text

def main():
    parser = argparse.ArgumentParser(description="Vietnamese Comment Sentiment Analysis")
    parser.add_argument('--data', type=str, required=True, help="Path to the dataset")
    parser.add_argument('--model', type=str, required=True, help="Path to save/load the model")
    parser.add_argument('--mode', type=str, choices=['train', 'predict'], required=True, help="Mode: train or predict")
    parser.add_argument('--text', type=str, help="Text to predict sentiment (required in predict mode)")
    
    args = parser.parse_args()

    if args.mode == 'train':
        print("Loading data...")
        data = load_data(args.data)
        print("Preprocessing data...")
        processed_data = preprocess_text(data)
        print("Training model...")
        model = SentimentAnalysisModel()
        model.train(processed_data)
        print(f"Saving model to {args.model}...")
        model.save(args.model)
        print("Training completed.")
    elif args.mode == 'predict':
        if not args.text:
            print("Error: --text argument is required in predict mode.")
            return
        print(f"Loading model from {args.model}...")
        model = SentimentAnalysisModel.load(args.model)
        print("Preprocessing input text...")
        processed_text = preprocess_text([args.text])
        print("Predicting sentiment...")
        sentiment = model.predict(processed_text[0])
        print(f"Predicted sentiment: {sentiment}")

if __name__ == "__main__":
    main()