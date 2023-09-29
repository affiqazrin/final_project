from EmotionDetection.emotion_detection import emotion_detector

def main():
    text_to_analyze = " I am glad this happened."
    result = emotion_detector(text_to_analyze)
    
    if result:
        print("Emotion detected:")
        print(result)

if __name__ == "__main__":
    main()