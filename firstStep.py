import json
import cv2
import easyocr
import matplotlib.pyplot as plt
import numpy as np


# Load the original JSON (player name -> jersey number)
with open('json/allNames.json', 'r') as f:
    name_to_jersey = json.load(f)

# read frame
frame_path = 'frames/frame1.png'

img = cv2.imread(frame_path)
if img is None:
    raise FileNotFoundError(f"Could not read image from path: {frame_path}")

# instance text detector
reader = easyocr.Reader(['en'], gpu=True)

processed_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# detect text on frame
text_ = reader.readtext(processed_img, allowlist='0123456789')

threshold = 0.25


def find_player_by_jersey(jersey_number):
    for name, number in name_to_jersey.items():
        if str(number) == jersey_number:
            return name
    return "Unknown"


for bbox, text, score in text_:
    cleaned_text = text.strip()

    if score > threshold and cleaned_text.isdigit():
        player_name = find_player_by_jersey(cleaned_text)
        print(f"Detected Jersey: {cleaned_text} | Player: {player_name} | Confidence: {score:.2f}")

        # Convert bbox points to integer tuples
        pt1 = tuple(map(int, bbox[0]))
        pt2 = tuple(map(int, bbox[2]))

        # Draw bounding box and label
        cv2.rectangle(img, pt1, pt2, (0, 255, 0), 2)
        cv2.putText(img, cleaned_text, pt1, cv2.FONT_HERSHEY_COMPLEX, 0.65, (255, 0, 0), 2)

# Show image
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.show()