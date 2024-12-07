import pandas as pd
import numpy as np

df = pd.read_csv('day2.csv')

# Part 2
def CheckSafetyScore(report):
    score = int()
    increasing = None
    for i, level in enumerate(report):
        if i == 0:
            continue

        previousLevel = report[i - 1]
        currentLevel = report[i]

        score = currentLevel - previousLevel
        if score < -3 or score > 3 or score == 0:
            return False
        if increasing == True and score < 0:
            return False
        if increasing == False and score > 0:
            return False
        
        if score < 0:
            increasing = False
        else: increasing = True
        
    return True

safeReportCount = 0
for index, report in df.iterrows():
    report = [x for x in report if not np.isnan(x)]
    if CheckSafetyScore(report):
        safeReportCount += 1 
    else: # Part 2
        for i, level in enumerate(report):
            reportCopy = report.copy()
            reportCopy.pop(i)
            if CheckSafetyScore(reportCopy):
                safeReportCount += 1
                break

print(safeReportCount)