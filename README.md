# 🇻🇳 VNmese_Cmt_Sentiment_Analysis

## 📌 Introduction
VNmese_Cmt_Sentiment_Analysis is a project for sentiment analysis of Vietnamese comments on e-commerce platforms or social media. The goal is to classify comments into **positive**, **negative**, or **neutral** using deep learning (DL) models and natural language processing (NLP).

## 🚀 Technologies Used
- **Programming Language**: Python
- **Data Processing**: Pandas, NumPy, PySpark
- **AI Models**: BERT, FastBERT, LSTM
- **Text Processing**: VNCoreNLP, Pyvi
- **Data Visualization**: Matplotlib, Seaborn, Tableau
- **Web Deployment**: Streamlit, Flask/FastAPI

## 📂 Project Structure
```
VNmese_Cmt_Sentiment_Analysis/
│-- data/                   # Training and test datasets
│-- models/                 # Trained model weights
│-- notebooks/              # Jupyter notebooks for model experimentation
│-- src/                    # Main source code
│   │-- preprocessing.py     # Text preprocessing
│   │-- train.py            # Model training
│   │-- predict.py          # Sentiment prediction
│   │-- app.py              # Web application using Streamlit
│-- requirements.txt        # Required dependencies
│-- README.md               # Project description
```

## 🔧 Installation Guide
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/VNmese_Cmt_Sentiment_Analysis.git
cd VNmese_Cmt_Sentiment_Analysis
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Application
```bash
streamlit run src/app.py
```

## 🎯 How to Use
1. Open the application in your browser.
2. Enter a Vietnamese comment in the input field.
3. Click the "Predict" button to get the sentiment analysis result.

## 📊 Sample Results
| Comment | Prediction |
|-----------|---------|
| "Sản phẩm rất tốt!" | 😊 Positive |
| "Dịch vụ quá tệ, thất vọng." | 😡 Negative |
| "Không có gì đặc biệt." | 😐 Neutral |

## 🔥 Demo (Optional)
[![Streamlit App](https://img.shields.io/badge/Streamlit-Demo-red)](https://your-demo-link.com)

## 📌 Contributions & Contact
- If you want to improve this project, feel free to submit a **pull request** or open an **issue** on GitHub!
- Contact: nhathuy200712@gmail.com

