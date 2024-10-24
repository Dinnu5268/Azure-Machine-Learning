from textblob import TextBlob
 
def determine_sentiment(sentence):
    analysis = TextBlob(sentence)
    # Determine the polarity of the sentence
    # Polarity is a float within the range [-1.0, 1.0]
    # where -1.0 is very negative and 1.0 is very positive
    polarity = analysis.sentiment.polarity
   
    # Determine sentiment based on polarity
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"
   
    return polarity
 
if __name__ == "__main__":
    # Get sentence input from the user
    sentence = input("Enter a sentence: ")
    sentiment = determine_sentiment(sentence)
    print(f"The sentiment of the given sentence is: {sentiment}")