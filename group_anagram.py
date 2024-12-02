from collections import defaultdict


def group_anagram(strs):
    example_dict = defaultdict(list)
    for str in strs:
        sorted_el = "".join(sorted(str))
        #     example_dict[sorted_el].append(str)
        if sorted_el in example_dict.keys():
            example_dict[sorted_el].append(str)

        else:
            example_dict[sorted_el] = [] + [example_dict.get(sorted_el, str)]
    resoult = [item for item in example_dict.values()]
    # return resoult
    # resoult = list(example_dict.values())
    return resoult


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
resoult = group_anagram(strs)
print(resoult)
