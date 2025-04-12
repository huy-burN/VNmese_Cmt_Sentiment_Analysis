from src.model import SentimentAnalysisModel
from src.utils import preprocess_text

def test_sentiment_analysis():
    # Khởi tạo modell
    model = SentimentAnalysisModel()
    
    # Ví dụ một số bình luận tiếng Việt
    comments = [
        "Sản phẩm rất tốt, tôi rất hài lòng!", 
        "Dịch vụ tệ quá, không nên mua",
        "Bình thường, không có gì đặc biệt",
        "Tuyệt vời, sẽ mua lại vào cái ngày tao chết",
        "Chất lượng kém, không đáng tiền"
    ]
    
    # Tiền xử lý văn bản
    processed_comments = preprocess_text(comments)
    
    # Dự đoán cảm xúc cho từng bình luận
    print("Kết quả phân tích cảm xúc:")
    print("-" * 50)
    for comment, processed_comment in zip(comments, processed_comments):
        sentiment = model.predict(processed_comment)
        print(f"Bình luận: {comment}")
        print(f"Cảm xúc: {sentiment}")
        print("-" * 50)

if __name__ == "__main__":
    test_sentiment_analysis()
