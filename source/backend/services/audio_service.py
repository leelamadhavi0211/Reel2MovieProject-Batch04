import subprocess

def extract_audio(video_path):
    audio_path = video_path.replace(".mp4", ".wav")

    subprocess.run([
        "ffmpeg", "-i", video_path, "-q:a", "0", "-map", "a", audio_path
    ])

    return audio_path


def recognize_audio(audio_path):
    # 🔥 Placeholder (replace with ACRCloud API)

    return {
        "audio_match": "Unknown",
        "confidence": 0.5
    }