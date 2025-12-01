import numpy as np
r,c = list(map(int,input().split()))
data = np.array([list(map(int, input().split())) for _ in range(r)])


print(data.T)
print(data.flatten())
