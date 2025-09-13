"""
Emotion Detection Web Application using Flask.

This Flask application exposes a web-based interface and a REST API endpoint to detect emotions
from input text using the `emotion_detector` function from the `EmotionDetection` module.

Routes:
    - `/emotionDetector`: Accepts a GET request with text input and returns emotion analysis.
    - `/`: Serves the homepage with a web interface to enter text for analysis.

To run the app:
    $ python app.py

The app listens on host 0.0.0.0 and port 5000 by default.
"""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("__name__")

@app.route("/emotionDetector")
def emotion_analyzer():
    """
    Analyze the emotions present in the input text.

    Query Parameters:
        textToAnalyze (str): The text string to be analyzed for emotional content.

    Returns:
        str: A formatted string showing the levels of five emotions (anger, disgust, fear,
             joy, sadness) and the dominant emotion. If the input is invalid, returns
             an error message prompting the user to try again.
    """
    text_to_analyse = request.args.get('textToAnalyze')
    emotion_result = emotion_detector(text_to_analyse)
    anger = emotion_result['anger']
    disgust = emotion_result['disgust']
    fear = emotion_result['fear']
    joy = emotion_result['joy']
    sadness = emotion_result['sadness']
    dominant_emotion = emotion_result['dominant_emotion']

    if dominant_emotion is None:
        return "Invalid text! Please try again"

    response_str = f"""For the given statement, the system response is
    'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, 'joy': {joy}, 'sadness': {sadness}.
    The dominant emotion is <strong>{dominant_emotion}</strong>."""
    return response_str

@app.route("/")
def render_index_page():
    """
    Render the main index HTML page.

    Returns:
        str: The rendered 'index.html' template that provides a UI for emotion detection.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
