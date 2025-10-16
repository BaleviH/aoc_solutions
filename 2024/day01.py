with open("2024/inputs/day01_input") as myfile:
    day1_input = myfile.readlines()

left_list = []
right_list = []

for i in day1_input:
    pair = i.split()
    left_list.append(int(pair[0]))
    right_list.append(int(pair[1]))

left_list.sort()
right_list.sort()
diff = 0

for i in range(len(day1_input)):
    diff += abs(left_list[i] - right_list[i])

print(diff)