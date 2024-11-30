from collections import defaultdict


def group_anagram(strs):
    example_dict = defaultdict(list)
    for str in strs:
        sorted_el = "".join(sorted(str))
        example_dict[sorted_el].append(str)

    resoult = list(example_dict.values())
    return resoult


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
resoult = group_anagram(strs)
print(resoult)
