def insert(intervals, newInterval):
    ans_lst = list()
    flag = True

    for i in range(len(intervals)):
        if flag and newInterval[1] < intervals[i][0]:
            ans_lst.append(newInterval)
            ans_lst.append(intervals[i])
            flag = False
        elif ((newInterval[0] <= intervals[i][0]) and (newInterval[1] >= intervals[i][0])) or (
                (newInterval[0] <= intervals[i][1]) and (newInterval[1] >= intervals[i][1])):
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
        elif (newInterval[0] >= intervals[i][0]) and (newInterval[1] <= intervals[i][1]):
            ans_lst.append(intervals[i])
            flag = False
        else:
            ans_lst.append(intervals[i])

    if len(ans_lst) == 0 or flag:
        ans_lst.append(newInterval)
    return ans_lst