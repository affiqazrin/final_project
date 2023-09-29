import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):

    def test_emotion_detection_statements(self):
        test_cases = [
            ("I am glad this happened", "joy"),
            ("I am really mad about this", "anger"),
            ("I feel disgusted just hearing about this", "disgust"),
            ("I am so sad about this", "sadness"),
            ("I am really afraid that this will happen", "fear"),
        ]

        for statement, expected_emotion in test_cases:
            with self.subTest(statement=statement, expected_emotion=expected_emotion):
                result = emotion_detector(statement)
                detected_emotion = max(result, key=result.get)  # Find the dominant emotion
                self.assertEqual(detected_emotion, expected_emotion)

if __name__ == '__main__':
    unittest.main()

