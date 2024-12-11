def merge_sorted(nums1, nums2, m, n):
    midx = m - 1
    nidx = n - 1
    right = m + n - 1

    while nidx >= 0:
        if midx >= 0 and nums1[midx] > nums2[nidx]:
            nums1[right] = nums1[midx]
            midx -= 1

        else:
            nums1[right] = nums2[nidx]
            nidx -= 1
        right -= 1


nums1 = [1, 2, 3, 0, 0, 0]
nums2 = [2, 5, 6]
m = 3
n = 3
merge_sorted(nums1, nums2, m, n)
