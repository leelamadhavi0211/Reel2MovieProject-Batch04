def fuse_results(video_result, audio_result):
    
    video_movie, video_score = video_result
    audio_movie = audio_result["audio_match"]
    audio_score = audio_result["confidence"]

    if video_movie == audio_movie:
        return video_movie, max(video_score, audio_score)

    # weighted decision
    if video_score > audio_score:
        return video_movie, video_score
    else:
        return audio_movie, audio_score