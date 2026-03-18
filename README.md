# AI-Based Player Detection from Sports Videos
# 📌 Overview

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

# ⚙️ How It Works

User uploads a video via the web interface

The application:

Saves the video locally

Extracts frames using OpenCV

Processes each frame using an AI detection function

Each detected player is counted based on frame appearances

The system ranks players by frequency

The top 3 players are displayed to the user

# 📂 Project Structure
<img width="681" height="190" alt="image" src="https://github.com/user-attachments/assets/48394f2e-ae0a-4c68-9d47-e02cc1b3478a" />

# ▶️ Installation & Setup
1. Clone the repository
git clone https://github.com/payamd/Computer-Vision---Reading-Jersey-Numbers.git
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
# 📊 Example Output
Top 3 Most Detected Players:
Player 10 → 120 frames
Player 7  → 95 frames
Player 23 → 80 frames

#💡 Use Cases

Sports analytics

Player tracking and performance analysis

Highlight generation

Broadcast analysis

# 👤 Author

Payam Davoudi
Full-stack developer with a focus on AI-driven applications and scalable systems.

# 📄 License

This project is licensed under the MIT License.
