import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import os

def match_video(input_embeddings):

    best_match = None
    best_score = 0

    for file in os.listdir("dataset/embeddings"):

        dataset_embeddings = np.load(f"dataset/embeddings/{file}")

        score = cosine_similarity(input_embeddings, dataset_embeddings).mean()

        if score > best_score:
            best_score = score
            best_match = file.replace(".npy", "")

    return best_match, float(best_score)