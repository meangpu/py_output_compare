def get_score_emoji(score, max_score):
    result = []
    for i in range(max_score):
        if i < score:
            result.append("🟢")
        else:
            result.append("🔴")

    final_score = "".join(result)
    return final_score
