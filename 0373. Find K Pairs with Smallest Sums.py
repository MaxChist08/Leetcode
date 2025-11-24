import heapq

def k_smallest_pairs(nums1, nums2, k):
    my_heap = [((nums1[0] + nums2[0]), (0, 0))]
    heapq.heapify(my_heap)

    used = {(0, 0)}
    ans = list()

    while k:
        k -= 1

        a = heapq.heappop(my_heap)
        ans.append([nums1[a[1][0]], nums2[a[1][1]]])

        if len(nums1) > a[1][0] + 1 and (a[1][0] + 1, a[1][1]) not in used:
            heapq.heappush(my_heap, (nums1[a[1][0] + 1] + nums2[a[1][1]], (a[1][0] + 1, a[1][1])))
            used.add((a[1][0] + 1, a[1][1]))
        if len(nums2) > a[1][1] + 1 and (a[1][0], a[1][1] + 1) not in used:
            heapq.heappush(my_heap, (nums1[a[1][0]] + nums2[a[1][1] + 1], (a[1][0], a[1][1] + 1)))
            used.add((a[1][0], a[1][1] + 1))

        heapq.heapify(my_heap)

    return ans