i = 1
friends = ["Jim", "Karen", "Kevin"]
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

while i <= 10:
    print(i)
    i += 1

print("")

for letter in "apple":
    print(letter)

print("")

for name in friends:
    print(name)

print("")

for index in range(len(friends)):
    print(index)

print("")

for index in range(5):
    if index == 0:
        print("first iteration")
    else:
        print("Not first")

print("")

for row in number_grid:
    print(row)
    for col in row:
        print(col)
