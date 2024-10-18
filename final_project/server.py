from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask('Emotion Detector')

@app.route("/emotionDetector")
def emotion_detection():
    # Get the text
    text_to_analyze = request.args.get('textToAnalyze')
    # Get the response
    response = emotion_detector(text_to_analyze)
    # Get the list and the dominant emotion
    list_response = []
    dominant_emotion = ""
    for key, value in response.items():
        if key == "dominant_emotion":
            dominant_emotion = value
        else:
            list_response.append(f"'{key}': {value}")
    # Convert list to text
    txt_response = ', '.join(list_response)
    # Output
    return f"For the given statement, the system response is {txt_response}. The dominant emotion is <strong>{dominant_emotion}</strong>."

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
