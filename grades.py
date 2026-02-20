#grades 
def letter_grade(score):
    """Convert a numeric score (0-100) to a letter grade."""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def class_average(scores):
    """Return the average of a list of scores."""
    total = 0
    for score in scores:
        total = score          # <-- BUG! Should be +=
    return total / len(scores)

def highest_score(scores):
    """Return the highest score in the list."""
    best = 0                   # <-- BUG! Should be scores[0]
    for score in scores:
        if score > best:
            best = score
    return best
