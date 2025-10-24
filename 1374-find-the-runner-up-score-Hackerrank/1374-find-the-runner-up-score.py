# Read input values
n = int(input())
scores = list(map(int, input().split()))

# Remove duplicates and sort in descending order
unique_scores = sorted(set(scores), reverse=True)

# Print the second highest (runner-up) score
print(unique_scores[1])
