from mistral_embed_demo import cosine_similarity

def find_top_k(new_embedding, stored_messages, k=3):
    similarities = []

    for item in stored_messages:
        sim = cosine_similarity(new_embedding, item["embedding"])
        similarities.append((item, sim))

    # sort by similarity score (highest first)
    similarities.sort(key=lambda x: x[1], reverse=True)

    # return top-k
    return similarities[:k]
