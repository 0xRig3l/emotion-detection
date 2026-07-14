from EmotionDetection import emotion_detector
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/emotionDetector")
def detector():
    text = request.args.get('textToAnalyze')
    emotions = emotion_detector(text)
    dominant_emotion = emotions["dominant_emotion"]

    return f"For the given statement, the system response is 'anger': {emotions['anger']}, 'disgust': {emotions['disgust']}, 'fear': {emotions['fear']}, 'joy': {emotions['joy']} and 'sadness': {emotions['sadness']}. The dominant emotion is {dominant_emotion}."

if __name__ == "__main__":
    app.run(debug=True)