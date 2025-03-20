# VNmese_Cmt_Sentiment_Analysis

## 📌 Giới thiệu
VNmese_Cmt_Sentiment_Analysis là một dự án phân tích cảm xúc của bình luận tiếng Việt trên các nền tảng thương mại điện tử hoặc mạng xã hội. Mục tiêu của dự án là phân loại bình luận thành **tích cực**, **tiêu cực**, hoặc **trung lập** bằng cách sử dụng các mô hình học sâu (Deep Learning) và xử lý ngôn ngữ tự nhiên (NLP).

## 🚀 Công nghệ sử dụng
- **Ngôn ngữ lập trình**: Python
- **Xử lý dữ liệu**: Pandas, NumPy, PySpark
- **Mô hình AI**: BERT, FastBERT, LSTM
- **Xử lý văn bản**: VNCoreNLP, Pyvi
- **Trực quan hóa dữ liệu**: Matplotlib, Seaborn, Tableau
- **Triển khai ứng dụng**: Streamlit, Flask/FastAPI

## 📂 Cấu trúc thư mục
```
VNmese_Cmt_Sentiment_Analysis/
│-- data/                   # Dữ liệu huấn luyện và kiểm tra
│-- models/                 # Trọng số mô hình đã huấn luyện
│-- notebooks/              # Notebook Jupyter để thử nghiệm mô hình
│-- src/                    # Mã nguồn chính
│   │-- preprocessing.py     # Tiền xử lý dữ liệu văn bản
│   │-- train.py            # Huấn luyện mô hình
│   │-- predict.py          # Dự đoán cảm xúc từ văn bản
│   │-- app.py              # Ứng dụng web với Streamlit
│-- requirements.txt        # Danh sách thư viện cần cài đặt
│-- README.md               # Mô tả dự án
```

## 🔧 Hướng dẫn cài đặt
### 1️⃣ Clone dự án
```bash
git clone https://github.com/yourusername/VNmese_Cmt_Sentiment_Analysis.git
cd VNmese_Cmt_Sentiment_Analysis
```

### 2️⃣ Cài đặt thư viện
```bash
pip install -r requirements.txt
```

### 3️⃣ Chạy ứng dụng
```bash
streamlit run src/app.py
```

## 🎯 Cách sử dụng
1. Mở ứng dụng trong trình duyệt.
2. Nhập một bình luận tiếng Việt vào ô nhập liệu.
3. Nhấn nút "Dự đoán" để nhận kết quả phân tích cảm xúc.

## 📊 Kết quả mẫu
| Bình luận | Dự đoán |
|-----------|---------|
| "Sản phẩm rất tốt!" | 😊 Tích cực |
| "Dịch vụ quá tệ, thất vọng." | 😡 Tiêu cực |
| "Không có gì đặc biệt." | 😐 Trung lập |

## 🔥 Demo (Tùy chọn)
[![Streamlit App](https://img.shields.io/badge/Streamlit-Demo-red)](https://your-demo-link.com)

## 📌 Đóng góp & Liên hệ
- Nếu bạn muốn cải tiến dự án, hãy gửi **pull request** hoặc mở **issue** trên GitHub!
- Liên hệ: nhathuy200712@gmail.com
