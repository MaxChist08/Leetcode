def merge(nums1, m, nums2, n):
    prev_index = -1

    for i in range(n):
        for j in range(prev_index + 1, m + n):
            if (j == m + i) or (nums1[j] > nums2[i]):
                nums1.insert(j, nums2[i])
                prev_index = j
                break

        nums1.pop(-1)