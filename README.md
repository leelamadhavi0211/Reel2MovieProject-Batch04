
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

---
### Screens

##1. Dashboard

# Figure1.1: Dashboard Screen

<img width="1366" height="768" alt="Screenshot (165)" src="https://github.com/user-attachments/assets/39d3773f-0c8d-4608-8c77-6b8f6e976044" />

The dashboard serves as the main landing page of the Reel2Movie application. It provides users with an overview of the system and allows quick navigation to movie identification features. The interface is designed to be simple, responsive, and user-friendly.

## 2. Login

# Figure 1.2: Login Screen

<img width="1366" height="768" alt="Screenshot (174)" src="https://github.com/user-attachments/assets/696f2068-a479-416c-acd2-39daf71648b5" />

The login page allows registered users to securely access their accounts. Users can authenticate using their email and password. Authentication is handled using JWT-based security to ensure protected access to application features.

## 3. Signup

# Figure 1.3: Signup Screen

<img width="1366" height="768" alt="Screenshot (175)" src="https://github.com/user-attachments/assets/ee06ea72-ef60-47d0-925b-84cf6a9cd789" />

The signup page enables new users to create an account by providing basic details such as username, email, and password. User information is securely stored in MongoDB, allowing personalized access to the platform.

## 4. Upload

# Figure 1.4: Media Upload Screen

<img width="1366" height="768" alt="Screenshot (176)" src="https://github.com/user-attachments/assets/f913ee6d-a1db-41ba-9d4c-ad9c5eafa45e" />

The upload screen allows users to upload video clips or provide social media video URLs such as YouTube Shorts or Instagram Reels. The uploaded content is processed by the backend system, where frames are extracted and analyzed using the CLIP model for movie identification.

## 5. Result

# Figure 1.5: Movie Prediction Result Screen

<img width="1366" height="768" alt="Screenshot (177)" src="https://github.com/user-attachments/assets/1317b371-2e8b-4229-b7b8-a82c39929dd0" />

The result page displays the movie identified by the AI model along with the confidence score. Additional movie information such as poster, title, release date, genres, and ratings is retrieved from TMDB and presented to the user in an organized format.


