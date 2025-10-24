# Enter your code here. Read input from STDIN. Print output to STDOUT# Read input values
m = int(input())                    # Number of elements in set A
a = set(map(int, input().split()))  # Elements of set A
n = int(input())                    # Number of elements in set B
b = set(map(int, input().split()))  # Elements of set B

# Compute symmetric difference
result = sorted(a.symmetric_difference(b))

# Print results line by line
for val in result:
    print(val)
