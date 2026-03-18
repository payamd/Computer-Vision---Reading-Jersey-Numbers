import shutil

from flask import Flask, render_template, request, redirect, url_for
import os
import cv2
from detect import process_frame, player_counts
import uuid

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
OUTPUT_FOLDER = 'outputs/output_frames'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_video():
    #Garbage collection :D
    clear_output_folder()
    player_counts.clear()

    video = request.files['video']
    if video:
        video_path = os.path.join(UPLOAD_FOLDER, f"{uuid.uuid4()}.mp4")
        video.save(video_path)
        process_video(video_path)
        return redirect(url_for('results'))
        #return "Video processed successfully. Check the output frames."
    return "Upload failed."

@app.route('/results')
def results():
    from detect import player_counts
    top_players = sorted(player_counts.items(), key=lambda x: x[1], reverse=True)[:3]
    return render_template('results.html', top_players=top_players)


def clear_output_folder():
    folder = OUTPUT_FOLDER
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)  # remove file
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)  # remove subdirectory if any
        except Exception as e:
            print(f'Failed to delete {file_path}. Reason: {e}')
    print('Output folder cleared.')

def process_video(video_path):
    cap = cv2.VideoCapture(video_path)
    frame_count = 0
    success = True

    while success:
        success, frame = cap.read()
        if success:
            frame_filename = os.path.join(OUTPUT_FOLDER, f"frame_{frame_count}.png")
            cv2.imwrite(frame_filename, frame)
            process_frame(frame_filename)
            frame_count += 1

    cap.release()

    # Show top 3 most seen players
    top_players = sorted(player_counts.items(), key=lambda x: x[1], reverse=True)[:3]
    print("\nTop 3 Most Detected Players:")
    for name, count in top_players:
        print(f"{name}: He or she was in {count} frames")

if __name__ == '__main__':
    app.run(debug=True)
