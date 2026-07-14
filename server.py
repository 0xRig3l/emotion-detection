"""
Server for the emotion detection flask application
"""
from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    """
    Index page
    """
    return render_template('index.html')


@app.route("/emotionDetector")
def detector():
    """
    Function to perform the emotion detection on endpoint /emotionDetector.
    It returns a formatted text with the output of the emotion detector function.
    """
    text = request.args.get('textToAnalyze')
    emotions = emotion_detector(text)
    dominant_emotion = emotions["dominant_emotion"]

    if any(emotion is None for emotion in emotions.values()):
        return "Invalid text! Please try again!"
    return (f"For the given statement, the system response is 'anger': {emotions['anger']},"
            f"'disgust': {emotions['disgust']}, 'fear': {emotions['fear']}, 'joy': "
            f"{emotions['joy']} and 'sadness': {emotions['sadness']}."
            f" The dominant emotion is {dominant_emotion}.")

if __name__ == "__main__":
    app.run(debug=True)
