
import cv2
import easyocr
import json
import matplotlib.pyplot as plt

#How many times each player is detected across all frames
from collections import defaultdict
player_counts = defaultdict(int)

with open('json/allNames.json', 'r') as f:
    name_to_jersey = json.load(f)

reader = easyocr.Reader(['en'], gpu=True)

def find_player_by_jersey(jersey_number):
    for name, number in name_to_jersey.items():
        if str(number) == jersey_number:
            return name
    return "Unknown"

def process_frame(frame_path):
    img = cv2.imread(frame_path)
    if img is None:
        return

    processed_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    text_ = reader.readtext(processed_img, allowlist='0123456789')
    threshold = 0.95

    for bbox, text, score in text_:
        cleaned_text = text.strip()
        if score > threshold and cleaned_text.isdigit():
            player_name = find_player_by_jersey(cleaned_text)
            if player_name and player_name != 'Unknown' :
                player_counts[player_name] += 1
                print(f"Detected Jersey: {cleaned_text} | Player: {player_name} | Confidence: {score:.2f} | frame: {frame_path}")
                pt1 = tuple(map(int, bbox[0]))
                pt2 = tuple(map(int, bbox[2]))
                cv2.rectangle(img, pt1, pt2, (0, 255, 0), 2)
                cv2.putText(img, f"{cleaned_text} ({player_name})", (pt1[0], pt1[1] - 10),
                cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 0, 0), 1)

    cv2.imwrite(frame_path, img)
