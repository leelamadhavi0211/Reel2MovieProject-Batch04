
 🎬 Reel2Movie – Movie Identification from Short Video Clips

Reel2Movie is a web application that automatically identifies the movie name from short video clips such as Instagram Reels or YouTube Shorts. Many short-video platforms share movie scenes without mentioning the original film, making it difficult for viewers to know the movie name. This project solves that problem by analyzing the uploaded video and extracting useful information from audio, visuals, and text to detect the movie.

The system allows users to upload a short video clip through a web interface. The backend processes the video by extracting key frames and audio segments. Audio recognition and visual analysis techniques are then applied to identify the most likely movie. The application also displays the confidence score and additional analysis details such as video information and audio information.

The platform is designed with a modern frontend interface and a scalable backend architecture to handle multimedia processing efficiently.

📌 Project Goal

The goal of Reel2Movie is to build an intelligent system that helps users quickly discover the original movie behind short video clips shared on social media platforms.

🚀 Features

  * Upload short video clips for movie identification
  * Automatic movie detection from video scenes
  * Audio analysis for detecting movie soundtracks or dialogues
  * Visual frame analysis for identifying movie scenes
  * Confidence score showing accuracy of prediction
  * Separate display of video analysis and audio analysis
  * Login and signup system for users
  * Limited uploads for guests and unlimited uploads for logged-in users
  * Clean and responsive dashboard UI



🛠 Tech Stack

  Frontend
  
    * React
    * Tailwind CSS
    * React Router
    * Axios
  
  Backend
  
    * Python
    * FastAPI
    * Uvicorn
  
  Video & Audio Processing
    
    * FFmpeg
    * OpenCV
    * MoviePy
  
  AI / Machine Learning
  
    * CLIP Model
    * PyTorch
    * NumPy
  
  Audio Recognition
  
    * ACRCloud API
  
  Text Extraction
  
    * spaCy
  
  Movie Data
  
    * TMDB API




