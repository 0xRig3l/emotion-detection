import requests

def emotion_detector(text_to_analyze):
    """
    This function analyzes the emotion of the text_to_analyze.
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }

    res_dict = requests.post(url, headers=headers, json=input_json).json()
    emotions_scores = res_dict["emotionPredictions"][0]["emotion"]
    dominant_emotion = max(emotions_scores, key=emotions_scores.get)    

    return {**emotions_scores, "dominant_emotion": dominant_emotion}
