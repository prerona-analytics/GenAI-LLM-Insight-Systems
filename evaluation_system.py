# Simple Prompt Evaluation System

def evaluate_output(output):
    score = 0

    # Rule 1: Length check
    if len(output.split()) <= 80:
        score += 1

    # Rule 2: Contains business insight keywords
    keywords = ["growth", "decline", "recommend", "increase", "decrease"]
    if any(k in output.lower() for k in keywords):
        score += 1

    # Rule 3: Clarity (basic check)
    if "." in output:
        score += 1

    return score


sample_output = "West region is growing due to skincare demand. Recommend increasing marketing."

print("Score:", evaluate_output(sample_output))
