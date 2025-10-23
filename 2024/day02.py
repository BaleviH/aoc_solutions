import os

day = os.path.splitext(os.path.basename(__file__))[0]
path = os.path.split(__file__)[0]
with open(f"{path}/inputs/{day}_input") as myfile:
    input = myfile.readlines()

def part1():
    safe = 0
    safe_idx = []
    for report_index, report in enumerate(input):
        report = report.split()
        report = list(map(int, report))
        ascending = False
        descending = False
        valid = True
        for idx, _ in enumerate(report):
            if idx == 0:
                continue
            if abs(report[idx] - report[idx-1]) > 3:
                valid = False
                break
            if (report[idx] > report[idx-1]):
                ascending = True
            elif (report[idx] < report[idx-1]):
                descending = True
            else: # not ascending or descending
                valid = False
                break
        if not valid:
            continue
        if ascending != descending:
            safe += 1
            safe_idx.append(int(report_index))
            
    safe_dict = {'safe_sum': safe,
                 'safe_idx_list' : safe_idx}
    return(safe_dict)

def part2_is_safe(report_fn):
    report_fn = report_fn.split()
    report_fn = list(map(int, report_fn))
    ascending = False
    descending = False
    valid = True
    for idx, _ in enumerate(report_fn):
        if idx == 0:
            continue
        if (abs(report_fn[idx] - report_fn[idx-1]) > 3):
            valid = False
            break
        if (report_fn[idx] > report_fn[idx-1]):
            ascending = True
        elif (report_fn[idx] < report_fn[idx-1]):
            descending = True
        else: # not ascending or descending
            valid = False
            break

    if not valid:
        return(False)
    if ascending != descending:
        return(True)
    else:
        return(False)

safe_p1_dict = part1()
safe_sum_dampened = 0
for report_index, report in enumerate(input):
    if report_index not in safe_p1_dict["safe_idx_list"]:
        report_list = report.split()
        dampener_options_dict = {}
        for i_to_be_removed, _ in enumerate(report_list):
            for i_to_be_added, _ in enumerate(report_list):
                report_list_copy = report_list.copy()
                if i_to_be_removed == i_to_be_added:
                    report_list_copy.pop(i_to_be_removed)
                    dampener_options_dict[f"without_idx{i_to_be_removed}"] = " ".join(report_list_copy)
                    continue
        for after_fail in dampener_options_dict:
            if part2_is_safe(dampener_options_dict[after_fail]):
                safe_sum_dampened += 1
                break


print(f"Part 1 is {safe_p1_dict["safe_sum"]} and Part 2 is {safe_sum_dampened+safe_p1_dict["safe_sum"]}")
