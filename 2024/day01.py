with open("2024/inputs/day01_input") as myfile:
    day1_input = myfile.readlines()

left_list = []
right_list = []

for i in day1_input:
    pair = i.split()
    left_list.append(int(pair[0]))
    right_list.append(int(pair[1]))

def part1_sort_calcdiff():
    left_list.sort()
    right_list.sort()
    diff = 0

    for i in range(len(day1_input)):
        diff += abs(left_list[i] - right_list[i])
    print(diff)

# Part 1 solution #
# part1_sort_calcdiff()

def part2_calc_similarity():
    simscore = 0
    for left in left_list:
        multiplier = 0
        for right in right_list:
            if left == right:
                multiplier += 1
        simscore += left * multiplier
    print(simscore)

part2_calc_similarity()