import os

day = os.path.splitext(os.path.basename(__file__))[0]
path = os.path.split(__file__)[0]
with open(f"{path}/inputs/{day}_input") as myfile:
    input = myfile.readlines()

safe = 0
for report in input:
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

print(safe)