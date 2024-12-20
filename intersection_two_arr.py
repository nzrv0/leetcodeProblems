def intersection(nums1, nums2):
    num = set(nums1)
    res = []
    for i in nums2:
        if i in num:
            res.append(i)
            num.remove(i)

    return res


(
    nums1,
    nums2,
) = [
    2,
    6,
    2,
    9,
    1,
], [7, 1]
res = intersection(nums1, nums2)
print(res)
