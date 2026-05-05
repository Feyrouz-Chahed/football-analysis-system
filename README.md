# Football Analysis Project

## Introduction
The goal of this project is to detect and track players, referees, and footballs in a video using YOLO, one of the best AI object detection models available. We will also train the model to improve its performance. Additionally, we will assign players to teams based on the colors of their t-shirts using Kmeans for pixel segmentation and clustering. With this information, we can measure a team's ball acquisition percentage in a match. We will also use optical flow to measure camera movement between frames, enabling us to accurately measure a player's movement. Furthermore, we will implement perspective transformation to represent the scene's depth and perspective, allowing us to measure a player's movement in meters rather than pixels. Finally, we will calculate a player's speed and the distance covered. This project covers various concepts and addresses real-world problems, making it suitable for both beginners and experienced machine learning engineers.

### Web Dashboard & Heatmap Upgrade (Recent Additions)
This project has recently been extended to include a fully interactive Web Dashboard and visual analytics. 
- Interactive Web Interface:** Built a Streamlit app that allows users to upload videos and watch the AI process them without touching the code.
- Automated Video Conversion:** Integrated imageio-ffmpeg to automatically convert OpenCV video outputs into web-friendly H.264 formats.
- Dynamic Player Heatmaps:** Users can now enter a specific Player ID through the dashboard to instantly generate a positional heatmap of that player on the pitch.

![Screenshot](output_videos/screenshot.png)

## Modules Used
The following modules are used in this project:
- YOLO: AI object detection model
- Kmeans: Pixel segmentation and clustering to detect t-shirt color
- Optical Flow: Measure camera movement
- Perspective Transformation: Represent scene depth and perspective
- Speed and distance calculation per player
- Streamlit: Interactive Web Dashboard (Added feature)
- FFmpeg (imageio-ffmpeg): Video codec conversion for browser compatibility (Added feature)
- Seaborn & mplsoccer: Dynamic heatmap generation and pitch visualization (Added feature)

## Trained Models
- [Trained Yolo v5](https://drive.google.com/file/d/1DC2kCygbBWUKheQ_9cFziCsYVSRw6axK/view?usp=sharing)

## Sample video
-  [Sample input video](https://drive.google.com/file/d/1t6agoqggZKx6thamUuPAIdN_1zR9v9S_/view?usp=sharing)

## Requirements
To run this project, you need to have the following requirements installed:
- Python 3.x
- ultralytics
- supervision
- OpenCV
- NumPy
- Matplotlib
- Pandas
- streamlit
- imageio-ffmpeg
- seaborn
- mplsoccer

## How to Run the Web Dashboard
1. Clone the repository and install the requirements:
pip install -r requirements.txt

2. Start the interactive web application by running:
streamlit run app.py

3. Upload your .mp4 or .avi video via the web interface, click "Analyse starten", and enter a player ID to generate their specific heatmap.