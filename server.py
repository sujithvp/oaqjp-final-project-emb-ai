"""
Flask server for analyzing the emotions in a given text statement.

Routes:
1. /emotionDetector: Analyzes a given statement for emotions and returns the results.
2. /: Renders the index.html page of the application.
"""

from flask import Flask, render_template, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

# Initialize Flask app
app = Flask(__name__)


@app.route("/emotionDetector", methods=['POST'])
def emo_analyzer():
    """
    Analyze the emotional content of a given statement.

    Returns:
        Response: JSON containing emotion analysis and a message.
    """
    data = request.get_json()
    statement = data.get("statement", "") if data else ""

    result = emotion_detector(statement)

    if result.get('dominant_emotion') is None:
        return jsonify(result=result, message="Invalid text! Please try again!")

    output_message = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, 'joy': {result['joy']}, "
        f"and 'sadness': {result['sadness']}. The dominant emotion is "
        f"{result['dominant_emotion']}."
    )
    return jsonify(result=result, message=output_message)


@app.route("/")
def render_index_page():
    """
    Render the index HTML page.

    Returns:
        str: Rendered HTML content.
    """
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
