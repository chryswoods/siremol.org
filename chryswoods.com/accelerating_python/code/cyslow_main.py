
from cyslow import load_and_parse_data, calculate_scores, get_index_of_best_score

# Load the data to be processed
(ids, varieties, data) = load_and_parse_data(5)

# Calculate all of the scores
scores = calculate_scores(data)

# Find the best pattern
best_pattern = get_index_of_best_score(scores)

# Print the result
print(f"The best score {scores[best_pattern]} comes from pattern {ids[best_pattern]}")
