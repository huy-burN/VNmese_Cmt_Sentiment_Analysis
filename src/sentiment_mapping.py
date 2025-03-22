def map_sentiment(score):
    """
    Map a sentiment score to a sentiment label.

    Args:
        score (float): Sentiment score ranging from -5 to 5.

    Returns:
        str: Sentiment label.
    """
    if -5 <= score < -3:
        return "Vô cùng tiêu cực"
    elif -3 <= score < -1:
        return "Tiêu cực"
    elif -1 <= score <= 1:
        return "Trung tính"
    elif 1 < score <= 3:
        return "Tích cực"
    elif 3 < score <= 5:
        return "Rất tích cực"
    else:
        return "Ngoài phạm vi"

# Example usage
if __name__ == "__main__":
    test_scores = [-4.5, -2.5, 0, 2, 4.5, 6]
    for score in test_scores:
        print(f"Score: {score}, Sentiment: {map_sentiment(score)}")