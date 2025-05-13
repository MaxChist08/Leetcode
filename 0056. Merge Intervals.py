def merge(intervals):
    def my_sort(lst):
        return lst[0]

    intervals = sorted(intervals, key=my_sort)

    temp_list = intervals[0]
    ans_list = []

    i = 1
    while i < len(intervals):
        if temp_list[1] >= intervals[i][0]:
            temp_list[1] = max(temp_list[1], intervals[i][1])
        else:
            ans_list.append([temp_list[0], temp_list[1]])
            temp_list[0] = intervals[i][0]
            temp_list[1] = intervals[i][1]
        i += 1

    if len(ans_list) == 0 or ans_list[-1] != temp_list:
        ans_list.append([temp_list[0], temp_list[1]])
    return ans_list