import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = {"raw_document": {"text": text_to_analyze}}

    try:
        response = requests.post(url, headers=headers, json=input_json)
        
        if response.status_code == 200:
            # Convert the response text into a dictionary
            response_data = json.loads(response.text)
            
            # Extract the required emotions and their scores
            emotion = response_data['emotionPredictions'][0]['emotion']
            
            # Find the dominant emotion with the highest score
            max_emotion = max(emotion, key=emotion.get)
            max_emotion_score = emotion[max_emotion]
            
            # Construct the output dictionary
            output = {
                max_emotion : max_emotion_score
            }
            
            return output
        else:
            print(f"Emotion detection request failed with status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None


#text_to_analyze = "I love this new technology."
#result = emotion_detector(text_to_analyze)
#print("Emotion detected:", result)