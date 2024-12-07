import pandas as pd

df = pd.read_csv('day1.csv')
test_left = [3,4,2,1,3,3]
test_right = [4,3,5,3,9,3]

# Part 1
left = sorted(df["left"])
right = sorted(df["right"])
dist = [abs((left[i] - right[i])) for i in range(len(left))]
print(sum(dist))

# Part2
total_score = sum([(i * right.count(i)) for i in left])

print(total_score)