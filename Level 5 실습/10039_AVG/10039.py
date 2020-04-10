inputList = []
for _ in range(5): inputList.append(int(input()))

filterGrade = lambda x: 40 if x<40 else x
filtered = list(map(filterGrade, inputList))

print(int(sum(filtered)/5))