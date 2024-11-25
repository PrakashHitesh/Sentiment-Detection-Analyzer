from django.shortcuts import render
from textblob import TextBlob
from .models import SentimentLog



def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment
    polarity = sentiment.polarity


    if polarity > 0.5:
        sentiment_category = 'Very Positive'
    elif 0 < polarity <= 0.5:
        sentiment_category = 'Positive'
    elif -0.5 <= polarity < 0:
        sentiment_category = 'Negative'
    elif polarity <= -0.5:
        sentiment_category = 'Very Negative'
    else:
        sentiment_category = 'Neutral'

    return sentiment_category, polarity



def sentiment_analysis(request):
    context = {}
    if request.method == 'POST':
        user_text = request.POST.get('text', '')
        if user_text.strip():
            sentiment, polarity = analyze_sentiment(user_text)

    
            SentimentLog.objects.create(text=user_text, sentiment=sentiment, polarity=polarity)

            context['user_text'] = user_text
            context['sentiment'] = sentiment
            context['polarity'] = round(polarity, 2)

    
    context['history'] = SentimentLog.objects.all().order_by('-timestamp')[:5]

    return render(request, 'analyze.html', context)