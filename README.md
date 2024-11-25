# Sentiment Detection Analyzer
## Description

The Sentiment Detection project analyzes the sentiment of a given text input using the **TextBlob** library. The project categorizes sentiments into **Very Positive**, **Positive**, **Neutral**,** Negative**, and **Very Negative** based on the text's polarity score. This is a web-based application developed using the **Django framework**, and it includes a clean and modern UI designed with **Bootstrap**.

## Features

  - Real-time Sentiment Analysis: Analyze text and categorize it into various sentiment classes.
  - Polarity Score Display: Shows the polarity score of the analyzed text.
  - Bootstrap-based Responsive UI: A modern and mobile-friendly interface.
  - Custom Sentiment Categories: Includes extra categories like "Very Positive" and "Very Negative" for a more detailed analysis.

## Technologies Used

  - Frontend: HTML, CSS (via Bootstrap 5)
  - Backend: Django
  - Sentiment Analysis: TextBlob Library

## Requirements

Make sure you have the following installed:

  - Python (3.8 or later)
  - Django (4.0 or later)
  - TextBlob library

## Setup and Installation

Follow these steps to run the project locally:

  1. **Clone the Repository**
     
     Open your terminal and run:


         git clone https://github.com/your-username/sentiment-detection-django.git
         cd sentiment-detection-django


2. **Install Dependencies**

   Install the required Python packages using:


       pip install textblob

3. **Migrations**

   Prepare the database by applying migrations:

       python manage.py makemigrations
       python manage.py migrate


4. **Run the Server**
   Start the Django development server:

       python manage.py runserver

   
    Open the app in your browser at http://127.0.0.1:8000/.

## Usage

  1. Enter the text you want to analyze in the input box.
  2. Click on the "Analyze Sentiment" button.
  3. View the sentiment category and polarity score on the same page.


## How Sentiment Analysis Works

  1. The user enters text into a form on the web page.
  2. The views.py file uses the TextBlob library to calculate the polarity of the text.
  3. Based on the polarity score:
     + 1 to 0.5: Very Positive
     + 0 to 0.5: Positive
     + 0: Neutral
     + -0.5 to 0: Negative
     + < to -0.5: Very Negative
  4. The results are displayed back to the user on the webpage.


## Example Outputs

  - Input: "I absolutely love this product!"
    
    Output: Very Positive (Polarity: 0.62)

  - Input: "I feel indifferent about the decision."
    
    Output: Neutral (Polarity: 0.0)

  - Input: "I hated the service at this restaurant."
    
    Output: Very Negative (Polarity: -0.9)


## Future Enhancements

  - Add more advanced sentiment analysis using machine learning models.
  - Support for multiple languages.
  - Display word-by-word sentiment analysis for detailed insights.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to improve this project.

## Acknowledgements

  - TextBlob for simple sentiment analysis.
  - Bootstrap for the modern and responsive design.
  - Django documentation for backend development.
     
