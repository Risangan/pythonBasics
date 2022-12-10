friends = ["Tom", "George", "Harry", "Steve"]
random_list = ["Tom", 2, False]
lucky_numbers = [2, 4, 5, 1, 3, 19, 23, 0]
print(friends)
friends[1] = "Mike"
print(friends[0])
print(random_list[2])
print(friends[-1])
print(friends[2:])
print(friends[1:3])

friends.append("Creed")
friends.extend(lucky_numbers)
print(friends)
friends.insert(1,"Kelly")
print(friends)
friends.remove("Steve")
print(friends)
print(friends.index("Kelly"))
print(friends.count("Creed"))
lucky_numbers.sort()
print(lucky_numbers)
lucky_numbers.reverse()
print(lucky_numbers)

friends2 = friends.copy()
print(friends2)