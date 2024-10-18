import requests
import json

def emotion_detector(text_to_analyze):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    INPUT_JSON = { "raw_document": { "text": text_to_analyze } }
    # Response
    response = requests.post(URL, json = INPUT_JSON, headers=HEADERS)
    # JSON convert
    json_result = json.loads(response.text)
    json_emotions = json_result['emotionPredictions'][0]['emotion']
    # Get scores
    anger_score = json_emotions['anger']
    disgust_score = json_emotions['disgust']
    fear_score = json_emotions['fear']
    joy_score = json_emotions['joy']
    sadness_score = json_emotions['sadness']
    # Dominant emotion
    emotions = ['anger', 'disgust', 'fear', 'joy', 'sadness']
    name_dominant = False
    for emotion in emotions:
        if not name_dominant:
            name_dominant = emotion
            continue
        if json_emotions[emotion] > json_emotions[name_dominant]:
            name_dominant = emotion
    # Output
    json_output = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': name_dominant
    }
    return json_output
