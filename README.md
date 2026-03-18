🎥 AI-Based Player Detection from Sports Videos
📌 Overview

This project is a web-based application that allows users to upload a sports video and automatically analyzes it to identify and rank players based on how frequently they appear.

The system processes the video frame by frame using computer vision techniques and outputs the top 3 most visible players.

🚀 Features

📤 Upload sports videos through a web interface

🎬 Extract frames from the uploaded video

🤖 Detect players (e.g., jersey numbers) using AI-based processing

📊 Count how often each player appears

🏆 Display the top 3 most detected players

🧹 Automatically clears previous results before processing new uploads

🏗️ Tech Stack

Backend: Flask (Python)

Computer Vision: OpenCV

AI Processing: Custom detection logic (detect.py)

Frontend: HTML (Flask templates)

Other: UUID, OS file handling

⚙️ How It Works

User uploads a video via the web interface

The application:

Saves the video locally

Extracts frames using OpenCV

Processes each frame using an AI detection function

Each detected player is counted based on frame appearances

The system ranks players by frequency

The top 3 players are displayed to the user

📂 Project Structure
.
├── app.py                 # Main Flask application
├── detect.py              # AI detection logic (process_frame, player_counts)
├── uploads/               # Uploaded videos
├── outputs/
│   └── output_frames/     # Extracted video frames
├── templates/
│   ├── index.html         # Upload page
│   └── results.html       # Results display
▶️ Installation & Setup
1. Clone the repository
git clone https://github.com/your-username/your-repo.git
cd your-repo
2. Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate   # macOS/Linux
# or
venv\Scripts\activate      # Windows
3. Install dependencies
pip install flask opencv-python
4. Run the application
python app.py
5. Open in browser
http://127.0.0.1:5000/
📊 Example Output
Top 3 Most Detected Players:
Player 10 → 120 frames
Player 7  → 95 frames
Player 23 → 80 frames
⚠️ Current Limitations

Processing is synchronous (can be slow for long videos)

Frames are saved to disk (not memory optimized)

Global state (player_counts) is not thread-safe

No progress indicator during processing

🔮 Future Improvements

⏱️ Add asynchronous/background processing (e.g., Celery)

⚡ Optimize frame processing (skip frames / in-memory processing)

📈 Add real-time progress updates

🎯 Improve detection accuracy with deep learning models

☁️ Deploy using Docker / Cloud services

💡 Use Cases

Sports analytics

Player tracking and performance analysis

Highlight generation

Broadcast analysis

👤 Author

Payam
Full-stack developer with a focus on AI-driven applications and scalable systems.

📄 License

This project is licensed under the MIT License.

If you want, I can also:

tailor this README specifically for job applications

add screenshots / demo GIFs

or make it more impressive for recruiters (very important for you right now)
